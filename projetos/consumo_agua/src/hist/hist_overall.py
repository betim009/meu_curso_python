import pandas as pd
import matplotlib.pyplot as plt


def hist_overall():
    try:
        df = pd.read_csv("./data/file_0.csv")
        plt.hist(df["Consumo"], bins=10, color="skyblue", edgecolor="red")
        plt.title("Distribuição do Consumo")
        plt.xlabel("Consumo")
        plt.ylabel("Frequência")
        ticks = plt.xticks()[0]
        plt.xticks(ticks, [f"{t/1_000_000:.1f}M" for t in ticks])
        plt.savefig("./reports/hist/hist_consumo.png")
        plt.show()
    except Exception as e:
        print(f"Erro ao gerar histograma: {e}")
        return False


def hist_class():
    try:
        df = pd.read_csv("./data/file_0.csv")
        consumo_classe = df.groupby("Classe")["Consumo"].mean().sort_values()

        consumo_classe.plot(kind="bar", color="lightgreen", edgecolor="black")
        plt.title("Consumo Médio por Classe")
        plt.ylabel("Consumo Médio")
        plt.xlabel("Classe")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("./reports/hist/consumo_classe.png")
        plt.show()
    except Exception as e:
        print(f"Erro ao gerar gráfico por classe: {e}")
        return False


def hist_regiao():
    try:
        df = pd.read_csv("./data/file_0.csv")
        consumo_regiao = df.groupby("Regiao")["Consumo"].mean().sort_values()

        consumo_regiao.plot(kind="bar", color="skyblue", edgecolor="black")
        plt.title("Consumo Médio por Região")
        plt.ylabel("Consumo Médio")
        plt.xlabel("Região")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("./reports/hist/consumo_regiao.png")
        plt.show()
    except Exception as e:
        print(f"Erro ao gerar gráfico por região: {e}")
        return False
