from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


CAMINHO_DADOS = Path(__file__).resolve().parents[1] / "dados" / "vendas_dashboard.csv"
ORDEM_MESES = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]


@st.cache_data
def carregar_dados():
    df = pd.read_csv(CAMINHO_DADOS)
    df["data"] = pd.to_datetime(df["data"])
    df["mes"] = pd.Categorical(df["mes"], categories=ORDEM_MESES, ordered=True)
    return df


def aplicar_filtros(df):
    st.sidebar.header("Filtros")

    data_inicio = st.sidebar.date_input("Data inicial", df["data"].min().date())
    data_fim = st.sidebar.date_input("Data final", df["data"].max().date())

    categoria = st.sidebar.selectbox("Categoria", ["Todas"] + sorted(df["categoria"].unique()))

    produtos = st.sidebar.multiselect(
        "Produtos",
        options=sorted(df["produto"].unique()),
        default=sorted(df["produto"].unique()),
    )

    vendedores = st.sidebar.multiselect(
        "Vendedores",
        options=sorted(df["vendedor"].unique()),
        default=sorted(df["vendedor"].unique()),
    )

    cidades = st.sidebar.multiselect(
        "Cidades",
        options=sorted(df["cidade"].unique()),
        default=sorted(df["cidade"].unique()),
    )

    df_filtrado = df.copy()
    df_filtrado = df_filtrado[
        (df_filtrado["data"].dt.date >= data_inicio)
        & (df_filtrado["data"].dt.date <= data_fim)
    ]

    if categoria != "Todas":
        df_filtrado = df_filtrado[df_filtrado["categoria"] == categoria]

    df_filtrado = df_filtrado[df_filtrado["produto"].isin(produtos)]
    df_filtrado = df_filtrado[df_filtrado["vendedor"].isin(vendedores)]
    df_filtrado = df_filtrado[df_filtrado["cidade"].isin(cidades)]

    return df_filtrado


def mostrar_kpis(df):
    faturamento = df["valor_total"].sum()
    pedidos = df["id_pedido"].nunique()
    ticket_medio = faturamento / pedidos
    produto_mais_vendido = df.groupby("produto")["quantidade"].sum().idxmax()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Faturamento total", f"R$ {faturamento:,.2f}")
    col2.metric("Pedidos", pedidos)
    col3.metric("Ticket medio", f"R$ {ticket_medio:,.2f}")
    col4.metric("Produto mais vendido", produto_mais_vendido)


def grafico_faturamento_mes(df):
    vendas_mes = df.groupby("mes", observed=False)["valor_total"].sum().reindex(ORDEM_MESES, fill_value=0)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(vendas_mes.index, vendas_mes.values, marker="o", color="steelblue")
    ax.set_title("Faturamento por mes")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Faturamento (R$)")
    ax.grid(True, axis="y", alpha=0.3)
    return fig


def grafico_faturamento_produto(df):
    vendas_produto = (
        df.groupby("produto")["valor_total"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(vendas_produto.index, vendas_produto.values, color="seagreen")
    ax.set_title("Faturamento por produto")
    ax.set_xlabel("Produto")
    ax.set_ylabel("Faturamento (R$)")
    ax.tick_params(axis="x", rotation=45)
    return fig


def grafico_faturamento_vendedor(df):
    vendas_vendedor = (
        df.groupby("vendedor")["valor_total"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(vendas_vendedor.index, vendas_vendedor.values, color="slateblue")
    ax.set_title("Faturamento por vendedor")
    ax.set_xlabel("Vendedor")
    ax.set_ylabel("Faturamento (R$)")
    return fig


def grafico_forma_pagamento(df):
    pagamentos = df.groupby("forma_pagamento")["valor_total"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.pie(pagamentos.values, labels=pagamentos.index, autopct="%1.1f%%", startangle=90)
    ax.set_title("Participacao por forma de pagamento")
    return fig


def mostrar_graficos(df):
    st.subheader("Analises visuais")

    st.pyplot(grafico_faturamento_mes(df))

    col1, col2 = st.columns(2)

    with col1:
        st.pyplot(grafico_faturamento_produto(df))

    with col2:
        st.pyplot(grafico_faturamento_vendedor(df))

    st.pyplot(grafico_forma_pagamento(df))


def mostrar_tabela(df):
    st.subheader("Dados detalhados")
    colunas = [
        "id_pedido",
        "data",
        "cliente",
        "cidade",
        "produto",
        "categoria",
        "vendedor",
        "quantidade",
        "valor_total",
    ]
    st.dataframe(df[colunas].sort_values("data"), use_container_width=True)


def main():
    st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

    st.title("Dashboard de Analise de Vendas")
    st.write("Painel interativo para acompanhar indicadores comerciais.")

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
