import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from plots.SalaryDistributionByCompanySize import show_salary_distribution_by_company_size
from plots.CorrelationMatrix import show_correlation_matrix
from plots.SalaryByExperienceLevel import show_salary_by_experience_level
from plots.HighestSalariesByJobTitle import show_highest_salaries_by_job_title
from plots.SalaryTrendsByExperienceLevel import show_salary_trends_by_experience_level
from plots.RemoteRationByWorkYear import show_remote_ratio_by_work_year


def streamlit_setup():
    st.set_page_config(layout="wide")


def main():
    streamlit_setup()
    df = pd.read_csv('DataScienceSalaries2024.csv')

    with st.sidebar:
        st.title("Data Science Salary Analysis")
        option = st.radio(
            "Select a Plot:",
        (
            "Descriptive Statistics",
            "Correlation Matrix",
            "Salary by Experience Level",
            "Highest Salaries by Job Title",
            "Salary Trends by Experience Level",
            "Remote Ratio by Work Year",
            "Salary Distribution by Company Size",
            "Summary",
        ),
    )
    if option == "Descriptive Statistics":
        st.header("Descriptive Statistics")
        st.image("images/descriptive_statistics.png")
        st.write("Figure 1: Descriptive statistics for key columns")
    elif option == "Correlation Matrix":
        st.header("Correlation Matrix")
        show_correlation_matrix(df)
        st.write("Figure 2: Correlation heatmap showing the relationships between the variables in the dataset. The strength of the correlation can be derived by the numerical value as well as the color (red showing positive, blue showing negative correlations ).")
    elif option == "Salary by Experience Level":
        st.header("Salary by Experience Level")
        show_salary_by_experience_level(df)
        st.write("Figure 3: Box plot illustrating the salary distributions across various experience levels. The median salary is represented by the central line, while the box boundaries denote the first and third quartiles. The remaining distribution is indicated by the whiskers, with outliers represented by points beyond the whiskers.")
    elif option == "Highest Salaries by Job Title":
        st.header("Highest Salaries by Job Title")
        show_highest_salaries_by_job_title(df)
        st.write("Figure 4: Bar chart illustrating the top 10 highest-paying data science job titles. The x-axis denotes the average annual salary in US dollars, while the y-axis represents the job titles.")
    elif option == "Salary Trends by Experience Level":
        st.header("Salary Trends by Experience Level")
        show_salary_trends_by_experience_level(df)
        st.write("Figure 5: Line plot showing the salary trends for different experience levels from 2021-2024. The shaded area around the line indicates a 95% confidence interval of the estimated average salary.")
    elif option == "Remote Ratio by Work Year":
        st.header("Remote Ratio by Work Year")
        show_remote_ratio_by_work_year(df)
        st.write("**Figure 6:** Bar charts illustrating the proportion of remote, hybrid, and on-site work arrangements. ")
    elif option == "Salary Distribution by Company Size":
        st.header("Salary Distribution by Company Size")
        show_salary_distribution_by_company_size(df)
        st.write("Figure 7: Box plots illustrating the salary distribution across company sizes.")
    elif option == "Summary":
        st.header("Summary")
        with open('text/summary.txt', 'r') as file:
            summary = file.read()
        st.write(summary)


if __name__ == "__main__":
    main()