from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PASTA_MODULO = Path(__file__).resolve().parents[1]
CAMINHO_DADOS = PASTA_MODULO / "dados" / "vendas_detalhadas.csv"
CAMINHO_GRAFICO = Path(__file__).resolve().parent / "grafico_pandas_vendedores.png"

df = pd.read_csv(CAMINHO_DADOS)

faturamento_vendedor = (
    df.groupby("vendedor")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
faturamento_vendedor.plot(kind="bar", color="slateblue")
plt.title("Faturamento por vendedor")
plt.xlabel("Vendedor")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=0)
plt.grid(True, axis="y", alpha=0.25)
plt.tight_layout()
plt.savefig(CAMINHO_GRAFICO, dpi=120)
plt.show()
