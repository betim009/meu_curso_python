import pandas as pd
import matplotlib.pyplot as plt


def init_csv():
    try:
        df = pd.read_excel("./data/consumo.xlsx", sheet_name=0)
        for i in range(2):
            df.to_csv(f"./reports/file_{i}.csv", index=False)
        return True
    except Exception as e:
        print(f"Erro ao gerar CSV: {e}")
        return False


def overall_average():
    try:
        df = pd.read_csv("./reports/file_0.csv")
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
    except Exception as e:
        print(f"Erro ao calcular estatísticas: {e}")
        return False


def overall_hist():
    try:
        df = pd.read_csv("./reports/file_0.csv")
        plt.hist(df["Consumo"], bins=10, color="skyblue", edgecolor="red")
        plt.title("Distribuição do Consumo")
        plt.xlabel("Consumo")
        plt.ylabel("Frequência")
        ticks = plt.xticks()[0]
        plt.xticks(ticks, [f"{t/1_000_000:.1f}M" for t in ticks])
        plt.savefig("./reports/hist_consumo.png")
        plt.show()
    except Exception as e:
        print(f"Erro ao gerar histograma: {e}")
        return False


def consumo_regiao():
    try:
        df = pd.read_csv("./reports/file_0.csv")
        consumo_regiao = df.groupby("Regiao")["Consumo"].mean().sort_values()

        consumo_regiao.plot(kind="bar", color="skyblue", edgecolor="black")
        plt.title("Consumo Médio por Região")
        plt.ylabel("Consumo Médio")
        plt.xlabel("Região")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("./reports/consumo_regiao.png")
        plt.show()
    except Exception as e:
        print(f"Erro ao gerar gráfico por região: {e}")
        return False


def consumo_classe():
    try:
        df = pd.read_csv("./reports/file_0.csv")
        consumo_classe = df.groupby("Classe")["Consumo"].mean().sort_values()

        consumo_classe.plot(kind="bar", color="lightgreen", edgecolor="black")
        plt.title("Consumo Médio por Classe")
        plt.ylabel("Consumo Médio")
        plt.xlabel("Classe")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("./reports/consumo_classe.png")
        plt.show()
    except Exception as e:
        print(f"Erro ao gerar gráfico por classe: {e}")
        return False


if __name__ == "__main__":
    overall_average()
    overall_hist()
    consumo_por_regiao()
    consumo_por_classe()
