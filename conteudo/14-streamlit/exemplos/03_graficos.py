from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


CAMINHO_DADOS = Path(__file__).resolve().parents[1] / "dados" / "vendas_dashboard.csv"


@st.cache_data
def carregar_dados():
    return pd.read_csv(CAMINHO_DADOS)


st.set_page_config(page_title="Graficos", layout="wide")
st.title("Graficos com Streamlit e Matplotlib")

df = carregar_dados()

vendas_mes = df.groupby("mes")["valor_total"].sum()
vendas_produto = (
    df.groupby("produto")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(vendas_mes.index, vendas_mes.values, marker="o", color="steelblue")
    ax.set_title("Faturamento por mes")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Faturamento (R$)")
    ax.grid(True, axis="y", alpha=0.3)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(vendas_produto.index, vendas_produto.values, color="seagreen")
    ax.set_title("Faturamento por produto")
    ax.set_xlabel("Produto")
    ax.set_ylabel("Faturamento (R$)")
    ax.tick_params(axis="x", rotation=45)
    st.pyplot(fig)
