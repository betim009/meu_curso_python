from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


CAMINHO_DADOS = Path(__file__).resolve().parents[1] / "dados" / "vendas_dashboard.csv"


@st.cache_data
def carregar_dados():
    df = pd.read_csv(CAMINHO_DADOS)
    df["data"] = pd.to_datetime(df["data"])
    return df


st.set_page_config(page_title="Filtros Interativos", layout="wide")
st.title("Dashboard com filtros")

df = carregar_dados()

st.sidebar.header("Filtros")

categorias = ["Todas"] + sorted(df["categoria"].unique())
categoria = st.sidebar.selectbox("Categoria", categorias)

produtos = st.sidebar.multiselect(
    "Produtos",
    options=sorted(df["produto"].unique()),
    default=sorted(df["produto"].unique()),
)

data_inicio = st.sidebar.date_input("Data inicial", df["data"].min().date())
data_fim = st.sidebar.date_input("Data final", df["data"].max().date())

df_filtrado = df.copy()

if categoria != "Todas":
    df_filtrado = df_filtrado[df_filtrado["categoria"] == categoria]

df_filtrado = df_filtrado[df_filtrado["produto"].isin(produtos)]
df_filtrado = df_filtrado[
    (df_filtrado["data"].dt.date >= data_inicio)
    & (df_filtrado["data"].dt.date <= data_fim)
]

if df_filtrado.empty:
    st.warning("Nenhuma venda encontrada para os filtros selecionados.")
    st.stop()

faturamento = df_filtrado["valor_total"].sum()
pedidos = df_filtrado["id_pedido"].nunique()
ticket_medio = faturamento / pedidos

col1, col2, col3 = st.columns(3)
col1.metric("Faturamento", f"R$ {faturamento:,.2f}")
col2.metric("Pedidos", pedidos)
col3.metric("Ticket medio", f"R$ {ticket_medio:,.2f}")

vendas_mes = df_filtrado.groupby("mes")["valor_total"].sum()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(vendas_mes.index, vendas_mes.values, marker="o")
ax.set_title("Faturamento filtrado por mes")
ax.set_xlabel("Mes")
ax.set_ylabel("Faturamento (R$)")
ax.grid(True, axis="y", alpha=0.3)
st.pyplot(fig)

st.dataframe(df_filtrado, use_container_width=True)
