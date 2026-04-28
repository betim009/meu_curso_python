from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PASTA_MODULO = Path(__file__).resolve().parents[1]
CAMINHO_DADOS = PASTA_MODULO / "dados" / "vendas_detalhadas.csv"
CAMINHO_GRAFICO = Path(__file__).resolve().parent / "grafico_pizza_categorias.png"

df = pd.read_csv(CAMINHO_DADOS)

faturamento_categoria = (
    df.groupby("categoria")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 6))
plt.pie(
    faturamento_categoria.values,
    labels=faturamento_categoria.index,
    autopct="%1.1f%%",
    startangle=90,
)
plt.title("Participacao do faturamento por categoria")
plt.tight_layout()
plt.savefig(CAMINHO_GRAFICO, dpi=120)
plt.show()
