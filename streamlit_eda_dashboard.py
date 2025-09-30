# churn_dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Churn Analysis Dashboard", layout="wide")
st.title("Customer Churn Analysis Dashboard")

# --- Load Data ---
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['Churn_numerical'] = df['Churn'].map({'Yes':1,'No':0})
    return df

# Provide your CSV path here
df = load_data("/Users/suri/Downloads/group2_dataset.csv")

st.subheader("Churn Distribution")
churn_counts = df['Churn'].value_counts()
fig, ax = plt.subplots()
ax.pie(churn_counts, labels=churn_counts.index, autopct='%1.1f%%', startangle=90, colors=['lightcoral','skyblue'])
ax.set_title("Churn Distribution (Yes vs No)")
st.pyplot(fig)

st.subheader("Churn Distribution by Gender")
genders = df['gender'].unique()
for g in genders:
    data = df[df['gender'] == g]['Churn'].value_counts()
    fig, ax = plt.subplots(figsize=(5,5))
    ax.pie(data, labels=data.index, autopct='%1.1f%%', startangle=90, colors=['orange','lightgreen'])
    ax.set_title(f"Churn Distribution for {g}")
    st.pyplot(fig)

st.subheader("Churn by Senior Citizen Status")
fig, ax = plt.subplots(figsize=(6,5))
sns.countplot(x="SeniorCitizen", hue="Churn", data=df, palette="Set1", ax=ax)
ax.set_title("Churn Count by Senior Citizen Status")
st.pyplot(fig)

st.subheader("Churn by Partner Status")
fig, ax = plt.subplots(figsize=(6,5))
sns.countplot(x="Partner", hue="Churn", data=df, palette="Set3", ax=ax)
ax.set_title("Churn Count by Partner Status")
st.pyplot(fig)

st.subheader("Churn by Dependents")
fig, ax = plt.subplots(figsize=(6,5))
sns.countplot(x="Dependents", hue="Churn", data=df, palette="coolwarm", ax=ax)
ax.set_title("Churn Count by Dependents")
st.pyplot(fig)

st.subheader("Churn by Internet Service")
fig, ax = plt.subplots(figsize=(7,5))
sns.countplot(x="InternetService", hue="Churn", data=df, palette="Set2", ax=ax)
ax.set_title("Churn Count by Internet Service Type")
st.pyplot(fig)

# --- Service & Contract Analysis ---
service_cols = ['StreamingTV','StreamingMovies','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','Contract']
df_internet = df[df['InternetService'] != "None"]

for col in service_cols:
    churn_rate = df_internet.groupby(col)['Churn_numerical'].mean().reset_index()
    churn_rate.columns = [col,'ChurnRate']
    fig, ax = plt.subplots(figsize=(6,4))
    sns.barplot(x=col, y='ChurnRate', data=churn_rate, palette="Set2", ax=ax)
    ax.set_title(f"Churn Rate by {col}")
    ax.set_ylim(0,1)
    st.pyplot(fig)

st.subheader("Churn Rate by Total Services & Contract Type")
service_columns = ['PhoneService','InternetService','StreamingTV','StreamingMovies']
for col in service_columns:
    df[col+'_num'] = df[col].map({'Yes': 1, 'No': 0, 'DSL': 1, 'Fiber optic': 1, 'None': 0})
df['TotalServices'] = df[[col+'_num' for col in service_columns]].sum(axis=1)
churn_by_services = df.groupby(['TotalServices','Contract'])['Churn_numerical'].mean().reset_index()
fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x='TotalServices', y='Churn_numerical', hue='Contract', data=churn_by_services, palette="Set2", ax=ax)
ax.set_title("Churn Rate by Number of Services & Contract Type")
st.pyplot(fig)

st.subheader("Churn Rate by Contract Type")
churn_by_contract = df.groupby('Contract')['Churn_numerical'].mean().reset_index()
fig, ax = plt.subplots(figsize=(6,4))
sns.barplot(x='Contract', y='Churn_numerical', data=churn_by_contract, palette="Set2", ax=ax)
ax.set_title("Churn Rate by Contract Type")
st.pyplot(fig)

st.subheader("Churn by Payment Method")
fig, ax = plt.subplots()
pd.crosstab(df['PaymentMethod'], df['Churn']).plot(kind='bar', stacked=True, ax=ax)
ax.set_ylabel("Number of Customers")
ax.set_title("Churn by Payment Method")
st.pyplot(fig)

