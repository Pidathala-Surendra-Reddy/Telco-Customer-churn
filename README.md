# Telco Customer Churn Analysis Dashboard
A Streamlit-based interactive dashboard for exploring and analyzing Telco customer churn. This dashboard provides visual insights into customer demographics, service usage, and churn behaviors to help understand patterns and trends.
Features
# Churn Overview
Pie chart showing percentage of customers who churned (Yes) vs stayed (No).
# Demographics Analysis
Churn distribution by gender, SeniorCitizen, Partner, and Dependents.
# Service Analysis
Churn by InternetService, StreamingTV, StreamingMovies, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport.
Churn rate by number of services and contract type.
# Contract and Payment
Churn rate by Contract type (Month-to-month, One year, Two year).
Churn by PaymentMethod.
# Charges & Tenure
Boxplots and violin plots of MonthlyCharges, TotalCharges, and tenure by churn status.
Churn rate by tenure buckets.
Average monthly charges by tenure for retained customers.
Comparison of churn for long-tenure customers with high vs low monthly charges.
# Customer Segmentation
Analyze churn behavior by service combinations and demographics (e.g., “Fiber + Streaming + Month-to-Month” vs “DSL + Two-Year Contract”).
Top customer segments with lowest churn.
# Correlation Analysis
Heatmap of numerical features (tenure, MonthlyCharges, TotalCharges) and churn correlations.
