import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def streamlit_setup():
    st.set_page_config(layout="wide")
    st.title("Data Science Salary Analysis")


def main():
    streamlit_setup()
    df = pd.read_csv('DataScience_salaries_2024.csv')


if __name__ == "__main__":
    main()