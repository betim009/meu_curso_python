# Projeto - Analise de Vendas de uma Empresa

Neste projeto, voce vai simular uma tarefa real de analise de dados.

Imagine que uma empresa vende produtos de tecnologia e precisa responder perguntas simples, mas importantes:

- quanto a empresa faturou?
- qual produto trouxe mais dinheiro?
- qual vendedor teve melhor resultado?
- quais cidades compraram mais?
- quais produtos venderam mais unidades?
- existem oportunidades de negocio nos dados?

## Arquivos usados

```text
../dados/vendas.csv
../dados/produtos.csv
```

## Passo 1 - Ler os dados

```python
import pandas as pd

vendas = pd.read_csv("../dados/vendas.csv")
produtos = pd.read_csv("../dados/produtos.csv")
```

## Passo 2 - Entender a base

```python
print(vendas.head())
print(vendas.info())
print(vendas.isna().sum())
```

Antes de calcular metricas, sempre confira a estrutura e a qualidade dos dados.

## Passo 3 - Criar metricas principais

```python
faturamento_total = vendas["valor_total"].sum()
ticket_medio = vendas["valor_total"].mean()
quantidade_vendas = vendas["id_venda"].count()
unidades_vendidas = vendas["quantidade"].sum()
```

Interpretacao:

- faturamento total mostra quanto entrou em vendas;
- ticket medio mostra o valor medio de cada venda;
- quantidade de vendas mostra o volume de pedidos;
- unidades vendidas mostra quantos itens foram vendidos.

## Passo 4 - Criar relatorios por grupo

### Faturamento por produto

```python
faturamento_produto = (
    vendas.groupby("produto")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)
```

### Faturamento por vendedor

```python
faturamento_vendedor = (
    vendas.groupby("vendedor")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)
```

### Relatorio por cidade

```python
relatorio_cidade = vendas.groupby("cidade").agg(
    faturamento=("valor_total", "sum"),
    quantidade_vendas=("id_venda", "count"),
    ticket_medio=("valor_total", "mean"),
)
```

## Passo 5 - Estimar lucro

Para calcular lucro estimado, precisamos juntar vendas com produtos, porque a tabela de produtos tem o custo.

```python
base = vendas.merge(produtos[["produto", "custo_unitario"]], on="produto", how="left")

base["lucro_estimado"] = base["valor_total"] - (base["custo_unitario"] * base["quantidade"])
```

## Passo 6 - Gerar insights

Insight e uma conclusao util baseada nos dados.

Exemplos:

- produto com maior faturamento;
- vendedor com maior faturamento;
- cidade com maior faturamento;
- produto com maior lucro estimado.

O arquivo `analise_vendas.py` contem o projeto completo.

## Como executar

Dentro da pasta `projeto`, rode:

```bash
python3 analise_vendas.py
```

## Codigo completo

Veja o arquivo `analise_vendas.py`.
