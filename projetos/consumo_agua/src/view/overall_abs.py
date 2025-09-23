from abc import ABC
import pandas as pd
import os


class OverallBase(ABC):
    def __init__(self, file_csv, alias):
        self.file_csv = file_csv
        self.alias = alias

    def overall_average(self):
        path = f"./data/processed/overall_{self.alias}_average.csv"
        if os.path.exists(path):
            show = pd.read_csv(path)
        else:
            df = pd.read_csv(self.file_csv)
            show = {
                "Média": df["Consumo"].mean(),
                "Mediana": df["Consumo"].median(),
                "Moda": df["Consumo"].mode().iloc[0],
                "Máximo": df["Consumo"].max(),
                "Mínimo": df["Consumo"].min(),
            }
            show = pd.DataFrame([show])
            show.to_csv(path, index=False)
        print(show)
        return show

    def overall_group_average(self, colunas, suffix):
        if isinstance(colunas, str):
            colunas = [colunas]
        path = f"./data/processed/overall_{self.alias}_{suffix}_average.csv"
        if os.path.exists(path):
            show = pd.read_csv(path)
        else:
            df = pd.read_csv(self.file_csv)
            show = (
                df.groupby(colunas)["Consumo"]
                .agg(
                    Quantidade="count",
                    Média="mean",
                    Mediana="median",
                    Moda=lambda x: x.mode().iloc[0] if not x.mode().empty else None,
                    Máximo="max",
                    Mínimo="min",
                )
                .reset_index()
            )
            show.to_csv(path, index=False)
        print(show)
        return show


class OverallStats(OverallBase):
    def overall_class_average(self):
        return self.overall_group_average("Classe", "class")

    def overall_region_average(self):
        return self.overall_group_average("Regiao", "region")

    def overall_region_class_average(self):
        return self.overall_group_average(["Regiao", "Classe"], "region_class")


class OverallStatsUF(OverallBase):
    def overall_uf_average(self):
        return self.overall_group_average("UF", "uf")

    def overall_region_average(self):
        return self.overall_group_average("Regiao", "region")

    def overall_region_class_average(self):
        return self.overall_group_average(["Regiao", "Classe"], "region_class")

    def overall_region_uf_class_average(self):
        return self.overall_group_average(["Regiao", "UF", "Classe"], "region_uf_class")


overall_sam = OverallStats("./data/file_0.csv", "arquivo_0")
overall_sam_uf = OverallStatsUF("./data/file_1.csv", "arquivo_1")
