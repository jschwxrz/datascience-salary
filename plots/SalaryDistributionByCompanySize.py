import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def show_salary_distribution_by_company_size(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='company_size', y='salary_in_usd', data=df)
    plt.title('Salary Distribution by Company Size')
    plt.xlabel('Company Size')
    plt.ylabel('Salary')
    plt.xticks(ticks=[0, 1, 2], labels=['Small', 'Medium', 'Large'], rotation=0) 
    plt.tight_layout()
    return st.pyplot(plt)
