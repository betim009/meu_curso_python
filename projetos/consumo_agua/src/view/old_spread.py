import pandas as pd
import numpy as np


def spread_overral():
    try:
        df = pd.read_csv("./data/file_0.csv")
        col_consumo = df["Consumo"]

        deviation = np.std(col_consumo, ddof=1)
        p25 = np.percentile(col_consumo, 25)
        p50 = np.percentile(col_consumo, 50)
        p75 = np.percentile(col_consumo, 75)

        show = {"Desvio": [deviation], "P25": [p25], "P50": [p50], "P75": [p75]}

        print(pd.DataFrame(show))
        pd.DataFrame(show).to_csv("./data/processed/spread_overral.csv", index=False)
    except Exception as e:
        print(f"Erro ao calcular o desvio: {e}")
        return False


def spread_class_consumo():
    try:
        df = pd.read_csv("./data/file_0.csv")

        show = (
            df.groupby("Classe")["Consumo"]
            .agg(
                Desvio=lambda x: np.std(x, ddof=1),
                P25=lambda x: np.percentile(x, 25),
                P50=lambda x: np.percentile(x, 50),
                P75=lambda x: np.percentile(x, 75),
            )
            .reset_index()
        )

        print(show)
        show.to_csv("./data/processed/spread_class_consumo.csv", index=False)
    except Exception as e:
        print(f"Erro ao calcular spread por Classe: {e}")
        return False


def spread_region_consumo():
    try:
        df = pd.read_csv("./data/file_0.csv")

        show = (
            df.groupby("Regiao")["Consumo"]
            .agg(
                Desvio=lambda x: np.std(x, ddof=1),
                P25=lambda x: np.percentile(x, 25),
                P50=lambda x: np.percentile(x, 50),
                P75=lambda x: np.percentile(x, 75),
            )
            .reset_index()
        )

        print(show)
        show.to_csv("./data/processed/spread_region_consumo.csv", index=False)
    except Exception as e:
        print(f"Erro ao calcular spread por Região: {e}")
        return False


def spread_region_class_consumo():
    try:
        df = pd.read_csv("./data/file_0.csv")

        show = (
            df.groupby(["Regiao", "Classe"])["Consumo"]
            .agg(
                Desvio=lambda x: np.std(x, ddof=1),
                P25=lambda x: np.percentile(x, 25),
                P50=lambda x: np.percentile(x, 50),
                P75=lambda x: np.percentile(x, 75),
            )
            .reset_index()
        )

        print(show)
        show.to_csv("./data/processed/spread_region_class_consumo.csv", index=False)
    except Exception as e:
        print(f"Erro ao calcular spread por Região e Classe: {e}")
        return False
