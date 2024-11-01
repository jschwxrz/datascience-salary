import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

def show_remote_ratio_by_work_year(df):
    work_arrangements = df.groupby(['work_year', 'remote_ratio']).size().unstack()
    work_arrangements.columns = ['On-site', 'Hybrid', 'Remote']
    work_arrangements.head()

    work_arrangements_total = work_arrangements.sum(axis=1)
    work_arrangements_pct = pd.DataFrame()
    for col in work_arrangements.columns:
        work_arrangements_pct[col] = work_arrangements[col] / work_arrangements_total * 100

    work_arrangements_pct = work_arrangements_pct[['Remote', 'Hybrid', 'On-site']]

    plot_data = work_arrangements_pct.reset_index().melt(
        id_vars=['work_year'],
        value_vars=['Remote', 'Hybrid', 'On-site'],
        var_name='Work Arrangement',
        value_name='Percentage'
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(data=plot_data, x='work_year', y='Percentage', hue='Work Arrangement')
    plt.title('Work Arrangements Percentage by Year')
    plt.xlabel('Work Year')
    plt.ylabel('Percentage (%)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    return st.pyplot(plt)