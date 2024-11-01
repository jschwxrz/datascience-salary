import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


def show_salary_trends_by_experience_level(df):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='work_year', y='salary_in_usd', hue="experience_level")
    plt.title('Salary Trends by Experience Level (2020-2024)')
    plt.xlabel('Year')
    plt.ylabel('Average Salary (USD)')
    plt.legend(title='Experience Level', loc='upper right')
    plt.tight_layout()
    return st.pyplot(plt)
