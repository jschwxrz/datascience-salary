import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def show_salary_by_experience_level(df):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='experience_level', y='salary_in_usd', data=df, order=['EN', 'MI', 'SE', 'EX'])
    plt.title('Salary Distribution by Experience Level')
    plt.xlabel('Experience Level')
    plt.ylabel('Salary (USD)')
    plt.xticks(ticks=['EN', 'MI', 'SE', 'EX'], labels=['Entry Level', 'Mid Level', 'Senior Level', 'Executive Level'], rotation=0)
    plt.tight_layout()
    return st.pyplot(plt)
