import streamlit as st
import pandas as pd

st.title("📊 Dashboard Nativo do Streamlit")

# -------------------------
# Dados de exemplo
# -------------------------
df = pd.DataFrame({
    "mes": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "vendas": [10, 15, 8, 20, 18, 25],
    "clientes": [5, 8, 3, 10, 9, 12]
})

# -------------------------
# Filtro
# -------------------------
st.sidebar.header("Filtros")

mostrar_clientes = st.sidebar.checkbox("Mostrar número de clientes")

# -------------------------
# KPI
# -------------------------
st.subheader("📌 Indicadores")

col1, col2 = st.columns(2)

col1.metric("Total de Vendas", df["vendas"].sum())
col2.metric("Média de Vendas por Mês", round(df["vendas"].mean(), 2))

# -------------------------
# Gráfico de Barras (Nativo)
# -------------------------
st.subheader("📊 Vendas por Mês (Bar Chart)")
st.bar_chart(df, x="mes", y="vendas")

# -------------------------
# Gráfico de Linha (Nativo)
# -------------------------
st.subheader("📈 Evolução das Vendas (Line Chart)")
st.line_chart(df, x="mes", y="vendas")

# -------------------------
# Gráfico opcional
# -------------------------
if mostrar_clientes:
    st.subheader("👥 Clientes por Mês (Area Chart)")
    st.area_chart(df, x="mes", y="clientes")

# -------------------------
# Tabela
# -------------------------
st.subheader("📋 Tabela de Dados")
st.dataframe(df)