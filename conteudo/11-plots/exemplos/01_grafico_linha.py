from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PASTA_MODULO = Path(__file__).resolve().parents[1]
CAMINHO_DADOS = PASTA_MODULO / "dados" / "vendas_mensais.csv"
CAMINHO_GRAFICO = Path(__file__).resolve().parent / "grafico_linha_faturamento.png"

df = pd.read_csv(CAMINHO_DADOS)

plt.figure(figsize=(9, 5))
plt.plot(df["mes"], df["faturamento"], marker="o", color="steelblue")
plt.title("Evolucao do faturamento mensal")
plt.xlabel("Mes")
plt.ylabel("Faturamento (R$)")
plt.grid(True, axis="y", alpha=0.3)
plt.tight_layout()
plt.savefig(CAMINHO_GRAFICO, dpi=120)
plt.show()
