# Exercicios - Pandas para Analise de Dados

Use principalmente o arquivo `../dados/vendas.csv`.

Os exercicios simulam tarefas comuns de uma pessoa analista de dados: abrir uma base, conferir colunas, calcular indicadores, criar rankings e validar problemas.

## Exercicios faceis

### 1. Primeira leitura da base

Leia o arquivo `vendas.csv` e mostre:

- as 5 primeiras linhas;
- a quantidade de linhas e colunas;
- os nomes das colunas.

### 2. Total de faturamento

Calcule o faturamento total da empresa usando a coluna `valor_total`.

### 3. Selecionando colunas para relatorio

Crie um novo DataFrame apenas com as colunas:

- `data`;
- `cliente`;
- `produto`;
- `valor_total`.

Mostre as 10 primeiras linhas.

### 4. Vendas de uma cidade

Filtre apenas as vendas da cidade de `Sao Paulo`.

Depois, mostre as colunas `cliente`, `produto` e `valor_total`.

### 5. Ticket medio

Calcule o ticket medio das vendas.

Ticket medio e o valor medio gasto por venda.

## Exercicios medios

### 6. Ranking de maiores vendas

Ordene a base pelo `valor_total`, do maior para o menor, e mostre as 5 maiores vendas.

### 7. Produto mais vendido em quantidade

Agrupe por `produto`, some a coluna `quantidade` e descubra qual produto teve mais unidades vendidas.

### 8. Faturamento por produto

Agrupe por `produto`, some `valor_total` e ordene do maior para o menor.

### 9. Relatorio por vendedor

Crie um relatorio agrupado por `vendedor` com:

- faturamento total;
- quantidade de vendas;
- ticket medio.

### 10. Vendas acima de R$ 1000

Filtre as vendas com `valor_total` maior que 1000.

Depois, responda:

- quantas vendas foram encontradas?
- qual foi o faturamento total dessas vendas?

## Exercicios desafiadores

### 11. Relatorio por cidade

Crie um relatorio por `cidade` com:

- faturamento total;
- quantidade de vendas;
- media por venda;
- maior venda.

Ordene pelo faturamento total, do maior para o menor.

### 12. Limpando dados problematicos

Use o arquivo `../dados/vendas_com_problemas.csv`.

Faca uma limpeza simples:

- remova duplicados;
- remova linhas sem `cliente`, `produto` ou `preco_unitario`;
- preencha `desconto` vazio com `0`;
- preencha `vendedor` vazio com `"Nao informado"`;
- converta a coluna `data` para data com `pd.to_datetime`;
- remova vendas com quantidade menor ou igual a zero;
- crie uma coluna `valor_total_recalculado`.

No final, mostre o DataFrame limpo.

### 13. Margem estimada por produto

Use os arquivos:

- `../dados/vendas.csv`;
- `../dados/produtos.csv`.

Junte as bases pela coluna `produto`.

Depois crie:

```text
lucro_estimado = valor_total - (custo_unitario * quantidade)
```

Gere um relatorio por produto com:

- faturamento;
- lucro estimado;
- unidades vendidas.

Ordene pelo lucro estimado, do maior para o menor.
