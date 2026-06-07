# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 14:40:13 2024

@author: Windows
"""
###Le Dang Trung Duc_21523002
import os as os
os.chdir(r'D:\VGU\GFE\Programing Languge\Project_TrungDuc\Innovation Data')

import pandas as pd
data_all_countries = pd.read_stata('New_Comprehensive_July_5_2024.dta')

developing_countries = [
    # Countries from the first image
    'Albania', 'Algeria', 'American Samoa', 'Argentina', 'Armenia', 'Azerbaijan', 
    'Belarus', 'Belize', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'China', 
    'Colombia', 'Costa Rica', 'Cuba', 'Dominica', 'Dominican Republic', 'Ecuador', 
    'Equatorial Guinea', 'Fiji', 'Gabon', 'Georgia', 'Grenada', 'Guatemala', 
    'Guyana', 'Indonesia', 'Jamaica', 'Jordan', 'Kazakhstan', 'Kosovo', 'Libya', 
    'Malaysia', 'Maldives', 'Marshall Islands', 'Mauritius', 'Mexico', 'Moldova', 
    'Montenegro', 'Mongolia', 'Namibia', 'North Macedonia', 'Palau', 'Paraguay', 
    'Peru', 'Serbia', 'South Africa', 'St. Lucia', 'St. Vincent and the Grenadines', 
    'Suriname', 'Thailand', 'Tonga', 'Türkiye', 'Turkmenistan', 'Tuvalu',
    
    # Additional countries from the second image
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
    'Zimbabwe'
]

# Assuming your DataFrame is named 'df'
developing_countries_df = data_all_countries[data_all_countries['country'].isin(developing_countries)]
print(developing_countries_df)
data_all_countries[['country_name', 'year']] = data_all_countries['country'].str.extract(r'([A-Za-z\s]+)(\d{4})')
print(data_all_countries[['country', 'country_name', 'year']].head())
developing_countries_df = data_all_countries[data_all_countries['country_name'].isin(developing_countries)]
print(developing_countries_df.head())
developing_countries_df = developing_countries_df.drop(columns=['country'])
columns = developing_countries_df.columns.tolist()
columns = ['country_name', 'year'] + [col for col in columns if col not in ['country_name', 'year']]
developing_countries_df = developing_countries_df[columns]
print(developing_countries_df.head())
columns_to_keep = [
    'country_name', 'year', 'stra_sector', 'size', 'b2a', 'b2b', 'b2c', 'b2d',
    'b8', 'b7', 'e2b', 'h1', 'h2', 'h5', 'h8', 'k3bc', 'l3a', 'l3b', 'l10', 'idstd'
]

developing_countries_df = developing_countries_df[columns_to_keep]
print(developing_countries_df.head())
print(developing_countries_df.head())
# Save the DataFrame to a CSV file
developing_countries_df.to_csv('developing_countries_filtered.csv', index=False)
countries = developing_countries_df['country_name'].unique()
# Display the list of countries
print("Countries included in the data:")
print(countries)

##################################################################################
#Merge with the data of Quality of Government (QoG)
file_path = r"D:\VGU\GFE\Programing Languge\Project_TrungDuc\Innovation Data\qog_bas_ts_jan24_stata14.dta"
# Load the Stata file into a DataFrame
qog_data = pd.read_stata(file_path)
# Display the first few rows of the DataFrame to verify it's loaded correctly
print(qog_data.head())
# Convert the 'year' column in both DataFrames to int
developing_countries_df['year'] = developing_countries_df['year'].astype(int)
qog_data['year'] = qog_data['year'].astype(int)
qog_data = qog_data.rename(columns={'cname': 'country_name'})
columns_to_keep = ["country_name", "year", "ccp_cc", "mad_gdppc", "gle_gdp", 
                   "gle_imp", "iiag_be", "lis_gini", "pwt_pop", 
                   "ross_gas_value_2014", "ross_oil_value_2014", "wdi_co2", 'wdi_gdpcapcon2015']
qog_data_subset = qog_data[columns_to_keep]
qog_data = qog_data_subset
merged_df = pd.merge(developing_countries_df, qog_data, on=['country_name', 'year'], how='left')
merged_df = merged_df[merged_df['year'] <= 2015]
merged_df.to_csv('merged_data_output.csv', index=False)
unique_years = merged_df['year'].unique()
print(f"Unique years: {unique_years}")

#####################################################################3
#####THE OIL PRICE:    
# Replace 'path_to_file.dta' with the actual file path
oil_price_df = pd.read_stata('gasoline-price-data.dta')
print(oil_price_df.head())    
developing_countries = [
    # Countries from the first image
    'Albania', 'Algeria', 'American Samoa', 'Argentina', 'Armenia', 'Azerbaijan', 
    'Belarus', 'Belize', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'China', 
    'Colombia', 'Costa Rica', 'Cuba', 'Dominica', 'Dominican Republic', 'Ecuador', 
    'Equatorial Guinea', 'Fiji', 'Gabon', 'Georgia', 'Grenada', 'Guatemala', 
    'Guyana', 'Indonesia', 'Jamaica', 'Jordan', 'Kazakhstan', 'Kosovo', 'Libya', 
    'Malaysia', 'Maldives', 'Marshall Islands', 'Mauritius', 'Mexico', 'Moldova', 
    'Montenegro', 'Mongolia', 'Namibia', 'North Macedonia', 'Palau', 'Paraguay', 
    'Peru', 'Serbia', 'South Africa', 'St. Lucia', 'St. Vincent and the Grenadines', 
    'Suriname', 'Thailand', 'Tonga', 'Türkiye', 'Turkmenistan', 'Tuvalu',
    
    # Additional countries from the second image
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
    'Zimbabwe','Macedonia, FYR'
]

oil_price_df = oil_price_df[oil_price_df['country'].isin(developing_countries)]
# Assuming 'oil_price_df' contains the 'year' and 'oil_price' columns
# Create a new column for the fiscal year (e.g., 2015, 2014, etc.)
# Assuming your DataFrame is df with columns 'FiscalYear', 'Month', and 'Price'
###################################################################################################
# Step 1: Define the fiscal year calculation function
import pandas as pd
# Step 1: Calculate the average price for each country and year
avg_prices_df = oil_price_df.groupby(['country', 'year'])['price_usd_2015'].mean().reset_index()
avg_prices_df['shifted_average_price'] = avg_prices_df.groupby('country')['price_usd_2015'].shift(1)
avg_prices_df.rename(columns={'shifted_average_price': 'average_price'}, inplace=True)
oil_price_df = pd.merge(oil_price_df, avg_prices_df[['country', 'year', 'average_price']], on=['country', 'year'], how='left')
################################################################################
#Now, I want to calculate the the average for the average_price_gap

# Step 1: Calculate the average price gap for each country and year
avg_price_gaps_df = oil_price_df.groupby(['country', 'year'])['bmgap2015adj'].mean().reset_index()
avg_price_gaps_df['previous_year_average_price_gap'] = avg_price_gaps_df.groupby('country')['bmgap2015adj'].shift(1)
avg_price_gaps_df.rename(columns={'previous_year_average_price_gap': 'average_price_gap'}, inplace=True)
oil_price_df = pd.merge(oil_price_df, avg_price_gaps_df[['country', 'year', 'average_price_gap']], on=['country', 'year'], how='left')
#####################################################################

#Now i have to calculate the price votality (standard deviation) in the fiscal years:
# Step 1: Calculate the price volatility (standard deviation) for each country and fiscal year
price_volatility_df = oil_price_df.groupby(['country', 'year'])['price_usd_2015'].std().reset_index()
price_volatility_df['previous_fiscal_year_volatility'] = price_volatility_df.groupby('country')['price_usd_2015'].shift(1)
price_volatility_df.rename(columns={'previous_fiscal_year_volatility': 'price_volatility'}, inplace=True)
oil_price_df = pd.merge(oil_price_df, price_volatility_df[['country', 'year', 'price_volatility']], on=['country', 'year'], how='left')

# Now 'oil_price_df' contains the price volatility from the previous fiscal year for each country and fiscal year

# Apply the function to each year in the DataFrame and create a new column for volatility
#############################################################
avg_gasoline_df = oil_price_df.groupby(['country', 'year'])['gasolinecons'].mean().reset_index()
avg_gasoline_df['previous_year_avg_gasoline'] = avg_gasoline_df.groupby('country')['gasolinecons'].shift(1)
avg_gasoline_df.rename(columns={'previous_year_avg_gasoline': 'average_gasoline_consumption'}, inplace=True)
oil_price_df = pd.merge(oil_price_df, avg_gasoline_df[['country', 'year', 'average_gasoline_consumption']], on=['country', 'year'], how='left')

###############################################################################################
#I want to calculate for the Average of Emission:
# Assuming your DataFrame is named 'oil_price_df' and has columns 'year', 'month', 'emissions', and 'country'
# Step 1: Calculate the average emissions for each country and year
# Step 1: Calculate the average emissions for each country and year
avg_emissions_df = oil_price_df.groupby(['country', 'year'])['emissions'].mean().reset_index()
avg_emissions_df['previous_year_average_emission'] = avg_emissions_df.groupby('country')['emissions'].shift(1)
avg_emissions_df.rename(columns={'previous_year_average_emission': 'average_emission'}, inplace=True)
oil_price_df = pd.merge(oil_price_df, avg_emissions_df[['country', 'year', 'average_emission']], on=['country', 'year'], how='left')
#Now, I want to calculate the the average for the benchmark price
# Get the unique years in the data
import pandas as pd
avg_benchmark_df = oil_price_df.groupby(['country', 'year'])['benchmark_2015_adj'].mean().reset_index()
avg_benchmark_df['previous_year_avg_benchmark'] = avg_benchmark_df.groupby('country')['benchmark_2015_adj'].shift(1)
avg_benchmark_df.rename(columns={'previous_year_avg_benchmark': 'average_benchmark'}, inplace=True)
oil_price_df = pd.merge(oil_price_df, avg_benchmark_df[['country', 'year', 'average_benchmark']], on=['country', 'year'], how='left')
#Now, I want to calculate the the average for the gasoline consumption:

#Now i want to merge the oil_price_df to the merged_df matching by "country_name" and "year"
###################################################################
oil_price_df['country'] = oil_price_df['country'].replace({
    'Macedonia, FYR': 'Noth Macedonia',
    'Dominican Republic': 'Dominica'
})
oil_price_df.to_csv('oil_price_data.csv', index=False)

selected_columns = ['country', 'year', 'average_price', 'price_volatility', 'average_price_gap', 'average_gasoline_consumption','average_emission', 'average_benchmark']
# Create a new DataFrame with unique values for 'country' and 'year'
unique_df = oil_price_df[selected_columns].drop_duplicates(subset=['country', 'year'])
print(unique_df.head())
unique_df = unique_df.rename(columns={'country': 'country_name'})
merged_data_final = pd.merge(merged_df, unique_df, on=['country_name', 'year'], how='left')
merged_data_final.to_csv('merged_data_final.csv', index=False)
merge_data_final_filtered = merged_data_final
merge_data_final_filtered = merge_data_final_filtered.reset_index(drop=True)
print(merge_data_final_filtered)
merged_df_2 = merge_data_final_filtered.merge(data_all_countries[['idstd', 'a0']], on='idstd', how='left')
merged_df_2 = merged_df_2.drop(columns=['stra_sector'])
cols = list(merged_df_2.columns)
cols.insert(1, cols.pop(cols.index('a0')))
merged_df_2 = merged_df_2[cols]
##############################################################################################

#Now, i want to CREATE Dummies variables for industry:
# Step 1: Create a dictionary mapping from 'idstd' to 'stra_sector' in the 'data_all_countries' DataFrame
idstd_to_sector = data_all_countries.set_index('idstd')['stra_sector'].to_dict()
# Step 2: Define a function to replace 'Indicator' with the corresponding 'stra_sector' value
def replace_indicator(row):
    if row['a0'] == 'Indicator':
        return idstd_to_sector.get(row['idstd'], row['a0'])
    return row['a0']
merged_df_2['a0'] = merged_df_2.apply(replace_indicator, axis=1)
print(merged_df_2['a0'].unique()) #check again
dummy_columns_to_drop = ['a0_Manufacturing', 'a0_Services', 'a0_Core','a0_Indicator']  # Replace with actual dummy column names
dummies = pd.get_dummies(merged_df_2['a0'], prefix='a0')
merged_df_2 = pd.concat([merged_df_2, dummies], axis=1)
print(merged_df_2['a0'].unique())

##############################################################################################
#Now, i want to calculate for the dummy or column 'size'
size_dummies = pd.get_dummies(merged_df_2['size'], prefix='size')
merged_df_2 = pd.concat([merged_df_2, size_dummies], axis=1)
#Now, i have to clean the data for column 'ccp_cc'
merged_df_2['ccp_cc'] = merged_df_2['ccp_cc'].str.replace("2. ", "", regex=False)
merged_df_2['ccp_cc'] = merged_df_2['ccp_cc'].str.replace("1. ", "", regex=False)
print(merged_df_2[['ccp_cc']].head())  # Displaying only the 'ccp_cc' column for verification
unique_countries = merged_df_2['country_name'].unique()
print(unique_countries)
##############################################################################################
#Now, i will calculate the average GDP per capital
# Assuming your DataFrame is named 'qog_data_subset' and has columns 'year', 'country', and 'wdi_gdpcapcon2015'
# Step 1: Sort the DataFrame by 'country' and 'year' to ensure correct alignment
qog_data_subset = qog_data_subset.sort_values(by=['country_name', 'year'])
# Step 2: Create the 'GDP_Year' column by shifting the 'wdi_gdpcapcon2015' values by 1 year within each country
qog_data_subset['GDP Percapita'] = qog_data_subset.groupby('country_name')['wdi_gdpcapcon2015'].shift(1)
qog_data_subset['average_GDP_percapita'] = qog_data_subset.groupby('country_name')['wdi_gdpcapcon2015'].transform(lambda x: x.shift(1).rolling(3).mean())
qog_data_subset['country_name'] = qog_data_subset['country_name'].replace('Viet Nam', 'Vietnam')
merged_df_3 = merged_df_2.merge(qog_data_subset[['country_name', 'year', 'GDP Percapita','average_GDP_percapita']],
                               on=['country_name', 'year'],
                               how='left')
merged_df_3 = merged_df_3.drop(columns=['ross_gas_value_2014', 'ross_oil_value_2014'])
boolean_columns = merged_df_3.select_dtypes(include=['bool']).columns
merged_df_3[boolean_columns] = merged_df_3[boolean_columns].astype(int)
print(merged_df_3.head())
merged_df_3.to_csv('Finale.csv', index=False)
### Now i decide to include more variale to my file
# Assuming data_b and data_d are your DataFrames
columns_to_match_2 = ['idstd', 'b7', 'b2b', 'k3bc', 'd3b', 'd3c', 'size', 'd3a', 'b5', 'c22b']
data_b_subset = data_all_countries[columns_to_match_2]
# Merging the dataframes on 'firm_id'
merged_df_4 = pd.merge(merged_df_3, data_b_subset, on='idstd', how='left')
# Display the merged dataframe
print(merged_df_4)
##############################################################################################
#####Now i want to calculate the the age of firms:
import numpy as np
import pandas as pd
merged_df_4['b5'] = pd.to_numeric(merged_df_4['b5'], errors='coerce')
merged_df_4 = merged_df_4.dropna(subset=['b5'])
merged_df_4['b5'] = merged_df_4['b5'].astype(int)
merged_df_4['institution_age'] = 2024 - merged_df_4['b5']
merged_df_4 = merged_df_4[merged_df_4['institution_age'] > 0]
merged_df_4['institution_age_ln'] = np.log(merged_df_4['institution_age'])
# Display the updated dataframe
print(merged_df_4)
merged_df_4['b7_x'] = pd.to_numeric(merged_df_4['b7_x'], errors='coerce')
merged_df_4 = merged_df_4.dropna(subset=['b7_x'])
merged_df_4['b7_x'] = merged_df_4['b7_x'].astype(int)
print(merged_df_4)
#### Now i drop c22b:
merged_df_4 = merged_df_4[merged_df_4['c22b'] != "Don't Know (Spontaneous)"]
merged_df_4 = merged_df_4.drop(columns=['b7_y', 'b2b_y', 'k3bc_y'])
merged_df_4 = merged_df_4.drop(columns=['size_y'])
print(merged_df_4)
### Drop Nan in b2b column:
merged_df_4['b2b_x'] = pd.to_numeric(merged_df_4['b2b_x'], errors='coerce')
merged_df_4 = merged_df_4.dropna(subset=['b2b_x'])
merged_df_4['b2b_x'] = merged_df_4['b2b_x'].astype(int)
### drop b2c b2d columns:
merged_df_4 = merged_df_4.drop(columns=['b2c', 'b2d'])
### drop l3a, l3b collumns:
merged_df_4 = merged_df_4.drop(columns=['l3a', 'l3b'])
# clean b8
merged_df_4 = merged_df_4[merged_df_4['b8'].isin(['Yes', 'No'])]
merged_df_4 = merged_df_4.drop(columns=['e2b'])
# Replace "Yes" with 1 and "No" with 0 in the 'b8' column
merged_df_4['b8'] = merged_df_4['b8'].replace({'Yes': 1, 'No': 0})
# List of columns to update
columns_to_update = ['h1', 'h5', 'h8', 'l10', 'ccp_cc', 'c22b']
# Replace "Yes" with 1 and "No" with 0 in the specified columns
merged_df_4[columns_to_update] = merged_df_4[columns_to_update].replace({'Yes': 1, 'No': 0})
merged_df_4 = merged_df_4.drop(columns=['d3b', 'd3a'])
## Thêm biến K30:
# Merge all_countries with merged_df_4 on 'k30' from all_countries and 'itstd' from merged_df_4
merged_df_5 = pd.merge(merged_df_4, data_all_countries[['idstd', 'k30']], on='idstd', how='left')
## Create dummy varibale for variable k30:
##clean k30:
merged_df_5 = merged_df_5[merged_df_5['k30'] != "Don't Know (Spontaneous)"]
merged_df_5 = merged_df_5[merged_df_5['k30'] != -8.0]
merged_df_5 = merged_df_5[merged_df_5['k30'] != "Does Not Apply"]
merged_df_5 = pd.get_dummies(merged_df_5, columns=['k30'], prefix='k30', drop_first=True)
merged_df_5 = merged_df_5.drop(columns=['k30_-8.0'])
#CLEAN
merged_df_5 = merged_df_5.replace({True: 1, False: 0})
merged_df_5 = merged_df_5.drop(columns=['k30_Does Not Apply'])
## convert column b2b:
# Convert 'b2b' column to numeric values by removing '%' and converting to float
merged_df_5['b2b_x'] = merged_df_5['b2b_x'].replace('%', '', regex=True).astype(float)
# Convert to binary: 1 if the value is different from 0, 0 otherwise
merged_df_5['b2b_x'] = merged_df_5['b2b_x'].apply(lambda x: 1 if x != 0 else 0)
## clean data:
merged_df_5 = merged_df_5.dropna(subset=['average_price_gap'])
merged_df_5.to_csv('merged_data_5.csv', index=False)
print(merged_df_5.columns)
merged_df_5.rename(columns=lambda x: x.strip().replace(' ', '_'), inplace=True)
merged_df_5 = merged_df_5.rename(columns={
    'b2b_x': 'foreign own',
    'h1': 'innovation_product',
    'h5': 'innovation_process',
    'b7_x': 'managerial_experience',
    'h8': 'r&d',
    'l10': 'formal_training',
    'ccp_cc': 'corruption',
    'c22b': 'website'
})

merged_df_6 = merged_df_5.dropna(subset=['innovation_product', 'foreign own', 'average_price_gap', 'managerial_experience', 'institution_age_ln', 
                                                   'size_Medium(20-99)', 'size_Large(100_And_Over)', 'website', 
                                                   'k30_Minor_obstacle', 'k30_Moderate_obstacle', 'k30_Major_obstacle', 
                                                   'k30_Very_severe_obstacle', 'a0_Manufacturing', 'a0_Services', 
                                                   'GDP_Percapita', 'average_emission', 'average_price', 'price_volatility','innovation_process'])
columns_to_filter = ['innovation_process', 'innovation_product', 'r&d', 'formal_training']

merged_df_6 = merged_df_6[~merged_df_6[columns_to_filter].isin(["Don't know (spontaneous)"]).any(axis=1)]
merged_df_6 = merged_df_6[merged_df_6['formal_training'] != "Don't Know (Spontaneous)"]
merged_df_6 = merged_df_6[merged_df_6['formal_training'] != -8]
merged_df_6['squared_mean_price'] = merged_df_6['average_price'] ** 2
# Taking the natural logarithm of 'squared_mean_price'.
merged_df_6['log_squared_mean_price'] = np.log(merged_df_6['squared_mean_price'])
merged_df_6['log_average_price_gap'] = np.log(merged_df_6['average_price_gap'])
merged_df_6['log_average_price'] = np.log(merged_df_6['average_price'])
unique_values_formal_training = merged_df_6['formal_training'].unique()
print(f"Unique values in 'formal_training': {unique_values_formal_training}")
merged_df_6.to_csv('merged_data_6.csv', index=False)
merged_df_6.rename(columns={'size_x': 'size'}, inplace=True)
# Expand the dataframe with more countries:   
    
    
unique_countries = data_all_countries['country_name'].unique()
print("Unique countries:", unique_countries)
unique_countries_2 = merged_df_6['country_name'].unique()
print("Unique countries:", unique_countries_2)
unique_countries_expanded = list(set(unique_countries) - set(unique_countries_2))
print("Unique countries:", unique_countries_expanded)
unique_countries_expanded = data_all_countries[data_all_countries['country_name'].isin(unique_countries_expanded)]
unique_countries_expanded = unique_countries_expanded.drop(columns=['country'])
columns_1 = unique_countries_expanded.columns.tolist()
columns_1 = ['country_name', 'year'] + [col for col in columns_1 if col not in ['country_name', 'year']]
unique_countries_expanded = unique_countries_expanded[columns_1]
print(unique_countries_expanded.head())
columns_to_keep_2 = [
    'country_name', 'year', 'stra_sector', 'size', 'b2a', 'b2b', 'b2c', 'b2d',
    'b8', 'b7', 'e2b', 'h1', 'h2', 'h5', 'h8', 'k3bc', 'l3a', 'l3b', 'l10', 'idstd'
]
# Filter the DataFrame to include only these columns
unique_countries_expanded = unique_countries_expanded[columns_to_keep_2]
print(unique_countries_expanded.head())
print(unique_countries_expanded.head())
countries_2 = unique_countries_expanded['country_name'].unique()
# Display the list of countries
print("Countries included in the data:")
print(countries_2)
##################################################################################
#Merge with the data of Quality of Nation
file_path = r"D:\VGU\GFE\Programing Languge\Project_TrungDuc\Innovation Data\qog_bas_ts_jan24_stata14.dta"
# Load the Stata file into a DataFrame
qog_data = pd.read_stata(file_path)
# Display the first few rows of the DataFrame to verify it's loaded correctly
print(qog_data.head())
# Convert the 'year' column in both DataFrames to int
unique_countries_expanded['year'] = unique_countries_expanded['year'].astype(int)
qog_data['year'] = qog_data['year'].astype(int)
# Rename 'cname' to 'country_name' in qog_data if not already done
qog_data = qog_data.rename(columns={'cname': 'country_name'})
# List of columns to keep
columns_to_keep = ["country_name", "year", "ccp_cc", "mad_gdppc", "gle_gdp", 
                   "gle_imp", "iiag_be", "lis_gini", "pwt_pop", 
                   "ross_gas_value_2014", "ross_oil_value_2014", "wdi_co2", 'wdi_gdpcapcon2015', 'vdem_corr']
# Subset the DataFrame to keep only the specified columns
qog_data_subset = qog_data[columns_to_keep]
qog_data = qog_data_subset
# Merge the DataFrames on 'country_name' and 'year', this data control for all variable 
merged_df_7 = pd.merge(unique_countries_expanded, qog_data, on=['country_name', 'year'], how='left')
merged_df_7 = merged_df_7[merged_df_7['year'] <= 2015]
#The oil price:
# Apply the function to each year in the DataFrame and create a new column
#Now i want to merge the oil_price_df to the merged_df matching by "country_name" and "year"
###################################################################
oil_price_df.to_csv('oil_price_data.csv', index=False)
selected_columns = ['country', 'year', 'average_price', 'price_volatility', 'average_price_gap', 'average_gasoline_consumption','average_emission', 'average_benchmark']
# Create a new DataFrame with unique values for 'country' and 'year'
unique_df = oil_price_df[selected_columns].drop_duplicates(subset=['country', 'year'])
# Display the first few rows of the new DataFrame to verify
print(unique_df.head())
# If necessary, rename 'country' in unique_df to 'country_name' to match merged_data
unique_df = unique_df.rename(columns={'country': 'country_name'})
# Merge unique_df with merged_data on 'country_name' and 'year'
unique_countries_unique_df = unique_df['country_name'].unique()
unique_countries_merged_df_7 = merged_df_7['country_name'].unique()

print("Unique countries in 'unique_df':")
print(unique_countries_unique_df)

print("\nUnique countries in 'merge_df_7':")
print(unique_countries_merged_df_7)
country_corrections = {
    'Antiguaandbarbuda': 'Antigua and Barbuda',
    'Central African Republic': 'Central African Republic',
    'Congo, Rep.': 'Congo',
    'Czechia': 'Czech Republic',
    'DominicanRepublic': 'Dominican Republic',
    'DRC': 'Congo, Dem. Rep.',
    'ElSalvador': 'El Salvador',
    'Iran, Islamic Rep.': 'Iran',
    'Kyrgyz Republic': 'Kyrgyzstan',
    'Latvia': 'Latvia',  # OK
    'Lithuania': 'Lithuania',  # OK
    'Malawi': 'Malawi',  # OK
    'Moldova': 'Moldova',  # OK
    'North Macedonia': 'North Macedonia',  # OK
    'PapuaNewGuinea': 'Papua New Guinea',
    'Philippines': 'Philippines',  # OK
    'Slovak Republic': 'Slovakia',
    'Southsudan': 'South Sudan',
    'Srilanka': 'Sri Lanka',
    'StKittsandNevis': 'St Kitts and Nevis',
    'StLucia': 'St Lucia',
    'StVincentandGrenadines': 'St Vincent and Grenadines',
    'TrinidadandTobago': 'Trinidad and Tobago',
    'rkiye': 'Turkey',
    'Viet Nam': 'Vietnam',
    'USA': 'United States',
    'UK': 'United Kingdom'
}

import pandas as pd
def correct_country_name(country_name, corrections):
    return corrections.get(country_name, country_name)
def drop_missing_countries(df, missing_list):
    return df[~df['country_name'].isin(missing_list)]
# Applying the corrections
merged_df_7['country_name'] = merged_df_7['country_name'].apply(lambda x: correct_country_name(x, country_corrections))
corrections = {
    'Egypt, Arab Rep.': 'Egypt',
    'Congo, Rep.': 'Congo, Dem. Rep.',
    'Kyrgyz Republic': 'Kyrgyzstan'
}
# Apply corrections to 'unique_df' and merge
unique_df['country_name'] = unique_df['country_name'].replace(corrections)
merged_data_final_2 = pd.merge(merged_df_7, unique_df, on=['country_name', 'year'], how='left')
merged_data_final_2.to_csv('merged_data_final_2.csv', index=False)
###########################################################################################
#drop all year <2007
# Assuming your DataFrame is named merge_data_final and has a column 'year'
# Filter the DataFrame to keep only rows where the year is greater than or equal to 2007
#Merge two data-frame:
merged_df_9 = merged_data_final_2.merge(data_all_countries[['idstd', 'a0']], on='idstd', how='left')
merged_df_9 = merged_df_9.drop(columns=['stra_sector'])
cols = list(merged_df_9.columns)
cols.insert(1, cols.pop(cols.index('a0')))
merged_df_9 = merged_df_9[cols]
##############################################################################################
#Now, i want to calculate for Dummy variables for industry:
#Indicator by the value of "stra_sector" in the data_all_countries dataframe by matching idstd
idstd_to_sector = data_all_countries.set_index('idstd')['stra_sector'].to_dict()
def replace_indicator(row):
    if row['a0'] == 'Indicator':
        return idstd_to_sector.get(row['idstd'], row['a0'])
    return row['a0']
#Apply the function to the 'a0' column in 'merged_df_2'
merged_df_9['a0'] = merged_df_9.apply(replace_indicator, axis=1)
print(merged_df_9['a0'].unique()) #check again
dummy_columns_to_drop = ['a0_Manufacturing', 'a0_Services', 'a0_Core','a0_Indicator']  # Replace with actual dummy column names
dummies = pd.get_dummies(merged_df_9['a0'], prefix='a0')
#Concatenate the dummy variables with the original DataFrame
merged_df_9 = pd.concat([merged_df_9, dummies], axis=1)
print(merged_df_9['a0'].unique())
#########
#Now, i want to calculate for the dummy variable for column 'size'
size_dummies = pd.get_dummies(merged_df_9['size'], prefix='size')
merged_df_2 = pd.concat([merged_df_9, size_dummies], axis=1)
merged_df_9['ccp_cc'] = merged_df_9['ccp_cc'].str.replace("2. ", "", regex=False)
merged_df_9['ccp_cc'] = merged_df_9['ccp_cc'].str.replace("1. ", "", regex=False)
print(merged_df_9[['ccp_cc']].head())  # Displaying only the 'ccp_cc' column for verification
unique_countries = merged_df_9['country_name'].unique()
print(unique_countries)
#################################################
#Now, i will calculate the average GDP per capital
# Assuming your DataFrame is named 'qog_data_subset' and has columns 'year', 'country', and 'wdi_gdpcapcon2015'
# Step 1: Sort the DataFrame by 'country' and 'year' to ensure correct alignment
qog_data_subset = qog_data_subset.sort_values(by=['country_name', 'year'])
# Step 2: Create the 'GDP_Year' column by shifting the 'wdi_gdpcapcon2015' values by 1 year within each country
qog_data_subset['GDP Percapita'] = qog_data_subset.groupby('country_name')['wdi_gdpcapcon2015'].shift(1)
# Step 2: Calculate the rolling average GDP per capita for the previous 3 years
qog_data_subset['average_GDP_percapita'] = qog_data_subset.groupby('country_name')['wdi_gdpcapcon2015'].transform(lambda x: x.shift(1).rolling(3).mean())
qog_data_subset['corruption_index'] = qog_data_subset.groupby('country_name')['vdem_corr'].shift(1)
qog_data_subset['country_name'] = qog_data_subset['country_name'].replace({
    'Viet Nam': 'Vietnam',
    'Tanzania, the United Republic of': 'Tanzania',
    'Moldova (the Republic of)': 'Moldova',
    'Philippines (the)': 'Philippines',
    'Congo (the Democratic Republic of the)': 'Congo, Dem. Rep.'
})
merged_df_10 = merged_df_9.merge(qog_data_subset[['country_name', 'year', 'GDP Percapita','average_GDP_percapita']],
                               on=['country_name', 'year'],
                               how='left')
merged_df_10 = merged_df_10.drop(columns=['ross_gas_value_2014', 'ross_oil_value_2014'])
#i want to convert all True False in to 1 and 0:
boolean_columns = merged_df_10.select_dtypes(include=['bool']).columns
merged_df_10[boolean_columns] = merged_df_10[boolean_columns].astype(int)
print(merged_df_10.head())
### Now i decide to include more variales to my file
columns_to_match_2 = ['idstd', 'b7', 'b2b', 'k3bc', 'd3b', 'd3c', 'size', 'd3a', 'b5', 'c22b']
data_b_subset = data_all_countries[columns_to_match_2]
merged_df_11 = pd.merge(merged_df_10, data_b_subset, on='idstd', how='left')
#####Now i want to calculate the the age of firms:
merged_df_11['b5'] = pd.to_numeric(merged_df_11['b5'], errors='coerce')
merged_df_11 = merged_df_11.dropna(subset=['b5'])
merged_df_11['b5'] = merged_df_11['b5'].astype(int)
merged_df_11['institution_age'] = 2024 - merged_df_11['b5']
merged_df_11 = merged_df_11[merged_df_11['institution_age'] > 0]
merged_df_11['institution_age_ln'] = np.log(merged_df_11['institution_age'])
print(merged_df_11)
merged_df_11['b7_x'] = pd.to_numeric(merged_df_11['b7_x'], errors='coerce')
# Remove rows with NaN values in 'b7' (which were non-integer originally)
merged_df_11 = merged_df_11.dropna(subset=['b7_x'])
# Optionally, convert 'b7' to integer if needed
merged_df_11['b7_x'] = merged_df_11['b7_x'].astype(int)
merged_df_11 = merged_df_11[merged_df_11['c22b'] != "Don't Know (Spontaneous)"]
merged_df_11 = merged_df_11.drop(columns=['b7_y', 'b2b_y', 'k3bc_y'])
merged_df_11 = merged_df_11.drop(columns=['size_y'])
merged_df_11['b2b_x'] = pd.to_numeric(merged_df_11['b2b_x'], errors='coerce')
merged_df_11 = merged_df_11.dropna(subset=['b2b_x'])
merged_df_11['b2b_x'] = merged_df_11['b2b_x'].astype(int)
### drop b2c b2d columns:
merged_df_11 = merged_df_11.drop(columns=['b2c', 'b2d'])
### drop l3a, l3b collumns:
merged_df_11 = merged_df_11.drop(columns=['l3a', 'l3b'])
# clean b8
merged_df_11 = merged_df_11[merged_df_11['b8'].isin(['Yes', 'No'])]
merged_df_11 = merged_df_11.drop(columns=['e2b'])
# Replace "Yes" with 1 and "No" with 0 in the 'b8' column
merged_df_11['b8'] = merged_df_11['b8'].replace({'Yes': 1, 'No': 0})
# List of columns to update
columns_to_update = ['h1', 'h5', 'h8', 'l10', 'ccp_cc', 'c22b']
# Replace "Yes" with 1 and "No" with 0 in the specified columns
merged_df_11[columns_to_update] = merged_df_11[columns_to_update].replace({'Yes': 1, 'No': 0})
merged_df_11 = merged_df_11.drop(columns=['d3b', 'd3a'])
# Merge all_countries with merged_df_4 on 'k30' from all_countries and 'itstd' from merged_df_4
merged_df_12 = pd.merge(merged_df_11, data_all_countries[['idstd', 'k30']], on='idstd', how='left')
## Create dummy varibale for variable k30:
##clean k30:
merged_df_12 = merged_df_12[merged_df_12['k30'] != "Don't Know (Spontaneous)"]
merged_df_12 = merged_df_12[merged_df_12['k30'] != -8.0]
merged_df_12 = merged_df_12[merged_df_12['k30'] != "Does Not Apply"]
merged_df_12 = pd.get_dummies(merged_df_12, columns=['k30'], prefix='k30', drop_first=True)
merged_df_12 = merged_df_12.drop(columns=['k30_-8.0'])
#CLEAN
merged_df_12 = merged_df_12.replace({True: 1, False: 0})
merged_df_12 = merged_df_12.drop(columns=['k30_Does Not Apply'])
## convert column b2b:
# Convert 'b2b' column to numeric values by removing '%' and converting to float
merged_df_12['b2b_x'] = merged_df_12['b2b_x'].replace('%', '', regex=True).astype(float)
# Convert to binary: 1 if the value is different from 0, 0 otherwise
merged_df_12['b2b_x'] = merged_df_12['b2b_x'].apply(lambda x: 1 if x != 0 else 0)
## clean data:
merged_df_12 = merged_df_12.dropna(subset=['average_price_gap'])
merged_df_12.to_csv('merged_data_5.csv', index=False)
print(merged_df_12.columns)
merged_df_12.rename(columns=lambda x: x.strip().replace(' ', '_'), inplace=True)
merged_df_12 = merged_df_12.rename(columns={
    'b2b_x': 'foreign own',
    'h1': 'innovation_product',
    'h5': 'innovation_process',
    'b7_x': 'managerial_experience',
    'h8': 'r&d',
    'l10': 'formal_training',
    'ccp_cc': 'corruption',
    'c22b': 'website'
})
#create dummies for company size:
merged_df_12.rename(columns={'size_x': 'size'}, inplace=True)
# Now create dummy variables for the 'size' column
dummy_df = pd.get_dummies(merged_df_12['size'], prefix='size')
# Concatenate the dummy variables with the original dataframe
merged_df_12 = pd.concat([merged_df_12, dummy_df], axis=1)    
columns_to_filter = ['innovation_process', 'innovation_product', 'r&d', 'formal_training']
merged_df_12 = merged_df_12[~merged_df_12[columns_to_filter].isin(["Don't know (spontaneous)"]).any(axis=1)]
merged_df_12 = merged_df_12[merged_df_12['formal_training'] != "Don't Know (Spontaneous)"]
merged_df_12 = merged_df_12[merged_df_12['formal_training'] != -8]
merged_df_12['squared_mean_price'] = merged_df_12['average_price'] ** 2
# Taking the natural ogarithm of 'squared_mean_price'.
merged_df_12['log_squared_mean_price'] = np.log(merged_df_12['squared_mean_price'])
merged_df_12['log_average_price_gap'] = np.log(merged_df_12['average_price_gap'])
merged_df_12['log_average_price'] = np.log(merged_df_12['average_price'])
unique_values_formal_training = merged_df_12['formal_training'].unique()
print(f"Unique values in 'formal_training': {unique_values_formal_training}")
merged_df_12.replace({True: 1, False: 0}, inplace=True)
merged_df_12.to_csv('merged_df_12.csv', index=False)
merged_df_6.rename(columns={'size_Large(100_And_Over)': 'size_Large(100 And Over)'}, inplace=True)
##merge 2 dataframe:
merged_result = pd.concat([merged_df_6, merged_df_12], ignore_index=True)
merged_result = merged_result.drop(['log_average_price_gap', 'gle_gdp', 'gle_imp', 'iiag_be', 'lis_gini'], axis=1)
columns_list = merged_result.columns.tolist()
print(columns_list)
###Calculate the log_average_price_gap
merged_result['log_benchmark_price'] = np.log(merged_result['average_benchmark'])
merged_result['log_average_price_gap'] = merged_result['log_average_price'] - merged_result['log_benchmark_price']
###Merge with the the TRPK Data:
file_path = "Firm Level TFP Estimates and Factor Ratios_July_5_2024.dta"
# Reading the .dta file into a DataFrame
df = pd.read_stata(file_path)
merged_result_1 = merged_result.merge(df[['idstd', 'l1', 'n2a', 'income', 'tfprVAKL']], on='idstd', how='left')
## CLEAN:
columns_to_exclude = [
    'a0_Chemicals_&_Chemical_Products', 'a0_Food', 'a0_Garments', 
    'a0_IT_&_IT_Services', 'a0_Machinery_&_Equipment', 
    'a0_Other_Services', 'a0_Rest_of_Universe', 'a0_Retail'
]
# Drop the columns from the DataFrame
merged_result_1 = merged_result_1.drop(columns=columns_to_exclude)
if 'a0' in merged_result_1.columns:
    merged_result_1 = merged_result_1.drop(columns=['a0'])
#CLEAN FIRM_PRODUCTIVITY:
firm_productivity = pd.merge(merged_result_1, data_all_countries[['idstd', 'a0']], on='idstd', how='left')
firm_productivity.rename(columns={'a0': 'industry'}, inplace=True)
dummies = pd.get_dummies(firm_productivity['industry'], prefix='industry')
firm_productivity = pd.concat([firm_productivity, dummies], axis=1)
firm_productivity = firm_productivity.dropna(subset=['tfprVAKL'])
firm_productivity = firm_productivity.rename(columns={'l1': 'num.employee', 'n2a': 'labour_cost'})
income_dummies = pd.get_dummies(firm_productivity['income'], prefix='income')
firm_productivity = pd.concat([firm_productivity, income_dummies], axis=1)
firm_productivity = firm_productivity.replace({True: 1, False: 0})
firm_productivity.rename(columns={'foreign own': 'foreign_own'}, inplace=True)
firm_productivity.rename(columns={'num.employee': 'num_employee'}, inplace=True)
firm_productivity.rename(columns={'size_Small(<20)': 'sizesmall'}, inplace=True)
firm_productivity.rename(columns={'size_Medium(20-99)': 'sizemedium'}, inplace=True)
firm_productivity.to_excel('firm_productivity.xlsx', index=False)
firm_productivity = firm_productivity.drop(columns=['corruption'])
qog_data_subset = qog_data_subset.sort_values('year')
qog_data_subset['corruption'] = qog_data_subset.groupby('country_name')['ccp_cc'].shift(1)
qog_data_subset = qog_data_subset.sort_index()
qog_data_subset['country_name'] = qog_data_subset['country_name'].replace({
    'Philippines (the)': 'Philippines',
    'Tanzania, the United Republic of': 'Tanzania',
    'Bolivia (Plurinational State of)': 'Bolivia',
    'Congo (the)': 'Congo, Dem. Rep.',
    'Vietnam, North': 'Vietnam',
    'Moldova (the Republic of)': 'Moldova'
})

firm_productivity = firm_productivity.merge(
    qog_data_subset[['country_name', 'year', 'corruption']],  # columns to merge from qog_data_subset
    on=['country_name', 'year'],  # merging on both country_name and year
    how='left'  # use left merge to keep all rows in firm_innovation
)
firm_productivity['corruption'] = firm_productivity['corruption'].replace({
    '1. Yes': 1,
    '2. No': 0
})
firm_productivity = firm_productivity[firm_productivity['corruption'] != '96. Other']
firm_productivity = firm_productivity[firm_productivity['corruption'] != '96. Other']
firm_productivity['labour_cost_numeric'] = pd.to_numeric(firm_productivity['labour_cost'], errors='coerce')
firm_productivity['log_labour_cost'] = np.log(firm_productivity['labour_cost_numeric'].replace(0, np.nan))
firm_productivity = firm_productivity[~firm_productivity['log_labour_cost'].isna() & ~np.isinf(firm_productivity['log_labour_cost'])]
firm_productivity['log_average_emission'] = np.log(firm_productivity['average_emission'])
firm_productivity['log_price_volatility'] = np.log(firm_productivity['price_volatility'].replace(0, np.nan))
firm_productivity['log_GDP_Percapita'] = np.log(firm_productivity['GDP_Percapita'])
firm_productivity = pd.get_dummies(firm_productivity, columns=['income'], drop_first=True)
firm_productivity = firm_productivity.rename(columns={"income_Low Income": "low_income"})
firm_productivity = firm_productivity.rename(columns={"corruption": "corruption_commission"})
firm_productivity = pd.merge(
    firm_productivity, 
    qog_data_subset[['year', 'country_name', 'corruption_index']], 
    on=['year', 'country_name'], 
    how='left'
)
firm_productivity = pd.get_dummies(firm_productivity, columns=['year'], drop_first=True)
firm_productivity.to_excel('firm_productivity.xlsx', index=False)




#############################################################################################3
                                            #FIRM INNOVATION:

developing_countries_df = data_all_countries[data_all_countries['country'].isin(developing_countries)]
print(developing_countries_df)
data_all_countries[['country_name', 'year']] = data_all_countries['country'].str.extract(r'([A-Za-z\s]+)(\d{4})')
print(data_all_countries[['country', 'country_name', 'year']].head())
developing_countries_df = data_all_countries[data_all_countries['country_name'].isin(developing_countries)]
print(developing_countries_df.head())
developing_countries_df = developing_countries_df.drop(columns=['country'])
columns = developing_countries_df.columns.tolist()
columns = ['country_name', 'year'] + [col for col in columns if col not in ['country_name', 'year']]
developing_countries_df = developing_countries_df[columns]
print(developing_countries_df.head())
#Extracted Data_Frame:
columns_to_keep = [
    'country_name', 'year', 'stra_sector', 'size', 'b2a', 'b2b', 'b2c', 'b2d',
    'b8', 'b7', 'e2b', 'h1', 'h2', 'h5', 'h8', 'k3bc', 'l3a', 'l3b', 'l10', 'idstd'
]
# Filter the DataFrame to include only these columns
developing_countries_df = developing_countries_df[columns_to_keep]
developing_countries_df.to_csv('developing_countries_filtered.csv', index=False)
countries = developing_countries_df['country_name'].unique()
file_path = r"D:\VGU\GFE\Programing Languge\Project_TrungDuc\Innovation Data\qog_bas_ts_jan24_stata14.dta"
qog_data = pd.read_stata(file_path)
print(qog_data.head())
developing_countries_df['year'] = developing_countries_df['year'].astype(int)
qog_data['year'] = qog_data['year'].astype(int)
qog_data = qog_data.rename(columns={'cname': 'country_name'})
columns_to_keep = ["country_name", "year", "ccp_cc", "mad_gdppc", "gle_gdp", 
                   "gle_imp", "iiag_be", "lis_gini", "pwt_pop", 
                   "ross_gas_value_2014", "ross_oil_value_2014", "wdi_co2", 'wdi_gdpcapcon2015']
# Subset the DataFrame to keep only the specified columns
qog_data_subset = qog_data[columns_to_keep]
qog_data = qog_data_subset
merged_df = pd.merge(developing_countries_df, qog_data, on=['country_name', 'year'], how='left')
merged_df = merged_df[merged_df['year'] <= 2015]
merged_df.to_csv('merged_data_output.csv', index=False)
unique_years = merged_df['year'].unique()
print(f"Unique years: {unique_years}")
#####################################################################################
#The oil price:
# Replace 'path_to_file.dta' with the actual file path
oil_price_df = pd.read_stata('gasoline-price-data.dta')
print(oil_price_df.head())    
oil_price_df = oil_price_df[oil_price_df['country'].isin(developing_countries)]
#Calculate the average fiscal years for 
# Step 1: Define the fiscal year calculation function
import pandas as pd
def fiscal_year(row):
    if row['month'] >= 7:  # Fiscal year starts in July
        return f"{row['year']}/{row['year'] + 1}"
    else:
        return f"{row['year'] - 1}/{row['year']}"
# Step 2: Create a 'fiscal_year' column
oil_price_df['fiscal_year'] = oil_price_df.apply(fiscal_year, axis=1)
# Step 3: Calculate the rolling average for each fiscal year, controlling for countries
average_prices = {}
# Group by 'country' to ensure the calculation is done within each country
for country, group in oil_price_df.groupby('country'):
    years = group['year'].unique()
    for year in range(min(years) + 4, max(years) + 1):
        relevant_fiscal_years = [
            f"{year-4}/{year-3}",
            f"{year-3}/{year-2}",
            f"{year-2}/{year-1}",
            f"{year-1}/{year}"
        ]
        filtered_data = group[group['fiscal_year'].isin(relevant_fiscal_years)]
        average_price = filtered_data['price_usd_2015'].mean()
        average_prices[(country, year)] = average_price
avg_prices_df = pd.DataFrame(list(average_prices.keys()), columns=['country', 'year'])
avg_prices_df['average_price'] = list(average_prices.values())
oil_price_df = pd.merge(oil_price_df, avg_prices_df, on=['country', 'year'], how='left')
#####################################################################################
#Now, I want to calculate the the average for the average_price_gap
def fiscal_year(row):
    if row['month'] >= 7:  # Fiscal year starts in July
        return f"{row['year']}/{row['year'] + 1}"
    else:
        return f"{row['year'] - 1}/{row['year']}"
oil_price_df['fiscal_year'] = oil_price_df.apply(fiscal_year, axis=1)
def fiscal_year(row):
    if row['month'] >= 7:  # Fiscal year starts in July
        return f"{row['year']}/{row['year'] + 1}"
    else:
        return f"{row['year'] - 1}/{row['year']}"
oil_price_df['fiscal_year'] = oil_price_df.apply(fiscal_year, axis=1)
average_price_gaps = {}
for country, group in oil_price_df.groupby('country'):
    years = group['year'].unique()
    for year in range(min(years) + 4, max(years) + 1):
        relevant_fiscal_years = [
            f"{year-4}/{year-3}",
            f"{year-3}/{year-2}",
            f"{year-2}/{year-1}",
            f"{year-1}/{year}"
        ]
        
        filtered_data = group[group['fiscal_year'].isin(relevant_fiscal_years)]
        average_price_gap = filtered_data['bmgap2015adj'].mean()
        average_price_gaps[(country, year)] = average_price_gap
avg_price_gaps_df = pd.DataFrame(list(average_price_gaps.keys()), columns=['country', 'year'])
avg_price_gaps_df['average_price_gap'] = list(average_price_gaps.values())
oil_price_df = pd.merge(oil_price_df, avg_price_gaps_df, on=['country', 'year'], how='left')
##################################################################################

#Now i have to calculate the price votality (standard deviation) in the fiscal years:
def fiscal_year(row):
    if row['month'] >= 7:  # Fiscal year starts in July
        return f"{row['year']}/{row['year'] + 1}"
    else:
        return f"{row['year'] - 1}/{row['year']}"
oil_price_df['fiscal_year'] = oil_price_df.apply(fiscal_year, axis=1)
price_volatility = {}
for country, group in oil_price_df.groupby('country'):
    years = group['year'].unique()
    for year in range(min(years) + 4, max(years) + 1):
        relevant_fiscal_years = [
            f"{year-4}/{year-3}",
            f"{year-3}/{year-2}",
            f"{year-2}/{year-1}",
            f"{year-1}/{year}"
        ]
        filtered_data = group[group['fiscal_year'].isin(relevant_fiscal_years)]
        price_vol = filtered_data['price_usd_2015'].std()
        price_volatility[(country, year)] = price_vol
price_volatility_df = pd.DataFrame(list(price_volatility.keys()), columns=['country', 'year'])
price_volatility_df['price_volatility'] = list(price_volatility.values())
oil_price_df = pd.merge(oil_price_df, price_volatility_df, on=['country', 'year'], how='left')
#############################################################
#I want to calculate Average Gasoline Consumption:
# Step 1: Define the fiscal year calculation function
def fiscal_year(row):
    if row['month'] >= 7:  # Fiscal year starts in July
        return f"{row['year']}/{row['year'] + 1}"
    else:
        return f"{row['year'] - 1}/{row['year']}"
oil_price_df['fiscal_year'] = oil_price_df.apply(fiscal_year, axis=1)
average_gasoline_consumption = {}
for country, group in oil_price_df.groupby('country'):
    years = group['year'].unique()
    for year in range(min(years) + 4, max(years) + 1):
        relevant_fiscal_years = [
            f"{year-4}/{year-3}",
            f"{year-3}/{year-2}",
            f"{year-2}/{year-1}",
            f"{year-1}/{year}"
        ]
        filtered_data = group[group['fiscal_year'].isin(relevant_fiscal_years)]
        avg_gasoline_consumption = filtered_data['gasolinecons'].mean()
        average_gasoline_consumption[(country, year)] = avg_gasoline_consumption
avg_gasoline_df = pd.DataFrame(list(average_gasoline_consumption.keys()), columns=['country', 'year'])
avg_gasoline_df['average_gasoline_consumption'] = list(average_gasoline_consumption.values())
oil_price_df = pd.merge(oil_price_df, avg_gasoline_df, on=['country', 'year'], how='left')
###############################################################################################

#I want to calculate for the Average of Emission:
# Assuming your DataFrame is named 'oil_price_df' and has columns 'year', 'month', 'emissions', and 'country'
# Step 1: Define the fiscal year calculation function
def fiscal_year(row):
    if row['month'] >= 7:  # Fiscal year starts in July
        return f"{row['year']}/{row['year'] + 1}"
    else:
        return f"{row['year'] - 1}/{row['year']}"
oil_price_df['fiscal_year'] = oil_price_df.apply(fiscal_year, axis=1)
average_emissions = {}
for country, group in oil_price_df.groupby('country'):
    years = group['year'].unique()
    for year in range(min(years) + 4, max(years) + 1):
        relevant_fiscal_years = [
            f"{year-4}/{year-3}",
            f"{year-3}/{year-2}",
            f"{year-2}/{year-1}",
            f"{year-1}/{year}"
        ]
        
        filtered_data = group[group['fiscal_year'].isin(relevant_fiscal_years)]
        avg_emission = filtered_data['emissions'].mean()
        average_emissions[(country, year)] = avg_emission
avg_emissions_df = pd.DataFrame(list(average_emissions.keys()), columns=['country', 'year'])
avg_emissions_df['average_emission'] = list(average_emissions.values())
oil_price_df = pd.merge(oil_price_df, avg_emissions_df, on=['country', 'year'], how='left')
#Now, I want to calculate the the average for the benchmark price
def fiscal_year(row):
    if row['month'] >= 7:  # Fiscal year starts in July
        return f"{row['year']}/{row['year'] + 1}"
    else:
        return f"{row['year'] - 1}/{row['year']}"
oil_price_df['fiscal_year'] = oil_price_df.apply(fiscal_year, axis=1)
average_benchmark_price = {}
for country, group in oil_price_df.groupby('country'):
    years = group['year'].unique()
    for year in range(min(years) + 4, max(years) + 1):
        relevant_fiscal_years = [
            f"{year-4}/{year-3}",
            f"{year-3}/{year-2}",
            f"{year-2}/{year-1}",
            f"{year-1}/{year}"
        ]
        filtered_data = group[group['fiscal_year'].isin(relevant_fiscal_years)]
        avg_benchmark = filtered_data['benchmark_2015_adj'].mean()
        average_benchmark_price[(country, year)] = avg_benchmark
avg_benchmark_df = pd.DataFrame(list(average_benchmark_price.keys()), columns=['country', 'year'])
avg_benchmark_df['avg_benchmark_df'] = list(average_benchmark_price.values())
oil_price_df = pd.merge(oil_price_df, avg_benchmark_df, on=['country', 'year'], how='left')



# Apply the function to each year in the DataFrame and create a new column
#Now i want to merge the oil_price_df to the merged_df matching by "country_name" and "year"
##########################################################################################
oil_price_df['country'] = oil_price_df['country'].replace({
    'Macedonia, FYR': 'Noth Macedonia',
    'Dominican Republic': 'Dominica'
})
oil_price_df.to_csv('oil_price_data.csv', index=False)
selected_columns = ['country', 'year', 'average_price', 'price_volatility', 'average_price_gap', 'average_gasoline_consumption','average_emission', 'avg_benchmark_df']
unique_df = oil_price_df[selected_columns].drop_duplicates(subset=['country', 'year'])
print(unique_df.head())
unique_df = unique_df.rename(columns={'country': 'country_name'})
merged_data_final = pd.merge(merged_df, unique_df, on=['country_name', 'year'], how='left')
merged_data_final.to_csv('merged_data_final.csv', index=False)
###########################################################################################3
#drop all year <2007
# Assuming your DataFrame is named merge_data_final and has a column 'year'
merge_data_final_filtered = merged_data_final
merge_data_final_filtered = merge_data_final_filtered.reset_index(drop=True)
print(merge_data_final_filtered)
merged_df_2 = merge_data_final_filtered.merge(data_all_countries[['idstd', 'a0']], on='idstd', how='left')
merged_df_2 = merged_df_2.drop(columns=['stra_sector'])
cols = list(merged_df_2.columns)
cols.insert(1, cols.pop(cols.index('a0')))
merged_df_2 = merged_df_2[cols]
##############################################################################################
#Now, i want to create for Dummy variables for industry:
idstd_to_sector = data_all_countries.set_index('idstd')['stra_sector'].to_dict()
def replace_indicator(row):
    if row['a0'] == 'Indicator':
        return idstd_to_sector.get(row['idstd'], row['a0'])
    return row['a0']
merged_df_2['a0'] = merged_df_2.apply(replace_indicator, axis=1)
print(merged_df_2['a0'].unique()) #check again
dummy_columns_to_drop = ['a0_Manufacturing', 'a0_Services', 'a0_Core','a0_Indicator']  # Replace with actual dummy column names
dummies = pd.get_dummies(merged_df_2['a0'], prefix='a0')
merged_df_2 = pd.concat([merged_df_2, dummies], axis=1)
print(merged_df_2['a0'].unique())

#Now, i want to calculate for the dummy variable for column 'size'
size_dummies = pd.get_dummies(merged_df_2['size'], prefix='size')
merged_df_2 = pd.concat([merged_df_2, size_dummies], axis=1)
#Now, i have to clean the data for column 'ccp_cc'
merged_df_2['ccp_cc'] = merged_df_2['ccp_cc'].str.replace("2. ", "", regex=False)
merged_df_2['ccp_cc'] = merged_df_2['ccp_cc'].str.replace("1. ", "", regex=False)
print(merged_df_2[['ccp_cc']].head())  # Displaying only the 'ccp_cc' column for verification
unique_countries = merged_df_2['country_name'].unique()
print(unique_countries)
#################################################
#Now, i will calculate the average GDP per capital
qog_data_subset = qog_data_subset.sort_values(by=['country_name', 'year'])
# Step 2: Create the 'GDP_Year' column by shifting the 'wdi_gdpcapcon2015' values by 1 year within each country
qog_data_subset['GDP Percapita'] = qog_data_subset.groupby('country_name')['wdi_gdpcapcon2015'].shift(1)
qog_data_subset['average_GDP_percapita'] = qog_data_subset.groupby('country_name')['wdi_gdpcapcon2015'].transform(lambda x: x.shift(1).rolling(3).mean())
qog_data_subset['country_name'] = qog_data_subset['country_name'].replace('Viet Nam', 'Vietnam')
merged_df_3 = merged_df_2.merge(qog_data_subset[['country_name', 'year', 'GDP Percapita','average_GDP_percapita']],
                               on=['country_name', 'year'],
                               how='left')
merged_df_3 = merged_df_3.drop(columns=['ross_gas_value_2014', 'ross_oil_value_2014'])
boolean_columns = merged_df_3.select_dtypes(include=['bool']).columns
merged_df_3[boolean_columns] = merged_df_3[boolean_columns].astype(int)
print(merged_df_3.head())
merged_df_3.to_csv('Finale.csv', index=False)
columns_to_match_2 = ['idstd', 'b7', 'b2b', 'k3bc', 'd3b', 'd3c', 'size', 'd3a', 'b5', 'c22b']
data_b_subset = data_all_countries[columns_to_match_2]
# Merging the dataframes on 'firm_id'
merged_df_4 = pd.merge(merged_df_3, data_b_subset, on='idstd', how='left')
# Display the merged dataframe
print(merged_df_4)
#####Now i want to calculate the the age of firms:
merged_df_4['b5'] = pd.to_numeric(merged_df_4['b5'], errors='coerce')
merged_df_4 = merged_df_4.dropna(subset=['b5'])
merged_df_4['b5'] = merged_df_4['b5'].astype(int)
merged_df_4['institution_age'] = 2024 - merged_df_4['b5']
merged_df_4 = merged_df_4[merged_df_4['institution_age'] > 0]
merged_df_4['institution_age_ln'] = np.log(merged_df_4['institution_age'])
merged_df_4['b7_x'] = pd.to_numeric(merged_df_4['b7_x'], errors='coerce')
merged_df_4 = merged_df_4.dropna(subset=['b7_x'])
merged_df_4['b7_x'] = merged_df_4['b7_x'].astype(int)
#### Now i drop c22b:
merged_df_4 = merged_df_4[merged_df_4['c22b'] != "Don't Know (Spontaneous)"]
merged_df_4 = merged_df_4.drop(columns=['b7_y', 'b2b_y', 'k3bc_y'])
merged_df_4 = merged_df_4.drop(columns=['size_y'])
### Drop Nan in b2b column:
merged_df_4['b2b_x'] = pd.to_numeric(merged_df_4['b2b_x'], errors='coerce')
merged_df_4 = merged_df_4.dropna(subset=['b2b_x'])
merged_df_4['b2b_x'] = merged_df_4['b2b_x'].astype(int)
### drop b2c b2d columns:
merged_df_4 = merged_df_4.drop(columns=['b2c', 'b2d'])
### drop l3a, l3b collumns:
merged_df_4 = merged_df_4.drop(columns=['l3a', 'l3b'])
# clean b8
merged_df_4 = merged_df_4[merged_df_4['b8'].isin(['Yes', 'No'])]
merged_df_4 = merged_df_4.drop(columns=['e2b'])
merged_df_4['b8'] = merged_df_4['b8'].replace({'Yes': 1, 'No': 0})
columns_to_update = ['h1', 'h5', 'h8', 'l10', 'ccp_cc', 'c22b']
# Replace "Yes" with 1 and "No" with 0 in the specified columns
merged_df_4[columns_to_update] = merged_df_4[columns_to_update].replace({'Yes': 1, 'No': 0})
merged_df_4 = merged_df_4.drop(columns=['d3b', 'd3a'])
# Merge all_countries with merged_df_4 on 'k30' from all_countries and 'itstd' from merged_df_4
merged_df_5 = pd.merge(merged_df_4, data_all_countries[['idstd', 'k30']], on='idstd', how='left')
merged_df_5 = merged_df_5[merged_df_5['k30'] != "Don't Know (Spontaneous)"]
merged_df_5 = merged_df_5[merged_df_5['k30'] != -8.0]
merged_df_5 = merged_df_5[merged_df_5['k30'] != "Does Not Apply"]
merged_df_5 = pd.get_dummies(merged_df_5, columns=['k30'], prefix='k30', drop_first=True)
merged_df_5 = merged_df_5.drop(columns=['k30_-8.0'])
merged_df_5 = merged_df_5.replace({True: 1, False: 0})
merged_df_5 = merged_df_5.drop(columns=['k30_Does Not Apply'])
merged_df_5['b2b_x'] = merged_df_5['b2b_x'].replace('%', '', regex=True).astype(float)
# Convert to binary: 1 if the value is different from 0, 0 otherwise
merged_df_5['b2b_x'] = merged_df_5['b2b_x'].apply(lambda x: 1 if x != 0 else 0)
## clean data:
merged_df_5 = merged_df_5.dropna(subset=['average_price_gap'])
merged_df_5.to_csv('merged_data_5.csv', index=False)
print(merged_df_5.columns)
merged_df_5.rename(columns=lambda x: x.strip().replace(' ', '_'), inplace=True)
merged_df_5 = merged_df_5.rename(columns={
    'b2b_x': 'foreign own',
    'h1': 'innovation_product',
    'h5': 'innovation_process',
    'b7_x': 'managerial_experience',
    'h8': 'r&d',
    'l10': 'formal_training',
    'ccp_cc': 'corruption',
    'c22b': 'website'
})
merged_df_6 = merged_df_5.dropna(subset=['innovation_product', 'foreign own', 'average_price_gap', 'managerial_experience', 'institution_age_ln', 
                                                   'size_Medium(20-99)', 'size_Large(100_And_Over)', 'website', 
                                                   'k30_Minor_obstacle', 'k30_Moderate_obstacle', 'k30_Major_obstacle', 
                                                   'k30_Very_severe_obstacle', 'a0_Manufacturing', 'a0_Services', 
                                                   'GDP_Percapita', 'average_emission', 'average_price', 'price_volatility','innovation_process'])
columns_to_filter = ['innovation_process', 'innovation_product', 'r&d', 'formal_training']

merged_df_6 = merged_df_6[~merged_df_6[columns_to_filter].isin(["Don't know (spontaneous)"]).any(axis=1)]
merged_df_6 = merged_df_6[merged_df_6['formal_training'] != "Don't Know (Spontaneous)"]
merged_df_6 = merged_df_6[merged_df_6['formal_training'] != -8]
merged_df_6['squared_mean_price'] = merged_df_6['average_price'] ** 2
# Taking the natural logarithm of 'squared_mean_price'.
merged_df_6['log_squared_mean_price'] = np.log(merged_df_6['squared_mean_price'])
merged_df_6['log_average_price_gap'] = np.log(merged_df_6['average_price_gap'])
merged_df_6['log_average_price'] = np.log(merged_df_6['average_price'])
unique_values_formal_training = merged_df_6['formal_training'].unique()
print(f"Unique values in 'formal_training': {unique_values_formal_training}")
merged_df_6.to_csv('merged_data_6.csv', index=False)
merged_df_6.rename(columns={'size_x': 'size'}, inplace=True)
# Expand the dataframe with more countries:
unique_countries = data_all_countries['country_name'].unique()
print("Unique countries:", unique_countries)
unique_countries_2 = merged_df_6['country_name'].unique()
print("Unique countries:", unique_countries_2)
unique_countries_expanded = list(set(unique_countries) - set(unique_countries_2))
print("Unique countries:", unique_countries_expanded)
unique_countries_expanded = data_all_countries[data_all_countries['country_name'].isin(unique_countries_expanded)]
unique_countries_expanded = unique_countries_expanded.drop(columns=['country'])
columns_1 = unique_countries_expanded.columns.tolist()
columns_1 = ['country_name', 'year'] + [col for col in columns_1 if col not in ['country_name', 'year']]
unique_countries_expanded = unique_countries_expanded[columns_1]
#Extracted Data_Frame:
columns_to_keep_2 = [
    'country_name', 'year', 'stra_sector', 'size', 'b2a', 'b2b', 'b2c', 'b2d',
    'b8', 'b7', 'e2b', 'h1', 'h2', 'h5', 'h8', 'k3bc', 'l3a', 'l3b', 'l10', 'idstd'
]
unique_countries_expanded = unique_countries_expanded[columns_to_keep_2]
countries_2 = unique_countries_expanded['country_name'].unique()
##################################################################################
#Merge with the data of Quality of Nation
file_path = r"D:\VGU\GFE\Programing Languge\Project_TrungDuc\Innovation Data\qog_bas_ts_jan24_stata14.dta"
# Load the Stata file into a DataFrame
qog_data = pd.read_stata(file_path)
unique_countries_expanded['year'] = unique_countries_expanded['year'].astype(int)
qog_data['year'] = qog_data['year'].astype(int)
qog_data = qog_data.rename(columns={'cname': 'country_name'})
columns_to_keep = ["country_name", "year", "ccp_cc", "mad_gdppc", "gle_gdp", 
                   "gle_imp", "iiag_be", "lis_gini", "pwt_pop", "gle_exp",
                   "ross_gas_value_2014", "ross_oil_value_2014", "wdi_co2", 'wdi_gdpcapcon2015','vdem_corr']
qog_data_subset = qog_data[columns_to_keep]
qog_data = qog_data_subset
merged_df_7 = pd.merge(unique_countries_expanded, qog_data, on=['country_name', 'year'], how='left')
merged_df_7 = merged_df_7[merged_df_7['year'] <= 2015]
###################################################################
oil_price_df.to_csv('oil_price_data.csv', index=False)
selected_columns = ['country', 'year', 'average_price', 'price_volatility', 'average_price_gap', 'average_gasoline_consumption','average_emission', 'avg_benchmark_df']
unique_df = oil_price_df[selected_columns].drop_duplicates(subset=['country', 'year'])
print(unique_df.head())
unique_df = unique_df.rename(columns={'country': 'country_name'})
unique_countries_unique_df = unique_df['country_name'].unique()
unique_countries_merged_df_7 = merged_df_7['country_name'].unique()
# Applying the corrections
merged_df_7['country_name'] = merged_df_7['country_name'].apply(lambda x: correct_country_name(x, country_corrections))

corrections = {
    'Egypt, Arab Rep.': 'Egypt',
    'Congo, Rep.': 'Congo, Dem. Rep.',
    'Kyrgyz Republic': 'Kyrgyzstan'
}
unique_df['country_name'] = unique_df['country_name'].replace(corrections)
merged_data_final_2 = pd.merge(merged_df_7, unique_df, on=['country_name', 'year'], how='left')
merged_data_final_2.to_csv('merged_data_final_2.csv', index=False)
##########################################################################################3
merged_df_9 = merged_data_final_2.merge(data_all_countries[['idstd', 'a0']], on='idstd', how='left')
merged_df_9 = merged_df_9.drop(columns=['stra_sector'])
cols = list(merged_df_9.columns)
cols.insert(1, cols.pop(cols.index('a0')))
merged_df_9 = merged_df_9[cols]
##############################################################################################
#Now, i want to calculate for Dummy variables for industry:
idstd_to_sector = data_all_countries.set_index('idstd')['stra_sector'].to_dict()
def replace_indicator(row):
    if row['a0'] == 'Indicator':
        return idstd_to_sector.get(row['idstd'], row['a0'])
    return row['a0']
merged_df_9['a0'] = merged_df_9.apply(replace_indicator, axis=1)
print(merged_df_9['a0'].unique()) #check again
dummy_columns_to_drop = ['a0_Manufacturing', 'a0_Services', 'a0_Core','a0_Indicator']  # Replace with actual dummy column names
dummies = pd.get_dummies(merged_df_9['a0'], prefix='a0')
merged_df_9 = pd.concat([merged_df_9, dummies], axis=1)
print(merged_df_9['a0'].unique())
#Now, i want to calculate for the dummy variable for column 'size'
size_dummies = pd.get_dummies(merged_df_9['size'], prefix='size')
merged_df_2 = pd.concat([merged_df_9, size_dummies], axis=1)
#Now, i have to clean the data for column 'ccp_cc'
# Step 1: Use str.replace() to remove the "2. " prefix from the 'ccp_cc' column
merged_df_9['ccp_cc'] = merged_df_9['ccp_cc'].str.replace("2. ", "", regex=False)
merged_df_9['ccp_cc'] = merged_df_9['ccp_cc'].str.replace("1. ", "", regex=False)
# Display the updated DataFrame
print(merged_df_9[['ccp_cc']].head())  # Displaying only the 'ccp_cc' column for verification
unique_countries = merged_df_9['country_name'].unique()
print(unique_countries)
#################################################
#Now, i will calculate the average GDP per capital
# Assuming your DataFrame is named 'qog_data_subset' and has columns 'year', 'country', and 'wdi_gdpcapcon2015'
# Step 1: Sort the DataFrame by 'country' and 'year' to ensure correct alignment
qog_data_subset = qog_data_subset.sort_values(by=['country_name', 'year'])
# Step 2: Create the 'GDP_Year' column by shifting the 'wdi_gdpcapcon2015' values by 1 year within each country
qog_data_subset['GDP Percapita'] = qog_data_subset.groupby('country_name')['wdi_gdpcapcon2015'].shift(1)
qog_data_subset['average_GDP_percapita'] = qog_data_subset.groupby('country_name')['wdi_gdpcapcon2015'].transform(lambda x: x.shift(1).rolling(3).mean())
qog_data_subset['average_corruption_index'] = qog_data_subset.groupby('country_name')['vdem_corr'].transform(lambda x: x.shift(1).rolling(3).mean())
qog_data_subset['country_name'] = qog_data_subset['country_name'].replace({
    'Viet Nam': 'Vietnam',
    'Tanzania, the United Republic of': 'Tanzania',
    'Moldova (the Republic of)': 'Moldova',
    'Philippines (the)': 'Philippines',
    'Congo (the Democratic Republic of the)': 'Congo, Dem. Rep.'
})
merged_df_10 = merged_df_9.merge(qog_data_subset[['country_name', 'year', 'GDP Percapita','average_GDP_percapita']],
                               on=['country_name', 'year'],
                               how='left')
merged_df_10 = merged_df_10.drop(columns=['ross_gas_value_2014', 'ross_oil_value_2014'])
boolean_columns = merged_df_10.select_dtypes(include=['bool']).columns
merged_df_10[boolean_columns] = merged_df_10[boolean_columns].astype(int)
print(merged_df_10.head())
columns_to_match_2 = ['idstd', 'b7', 'b2b', 'k3bc', 'd3b', 'd3c', 'size', 'd3a', 'b5', 'c22b']
data_b_subset = data_all_countries[columns_to_match_2]
# Merging the dataframes on 'firm_id'
merged_df_11 = pd.merge(merged_df_10, data_b_subset, on='idstd', how='left')
#####Now i want to calculate the the age of firms:
merged_df_11['b5'] = pd.to_numeric(merged_df_11['b5'], errors='coerce')
merged_df_11 = merged_df_11.dropna(subset=['b5'])
merged_df_11['b5'] = merged_df_11['b5'].astype(int)
merged_df_11['institution_age'] = 2024 - merged_df_11['b5']
merged_df_11 = merged_df_11[merged_df_11['institution_age'] > 0]
merged_df_11['institution_age_ln'] = np.log(merged_df_11['institution_age'])
print(merged_df_11)
merged_df_11['b7_x'] = pd.to_numeric(merged_df_11['b7_x'], errors='coerce')
merged_df_11 = merged_df_11.dropna(subset=['b7_x'])
merged_df_11['b7_x'] = merged_df_11['b7_x'].astype(int)    
merged_df_11 = merged_df_11[merged_df_11['c22b'] != "Don't Know (Spontaneous)"]
merged_df_11 = merged_df_11.drop(columns=['b7_y', 'b2b_y', 'k3bc_y'])
merged_df_11 = merged_df_11.drop(columns=['size_y'])
merged_df_11['b2b_x'] = pd.to_numeric(merged_df_11['b2b_x'], errors='coerce')
merged_df_11 = merged_df_11.dropna(subset=['b2b_x'])
merged_df_11['b2b_x'] = merged_df_11['b2b_x'].astype(int)
merged_df_11 = merged_df_11.drop(columns=['b2c', 'b2d'])
merged_df_11 = merged_df_11.drop(columns=['l3a', 'l3b'])
# clean b8
merged_df_11 = merged_df_11[merged_df_11['b8'].isin(['Yes', 'No'])]
merged_df_11 = merged_df_11.drop(columns=['e2b'])
merged_df_11['b8'] = merged_df_11['b8'].replace({'Yes': 1, 'No': 0})
# List of columns to update
columns_to_update = ['h1', 'h5', 'h8', 'l10', 'ccp_cc', 'c22b']
# Replace "Yes" with 1 and "No" with 0 in the specified columns
merged_df_11[columns_to_update] = merged_df_11[columns_to_update].replace({'Yes': 1, 'No': 0})
merged_df_11 = merged_df_11.drop(columns=['d3b', 'd3a'])
# Merge all_countries with merged_df_4 on 'k30' from all_countries and 'itstd' from merged_df_4
merged_df_12 = pd.merge(merged_df_11, data_all_countries[['idstd', 'k30']], on='idstd', how='left')
## Create dummy varibale for variable k30:
##clean k30:
merged_df_12 = merged_df_12[merged_df_12['k30'] != "Don't Know (Spontaneous)"]
merged_df_12 = merged_df_12[merged_df_12['k30'] != -8.0]
merged_df_12 = merged_df_12[merged_df_12['k30'] != "Does Not Apply"]
merged_df_12 = pd.get_dummies(merged_df_12, columns=['k30'], prefix='k30', drop_first=True)
merged_df_12 = merged_df_12.drop(columns=['k30_-8.0'])
merged_df_12 = merged_df_12.replace({True: 1, False: 0})
merged_df_12 = merged_df_12.drop(columns=['k30_Does Not Apply'])
## convert column b2b:
# Convert 'b2b' column to numeric values by removing '%' and converting to float
merged_df_12['b2b_x'] = merged_df_12['b2b_x'].replace('%', '', regex=True).astype(float)
# Convert to binary: 1 if the value is different from 0, 0 otherwise
merged_df_12['b2b_x'] = merged_df_12['b2b_x'].apply(lambda x: 1 if x != 0 else 0)
## clean data:
merged_df_12 = merged_df_12.dropna(subset=['average_price_gap'])
merged_df_12.to_csv('merged_data_5.csv', index=False)
print(merged_df_12.columns)
merged_df_12.rename(columns=lambda x: x.strip().replace(' ', '_'), inplace=True)
merged_df_12 = merged_df_12.rename(columns={
    'b2b_x': 'foreign own',
    'h1': 'innovation_product',
    'h5': 'innovation_process',
    'b7_x': 'managerial_experience',
    'h8': 'r&d',
    'l10': 'formal_training',
    'ccp_cc': 'corruption',
    'c22b': 'website'
})
#create dummies for company size:
merged_df_12.rename(columns={'size_x': 'size'}, inplace=True)
dummy_df = pd.get_dummies(merged_df_12['size'], prefix='size')
merged_df_12 = pd.concat([merged_df_12, dummy_df], axis=1)    
columns_to_filter = ['innovation_process', 'innovation_product', 'r&d', 'formal_training']
merged_df_12 = merged_df_12[~merged_df_12[columns_to_filter].isin(["Don't know (spontaneous)"]).any(axis=1)]
merged_df_12 = merged_df_12[merged_df_12['formal_training'] != "Don't Know (Spontaneous)"]
merged_df_12 = merged_df_12[merged_df_12['formal_training'] != -8]
merged_df_12['squared_mean_price'] = merged_df_12['average_price'] ** 2
# Taking the natural logarithm of 'squared_mean_price'.
merged_df_12['log_squared_mean_price'] = np.log(merged_df_12['squared_mean_price'])
merged_df_12['log_average_price_gap'] = np.log(merged_df_12['average_price_gap'])
merged_df_12['log_average_price'] = np.log(merged_df_12['average_price'])
unique_values_formal_training = merged_df_12['formal_training'].unique()
print(f"Unique values in 'formal_training': {unique_values_formal_training}")
merged_df_12.replace({True: 1, False: 0}, inplace=True)
merged_df_12.to_csv('merged_df_12.csv', index=False)
merged_df_6.rename(columns={'size_Large(100_And_Over)': 'size_Large(100 And Over)'}, inplace=True)
##merge 2 dataframe:
merged_result = pd.concat([merged_df_6, merged_df_12], ignore_index=True)
merged_result = merged_result.drop(['log_average_price_gap', 'gle_gdp', 'gle_imp', 'iiag_be', 'lis_gini'], axis=1)
columns_list = merged_result.columns.tolist()
print(columns_list)
###Calculate the log_average_price_gap
merged_result['log_benchmark_price'] = np.log(merged_result['avg_benchmark_df'])
merged_result['log_average_price_gap'] = merged_result['log_average_price'] - merged_result['log_benchmark_price']
###Merge with the the TRPK Data:
file_path = "Firm Level TFP Estimates and Factor Ratios_July_5_2024.dta"
# Reading the .dta file into a DataFrame
df = pd.read_stata(file_path)
merged_result_1 = merged_result.merge(df[['idstd', 'l1', 'n2a', 'income', 'tfprVAKL']], on='idstd', how='left')
# I want to create the dataframe for productivity:
merged_result_2 = merged_result_1.dropna(subset=['innovation_product'])
# Getting the unique values in the 'year' column
unique_years = merged_result_2['year'].unique()
### after extended the data, we have 38156 observations with 57 countries 
columns_to_exclude = [
    'a0_Chemicals_&_Chemical_Products', 'a0_Food', 'a0_Garments', 
    'a0_IT_&_IT_Services', 'a0_Machinery_&_Equipment', 
    'a0_Other_Services', 'a0_Rest_of_Universe', 'a0_Retail'
]
# Drop the columns from the DataFrame
merged_result_1 = merged_result_1.drop(columns=columns_to_exclude)
if 'a0' in merged_result_1.columns:
    merged_result_1 = merged_result_1.drop(columns=['a0'])
firm_innovation = pd.merge(merged_result_1, data_all_countries[['idstd', 'a0']], on='idstd', how='left')
firm_innovation.rename(columns={'a0': 'industry'}, inplace=True)
dummies = pd.get_dummies(firm_innovation['industry'], prefix='industry')
firm_innovation = pd.concat([firm_innovation, dummies], axis=1)
firm_innovation.rename(columns={'foreign own': 'foreign_own'}, inplace=True)
firm_innovation.rename(columns={'num.employee': 'num_employee'}, inplace=True)
firm_innovation.rename(columns={'size_Small(<20)': 'sizesmall'}, inplace=True)
firm_innovation.rename(columns={'size_Medium(20-99)': 'sizemedium'}, inplace=True)
firm_innovation = firm_innovation.dropna(subset=['innovation_product'])
firm_innovation = firm_innovation[firm_innovation['innovation_product'] != -8]
firm_innovation = firm_innovation.rename(columns={
    'l1': 'number_employee',
    'n2a': 'labour_cost'
})

#print(firm_innovation['labour_cost'].dtype)
missing_corruption = firm_innovation[firm_innovation['corruption'].isna()]
# Display the missing values with corresponding country names
missing_corruption[['country_name', 'corruption']]
#I want to clean the data:
firm_innovation = firm_innovation.drop(columns=['corruption'])
qog_data_subset = qog_data_subset.sort_values('year')
qog_data_subset['corruption'] = qog_data_subset.groupby('country_name')['ccp_cc'].shift(1)
qog_data_subset = qog_data_subset.sort_index()
qog_data_subset['country_name'] = qog_data_subset['country_name'].replace({
    'Philippines (the)': 'Philippines',
    'Tanzania, the United Republic of': 'Tanzania',
    'Bolivia (Plurinational State of)': 'Bolivia',
    'Congo (the)': 'Congo, Dem. Rep.',
    'Vietnam, North': 'Vietnam',
    'Moldova (the Republic of)': 'Moldova'
})
firm_innovation = firm_innovation.merge(
    qog_data_subset[['country_name', 'year', 'corruption']],  # columns to merge from qog_data_subset
    on=['country_name', 'year'],  # merging on both country_name and year
    how='left'  # use left merge to keep all rows in firm_innovation
)
firm_innovation['corruption'] = firm_innovation['corruption'].replace({
    '1. Yes': 1,
    '2. No': 0
})
missing_corruption = firm_innovation[firm_innovation['corruption'].isna()]
print(missing_corruption)
firm_innovation = firm_innovation[firm_innovation['corruption'] != '96. Other']

firm_innovation['log_average_emission'] = np.log(firm_innovation['average_emission'])
firm_innovation['log_price_volatility'] = np.log(firm_innovation['price_volatility'].replace(0, np.nan))
firm_innovation['log_GDP_Percapita'] = np.log(firm_innovation['GDP_Percapita'])
firm_innovation['log_average_GDP_percapita'] = np.log(firm_innovation['average_GDP_percapita'])
firm_innovation = pd.merge(
    firm_innovation, 
    qog_data_subset[['year', 'country_name', 'average_corruption_index']], 
    on=['year', 'country_name'], 
    how='left'
)

year_counts = firm_innovation['year'].value_counts().sort_index()
print(year_counts)
firm_innovation = pd.get_dummies(firm_innovation, columns=['year'], drop_first=True)
firm_innovation = pd.get_dummies(firm_innovation, columns=['income'], drop_first=True)
firm_innovation = firm_innovation.rename(columns={"income_Low Income": "low_income"})
firm_innovation = firm_innovation.rename(columns={"corruption": "corruption_commission"})
firm_innovation.to_excel('firm_innovation.xlsx', index=False)



################################################# REGRESSION MODEL ######################################################
                                                 
                                                #FIRM PRODUCTIVITY
## WE NEED TO IMPORT THE EXPORTED EXCEL FILE (ABOVE) AGAIN TO RUN THE REGRESSION, PLEASE RUN THE FILE_PATH CODE OF YOUR COMPUTER BELOW TO DO REGRESSION
file_path = 'D:/VGU/GFE/Programing Languge/Project_TrungDuc/Innovation Data/firm_productivity.xlsx'
df = pd.read_excel(file_path)

import statsmodels.api as sm
import statsmodels.formula.api as smf

# Assuming your data is in a pandas DataFrame called 'firm_productivity'

# Define the formula for the multiple linear regression
model_formula = (
    "tfprVAKL ~ foreign_own + managerial_experience + formal_training + website + "
    "institution_age_ln + log_squared_mean_price + low_income + "
    "log_average_price_gap + log_average_emission + log_price_volatility + log_GDP_Percapita + "
    "corruption_commission  + sizesmall + sizemedium + corruption_index + "
    "k30_No_obstacle + k30_Minor_obstacle + k30_Moderate_obstacle + k30_Major_obstacle + year_2009 + year_2012 + year_2013 + year_2014 + year_2015 + year_2010 + year_2011 "
)

model = smf.ols(formula=model_formula, data=df).fit()

# Print the summary of the model
print(model.summary())

##Interaction term for the log_average_price_gap*log_price_volatily:

model_formula = (
    "tfprVAKL ~ foreign_own + managerial_experience + formal_training + website + "
    "institution_age_ln + log_squared_mean_price + low_income + "
    "log_average_price_gap * log_price_volatility + "  # Interaction term
    "log_average_emission + log_GDP_Percapita + "
    "corruption_commission + sizesmall + sizemedium + corruption_index + "
    "k30_No_obstacle + k30_Minor_obstacle + k30_Moderate_obstacle + k30_Major_obstacle + "
    "year_2009 + year_2012 + year_2013 + year_2014 + year_2015 + year_2010 + year_2011"
)

# Fit the OLS model with the interaction term
model = smf.ols(formula=model_formula, data=df).fit()

# Print the summary of the model
print(model.summary())
# TEST FOR tfprVAKL for stationary:
from statsmodels.tsa.stattools import adfuller
productivity = df['tfprVAKL']  # Dependent variable
# Perform ADF test on 'tfprVAk' (productivity)
result = adfuller(productivity.dropna())  # Drop NaN values if any

# Extract and display results
print("ADF Statistic: {:.4f}".format(result[0]))
print("p-value: {:.4f}".format(result[1]))
print("Critical Values:")
for key, value in result[4].items():
    print(f"   {key}: {value:.4f}")
    
    
    
#GEE Models for Firm Productivity
import statsmodels.formula.api as smf
from statsmodels.genmod.cov_struct import Exchangeable

model_formula = (
    "tfprVAKL ~ foreign_own + managerial_experience + formal_training + website + "
    "institution_age_ln + log_squared_mean_price + corruption_commission + corruption_index + low_income + "
    "log_average_price_gap + log_average_emission + log_price_volatility + log_GDP_Percapita + "
    "sizesmall + sizemedium + "
    "k30_No_obstacle + k30_Minor_obstacle + k30_Moderate_obstacle + k30_Major_obstacle + "
    "year_2012 + year_2013 + year_2014 + year_2015 + year_2010 + year_2009 "
)

# Define the GEE model, assuming 'country' is the grouping variable for clustering
gee_model = smf.gee(
    formula=model_formula, 
    data=df, 
    groups=df['country_name'],  # Replace 'country' with the appropriate grouping variable
    cov_struct=Exchangeable()  # Define the correlation structure, e.g., Exchangeable or Autoregressive
)

# Fit the model
gee_results = gee_model.fit()

# Print the summary of the model
print(gee_results.summary())
log_likelihood = gee_results.llf  # Log-likelihood of the fitted model
num_params = len(gee_results.params)  # Number of parameters in the model

# Calculate QIC
qic = -2 * log_likelihood + 2 * num_params

# Print the QIC value
print(f"QIC: {qic}")

### Include interaction term:
import statsmodels.formula.api as smf
from statsmodels.genmod.cov_struct import Exchangeable

model_formula = (
    "tfprVAKL ~ foreign_own + managerial_experience + formal_training + website + "
    "institution_age_ln + log_squared_mean_price + corruption_commission + corruption_index + low_income + "
    "log_average_price_gap * log_price_volatility + "  # Interaction term
    "log_average_emission + log_GDP_Percapita + "
    "sizesmall + sizemedium + "
    "k30_No_obstacle + k30_Minor_obstacle + k30_Moderate_obstacle + k30_Major_obstacle + "
    "year_2012 + year_2013 + year_2014 + year_2015 + year_2010 + year_2009"
)

# Define the GEE model, assuming 'country' is the grouping variable for clustering
gee_model = smf.gee(
    formula=model_formula, 
    data=df, 
    groups=df['country_name'],  # Replace 'country_name' with the appropriate grouping variable
    cov_struct=Exchangeable()  # Define the correlation structure, e.g., Exchangeable or Autoregressive
)

# Fit the model
gee_results = gee_model.fit()
# Print the summary of the model
print(gee_results.summary())
# Calculate QIC
log_likelihood = gee_results.llf  # Log-likelihood of the fitted model
num_params = len(gee_results.params)  # Number of parameters in the model
# Calculate QIC
qic = -2 * log_likelihood + 2 * num_params
# Print the QIC value
print(f"QIC: {qic}")
##############################################################################################################################
                                                     #FIRM_INNOVATION
import statsmodels.formula.api as smf
import pandas as pd
file_path = 'D:/VGU/GFE/Programing Languge/Project_TrungDuc/Innovation Data/firm_innovation.xlsx'
df_1 = pd.read_excel(file_path)

# Define the formula for the probit regression model
probit_formula = (
    "innovation_product ~ foreign_own + managerial_experience + formal_training + website + "
    "institution_age_ln + log_squared_mean_price + "
    "log_average_price_gap + log_average_emission + log_price_volatility + log_average_GDP_percapita + low_income + "
    "a0_Services + a0_Manufacturing + sizesmall + sizemedium + year_2012 + year_2013 + average_corruption_index + year_2015 + "
    "year_2014 + corruption_commission + "
    "k30_No_obstacle + k30_Minor_obstacle + k30_Moderate_obstacle + k30_Major_obstacle"
)

probit_model = smf.probit(formula=probit_formula, data=df_1).fit()
print(probit_model.summary())
marginal_effects = probit_model.get_margeff()
print(marginal_effects.summary())
probit_model_robust = smf.probit(formula=probit_formula, data=df_1).fit(cov_type='HC3')
print(probit_model_robust.summary())

#GEE Model

import statsmodels.formula.api as smf
from statsmodels.genmod.cov_struct import Exchangeable

# Define the formula for the GEE logistic regression model
logit_formula = (
    "innovation_product ~ foreign_own + managerial_experience + formal_training + website + "
    "institution_age_ln + log_squared_mean_price + average_corruption_index + "
    "log_average_price_gap + log_average_emission + log_price_volatility + log_average_GDP_percapita + "
    "a0_Services + a0_Manufacturing + sizesmall + sizemedium + year_2011 + year_2012 + year_2013 + "
    " corruption_commission + low_income + "
    "k30_No_obstacle + k30_Minor_obstacle + k30_Moderate_obstacle + k30_Major_obstacle"
)


gee_model = smf.gee(
    formula=logit_formula, 
    data=df_1, 
    groups=df_1['country_name'],  # Replace 'country' with your actual grouping variable (e.g., firms or countries)
    family=sm.families.Binomial(),  # Logistic regression requires a binomial family
    cov_struct=Exchangeable()  # Define the correlation structure, e.g., Exchangeable or Independent
)

gee_results = gee_model.fit()
print(gee_results.summary())
gee_results_robust = gee_model.fit(cov_type='robust')
print(gee_results_robust.summary())
# Calculate QIC
log_likelihood = gee_results.llf  # Log-likelihood of the fitted model
num_params = len(gee_results.params)  # Number of parameters in the model
# Calculate QIC
qic = -2 * log_likelihood + 2 * num_params
# Print the QIC value
print(f"QIC: {qic}")

##interaction term for probit regression:
probit_formula = (
    "innovation_product ~ foreign_own + managerial_experience + formal_training + website + "
    "institution_age_ln + log_squared_mean_price + "
    "log_average_price_gap * log_price_volatility + average_price + log_average_emission + "
    "log_average_GDP_percapita + a0_Services + a0_Manufacturing + sizesmall + sizemedium + "
    "year_2012 + year_2013 + average_corruption_index + year_2011 + year_2014 + corruption_commission + "
    "k30_No_obstacle + k30_Minor_obstacle + k30_Moderate_obstacle + k30_Major_obstacle"
)

# Fit the Probit model
probit_model = smf.probit(formula=probit_formula, data=df_1).fit()

# Print the summary of the model
print(probit_model.summary())

marginal_effects = probit_model.get_margeff()
print(marginal_effects.summary())

## GEE Regression with interaction term
gee_formula = (
    "innovation_product ~ foreign_own + managerial_experience + formal_training + website + "
    "institution_age_ln + log_squared_mean_price + average_corruption_index + "
    "log_average_price_gap * log_price_volatility + log_average_emission + log_average_GDP_percapita + "
    "a0_Services + a0_Manufacturing + sizesmall + sizemedium + year_2013 + year_2011 + year_2012 + "
    "corruption_commission + "
    "k30_No_obstacle + k30_Minor_obstacle + k30_Moderate_obstacle + k30_Major_obstacle"
)
# Define the GEE model with a binomial family and an Exchangeable correlation structure
gee_model = smf.gee(
    formula=gee_formula, 
    data=df_1, 
    groups=df_1['country_name'],  # Group by country or other clusters in your dataset
    family=sm.families.Binomial(),  # Logistic regression requires a binomial family
    cov_struct=Exchangeable()  # Exchangeable correlation structure
)
# Fit the GEE model
gee_result = gee_model.fit()
# Print the summary of the GEE model
print(gee_result.summary())
# Calculate QIC
log_likelihood = gee_results.llf  # Log-likelihood of the fitted model
num_params = len(gee_results.params)  # Number of parameters in the model
# Calculate QIC
qic = -2 * log_likelihood + 2 * num_params
# Print the QIC value
print(f"QIC: {qic}")
                                       
                                                     # Process Innovation:
probit_formula = (
    "innovation_process ~ foreign_own + managerial_experience + formal_training + website + "
    "institution_age_ln + log_squared_mean_price + "
    "log_average_price_gap + log_average_emission + log_price_volatility + log_average_GDP_percapita + low_income + "
    "a0_Services + a0_Manufacturing + sizesmall + sizemedium + year_2012 + year_2013 + average_corruption_index + year_2011 + "
    "year_2014 + corruption_commission + "
    "k30_No_obstacle + k30_Minor_obstacle + k30_Moderate_obstacle + k30_Major_obstacle"
)

probit_model = smf.probit(formula=probit_formula, data=df_1).fit()
# Print the summary of the model
print(probit_model.summary())
marginal_effects = probit_model.get_margeff()

# Display the summary of the Marginal Effects
print(marginal_effects.summary())

import statsmodels.formula.api as smf
import statsmodels.api as sm
from statsmodels.genmod.cov_struct import Exchangeable

# GEE logistic regression model:
logit_formula = (
    "innovation_process ~ foreign_own + managerial_experience + formal_training + website + "
    "institution_age_ln + log_squared_mean_price + average_corruption_index + "
    "log_average_price_gap + log_average_emission + log_price_volatility + log_average_GDP_percapita + "
    "a0_Services + a0_Manufacturing + sizesmall + sizemedium + year_2013 + year_2015 + year_2014 + year_2011 + "
    " corruption_commission + "
    "k30_No_obstacle + k30_Minor_obstacle + k30_Moderate_obstacle + k30_Major_obstacle"
)

# Define the GEE model, using a binomial family for logistic regression and an Exchangeable correlation structure
gee_model = smf.gee(
    formula=logit_formula, 
    data=df_1, 
    groups=df_1['country_name'],  # Replace 'country' with your actual grouping variable (e.g., firms or countries)
    family=sm.families.Binomial(),  # Logistic regression requires a binomial family
    cov_struct=Exchangeable()  # Define the correlation structure, e.g., Exchangeable or Independent
)

# Fit the model
gee_results = gee_model.fit()
# Print the summary of the GEE model
print(gee_results.summary())
# Calculate QIC
log_likelihood = gee_results.llf  # Log-likelihood of the fitted model
num_params = len(gee_results.params)  # Number of parameters in the model
# Calculate QIC
qic = -2 * log_likelihood + 2 * num_params
# Print the QIC value
print(f"QIC: {qic}")
##interaction term:
probit_formula = (
    "innovation_process ~ foreign_own + managerial_experience + formal_training + website + "
    "institution_age_ln + log_squared_mean_price + "
    "log_average_price_gap * log_price_volatility + average_price + log_average_emission + "
    "log_average_GDP_percapita + a0_Services + a0_Manufacturing + sizesmall + sizemedium + "
    "year_2012 + year_2013 + average_corruption_index + year_2011 + year_2014 + corruption_commission + "
    "k30_No_obstacle + k30_Minor_obstacle + k30_Moderate_obstacle + k30_Major_obstacle"
)

# Fit the Probit model
probit_model = smf.probit(formula=probit_formula, data=df_1).fit()
# Print the summary of the model
print(probit_model.summary())
marginal_effects = probit_model.get_margeff()
# Display the summary of the Marginal Effects
print(marginal_effects.summary())

# Define the formula with the interaction term between log_price_volatility and log_average_price_gap
gee_formula = (
    "innovation_process ~ foreign_own + managerial_experience + formal_training + website + "
    "institution_age_ln + log_squared_mean_price + average_corruption_index + "
    "log_average_price_gap * log_price_volatility + log_average_emission + log_average_GDP_percapita + "
    "a0_Services + a0_Manufacturing + sizesmall + sizemedium + year_2013 + year_2011 + year_2015 + year_2014 + "
    "corruption_commission + "
    "k30_No_obstacle + k30_Minor_obstacle + k30_Moderate_obstacle + k30_Major_obstacle"
)
# Define the GEE model with a binomial family and an Exchangeable correlation structure
gee_model = smf.gee(
    formula=gee_formula, 
    data=df_1, 
    groups=df_1['country_name'],  # Group by country or other clusters in your dataset
    family=sm.families.Binomial(),  # Logistic regression requires a binomial family
    cov_struct=Exchangeable()  # Exchangeable correlation structure
)
# Fit the GEE model
gee_result = gee_model.fit()
# Print the summary of the GEE model
print(gee_result.summary())
# Calculate QIC
log_likelihood = gee_results.llf  # Log-likelihood of the fitted model
num_params = len(gee_results.params)  # Number of parameters in the model
# Calculate QIC
qic = -2 * log_likelihood + 2 * num_params
# Print the QIC value
print(f"QIC: {qic}")
