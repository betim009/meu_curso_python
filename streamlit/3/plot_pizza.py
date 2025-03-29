import pandas as pd
import matplotlib.pyplot as plt


def create_plot_pizza():
    file = pd.read_csv("pacientes.csv")

    masc = file[file["sexo"] == "M"]
    fem = file[file["sexo"] == "F"]

    labels = ["Masculino", "Feminino"]
    sizes = [len(masc), len(fem)]

    # Cria a figura e o gráfico
    fig, ax = plt.subplots(figsize=(3, 2))
    ax.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90,
        textprops={"fontsize": 4},
    )
    ax.set_title("Quantidade de consultas por sexo", fontsize=8)

    return fig  # Retorna a figura para o Streamlit
