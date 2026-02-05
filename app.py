import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Teste",
    layout="wide"
)
st.title("Dash de teste")
st.write("Dashboard local")

df = pd.DataFrame(
    {"Categoria":["A","B","C","D"],
     "Valor":[10,25,40,55]
     }
)

st.bar_chart(df.set_index("Categoria"))