st.subheader("MonthlyCharges, TotalCharges, Tenure Analysis")
fig, axes = plt.subplots(1,3, figsize=(15,4))
sns.boxplot(x='Churn', y='MonthlyCharges', data=df, palette="Set1", ax=axes[0])
axes[0].set_title("Monthly Charges vs Churn")
sns.boxplot(x='Churn', y='TotalCharges', data=df, palette="Set2", ax=axes[1])
axes[1].set_title("Total Charges vs Churn")
sns.boxplot(x='Churn', y='tenure', data=df, palette="Set3", ax=axes[2])
axes[2].set_title("Tenure vs Churn")
st.pyplot(fig)

st.subheader("Tenure Distribution KDE Plot")
fig, ax = plt.subplots(figsize=(10,5))
sns.kdeplot(data=df, x='tenure', hue='Churn', fill=True, palette=['orange','lightgreen'], alpha=0.5, ax=ax)
ax.set_title("Tenure Distribution: Churners vs Non-Churners")
st.pyplot(fig)

st.subheader("Churn Rate by Tenure Buckets")
bins = [0,6,12,18,24,36,48,60,72]
labels = ['0-6','7-12','13-18','19-24','25-36','37-48','49-60','61-72']
df['tenure_bucket'] = pd.cut(df['tenure'], bins=bins, labels=labels, right=True)
churn_by_tenure = df.groupby('tenure_bucket')['Churn_numerical'].mean().reset_index()
churn_by_tenure['ChurnRate'] = churn_by_tenure['Churn_numerical']*100
fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(x='tenure_bucket', y='ChurnRate', data=churn_by_tenure, palette="Blues_d", ax=ax)
ax.set_title("Churn Rate by Tenure Buckets")
ax.set_ylim(0,50)
st.pyplot(fig)

st.subheader("Average Monthly Charges by Tenure Bucket")
stayed = df[df['Churn'] == 'No']
avg_monthly_by_tenure = stayed.groupby('tenure_bucket')['MonthlyCharges'].mean().reset_index()
avg_monthly_by_tenure.columns = ['TenureBucket','AvgMonthlyCharges']
fig, ax = plt.subplots(figsize=(8,4))
sns.barplot(x='TenureBucket', y='AvgMonthlyCharges', data=avg_monthly_by_tenure, palette="Greens_d", ax=ax)
ax.set_title("Average Monthly Charges by Tenure Bucket (Stayed Customers)")
st.pyplot(fig)

st.subheader("High vs Low Monthly Charges for Long-Tenure Customers")
long_tenure = df[df['tenure']>=24]
median_charge = long_tenure['MonthlyCharges'].median()
high_charge = long_tenure[long_tenure['MonthlyCharges']>median_charge]
low_charge = long_tenure[long_tenure['MonthlyCharges']<=median_charge]
high_churn_rate = high_charge['Churn_numerical'].mean()
low_churn_rate = low_charge['Churn_numerical'].mean()
fig, ax = plt.subplots()
ax.bar(['High Charges','Low Charges'], [high_churn_rate, low_churn_rate], color=['lightgrey','lightpink'])
ax.set_ylabel('Churn Rate')
ax.set_title('Churn Rate for Long-Tenure Customers by Monthly Charges')
st.pyplot(fig)

st.subheader("Customer Segment Churn Comparison")
segment1 = df[(df['InternetService']=='Fiber optic') & (df['StreamingTV']=='Yes') & (df['Contract']=='Month-to-month')]
segment2 = df[(df['InternetService']=='DSL') & (df['Contract']=='Two year')]
churn_segment1 = segment1['Churn_numerical'].mean()
churn_segment2 = segment2['Churn_numerical'].mean()
fig, ax = plt.subplots()
ax.bar(['Fiber+Streaming+Month','DSL+TwoYear'], [churn_segment1,churn_segment2], color=['lavender','green'])
ax.set_ylabel('Churn Rate')
ax.set_title('Churn Rate by Customer Segment')
st.pyplot(fig)

st.subheader("Top 10 Lowest Churn Customer Segments")
segments = df.groupby(['InternetService','Contract','StreamingTV']).agg(churn_rate=('Churn_numerical','mean')).reset_index()
segments_sorted = segments.sort_values('churn_rate').head(10)
fig, ax = plt.subplots(figsize=(12,6))
sns.barplot(
    x='churn_rate',
    y=segments_sorted.apply(lambda row: f"{row['InternetService']} | {row['Contract']} | {row['StreamingTV']}", axis=1),
    data=segments_sorted,
    palette='viridis',
    ax=ax
)
ax.set_xlabel('Churn Rate')
ax.set_ylabel('Customer Segment')
ax.set_title('Top 10 Customer Segments with Lowest Churn')
st.pyplot(fig)

st.subheader("Correlation Heatmap of Numerical Features")
numeric_cols = ['tenure','MonthlyCharges','TotalCharges','Churn_numerical']
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f", center=0, ax=ax)
ax.set_title('Correlation Heatmap of Numerical Features')
st.pyplot(fig)
