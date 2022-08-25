import streamlit as st
import pandas as pd

st.write('Hola mundo')

data = pd.read_csv('data/churn_operacion_1.csv')

st.dataframe(data)
