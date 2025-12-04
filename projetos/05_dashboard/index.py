import pandas as pd
import streamlit as st

from src.utils.pagamentos import total_pagamentos, total_pagamentos_mes

DATA_PATH = "src/data/gestao_pagamentos.csv"
MES_NOMES = ["", "Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]


@st.cache_data
def carregar_pagamentos():
    return pd.read_csv(DATA_PATH, parse_dates=["data_pagamento"])


def preparar_mensal(ano):
    mensal_dict = total_pagamentos_mes(ano)
    mensal_df = (
        pd.DataFrame.from_dict(mensal_dict, orient="index")
        .reset_index()
        .rename(columns={"index": "mes"})
        .sort_values("mes")
    )
    if "valor_total" not in mensal_df.columns:
        mensal_df["valor_total"] = 0
    if "qtd_pagamentos" not in mensal_df.columns:
        mensal_df["qtd_pagamentos"] = 0
    mensal_df["mes_nome"] = mensal_df["mes"].apply(lambda m: MES_NOMES[int(m)])
    return mensal_df


def main():
    st.set_page_config(page_title="Dashboard de Pagamentos", layout="wide")
    st.title("Dashboard de Pagamentos")

    df = carregar_pagamentos()
    if df.empty:
        st.warning("Nenhum pagamento encontrado no CSV.")
        return

    anos = sorted(df["data_pagamento"].dt.year.unique())
    ano_escolhido = st.selectbox("Selecione o ano", anos, index=len(anos) - 1)

    totais = total_pagamentos()
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de pagamentos", totais["total_pagamentos"])
    col2.metric("Primeiro pagamento", totais["primeiro_pagamento"])
    col3.metric("Ultimo pagamento", totais["ultimo_pagamento"])

    st.subheader("Pagamentos por mes")
    mensal_df = preparar_mensal(ano_escolhido)

    col_a, col_b = st.columns(2)
    col_a.bar_chart(mensal_df, x="mes_nome", y="valor_total")
    col_b.bar_chart(mensal_df, x="mes_nome", y="qtd_pagamentos")

    st.dataframe(mensal_df[["mes_nome", "valor_total", "qtd_pagamentos"]].reset_index(drop=True))

    st.subheader("Tabela completa de pagamentos")
    st.dataframe(df.sort_values("data_pagamento"))


if __name__ == "__main__":
    main()
