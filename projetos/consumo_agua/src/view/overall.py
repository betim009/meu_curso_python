import os
import pandas as pd


class OverallStats:
    def __init__(self, file_csv, alias):
        self.file_csv = file_csv
        self.alias = alias

    def overall_average(self):
        try:
            path = f"./data/processed/overall_{self.alias}_average.csv"
            if os.path.exists(path):
                show = pd.read_csv(path)
                print(show)
            else:
                df = pd.read_csv(self.file_csv)
                col_consumo = df["Consumo"]

                media = col_consumo.mean()
                mediana = col_consumo.median()
                moda = col_consumo.mode()[0]
                maior = col_consumo.max()
                menor = col_consumo.min()

                show = {
                    "Média": [media],
                    "Mediana": [mediana],
                    "Moda": [moda],
                    "Maior Consumo": [maior],
                    "Menor Consumo": [menor],
                }

                show = pd.DataFrame(show)
                show.to_csv(path, index=False)
                print(show)
        except Exception as e:
            print(f"Erro ao calcular estatísticas: {e}")
            return False

    def overall_group_average(self, coluna):
        try:
            path = f"./data/processed/overall_{self.alias}_{coluna.lower()}_average.csv"
            if os.path.exists(path):
                show = pd.read_csv(path)
                print(show)
            else:
                df = pd.read_csv(self.file_csv)
                show = (
                    df.groupby(coluna)["Consumo"]
                    .agg(
                        Quantidade="count",
                        Media="mean",
                        Mediana="median",
                        Moda=lambda x: x.mode()[0] if not x.mode().empty else None,
                        Maior_Consumo="max",
                        Menor_Consumo="min",
                    )
                    .reset_index()
                )
                show.to_csv(path, index=False)
                print(show)
        except Exception as e:
            print(f"Erro ao calcular estatísticas por {coluna}: {e}")
            return False

    def overall_class_average(self):
        return self.overall_group_average("Classe")

    def overall_region_average(self):
        return self.overall_group_average("Regiao")

    def overall_region_class_average(self):
        try:
            path = f"./data/processed/overall_{self.alias}_region_class_average.csv"
            if os.path.exists(path):
                show = pd.read_csv(path)
                print(show)
            else:
                df = pd.read_csv(self.file_csv)
                show = (
                    df.groupby(["Regiao", "Classe"])["Consumo"]
                    .agg(
                        Quantidade="count",
                        Media="mean",
                        Mediana="median",
                        Moda=lambda x: x.mode()[0] if not x.mode().empty else None,
                        Maior_Consumo="max",
                        Menor_Consumo="min",
                    )
                    .reset_index()
                )
                show.to_csv(path, index=False)
                print(show)
        except Exception as e:
            print(f"Erro ao calcular estatísticas por Região e Classe: {e}")
            return False


overall_sam = OverallStats("./data/file_0.csv", "consumo_sam")
overall_sam_uf = OverallStats("./data/file_1.csv", "consumo_sam_uf")
