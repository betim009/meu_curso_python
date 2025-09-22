import pandas as pd
import numpy as np
import os


class SpreadStats:
    def __init__(self, file_csv="./data/file_0.csv"):
        self.file_csv = file_csv

    def spread_overral(self):
        try:
            df = pd.read_csv(self.file_csv)
            col_consumo = df["Consumo"]

            deviation = np.std(col_consumo, ddof=1)
            p25 = np.percentile(col_consumo, 25)
            p50 = np.percentile(col_consumo, 50)
            p75 = np.percentile(col_consumo, 75)

            show = {"Desvio": [deviation], "P25": [p25], "P50": [p50], "P75": [p75]}

            print(pd.DataFrame(show))
            path = "./data/processed/spread_overral.csv"
            if not os.path.exists(path):
                pd.DataFrame(show).to_csv(path, index=False)
        except Exception as e:
            print(f"Erro ao calcular spread geral: {e}")
            return False

    def spread_class_consumo(self):
        try:
            df = pd.read_csv(self.file_csv)
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
            path = "./data/processed/spread_class_consumo.csv"
            if not os.path.exists(path):
                show.to_csv(path, index=False)
        except Exception as e:
            print(f"Erro ao calcular spread por Classe: {e}")
            return False

    def spread_region_consumo(self):
        try:
            df = pd.read_csv(self.file_csv)
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
            path = "./data/processed/spread_region_consumo.csv"
            if not os.path.exists(path):
                show.to_csv(path, index=False)
        except Exception as e:
            print(f"Erro ao calcular spread por Região: {e}")
            return False

    def spread_region_class_consumo(self):
        try:
            df = pd.read_csv(self.file_csv)
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
            path = "./data/processed/spread_region_class_consumo.csv"
            if not os.path.exists(path):
                show.to_csv(path, index=False)
        except Exception as e:
            print(f"Erro ao calcular spread por Região e Classe: {e}")
            return False


spread = SpreadStats()