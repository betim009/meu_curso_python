import pandas as pd

DATA_PATH = "src/data/gestao_pagamentos.csv"


def _carregar_df():
    df = pd.read_csv(DATA_PATH, parse_dates=["data_pagamento"])
    df["valor_parcela"] = pd.to_numeric(df["valor_parcela"], errors="coerce")
    df["ano"] = df["data_pagamento"].dt.year
    df["mes"] = df["data_pagamento"].dt.month
    return df


def total_pagamentos():
    df = _carregar_df()
    return {
        "primeiro_pagamento": df["data_pagamento"].min().date().isoformat(),
        "ultimo_pagamento": df["data_pagamento"].max().date().isoformat(),
        "total_pagamentos": len(df),
    }


def total_pagamentos_mes(ano):
    df = _carregar_df()
    df_ano = df[df["ano"] == ano]
    agg = (
        df_ano.groupby("mes")["valor_parcela"]
        .agg(valor_total="sum", qtd_pagamentos="size")
        .sort_index()
    )
    return agg.to_dict(orient="index")




def resgatar_pagemtnso_mes(ano, mes):
    """
    Total pago em um mês/ano específico.
    Retorna float (0 se não houver pagamentos no período).
    """
    df = _carregar_df()
    df_filt = df[(df["ano"] == ano) & (df["mes"] == mes)]
    return float(df_filt["valor_parcela"].sum())
