# 09 - Pandas para Analise de Dados

Neste modulo voce vai aprender a usar Python para trabalhar com dados em formato de tabela, como planilhas de vendas, listas de clientes, catalogos de produtos e relatorios de faturamento.

O objetivo e entender como uma pessoa que trabalha com dados pensa: carregar dados, verificar a qualidade, selecionar informacoes importantes, calcular metricas e transformar dados brutos em respostas uteis para uma empresa.

## Estrutura do modulo

```text
09-pandas/
  README.md
  dados/
    vendas.csv
    clientes.csv
    produtos.csv
    vendas_com_problemas.csv
  exemplos/
    01_lendo_dados.py
    02_manipulando_dados.py
    03_agrupamentos.py
    04_limpeza_de_dados.py
  exercicios/
    exercicios.md
    gabaritos/
      gabaritos.md
      gabaritos.py
  projeto/
    README.md
    analise_vendas.py
```

## 1. Introducao

### O que e analise de dados?

Analise de dados e o processo de transformar dados em informacoes uteis para tomar decisoes.

Exemplos reais:

- uma loja quer saber qual produto mais vende;
- uma empresa quer descobrir qual cidade gera mais faturamento;
- um gestor quer saber se o ticket medio esta subindo ou caindo;
- uma area financeira quer conferir se existem vendas com preco vazio, quantidade errada ou dados duplicados.

Dados sozinhos sao registros. Analise de dados transforma esses registros em respostas.

### O que e pandas?

`pandas` e uma biblioteca Python criada para trabalhar com dados em formato de tabela.

Pense em uma tabela como uma planilha:

| data | cliente | produto | quantidade | preco_unitario |
|---|---|---|---:|---:|
| 2026-01-05 | Ana Souza | Mouse sem fio | 2 | 89.90 |
| 2026-01-06 | Bruno Lima | Teclado mecanico | 1 | 249.90 |

Com pandas, conseguimos abrir arquivos CSV, visualizar linhas, selecionar colunas, filtrar registros, ordenar dados, calcular soma/media/contagem, agrupar informacoes e preparar relatorios.

### Onde pandas e usado no mercado?

Pandas aparece em tarefas de analise de dados, automacao de relatorios, business intelligence, financeiro, marketing, vendas, operacoes, ciencia de dados e exploracao inicial de bases.

Muitas empresas ainda usam planilhas diariamente. Pandas permite automatizar e analisar essas planilhas com mais controle.

## Preparando o ambiente

Instale o pandas:

```bash
pip install pandas
```

Em todos os exemplos, usamos:

```python
import pandas as pd
```

`pd` e um apelido convencional para evitar escrever `pandas` toda hora.

## 2. DataFrame

Um `DataFrame` e a principal estrutura do pandas. Ele e uma tabela dentro do Python, formada por colunas, linhas e indice.

- Colunas: campos da tabela, como `produto`, `cidade`, `preco_unitario`.
- Linhas: registros, como cada venda realizada.
- Indice: numeracao que identifica cada linha.

Exemplo:

```python
import pandas as pd

dados = {
    "produto": ["Mouse sem fio", "Teclado mecanico", "Monitor 24"],
    "quantidade": [2, 1, 1],
    "preco_unitario": [89.90, 249.90, 899.90],
}

df = pd.DataFrame(dados)
print(df)
```

Saida esperada:

```text
             produto  quantidade  preco_unitario
0      Mouse sem fio           2           89.90
1  Teclado mecanico           1          249.90
2        Monitor 24           1          899.90
```

### Como visualizar dados

Em bases reais, voce nao imprime tudo de uma vez. Use comandos de inspecao:

```python
print(df.head())      # primeiras linhas
print(df.tail())      # ultimas linhas
print(df.shape)       # quantidade de linhas e colunas
print(df.columns)     # nomes das colunas
print(df.info())      # tipos de dados e valores ausentes
print(df.describe())  # estatisticas das colunas numericas
```

## 3. Leitura de dados

