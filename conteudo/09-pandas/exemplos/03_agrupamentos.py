import pandas as pd
from pathlib import Path

CAMINHO_DADOS = Path(__file__).resolve().parents[1] / "dados" / "vendas.csv"

df = pd.read_csv(CAMINHO_DADOS)

faturamento_por_produto = (
    df.groupby("produto")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

print("Faturamento por produto:")
print(faturamento_por_produto)

relatorio_por_vendedor = df.groupby("vendedor").agg(
    faturamento=("valor_total", "sum"),
    quantidade_vendas=("id_venda", "count"),
    ticket_medio=("valor_total", "mean"),
)

print("\nRelatorio por vendedor:")
print(relatorio_por_vendedor.sort_values(by="faturamento", ascending=False))
