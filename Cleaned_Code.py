# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 20:33:45 2026

@author: admin
"""
"""
Created on Sun Oct 13 14:40:13 2024
@author: Windows
### Le Dang Trung Duc_21523002
"""
import os
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.genmod.cov_struct import Exchangeable
from statsmodels.tsa.stattools import adfuller

# ==========================================
# 1. SETUP AND DATA LOADING
# ==========================================
# Set your working directory here
os.chdir(r'D:\VGU\GFE\Programing Languge\Project_TrungDuc\Innovation Data')

print("Loading datasets...")
data_all_countries = pd.read_stata('New_Comprehensive_July_5_2024.dta')
qog_data = pd.read_stata('qog_bas_ts_jan24_stata14.dta')
oil_price_df = pd.read_stata('gasoline-price-data.dta')
tfp_data = pd.read_stata('Firm Level TFP Estimates and Factor Ratios_July_5_2024.dta')

# ==========================================
# 2. COUNTRY FILTERING & BASE DATA PREP
# ==========================================
developing_countries = [
    'Albania', 'Algeria', 'American Samoa', 'Argentina', 'Armenia', 'Azerbaijan', 
    'Belarus', 'Belize', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'China', 
    'Colombia', 'Costa Rica', 'Cuba', 'Dominica', 'Dominican Republic', 'Ecuador', 
    'Equatorial Guinea', 'Fiji', 'Gabon', 'Georgia', 'Grenada', 'Guatemala', 
    'Guyana', 'Indonesia', 'Jamaica', 'Jordan', 'Kazakhstan', 'Kosovo', 'Libya', 
    'Malaysia', 'Maldives', 'Marshall Islands', 'Mauritius', 'Mexico', 'Moldova', 
    'Montenegro', 'Mongolia', 'Namibia', 'North Macedonia', 'Palau', 'Paraguay', 
    'Peru', 'Serbia', 'South Africa', 'St. Lucia', 'St. Vincent and the Grenadines', 
    'Suriname', 'Thailand', 'Tonga', 'Türkiye', 'Turkmenistan', 'Tuvalu',
    'Angola', 'Bangladesh', 'Benin', 'Bhutan', 'Bolivia', 'Cabo Verde', 
    'Cambodia', 'Cameroon', 'Comoros', 'Congo, Rep.', 'Côte d\'Ivoire', 
    'Djibouti', 'Egypt, Arab Rep.', 'El Salvador', 'Eswatini', 'Ghana', 
    'Haiti', 'Honduras', 'India', 'Iraq', 'Iran, Islamic Rep.', 'Kenya', 
    'Kiribati', 'Kyrgyz Republic', 'Lao PDR', 'Lebanon', 'Lesotho', 
    'Mauritania', 'Micronesia, Fed. Sts.', 'Morocco', 'Myanmar', 'Nepal', 
    'Nicaragua', 'Nigeria', 'Pakistan', 'Papua New Guinea', 'Philippines', 
    'Samoa', 'São Tomé and Príncipe', 'Senegal', 'Solomon Islands', 
    'Sri Lanka', 'Tajikistan', 'Tanzania', 'Timor-Leste', 'Tunisia', 
    'Ukraine', 'Uzbekistan', 'Vanuatu', 'Vietnam', 'West Bank and Gaza', 
    'Zimbabwe', 'Macedonia, FYR'
]

# Extract country names and years
data_all_countries[['country_name', 'year']] = data_all_countries['country'].str.extract(r'([A-Za-z\s]+)(\d{4})')
developing_countries_df = data_all_countries[data_all_countries['country_name'].isin(developing_countries)].copy()

columns_to_keep = [
    'country_name', 'year', 'stra_sector', 'size', 'b2a', 'b2b', 'b2c', 'b2d',
    'b8', 'b7', 'e2b', 'h1', 'h2', 'h5', 'h8', 'k3bc', 'l3a', 'l3b', 'l10', 'idstd'
]
developing_countries_df = developing_countries_df[columns_to_keep]
developing_countries_df['year'] = developing_countries_df['year'].astype(int)

# ==========================================
# 3. QUALITY OF GOVERNMENT (QoG) DATA
# ==========================================
qog_data = qog_data.rename(columns={'cname': 'country_name'})
qog_data['year'] = qog_data['year'].astype(int)

qog_cols = [
    "country_name", "year", "ccp_cc", "mad_gdppc", "gle_gdp", "gle_exp",
    "gle_imp", "iiag_be", "lis_gini", "pwt_pop", 
    "ross_gas_value_2014", "ross_oil_value_2014", "wdi_co2", 'wdi_gdpcapcon2015', 'vdem_corr'
]
qog_data_subset = qog_data[[col for col in qog_cols if col in qog_data.columns]].copy()

# Fix QoG Country Names for consistency
qog_data_subset['country_name'] = qog_data_subset['country_name'].replace({
    'Viet Nam': 'Vietnam', 'Vietnam, North': 'Vietnam',
    'Tanzania, the United Republic of': 'Tanzania',
    'Moldova (the Republic of)': 'Moldova',
    'Philippines (the)': 'Philippines',
    'Congo (the Democratic Republic of the)': 'Congo, Dem. Rep.',
    'Congo (the)': 'Congo, Dem. Rep.',
    'Bolivia (Plurinational State of)': 'Bolivia'
})

qog_data_subset = qog_data_subset.sort_values(by=['country_name', 'year'])
qog_data_subset['GDP_Percapita'] = qog_data_subset.groupby('country_name')['wdi_gdpcapcon2015'].shift(1)
qog_data_subset['average_GDP_percapita'] = qog_data_subset.groupby('country_name')['wdi_gdpcapcon2015'].transform(lambda x: x.shift(1).rolling(3).mean())
if 'vdem_corr' in qog_data_subset.columns:
    qog_data_subset['corruption_index'] = qog_data_subset.groupby('country_name')['vdem_corr'].shift(1)
    qog_data_subset['average_corruption_index'] = qog_data_subset.groupby('country_name')['vdem_corr'].transform(lambda x: x.shift(1).rolling(3).mean())
qog_data_subset['corruption'] = qog_data_subset.groupby('country_name')['ccp_cc'].shift(1)

merged_df = pd.merge(developing_countries_df, qog_data_subset, on=['country_name', 'year'], how='left')
merged_df = merged_df[merged_df['year'] <= 2015]

# ==========================================
# 4. CLEAN FIRM-LEVEL FEATURES FIRST
# ==========================================
print("Cleaning firm-level data...")
idstd_to_sector = data_all_countries.set_index('idstd')['stra_sector'].to_dict()
merged_df = merged_df.merge(data_all_countries[['idstd', 'a0', 'k30', 'b5', 'c22b', 'd3a', 'd3b', 'd3c']], on='idstd', how='left')
merged_df['a0'] = merged_df.apply(lambda row: idstd_to_sector.get(row['idstd'], row['a0']) if row['a0'] == 'Indicator' else row['a0'], axis=1)

# Clean Text and Convert to Binaries/Numerics
if 'ccp_cc' in merged_df.columns:
    merged_df['ccp_cc'] = merged_df['ccp_cc'].str.replace(r"[12]\. ", "", regex=True)

# Firm Age
merged_df['b5'] = pd.to_numeric(merged_df['b5'], errors='coerce')
merged_df['institution_age'] = 2024 - merged_df['b5']
merged_df = merged_df[merged_df['institution_age'] > 0]
merged_df['institution_age_ln'] = np.log(merged_df['institution_age'])

# Numeric variables
merged_df['b7_x'] = pd.to_numeric(merged_df['b7_x'] if 'b7_x' in merged_df else merged_df['b7'], errors='coerce')
merged_df['b2b_x'] = pd.to_numeric(merged_df['b2b_x'] if 'b2b_x' in merged_df else merged_df['b2b'], errors='coerce')
merged_df['b2b_x'] = merged_df['b2b_x'].replace('%', '', regex=True).astype(float).apply(lambda x: 1 if pd.notnull(x) and x != 0 else 0)

merged_df = merged_df[merged_df['c22b'] != "Don't Know (Spontaneous)"]
merged_df = merged_df[merged_df['b8'].isin(['Yes', 'No'])]

cols_to_binary = ['b8', 'h1', 'h5', 'h8', 'l10', 'ccp_cc', 'c22b', 'corruption']
for col in cols_to_binary:
    if col in merged_df.columns:
        merged_df[col] = merged_df[col].replace({'Yes': 1, 'No': 0, '1. Yes': 1, '2. No': 0})

# Clean K30 Obstacles
merged_df = merged_df[~merged_df['k30'].isin(["Don't Know (Spontaneous)", -8.0, "Does Not Apply"])]

# Rename final variables
merged_df = merged_df.rename(columns={
    'b2b_x': 'foreign_own', 'h1': 'innovation_product', 'h5': 'innovation_process',
    'b7_x': 'managerial_experience', 'h8': 'r&d', 'l10': 'formal_training',
    'c22b': 'website', 'a0': 'industry'
})

# Filter out nulls and "Don't know" entries
cols_to_filter = ['innovation_process', 'innovation_product', 'r&d', 'formal_training']
merged_df = merged_df[~merged_df[cols_to_filter].isin(["Don't know (spontaneous)", -8, "Don't Know (Spontaneous)"]).any(axis=1)]

# ==========================================
# 5. OIL PRICE DATA PROCESSING (SPLIT LOGIC)
# ==========================================
print("Processing oil price data (Productivity & Innovation)...")
oil_price_df = oil_price_df[oil_price_df['country'].isin(developing_countries)].copy()

# Standardize country names across datasets
country_corrections = {
    'Macedonia, FYR': 'North Macedonia', 'Dominican Republic': 'Dominica',
    'Antiguaandbarbuda': 'Antigua and Barbuda', 'Congo, Rep.': 'Congo, Dem. Rep.',
    'Czechia': 'Czech Republic', 'DRC': 'Congo, Dem. Rep.', 'ElSalvador': 'El Salvador',
    'Iran, Islamic Rep.': 'Iran', 'Kyrgyz Republic': 'Kyrgyzstan', 'PapuaNewGuinea': 'Papua New Guinea',
    'Slovak Republic': 'Slovakia', 'Southsudan': 'South Sudan', 'Srilanka': 'Sri Lanka',
    'StKittsandNevis': 'St Kitts and Nevis', 'StLucia': 'St Lucia',
    'StVincentandGrenadines': 'St Vincent and Grenadines', 'TrinidadandTobago': 'Trinidad and Tobago',
    'rkiye': 'Turkey', 'USA': 'United States', 'UK': 'United Kingdom', 'Egypt, Arab Rep.': 'Egypt'
}
oil_price_df['country'] = oil_price_df['country'].replace(country_corrections)

# --- 5.1 DATA FOR FIRM PRODUCTIVITY (1-year lag / Shift 1) ---
prod_oil_df = oil_price_df.groupby(['country', 'year']).agg({
    'price_usd_2015': 'mean',
    'bmgap2015adj': 'mean',
    'gasolinecons': 'mean',
    'emissions': 'mean',
    'benchmark_2015_adj': 'mean'
}).reset_index()

volatility_df = oil_price_df.groupby(['country', 'year'])['price_usd_2015'].std().reset_index().rename(columns={'price_usd_2015': 'price_volatility'})
prod_oil_df = prod_oil_df.merge(volatility_df, on=['country', 'year'], how='left')

prod_oil_cols = ['price_usd_2015', 'bmgap2015adj', 'price_volatility', 'gasolinecons', 'emissions', 'benchmark_2015_adj']
for col in prod_oil_cols:
    prod_oil_df[col] = prod_oil_df.groupby('country')[col].shift(1)

prod_oil_df.columns = ['country_name', 'year', 'average_price', 'average_price_gap', 'average_gasoline_consumption', 'average_emission', 'avg_benchmark_df', 'price_volatility']

# --- 5.2 DATA FOR FIRM INNOVATION (3-year rolling average / Fiscal Year) ---
oil_price_df['fiscal_year'] = oil_price_df.apply(lambda row: f"{row['year']}/{row['year'] + 1}" if row['month'] >= 7 else f"{row['year'] - 1}/{row['year']}", axis=1)

inno_metrics_dict = {}
for country, group in oil_price_df.groupby('country'):
    years = group['year'].unique()
    for year in range(min(years) + 4, max(years) + 1):
        relevant_fiscal_years = [f"{y}/{y+1}" for y in range(year-4, year)]
        filtered_data = group[group['fiscal_year'].isin(relevant_fiscal_years)]
        
        inno_metrics_dict[(country, year)] = {
            'average_price': filtered_data['price_usd_2015'].mean(),
            'average_price_gap': filtered_data['bmgap2015adj'].mean(),
            'price_volatility': filtered_data['price_usd_2015'].std(),
            'average_gasoline_consumption': filtered_data['gasolinecons'].mean(),
            'average_emission': filtered_data['emissions'].mean(),
            'avg_benchmark_df': filtered_data['benchmark_2015_adj'].mean()
        }

inno_oil_df = pd.DataFrame.from_dict(inno_metrics_dict, orient='index').reset_index()
inno_oil_df.columns = ['country_name', 'year', 'average_price', 'average_price_gap', 'price_volatility', 'average_gasoline_consumption', 'average_emission', 'avg_benchmark_df']

# ==========================================
# 6. CREATE FINAL DATASETS & APPLY LOGARITHMS
# ==========================================
print("Generating final analytical datasets...")
def finalize_dataset(df_base, oil_data, is_productivity=False):
    # Merge base data with corresponding oil price data
    df = pd.merge(df_base, oil_data, on=['country_name', 'year'], how='left')
    df = df.dropna(subset=['foreign_own', 'average_price_gap', 'managerial_experience', 'institution_age_ln', 'average_price'])
    
    # Calculate Log Variables
    df['squared_mean_price'] = df['average_price'] ** 2
    df['log_squared_mean_price'] = np.log(df['squared_mean_price'])
    df['log_average_price_gap'] = np.log(df['average_price_gap'])
    df['log_average_price'] = np.log(df['average_price'])
    df['log_benchmark_price'] = np.log(df['avg_benchmark_df'])
    df['log_average_emission'] = np.log(df['average_emission'])
    df['log_price_volatility'] = np.log(df['price_volatility'].replace(0, np.nan))
    df['log_GDP_Percapita'] = np.log(df['GDP_Percapita'])
    if 'average_GDP_percapita' in df.columns:
        df['log_average_GDP_percapita'] = np.log(df['average_GDP_percapita'])

    # Create Dummies
    df = pd.get_dummies(df, columns=['k30', 'size', 'industry', 'year'], prefix=['k30', 'size', 'industry', 'year'], drop_first=True)
    df.rename(columns={'size_Small(<20)': 'sizesmall', 'size_Medium(20-99)': 'sizemedium', 'size_Large(100_And_Over)': 'size_large'}, inplace=True)
    df.rename(columns={'corruption': 'corruption_commission'}, inplace=True)
    
    # Target-specific variables
    if is_productivity:
        df = df.merge(tfp_data[['idstd', 'l1', 'n2a', 'income', 'tfprVAKL']], on='idstd', how='left')
        df = df.rename(columns={'l1': 'num_employee', 'n2a': 'labour_cost'})
        df['labour_cost_numeric'] = pd.to_numeric(df['labour_cost'], errors='coerce')
        df['log_labour_cost'] = np.log(df['labour_cost_numeric'].replace(0, np.nan))
        df = pd.get_dummies(df, columns=['income'], drop_first=True).rename(columns={"income_Low Income": "low_income"})
        df = df.dropna(subset=['tfprVAKL'])
    else:
        df = df.merge(tfp_data[['idstd', 'income']], on='idstd', how='left')
        df = pd.get_dummies(df, columns=['income'], drop_first=True).rename(columns={"income_Low Income": "low_income"})
        df = df.dropna(subset=['innovation_product'])
        
    df.replace({True: 1, False: 0}, inplace=True)
    df.columns = df.columns.str.replace(' ', '_')
    return df

# Create Firm Productivity Dataset
firm_productivity = finalize_dataset(merged_df, prod_oil_df, is_productivity=True)
firm_productivity.to_excel('firm_productivity.xlsx', index=False)

# Create Firm Innovation Dataset
firm_innovation = finalize_dataset(merged_df, inno_oil_df, is_productivity=False)
firm_innovation.to_excel('firm_innovation.xlsx', index=False)


# ==========================================
# 7. STATISTICAL MODELING
# ==========================================
def print_qic(model_results):
    qic = -2 * model_results.llf + 2 * len(model_results.params)
    print(f"QIC: {qic}\n")

# ------------------------------------------
# A. FIRM PRODUCTIVITY MODELS
# ------------------------------------------
print("\n" + "="*50)
print("--- FIRM PRODUCTIVITY (OLS & GEE) ---")
print("="*50)

prod_formula = (
    "tfprVAKL ~ foreign_own + managerial_experience + formal_training + website + "
    "institution_age_ln + log_squared_mean_price + low_income + "
    "log_average_price_gap + log_average_emission + log_price_volatility + log_GDP_Percapita + "
    "corruption_commission + sizesmall + sizemedium + corruption_index + "
    "k30_No_obstacle + k30_Minor_obstacle + k30_Moderate_obstacle + k30_Major_obstacle + "
    "year_2009 + year_2010 + year_2011 + year_2012 + year_2013 + year_2014 + year_2015"
)
prod_formula_interaction = prod_formula.replace("log_average_price_gap + log_average_emission + log_price_volatility", 
                                                "log_average_price_gap * log_price_volatility + log_average_emission")

# Check for Stationarity (ADF Test)
print("ADF Test on tfprVAKL:")
adf_result = adfuller(firm_productivity['tfprVAKL'].dropna())
print(f"ADF Statistic: {adf_result[0]:.4f}, p-value: {adf_result[1]:.4f}\n")

print("1. OLS MODEL - Base")
print(smf.ols(formula=prod_formula, data=firm_productivity).fit().summary())

print("\n2. OLS MODEL - Interaction")
print(smf.ols(formula=prod_formula_interaction, data=firm_productivity).fit().summary())

print("\n3. GEE MODEL - Base")
gee_prod = smf.gee(formula=prod_formula, data=firm_productivity, groups=firm_productivity['country_name'], cov_struct=Exchangeable()).fit()
print(gee_prod.summary())
print_qic(gee_prod)

print("\n4. GEE MODEL - Interaction")
gee_prod_int = smf.gee(formula=prod_formula_interaction, data=firm_productivity, groups=firm_productivity['country_name'], cov_struct=Exchangeable()).fit()
print(gee_prod_int.summary())
print_qic(gee_prod_int)

# ------------------------------------------
# B. FIRM INNOVATION MODELS
# ------------------------------------------
print("\n" + "="*50)
print("--- FIRM INNOVATION (PROBIT & GEE) ---")
print("="*50)

base_inno_formula = (
    " ~ foreign_own + managerial_experience + formal_training + website + "
    "institution_age_ln + log_squared_mean_price + log_average_price_gap + "
    "log_average_emission + log_price_volatility + log_average_GDP_percapita + low_income + "
    "industry_Services + industry_Manufacturing + sizesmall + sizemedium + "
    "year_2011 + year_2012 + year_2013 + year_2014 + year_2015 + "
    "average_corruption_index + corruption_commission + "
    "k30_No_obstacle + k30_Minor_obstacle + k30_Moderate_obstacle + k30_Major_obstacle"
)

interaction_inno_formula = base_inno_formula.replace("log_average_price_gap + log_average_emission + log_price_volatility",
                                                     "log_average_price_gap * log_price_volatility + log_average_emission + average_price")

for target in ['innovation_product', 'innovation_process']:
    print(f"\n--- Modeling for {target.upper()} ---")
    formula_standard = target + base_inno_formula
    formula_interact = target + interaction_inno_formula
    
    print("\n1. PROBIT MODEL - Base")
    probit_model = smf.probit(formula=formula_standard, data=firm_innovation).fit(disp=0)
    print(probit_model.summary())
    print("\n[Marginal Effects]")
    print(probit_model.get_margeff().summary())
    
    print("\n2. PROBIT MODEL - Interaction")
    probit_interact = smf.probit(formula=formula_interact, data=firm_innovation).fit(disp=0)
    print(probit_interact.summary())
    
    print("\n3. GEE LOGIT MODEL - Base")
    gee_logit = smf.gee(formula=formula_standard, data=firm_innovation, groups=firm_innovation['country_name'], family=sm.families.Binomial(), cov_struct=Exchangeable()).fit()
    print(gee_logit.summary())
    print_qic(gee_logit)
    
    print("\n4. GEE LOGIT MODEL - Interaction")
    gee_logit_int = smf.gee(formula=formula_interact, data=firm_innovation, groups=firm_innovation['country_name'], family=sm.families.Binomial(), cov_struct=Exchangeable()).fit()
    print(gee_logit_int.summary())
    print_qic(gee_logit_int)

print("Data processing and modeling completed successfully!")