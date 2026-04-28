from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PASTA_MODULO = Path(__file__).resolve().parents[1]
CAMINHO_DADOS = PASTA_MODULO / "dados" / "vendas_detalhadas.csv"
CAMINHO_GRAFICO = Path(__file__).resolve().parent / "grafico_barras_produtos.png"

df = pd.read_csv(CAMINHO_DADOS)

vendas_por_produto = (
    df.groupby("produto")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 5))
plt.bar(vendas_por_produto.index, vendas_por_produto.values, color="seagreen")
plt.title("Faturamento por produto")
plt.xlabel("Produto")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=45, ha="right")
plt.grid(True, axis="y", alpha=0.25)
plt.tight_layout()
plt.savefig(CAMINHO_GRAFICO, dpi=120)
plt.show()
