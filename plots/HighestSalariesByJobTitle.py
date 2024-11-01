import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def show_highest_salaries_by_job_title(df):
    highest_salaries = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    sns.barplot(x=highest_salaries.values, y=highest_salaries.index)
    plt.title('Top 10 Highest Paying Data Science Jobs')
    plt.xlabel('Average Salary (USD)')
    plt.ylabel('Job Title')
    plt.tight_layout()
    return st.pyplot(plt)
