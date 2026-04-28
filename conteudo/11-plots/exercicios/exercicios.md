# Exercicios - Visualizacao de Dados

Use os arquivos:

- `../dados/vendas_mensais.csv`
- `../dados/vendas_detalhadas.csv`

Os exercicios simulam demandas comuns em empresas: mostrar evolucao de vendas, comparar produtos, analisar categorias e criar graficos para relatorios.

## Exercicios faceis

### 1. Grafico de linha do faturamento mensal

Leia `vendas_mensais.csv` e crie um grafico de linha mostrando `mes` no eixo X e `faturamento` no eixo Y.

Adicione:

- titulo;
- nome do eixo X;
- nome do eixo Y.

### 2. Grafico de barras de pedidos por mes

Leia `vendas_mensais.csv` e crie um grafico de barras com a quantidade de `pedidos` por `mes`.

### 3. Grafico de barras por vendedor

Leia `vendas_detalhadas.csv`, agrupe por `vendedor` e some `valor_total`.

Crie um grafico de barras com o faturamento por vendedor.

### 4. Grafico de pizza por forma de pagamento

Leia `vendas_detalhadas.csv`, agrupe por `forma_pagamento` e some `valor_total`.

Crie um grafico de pizza mostrando a participacao de cada forma de pagamento.

### 5. Salvar um grafico

Crie qualquer grafico dos exercicios anteriores e salve em PNG usando `plt.savefig()`.

## Exercicios medios

### 6. Top 5 produtos por faturamento

Agrupe as vendas por `produto`, some `valor_total`, ordene do maior para o menor e mostre apenas os 5 primeiros em um grafico de barras.

### 7. Quantidade vendida por produto

Agrupe por `produto`, some `quantidade` e crie um grafico de barras horizontais.

Use barras horizontais porque os nomes dos produtos podem ser longos.

### 8. Evolucao do ticket medio

Use `vendas_mensais.csv` e crie um grafico de linha para `ticket_medio`.

Adicione marcadores nos pontos.

### 9. Comparar faturamento e pedidos

Use `vendas_mensais.csv` e crie dois graficos na mesma figura:

- primeiro: faturamento por mes;
- segundo: pedidos por mes.

Dica: use `plt.subplot()`.

### 10. Grafico com pandas `.plot()`

Use pandas `.plot(kind="bar")` para criar um grafico de faturamento por categoria.

## Exercicios desafiadores

### 11. Dashboard simples em uma figura

Crie uma figura com 4 graficos:

- linha: faturamento mensal;
- barras: top 5 produtos por faturamento;
- barras: faturamento por vendedor;
- pizza: participacao por categoria.

Use `plt.subplot()` ou `plt.subplots()`.

### 12. Comparacao de categorias por mes

Use `vendas_detalhadas.csv`.

Agrupe por `mes` e `categoria`, some `valor_total` e gere um grafico de barras agrupadas ou uma tabela dinamica com `.plot(kind="bar")`.

### 13. Relatorio visual salvo em arquivos

Crie um script que gere e salve pelo menos 3 graficos em PNG:

- `faturamento_mensal.png`;
- `top_produtos.png`;
- `categorias.png`.

Organize o codigo em funcoes.
