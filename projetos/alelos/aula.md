# 📘 Material Didático -- Introdução ao Pandas com Excel

------------------------------------------------------------------------

# 📑 Índice

1.  O que é Pandas?
2.  O que é um DataFrame?
3.  Lendo um arquivo Excel (`read_excel`)
4.  Explorando os dados
5.  Selecionando colunas e linhas
6.  Aplicando filtros
7.  Criando e alterando colunas
8.  Limpando dados
9.  Agrupando informações (`groupby`)
10. Ordenando dados
11. Exportando para Excel

------------------------------------------------------------------------

# 1️⃣ O que é Pandas?

Pandas é uma **biblioteca do Python** usada para trabalhar com:

-   Planilhas
-   Tabelas
-   Dados organizados em linhas e colunas

É muito utilizada para análise de dados e manipulação de arquivos Excel.

------------------------------------------------------------------------

# 2️⃣ O que é um DataFrame?

Um **DataFrame** é como uma planilha do Excel dentro do Python.

Ele possui:

-   Linhas
-   Colunas
-   Índice (numeração das linhas)

Quando carregamos um Excel no Pandas, ele vira um DataFrame.

------------------------------------------------------------------------

# 3️⃣ Lendo um arquivo Excel

## Importando a biblioteca

``` python
import pandas as pd
```

## Lendo o arquivo

``` python
df = pd.read_excel("vendas.xlsx")
print(df)
```

Explicação:

-   `read_excel()` lê o arquivo Excel.
-   `"vendas.xlsx"` é o nome do arquivo.
-   `df` armazena o DataFrame.

------------------------------------------------------------------------

# 4️⃣ Explorando os dados

## Ver primeiras linhas

``` python
df.head()
```

## Ver últimas linhas

``` python
df.tail()
```

## Informações gerais

``` python
df.info()
```

## Quantidade de linhas e colunas

``` python
df.shape
```

## Nome das colunas

``` python
df.columns
```

## Tipos das colunas

``` python
df.dtypes
```

------------------------------------------------------------------------

# 5️⃣ Selecionando colunas e linhas

## Selecionar uma coluna

``` python
df["nome"]
```

## Selecionar múltiplas colunas

``` python
df[["nome", "idade"]]
```

## Selecionar linha pelo índice

``` python
df.loc[0]
```

## Seleção por posição

``` python
df.iloc[0]
```

------------------------------------------------------------------------

# 6️⃣ Aplicando filtros

## Exemplo: idade maior que 18

``` python
df[df["idade"] > 18]
```

## Duas condições

``` python
df[(df["idade"] > 18) & (df["cidade"] == "Iúna")]
```

------------------------------------------------------------------------

# 7️⃣ Criando e Alterando Colunas

## Criar nova coluna

``` python
df["ano_nascimento"] = 2025 - df["idade"]
```

## Alterar tipo

``` python
df["idade"] = df["idade"].astype(int)
```

------------------------------------------------------------------------

# 8️⃣ Limpando Dados

## Ver valores nulos

``` python
df.isnull()
```

## Contar valores nulos

``` python
df.isnull().sum()
```

## Remover valores vazios

``` python
df.dropna()
```

## Preencher valores vazios

``` python
df.fillna(0)
```

## Remover duplicados

``` python
df.drop_duplicates()
```

------------------------------------------------------------------------

# 9️⃣ Agrupando Informações

``` python
df.groupby("cidade")["vendas"].sum()
```

------------------------------------------------------------------------

# 🔟 Ordenando Dados

``` python
df.sort_values("idade")
```

``` python
df.sort_values("idade", ascending=False)
```

------------------------------------------------------------------------

# 1️⃣1️⃣ Exportando para Excel

``` python
df.to_excel("novo_arquivo.xlsx", index=False)
```

------------------------------------------------------------------------

# 🎯 Fluxo Completo

Ler → Explorar → Selecionar → Filtrar → Alterar → Limpar → Agrupar →
Ordenar → Exportar
