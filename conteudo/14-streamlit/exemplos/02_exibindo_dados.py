from pathlib import Path

import pandas as pd
import streamlit as st


CAMINHO_DADOS = Path(__file__).resolve().parents[1] / "dados" / "vendas_dashboard.csv"


@st.cache_data
def carregar_dados():
    return pd.read_csv(CAMINHO_DADOS)


st.set_page_config(page_title="Exibindo Dados", layout="wide")

st.title("Exibindo dados de vendas")

df = carregar_dados()

faturamento_total = df["valor_total"].sum()
quantidade_pedidos = df["id_pedido"].nunique()
ticket_medio = faturamento_total / quantidade_pedidos

col1, col2, col3 = st.columns(3)
col1.metric("Faturamento", f"R$ {faturamento_total:,.2f}")
col2.metric("Pedidos", quantidade_pedidos)
col3.metric("Ticket medio", f"R$ {ticket_medio:,.2f}")

st.subheader("Tabela de vendas")
st.dataframe(df, use_container_width=True)
