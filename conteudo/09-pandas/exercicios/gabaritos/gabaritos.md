# Gabaritos Comentados - Pandas

## 1. Primeira leitura da base

```python
import pandas as pd

df = pd.read_csv("../dados/vendas.csv")

print(df.head())
print(df.shape)
print(df.columns)
```

Explicacao:

- `read_csv()` carrega o arquivo;
- `head()` mostra uma amostra inicial;
- `shape` mostra linhas e colunas;
- `columns` mostra os nomes das colunas.

## 2. Total de faturamento

```python
import pandas as pd

df = pd.read_csv("../dados/vendas.csv")

faturamento_total = df["valor_total"].sum()
print(f"Faturamento total: R$ {faturamento_total:.2f}")
```

Explicacao: `sum()` soma todos os valores da coluna.

## 3. Selecionando colunas para relatorio

```python
import pandas as pd

df = pd.read_csv("../dados/vendas.csv")

relatorio = df[["data", "cliente", "produto", "valor_total"]]
print(relatorio.head(10))
```

Explicacao: para selecionar varias colunas, usamos uma lista dentro dos colchetes.

## 4. Vendas de uma cidade

```python
import pandas as pd

df = pd.read_csv("../dados/vendas.csv")

vendas_sp = df[df["cidade"] == "Sao Paulo"]
print(vendas_sp[["cliente", "produto", "valor_total"]])
```

Explicacao: o filtro retorna apenas linhas em que a cidade e Sao Paulo.

## 5. Ticket medio

```python
import pandas as pd

df = pd.read_csv("../dados/vendas.csv")

ticket_medio = df["valor_total"].mean()
print(f"Ticket medio: R$ {ticket_medio:.2f}")
```

Explicacao: `mean()` calcula a media.

## 6. Ranking de maiores vendas

```python
import pandas as pd

df = pd.read_csv("../dados/vendas.csv")

maiores_vendas = df.sort_values(by="valor_total", ascending=False)
print(maiores_vendas.head(5))
```

Explicacao: `ascending=False` ordena do maior para o menor.

## 7. Produto mais vendido em quantidade

```python
import pandas as pd

df = pd.read_csv("../dados/vendas.csv")

quantidade_por_produto = (
    df.groupby("produto")["quantidade"]
    .sum()
    .sort_values(ascending=False)
)

print(quantidade_por_produto)
print("Produto mais vendido:", quantidade_por_produto.index[0])
```

Explicacao: o agrupamento soma a quantidade por produto. O primeiro item do ranking e o mais vendido.

## 8. Faturamento por produto

```python
import pandas as pd

df = pd.read_csv("../dados/vendas.csv")

faturamento_por_produto = (
    df.groupby("produto")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

print(faturamento_por_produto)
```

Explicacao: essa e uma das analises mais comuns em vendas.

## 9. Relatorio por vendedor

```python
import pandas as pd

df = pd.read_csv("../dados/vendas.csv")

relatorio_vendedor = df.groupby("vendedor").agg(
    faturamento_total=("valor_total", "sum"),
    quantidade_vendas=("id_venda", "count"),
    ticket_medio=("valor_total", "mean"),
)

print(relatorio_vendedor.sort_values(by="faturamento_total", ascending=False))
```

Explicacao: `agg()` permite calcular varias metricas ao mesmo tempo.

## 10. Vendas acima de R$ 1000

```python
import pandas as pd

df = pd.read_csv("../dados/vendas.csv")

vendas_altas = df[df["valor_total"] > 1000]

print(vendas_altas)
print("Quantidade:", vendas_altas["id_venda"].count())
print(f"Faturamento: R$ {vendas_altas['valor_total'].sum():.2f}")
```

Explicacao: depois de filtrar, calculamos metricas apenas sobre o resultado filtrado.

## 11. Relatorio por cidade

```python
import pandas as pd

df = pd.read_csv("../dados/vendas.csv")

relatorio_cidade = df.groupby("cidade").agg(
    faturamento_total=("valor_total", "sum"),
    quantidade_vendas=("id_venda", "count"),
    media_por_venda=("valor_total", "mean"),
    maior_venda=("valor_total", "max"),
)

relatorio_cidade = relatorio_cidade.sort_values(
    by="faturamento_total",
    ascending=False,
)

print(relatorio_cidade)
```

Explicacao: esse relatorio permite comparar o desempenho comercial por regiao.

## 12. Limpando dados problematicos

```python
import pandas as pd

df = pd.read_csv("../dados/vendas_com_problemas.csv")

df = df.drop_duplicates()
df = df.dropna(subset=["cliente", "produto", "preco_unitario"])

df["desconto"] = df["desconto"].fillna(0)
df["vendedor"] = df["vendedor"].fillna("Nao informado")
df["data"] = pd.to_datetime(df["data"], errors="coerce")

df = df[df["quantidade"] > 0]
df["valor_total_recalculado"] = (df["preco_unitario"] * df["quantidade"]) - df["desconto"]

print(df)
```

Explicacao: a limpeza remove dados sem campos essenciais, trata vazios e recalcula a metrica principal.

## 13. Margem estimada por produto

```python
import pandas as pd

vendas = pd.read_csv("../dados/vendas.csv")
produtos = pd.read_csv("../dados/produtos.csv")

base = vendas.merge(produtos[["produto", "custo_unitario"]], on="produto", how="left")

base["lucro_estimado"] = base["valor_total"] - (base["custo_unitario"] * base["quantidade"])

relatorio_margem = base.groupby("produto").agg(
    faturamento=("valor_total", "sum"),
    lucro_estimado=("lucro_estimado", "sum"),
    unidades_vendidas=("quantidade", "sum"),
)

relatorio_margem = relatorio_margem.sort_values(
    by="lucro_estimado",
    ascending=False,
)

print(relatorio_margem)
```

Explicacao: `merge()` junta as vendas com a tabela de produtos para trazer o custo unitario. Com isso, conseguimos estimar lucro.
