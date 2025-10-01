# 📊 Telco Customer Churn Analysis
# Overview
This project explores customer churn in the telecommunications industry using the Telco Customer Churn dataset. Through Exploratory Data Analysis (EDA) and machine learning, we aim to identify patterns and factors influencing customer retention.
# 📂 Dataset
The dataset includes customer-level information such as:
- Demographic Information: gender, senior citizen, partner, dependents
- Services: phone, multiple lines, internet, online security, online backup, device protection, tech support, streaming TV/movies
- Customer Account Information: Tenure, contract type, payment method, paperless billing, monthly charges, total charges
- Target: Churn (Yes/No)
Churn status (Yes = customer left, No = customer stayed)

# Key Analysis:
# 1. Churn Overview
- Overall churn percentage.
- Churn by demographics (gender, senior citizen, partner, dependents).
# 2. Service Usage & Churn
- Churn by internet service type.
- Churn by streaming/security/backup/tech support.
- Effect of multiple services on churn.
# 3. Contract & Billing
- Churn by contract type & payment method.
- Compare monthly/total charges & tenure for churned vs. non-churned.
- Outlier detection in charges & tenure.
# 4. Tenure & Loyalty
- Churn by tenure buckets.
- Identify critical churn threshold.
- Monthly charges trend across tenure for loyal customers.
# 5. Feature Correlation
- Correlation between tenure, monthly charges, total charges.
- Interaction: contract type × charges × churn.
# 6. Segmentation
- Segment churn by service + demographics.
- Identify groups with lowest churn.
# 7. Data Quality
- Missing values (e.g., blank TotalCharges).
- Outliers handling.
# 8. Visualizations
- Pie chart (Yes vs No churn).
- Bar chart/heatmap: churn by contract & internet.
- Boxplots: charges vs churn.
- Scatterplots: tenure vs total charges.
- Correlation heatmap.
# 🖥️ Streamlit Dashboard
- Interactive app to:
- Explore churn % and churn distribution.
- Filter by demographics, contract type, internet service.
- Visualize tenure, services, and billing effects on churn.
# 🔗 Resources
- **Streamlit Dashboard**: [Explore the interactive dashboard](https://telco-customer-churn-by-surendra.streamlit.app/)
- **Google Colab Notebook**: [Access the EDA and modeling notebook](https://colab.research.google.com/drive/10_JyV0oH1R9C_OVgTapmr0tmNge0KXVU?usp=sharing)
  
# Telco-Churn-structure/
 - ┣ 📄 README.md                    &emsp; # Project overview
 - ┣ 📄 churn_dashboard.py           &emsp; # Streamlit dashboard
 - ┣ 📄 analysis.ipynb               &emsp; # Notebook with EDA and analysis
 - ┣ 📂 data/                        &emsp; # Dataset files
 - ┣ 📄 requirements.txt             &emsp; # Python dependencies
