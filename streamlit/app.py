import streamlit as st
import pandas as pd
import plotly.express as px

# Título da aplicação
st.title("Relatório de Vendas")

# Lendo o CSV
df = pd.read_csv("data.csv")

# Criando gráfico de barras com Plotly
fig = px.bar(df, x="vendedores", y="valor_venda", title="Vendas por Vendedor", text_auto=True)

# Exibindo no Streamlit
st.plotly_chart(fig)
