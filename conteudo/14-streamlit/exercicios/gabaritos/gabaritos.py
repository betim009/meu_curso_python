from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


CAMINHO_DADOS = Path(__file__).resolve().parents[2] / "dados" / "vendas_dashboard.csv"


@st.cache_data
def carregar_dados():
    df = pd.read_csv(CAMINHO_DADOS)
    df["data"] = pd.to_datetime(df["data"])
    return df


def aplicar_filtros(df):
    st.sidebar.header("Filtros")

    categoria = st.sidebar.selectbox("Categoria", ["Todas"] + sorted(df["categoria"].unique()))
    produtos = st.sidebar.multiselect(
        "Produtos",
        sorted(df["produto"].unique()),
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

    return df_filtrado


def mostrar_kpis(df):
    faturamento = df["valor_total"].sum()
    pedidos = df["id_pedido"].nunique()
    ticket_medio = faturamento / pedidos
    produto_lider = df.groupby("produto")["quantidade"].sum().idxmax()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Faturamento", f"R$ {faturamento:,.2f}")
    col2.metric("Pedidos", pedidos)
    col3.metric("Ticket medio", f"R$ {ticket_medio:,.2f}")
    col4.metric("Produto mais vendido", produto_lider)


def mostrar_graficos(df):
    vendas_mes = df.groupby("mes")["valor_total"].sum()
    vendas_vendedor = df.groupby("vendedor")["valor_total"].sum().sort_values(ascending=False)

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
        ax.bar(vendas_vendedor.index, vendas_vendedor.values, color="seagreen")
        ax.set_title("Faturamento por vendedor")
        ax.set_xlabel("Vendedor")
        ax.set_ylabel("Faturamento (R$)")
        st.pyplot(fig)


def mostrar_tabela(df):
    st.subheader("Dados filtrados")
    st.dataframe(df, use_container_width=True)


def main():
    st.set_page_config(page_title="Gabarito Dashboard", layout="wide")
    st.title("Dashboard de Vendas - Gabarito")

    df = carregar_dados()
    df_filtrado = aplicar_filtros(df)

    if df_filtrado.empty:
        st.warning("Nenhum dado encontrado para os filtros selecionados.")
        st.stop()

    mostrar_kpis(df_filtrado)
    mostrar_graficos(df_filtrado)
    mostrar_tabela(df_filtrado)


if __name__ == "__main__":
    main()
