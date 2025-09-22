import os
import pandas as pd


def overall_average():
    try:
        df = pd.read_csv("./data/file_0.csv")
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

        print(pd.DataFrame(show))
        path = "./data/processed/overall_average.csv"
        if not os.path.exists(path):
            pd.DataFrame(show).to_csv(path, index=False)
    except Exception as e:
        print(f"Erro ao calcular estatísticas: {e}")
        return False



# Função genérica para evitar duplicação de código
def overall_group_average(coluna):
    try:
        df = pd.read_csv("./data/file_0.csv")
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
        print(show)
        path = f"./data/processed/overall_{coluna.lower()}_average.csv"
        if not os.path.exists(path):
            show.to_csv(path, index=False)
    except Exception as e:
        print(f"Erro ao calcular estatísticas por {coluna}: {e}")
        return False


def overall_class_average():
    return overall_group_average("Classe")


def overall_region_average():
    return overall_group_average("Regiao")


# Estatísticas agrupando por Região e Classe ao mesmo tempo
def overall_region_class_average():
    try:
        df = pd.read_csv("./data/file_0.csv")
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
        print(show)
        path = "./data/processed/overall_region_class_average.csv"
        if not os.path.exists(path):
            show.to_csv(path, index=False)
    except Exception as e:
        print(f"Erro ao calcular estatísticas por Região e Classe: {e}")
        return False