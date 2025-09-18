import pandas as pd
import matplotlib.pyplot as plt


def scatter_plot(x, y, xlabel, ylabel, title, filename):
    try:
        plt.figure(figsize=(10, 6))
        plt.scatter(x, y, alpha=0.5, color="blue")
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(filename)
        plt.show()
    except Exception as e:
        print(f"Erro ao gerar gráfico: {e}")
        return False

def scatter_class():
    try:
        df = pd.read_csv("./data/file_0.csv")
        scatter_plot(
            x=df["Classe"],
            y=df["Consumo"],
            xlabel="Classe",
            ylabel="Consumo",
            title="Dispersão: Consumo por Classe",
            filename="./reports/scatter/scatter_consumo_classe.png"
        )
    except Exception as e:
        print(f"Erro ao gerar gráfico de dispersão por Classe: {e}")
        return False


def scatter_region():
    try:
        df = pd.read_csv("./data/file_0.csv")
        scatter_plot(
            x=df["Regiao"],
            y=df["Consumo"],
            xlabel="Regiao",
            ylabel="Consumo",
            title="Dispersão: Consumo por Regiao",
            filename="./reports/scatter/scatter_consumo_regiao.png"
        )
    except Exception as e:
        print(f"Erro ao gerar gráfico de dispersão por Região: {e}")
        return False


def scatter_region_class():
    try:
        df = pd.read_csv("./data/file_0.csv")
        df["Regiao_Classe"] = df["Regiao"].astype(str) + " - " + df["Classe"].astype(str)
        scatter_plot(
            x=df["Regiao_Classe"],
            y=df["Consumo"],
            xlabel="Região - Classe",
            ylabel="Consumo",
            title="Dispersão: Consumo por Região e Classe",
            filename="./reports/scatter/scatter_consumo_regiao_classe.png"
        )
    except Exception as e:
        print(f"Erro ao gerar gráfico de dispersão por Região e Classe: {e}")
        return False