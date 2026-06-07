# Fossil Fuel Policies and Firm Innovations: Evidence from a Developing Countries Database

**Presented at:** The 10th International Conference on Sustainable Urban Development (ICSUD), October 03, 2024  
**Authors:** Dr. Le Van Ha - Supervisor, Le Dang Trung Duc - Speaker/Author, Nguyen Quoc Minh - Co-Author

**Institution:** Vietnamese-German University (VGU) - Global Finance and Economics (GFE)  

---

## 📌 Abstract & Motivation

Innovation is a key driver of economic growth and competitiveness, particularly in developing countries characterized by rapid economic transitions and market volatility. In such environments, fuel prices significantly impact production costs, operational strategies, and market dynamics. 

This project explores the empirical relationship between national fossil fuel price regulations (taxes, subsidies, and price volatility) and firm-level innovation (product and process) across developing nations. By understanding this relationship, we aim to provide actionable insights for policymakers to design fuel regulations that foster technological adoption and resilience while maintaining economic stability.

## 📊 Data Infrastructure

The empirical analysis is constructed by integrating four distinct datasets via firm-level identifiers and temporal alignment:

1. **World Bank Enterprise Survey (WBES) & Innovation Follow-up Survey (IFS):** Standardized survey data encompassing 321,500 firm-level observations across 47 developing countries (2011–2015).
2. **Global Gasoline Price Data:** Monthly retail gasoline prices and international benchmark prices to calculate national net taxes and subsidies.
3. **Quality of Government (QoG):** National-level macroeconomic and institutional controls (e.g., GDP per capita, Corruption Index).
4. **Total Factor Productivity (TFP):** Firm-level productivity estimates utilizing the Cobb-Douglas production function framework.

## 🔬 Methodology

Due to the hierarchical and non-panel structure of the data (firms nested within industries, nested within countries over time), we employ robust econometric frameworks to account for unobserved heterogeneity and within-cluster correlations.

### 1. Firm Innovation (Binary Outcomes)
To evaluate the propensity of a firm to introduce a new product or process, we utilize **Probit Regression** and **Multilevel/GEE Logistic Regression Models**:

$$logit(P(Y_{ij}=1))=\beta_{0}+\sum_{k=1}^{K}\beta_{k}X_{ijk}+u_{j}$$

For interaction effects (e.g., Price Gap $\times$ Price Volatility):

$$logit(P(Y_{ij}=1))=\beta_{0}+\beta_{1}X_{1ij}+\beta_{2}X_{2j}+\beta_{3}(X_{1ij}\times X_{2ij})+u_{j}$$

Where $u_{j}\sim N(0,\sigma_{y}^{2})$ represents the random effect for country $j$.

### 2. Firm Productivity (Continuous Outcomes)
To evaluate the impact on Total Factor Productivity (`tfprVAKL`), we utilize **Ordinary Least Squares (OLS)** and **GEE Models** with population-averaged estimates and an Exchangeable correlation structure.

## 💡 Key Findings

* **The Dual Effect of Taxation:** High taxation (a positive average price gap) sends a signal to reduce consumption or shift towards alternatives, incentivizing product innovation. Firms facing higher fuel costs are driven to innovate as a strategic response to operational pressures.
* **The U-Shaped Productivity Curve:** The squared mean price exhibits a statistically significant impact on productivity, suggesting that while moderate price increases may initially hinder productivity, sustained high prices eventually force firms to find efficiencies and adapt.
* **Volatility Undermines Policy:** The interaction term between `average_price_gap` and `price_volatility` is significantly negative. High market volatility creates uncertainty, making consumers and firms risk-averse and hesitant to invest in energy-efficient technologies, thereby neutralizing the intended behavioral shifts of both tax and subsidy policies.

## 🏛 Policy Implications

1. **Prioritize Market Stability:** For fuel taxation or subsidy frameworks to successfully drive innovation, governments and regulators must first focus on reducing extreme market volatility. A predictable pricing environment allows economic agents to better assess and react to policy signals.
2. **Targeted Innovation Support:** Governments should couple fuel taxation with direct tax incentives or subsidies for R&D to help firms navigate cost pressures while upgrading their technological capabilities.

## 🚀 Repository Structure & Usage

* `/data/`: Contains the raw `.dta` files (WBES, QoG, Gasoline Prices, TFP). *(Note: Proprietary datasets may require access permissions).*
* `/scripts/`: Python scripts for data cleaning, merging, rolling average calculations (e.g., 1-year vs 3-year fiscal lag definitions), and econometric modeling using `statsmodels`.
* `/output/`: Generated analytical datasets (`firm_innovation.xlsx`, `firm_productivity.xlsx`) and regression summary logs.
* `/docs/`: Conference slide deck and the technical programming language report.

### Running the Analysis
```bash
# 1. Clone the repository
git clone [https://github.com/yourusername/fossil-fuel-innovation.git](https://github.com/yourusername/fossil-fuel-innovation.git)

# 2. Install dependencies
pip install pandas numpy statsmodels openpyxl

# 3. Execute the main pipeline
python scripts/main_analysis.py
