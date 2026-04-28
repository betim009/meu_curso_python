# Gabaritos Comentados - Streamlit

## 1. Primeiro app

```python
import streamlit as st

st.title("Primeiro app")
st.write("Exemplo simples de interface com Python.")

nome = st.text_input("Digite seu nome")

if st.button("Enviar"):
    st.success(f"Ola, {nome}!")
```

Explicacao: `text_input` recebe dados do usuario e `button` executa uma acao.

## 2. Mostrar tabela de vendas

```python
from pathlib import Path

import pandas as pd
import streamlit as st

CAMINHO = Path(__file__).resolve().parents[2] / "dados" / "vendas_dashboard.csv"

df = pd.read_csv(CAMINHO)

st.title("Tabela de vendas")
st.dataframe(df, use_container_width=True)
```

Explicacao: `st.dataframe()` mostra uma tabela interativa.

## 3. Criar KPIs

```python
faturamento = df["valor_total"].sum()
pedidos = df["id_pedido"].nunique()
ticket_medio = faturamento / pedidos

col1, col2, col3 = st.columns(3)
col1.metric("Faturamento", f"R$ {faturamento:,.2f}")
col2.metric("Pedidos", pedidos)
col3.metric("Ticket medio", f"R$ {ticket_medio:,.2f}")
```

Explicacao: `st.metric()` destaca indicadores importantes.

## 4. Mostrar primeiras linhas

```python
st.dataframe(df.head(10), use_container_width=True)
```

Explicacao: `head(10)` mostra as 10 primeiras linhas.

## 5. Filtro por cidade

```python
cidades = sorted(df["cidade"].unique())
cidade = st.selectbox("Cidade", cidades)

df_filtrado = df[df["cidade"] == cidade]

st.dataframe(df_filtrado, use_container_width=True)
```

Explicacao: `selectbox` permite escolher uma opcao.

## 6. Filtro por categoria

```python
categorias = ["Todas"] + sorted(df["categoria"].unique())
categoria = st.selectbox("Categoria", categorias)

if categoria == "Todas":
    df_filtrado = df
else:
    df_filtrado = df[df["categoria"] == categoria]

st.dataframe(df_filtrado, use_container_width=True)
```

Explicacao: a opcao `Todas` evita obrigar o usuario a escolher apenas uma categoria.

## 7. Filtro por produto com multiselect

```python
produtos = st.multiselect(
    "Produtos",
    options=sorted(df["produto"].unique()),
    default=sorted(df["produto"].unique()),
)

df_filtrado = df[df["produto"].isin(produtos)]

st.dataframe(df_filtrado, use_container_width=True)
```

Explicacao: `isin()` filtra linhas cujo produto esta na lista selecionada.

## 8. Grafico de faturamento por mes

```python
import matplotlib.pyplot as plt

vendas_mes = df.groupby("mes")["valor_total"].sum()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(vendas_mes.index, vendas_mes.values, marker="o")
ax.set_title("Faturamento por mes")
ax.set_xlabel("Mes")
ax.set_ylabel("Faturamento (R$)")
ax.grid(True, axis="y", alpha=0.3)

st.pyplot(fig)
```

Explicacao: `st.pyplot(fig)` exibe o grafico matplotlib no Streamlit.

## 9. Grafico de faturamento por produto

```python
vendas_produto = (
    df.groupby("produto")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(10, 4))
ax.bar(vendas_produto.index, vendas_produto.values)
ax.set_title("Faturamento por produto")
ax.tick_params(axis="x", rotation=45)

st.pyplot(fig)
```

Explicacao: barras sao boas para comparar categorias.

## 10. Filtro de periodo

```python
df["data"] = pd.to_datetime(df["data"])

data_inicio = st.date_input("Data inicial", df["data"].min().date())
data_fim = st.date_input("Data final", df["data"].max().date())

df_filtrado = df[
    (df["data"].dt.date >= data_inicio)
    & (df["data"].dt.date <= data_fim)
]

st.dataframe(df_filtrado, use_container_width=True)
```

Explicacao: datas precisam ser convertidas com `pd.to_datetime`.

## 11. Dashboard com KPIs e filtros

```python
df["data"] = pd.to_datetime(df["data"])

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

if df_filtrado.empty:
    st.warning("Nenhum dado encontrado.")
    st.stop()

faturamento = df_filtrado["valor_total"].sum()
pedidos = df_filtrado["id_pedido"].nunique()
ticket_medio = faturamento / pedidos

col1, col2, col3 = st.columns(3)
col1.metric("Faturamento", f"R$ {faturamento:,.2f}")
col2.metric("Pedidos", pedidos)
col3.metric("Ticket medio", f"R$ {ticket_medio:,.2f}")

st.dataframe(df_filtrado, use_container_width=True)
```

Explicacao: filtros na sidebar deixam o dashboard mais organizado.

## 12. Dashboard com dois graficos

```python
vendas_mes = df_filtrado.groupby("mes")["valor_total"].sum()
vendas_vendedor = df_filtrado.groupby("vendedor")["valor_total"].sum().sort_values(ascending=False)

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(vendas_mes.index, vendas_mes.values, marker="o")
    ax.set_title("Faturamento por mes")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(vendas_vendedor.index, vendas_vendedor.values)
    ax.set_title("Faturamento por vendedor")
    st.pyplot(fig)
```

Explicacao: `st.columns()` organiza graficos lado a lado.

## 13. Projeto organizado em funcoes

Veja o arquivo `gabaritos.py`, que contem um app completo organizado em funcoes.