Na vida real, os dados geralmente vem de arquivos, bancos de dados, sistemas internos ou exportacoes de planilhas.

CSV e um arquivo de texto que representa uma tabela. Cada linha e um registro, e cada coluna e separada por virgula.

```python
import pandas as pd

df = pd.read_csv("dados/vendas.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
```

`pd.read_csv()` le o arquivo e devolve um DataFrame.

Antes de analisar, sempre entenda:

- quantas linhas existem;
- quais colunas existem;
- quais tipos de dados aparecem;
- se ha valores vazios.

## 4. Manipulacao basica

### Selecionar uma coluna

```python
produtos = df["produto"]
print(produtos.head())
```

### Selecionar varias colunas

```python
resumo = df[["data", "cliente", "produto", "valor_total"]]
print(resumo.head())
```

Para varias colunas, usamos dois pares de colchetes: `[[...]]`.

### Filtrar dados

Filtrar significa pegar apenas as linhas que obedecem a uma regra.

```python
vendas_altas = df[df["valor_total"] > 1000]
print(vendas_altas)
```

```python
vendas_sp = df[df["cidade"] == "Sao Paulo"]
print(vendas_sp)
```

```python
vendas_quantidade_alta = df[df["quantidade"] >= 3]
print(vendas_quantidade_alta)
```

### Combinar filtros

Use `&` para E, `|` para OU e parenteses em cada condicao.

```python
vendas_sp_altas = df[(df["cidade"] == "Sao Paulo") & (df["valor_total"] > 1000)]
print(vendas_sp_altas)
```

### Ordenar dados

```python
ordenado = df.sort_values(by="valor_total", ascending=False)
print(ordenado.head())
```

`ascending=False` coloca do maior para o menor.

## 5. Estatisticas simples

Pandas facilita calculos comuns em relatorios:

```python
faturamento_total = df["valor_total"].sum()
ticket_medio = df["valor_total"].mean()
quantidade_vendas = df["id_venda"].count()
menor_venda = df["valor_total"].min()
maior_venda = df["valor_total"].max()

print(f"Faturamento total: R$ {faturamento_total:.2f}")
print(f"Ticket medio: R$ {ticket_medio:.2f}")
print(f"Quantidade de vendas: {quantidade_vendas}")
print(f"Menor venda: R$ {menor_venda:.2f}")
print(f"Maior venda: R$ {maior_venda:.2f}")
```

Ticket medio e o valor medio gasto por venda.

## 6. Agrupamentos

Agrupar dados significa juntar linhas por uma categoria e calcular algum resultado.

Exemplo real: faturamento por produto.

```python
faturamento_por_produto = df.groupby("produto")["valor_total"].sum()
print(faturamento_por_produto)
```

Leia assim:

- agrupe por `produto`;
- olhe para a coluna `valor_total`;
- some os valores de cada grupo.

Ordenando o resultado:

```python
ranking_produtos = (
    df.groupby("produto")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

print(ranking_produtos)
```

Mais exemplos:

```python
vendas_por_cidade = df.groupby("cidade")["id_venda"].count()
print(vendas_por_cidade)
```

```python
faturamento_por_vendedor = (
    df.groupby("vendedor")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

print(faturamento_por_vendedor)
```

### Mais de uma metrica por grupo

```python
relatorio_produtos = df.groupby("produto").agg(
    faturamento=("valor_total", "sum"),
    unidades_vendidas=("quantidade", "sum"),
    ticket_medio=("valor_total", "mean"),
)

print(relatorio_produtos)
```

Esse formato e muito usado em analises profissionais porque cria um relatorio resumido.

## 7. Limpeza de dados

Dados reais quase sempre tem problemas:

- campos vazios;
- nomes digitados de formas diferentes;
- numeros como texto;
- datas em formato incorreto;
- linhas duplicadas;
- quantidades negativas;
- precos ausentes.

Use `dados/vendas_com_problemas.csv` para praticar.

### Verificando valores nulos

