import streamlit as st
import pandas as pd

st.title('Machine Learning Test App')

st.info('Test of machine learning model')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
df
