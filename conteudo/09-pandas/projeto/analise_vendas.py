import pandas as pd
from pathlib import Path


def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


PASTA_DADOS = Path(__file__).resolve().parents[1] / "dados"

vendas = pd.read_csv(PASTA_DADOS / "vendas.csv")
produtos = pd.read_csv(PASTA_DADOS / "produtos.csv")

print("=== ANALISE DE VENDAS ===")
print("\nPrimeiras linhas da base:")
print(vendas.head())

print("\nResumo da base:")
print(vendas.info())

print("\nValores ausentes:")
print(vendas.isna().sum())

faturamento_total = vendas["valor_total"].sum()
ticket_medio = vendas["valor_total"].mean()
quantidade_vendas = vendas["id_venda"].count()
unidades_vendidas = vendas["quantidade"].sum()

print("\n=== METRICAS GERAIS ===")
print(f"Faturamento total: {formatar_moeda(faturamento_total)}")
print(f"Ticket medio: {formatar_moeda(ticket_medio)}")
print(f"Quantidade de vendas: {quantidade_vendas}")
print(f"Unidades vendidas: {unidades_vendidas}")

faturamento_produto = (
    vendas.groupby("produto")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

unidades_por_produto = (
    vendas.groupby("produto")["quantidade"]
    .sum()
    .sort_values(ascending=False)
)

faturamento_vendedor = (
    vendas.groupby("vendedor")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

relatorio_cidade = vendas.groupby("cidade").agg(
    faturamento=("valor_total", "sum"),
    quantidade_vendas=("id_venda", "count"),
    ticket_medio=("valor_total", "mean"),
)

relatorio_cidade = relatorio_cidade.sort_values(by="faturamento", ascending=False)

base_lucro = vendas.merge(
    produtos[["produto", "custo_unitario"]],
    on="produto",
    how="left",
)

base_lucro["lucro_estimado"] = (
    base_lucro["valor_total"] - (base_lucro["custo_unitario"] * base_lucro["quantidade"])
)

lucro_por_produto = base_lucro.groupby("produto").agg(
    faturamento=("valor_total", "sum"),
    lucro_estimado=("lucro_estimado", "sum"),
    unidades_vendidas=("quantidade", "sum"),
)

lucro_por_produto = lucro_por_produto.sort_values(
    by="lucro_estimado",
    ascending=False,
)

print("\n=== FATURAMENTO POR PRODUTO ===")
print(faturamento_produto)

print("\n=== UNIDADES VENDIDAS POR PRODUTO ===")
print(unidades_por_produto)

print("\n=== FATURAMENTO POR VENDEDOR ===")
print(faturamento_vendedor)

print("\n=== RELATORIO POR CIDADE ===")
print(relatorio_cidade)

print("\n=== LUCRO ESTIMADO POR PRODUTO ===")
print(lucro_por_produto)

produto_maior_faturamento = faturamento_produto.index[0]
vendedor_maior_faturamento = faturamento_vendedor.index[0]
cidade_maior_faturamento = relatorio_cidade.index[0]
produto_maior_lucro = lucro_por_produto.index[0]

print("\n=== INSIGHTS ===")
print(f"Produto com maior faturamento: {produto_maior_faturamento}")
print(f"Vendedor com maior faturamento: {vendedor_maior_faturamento}")
print(f"Cidade com maior faturamento: {cidade_maior_faturamento}")
print(f"Produto com maior lucro estimado: {produto_maior_lucro}")

print("\nInterpretacao:")
print("- Produtos de maior faturamento ajudam a entender onde esta a principal receita.")
print("- O ranking de vendedores mostra desempenho comercial por pessoa.")
print("- A analise por cidade mostra regioes com maior potencial.")
print("- O lucro estimado evita olhar apenas para faturamento, pois considera o custo.")
