import pandas as pd
from pathlib import Path

CAMINHO_DADOS = Path(__file__).resolve().parents[1] / "dados" / "vendas.csv"

df = pd.read_csv(CAMINHO_DADOS)

colunas_principais = df[["data", "cliente", "produto", "valor_total"]]
print("Colunas principais:")
print(colunas_principais.head())

vendas_sao_paulo = df[df["cidade"] == "Sao Paulo"]
print("\nVendas de Sao Paulo:")
print(vendas_sao_paulo[["cliente", "produto", "valor_total"]])

vendas_altas = df[df["valor_total"] > 1000]
print("\nVendas acima de R$ 1000:")
print(vendas_altas[["cliente", "produto", "valor_total"]])

ranking = df.sort_values(by="valor_total", ascending=False)
print("\nMaiores vendas:")
print(ranking[["cliente", "produto", "valor_total"]].head())
