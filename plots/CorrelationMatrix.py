import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


def show_correlation_matrix(df):
    df_encoded = df.copy()
    categorical_columns = ['experience_level', 'employment_type', 'job_title', 
                      'employee_residence', 'company_location', 'company_size',
                      'salary_currency']
    for column in categorical_columns:
        df_encoded[column] = df_encoded[column].astype('category').cat.codes

    plt.figure(figsize=(10, 6))
    sns.heatmap(df_encoded.corr(), 
                annot=True, 
            cmap='coolwarm', 
                center=0, 
                fmt='.2f')
    plt.xticks(rotation=45, ha='right')
    plt.title('Correlation Matrix of Key Variables')
    plt.tight_layout()
    return st.pyplot(plt)