```python
df = pd.read_csv("dados/vendas_com_problemas.csv")

print(df.isna().sum())
```

`isna()` verifica valores ausentes. `sum()` conta quantos ausentes existem em cada coluna.

### Removendo linhas sem informacao essencial

```python
df = df.dropna(subset=["cliente", "produto"])
```

### Preenchendo valores ausentes

```python
df["vendedor"] = df["vendedor"].fillna("Nao informado")
df["desconto"] = df["desconto"].fillna(0)
```

### Convertendo datas

```python
df["data"] = pd.to_datetime(df["data"], errors="coerce")
```

`errors="coerce"` transforma datas invalidas em valor nulo. Isso ajuda a identificar problemas sem quebrar o codigo.

### Removendo duplicados

```python
df = df.drop_duplicates()
```

### Recalculando valor total

```python
df["valor_total"] = (df["preco_unitario"] * df["quantidade"]) - df["desconto"]
```

Em bases reais, nem sempre podemos confiar em todos os campos. Quando ha preco, quantidade e desconto, podemos recalcular o total.

## 8. Boas praticas

Use nomes claros:

```python
faturamento_por_produto = df.groupby("produto")["valor_total"].sum()
```

Confira os dados antes de analisar:

```python
print(df.head())
print(df.info())
print(df.isna().sum())
```

Nao altere dados sem entender. Antes de apagar ou preencher valores vazios, pergunte:

- essa coluna e essencial?
- posso preencher com zero?
- faz sentido remover a linha?
- existe uma regra de negocio?

Separe etapas:

1. importar bibliotecas;
2. carregar dados;
3. inspecionar;
4. limpar;
5. criar colunas calculadas;
6. gerar metricas;
7. interpretar resultados.

## 9. Erros comuns

### Nao entender DataFrame

Um DataFrame nao e uma lista comum. Ele e uma tabela com linhas e colunas.

### Errar nome da coluna

```python
df["Valor Total"]
```

Se a coluna se chama `valor_total`, isso gera erro.

Use:

```python
print(df.columns)
```

### Esquecer parenteses em filtros combinados

Errado:

```python
df[df["cidade"] == "Sao Paulo" & df["valor_total"] > 1000]
```

Certo:

```python
df[(df["cidade"] == "Sao Paulo") & (df["valor_total"] > 1000)]
```

### Misturar texto com numero

Se uma coluna numerica for lida como texto, calculos podem falhar.

```python
print(df.dtypes)
```

### Confiar cegamente no arquivo

Arquivos de empresas podem vir com dados errados. Sempre valide.

## 10. Mini desafios

Use o arquivo `dados/vendas.csv`.

### Mini desafio 1

Leia o CSV e mostre as 5 primeiras linhas.

### Mini desafio 2

Mostre apenas as colunas `cliente`, `produto` e `valor_total`.

### Mini desafio 3

Filtre apenas as vendas da cidade de `Sao Paulo`.

### Mini desafio 4

Calcule o faturamento total da empresa.

### Mini desafio 5

Mostre o produto com maior faturamento total.

### Mini desafio 6

Calcule o faturamento por vendedor e ordene do maior para o menor.

### Mini desafio 7

Leia `dados/vendas_com_problemas.csv` e conte quantos valores vazios existem em cada coluna.

## 11. Resumo

Neste modulo voce aprendeu que:

- pandas e uma biblioteca para trabalhar com dados em tabelas;
- DataFrame e a tabela principal do pandas;
- `read_csv()` carrega arquivos CSV;
- `head()`, `info()`, `shape` e `columns` ajudam a entender os dados;
- filtros permitem selecionar linhas especificas;
- `sort_values()` ordena os dados;
- `sum()`, `mean()` e `count()` geram metricas simples;
- `groupby()` cria relatorios por categoria;
- dados reais precisam de limpeza e validacao;
- boas analises seguem etapas claras.

Ao final deste modulo, voce ja consegue criar analises simples de vendas, clientes e faturamento usando Python de forma parecida com tarefas reais do mercado.
