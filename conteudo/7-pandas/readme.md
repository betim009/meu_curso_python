
# 🍍 Trabalhando com Dados em Python usando a Biblioteca Pandas

Vamos aprender a:

- O que é e como funciona um **DataFrame**
- Como criar, salvar e ler **arquivos `.csv`**
- Como ordenar, filtrar e classificar dados com **métodos**
- Como fazer **análises simples**, como calcular média de preços
- Como **evitar erros comuns**

Tudo isso com um tema simples e fácil de entender: **frutas e seus preços**. 🍓🍊🍇

---

## 🧠 O que é o Pandas?

O **Pandas** é uma biblioteca do Python que serve para trabalhar com **dados tabulares** (como planilhas do Excel ou tabelas do Google Sheets).

> Ele nos permite criar, visualizar, filtrar, salvar e analisar dados de forma **rápida e prática**.

---

## 🍽 O que é um DataFrame?

Um **DataFrame** é uma **tabela** com **linhas e colunas**. Cada coluna tem um nome, e cada linha representa uma entrada (um dado).

Por exemplo:

| fruta     | preco |
|-----------|-------|
| Morango   | 2.19  |
| Laranja   | 3.00  |

Essa estrutura é usada para **organizar os dados na memória do Python**, e é o formato mais comum de se trabalhar com dados no Pandas.

---

## Parte 1 – Criando e Salvando um DataFrame

### ✍️ Quando usar?

Use isso quando você **tem dados no código** (listas ou dicionários) e quer **organizar em tabela** e **salvar** num arquivo `.csv`.

### ✅ Como fazer isso?

```python
import pandas as pd  # Importa a biblioteca pandas

# Dicionário com frutas e seus preços
dados = {
    "fruta": ["Morango", "Laranja", "Melancia", "Manga", "Goiaba"],
    "preco": [2.19, 3.0, 1.77, 3.5, 2.09],
}

# Cria o DataFrame (tabela)
df = pd.DataFrame(dados)

# Mostra a tabela
print(df)

# Salva o DataFrame num arquivo CSV (planilha simples)
df.to_csv("./7-pandas/new_frutas.csv", index=False)
```

### 🧾 Explicação passo a passo:

- `pd.DataFrame()` → Cria a tabela (DataFrame) a partir de um dicionário.
- `.to_csv()` → Salva a tabela como arquivo `.csv`.
- `index=False` → Evita salvar o número da linha (o índice) no arquivo.

---

### ⚠️ Cuidado!

- Se você **salvar sem o `index=False`**, vai aparecer uma coluna extra com números.
- Se o arquivo já existir, ele será **sobrescrito** (apagado e refeito).

---

## Parte 2 – Lendo e Ordenando os Dados

### ✍️ Quando usar?

Use quando você já tem um arquivo `.csv` e quer **ver ou organizar os dados** dele no Python.

```python
import pandas as pd

# Lê a tabela (DataFrame) do arquivo CSV
df = pd.read_csv("./7-pandas/frutas.csv")

# Mostra os dados lidos
print(df)

# Ordena os dados por preço (do menor para o maior)
df_ordenado = df.sort_values(by="preco")

# Mostra a tabela ordenada
print("\nLista de Frutas e Preços (Ordenado por Preço):")
print(df_ordenado)

# Mostra apenas os nomes das frutas
print("\nNomes das Frutas:")
print(df["fruta"])
```

---

### 🧾 Explicação dos termos:

- `.read_csv()` → **Lê um arquivo `.csv`** e transforma em DataFrame.
- `.sort_values(by="preco")` → É um **método** que serve para **ordenar os dados** de acordo com a coluna escolhida (`preco`, nesse caso).
- `df["fruta"]` → Mostra apenas a coluna chamada `"fruta"`.

---

## Parte 3 – Filtrando, Classificando e Calculando

### ✍️ Quando usar?

Use quando você quiser **trabalhar com regras**, como:
- Ver apenas frutas baratas
- Classificar como “Barato” ou “Caro”
- Calcular médias

```python
import pandas as pd

# Lê os dados do arquivo
df = pd.read_csv("./7-pandas/frutas.csv")

# Filtra as frutas com preço menor que 3.0
frutas_baratas = df[df["preco"] < 3.0]
print("Frutas com preço menor que 3.0:")
print(frutas_baratas)

# Cria uma nova coluna com a categoria
df["categoria"] = df["preco"].apply(lambda x: "Barato" if x < 3.0 else "Caro")
print("\nFrutas com Categorias:")
print(df)

# Calcula a média dos preços
media_precos = df["preco"].mean()
print(f"\nMédia dos Preços das Frutas: {media_precos:.2f}")
```

---

### 🧾 Explicação:

- `df[df["preco"] < 3.0]` → Isso é um **filtro**. Ele pega só as linhas onde o preço é menor que 3.
- `.apply()` com `lambda` → Serve para **criar uma regra personalizada** para cada valor da coluna.
- `.mean()` → Calcula a **média** de todos os valores da coluna.

---

## 🚨 Cuidado! Não faça isso...

- Não esqueça de verificar se o **arquivo existe** antes de tentar ler.
- Sempre revise o nome das **colunas** ao usar filtros ou ordenações.
- Evite sobrescrever arquivos importantes usando `to_csv()` com o mesmo nome.

---

## 🧪 Desafio

### Crie uma nova coluna chamada `"faixa"`:
- Se o preço for menor que 2 → classifique como `"Muito barato"`
- Se estiver entre 2 e 3 → classifique como `"Barato"`
- Se for acima de 3 → classifique como `"Caro"`

Depois, salve isso em um novo arquivo chamado `frutas_categorizadas.csv`.

---

## ✅ Gabarito do desafio

```python
import pandas as pd

df = pd.read_csv("./7-pandas/frutas.csv")

# Função que classifica a faixa de preço
def classificar(preco):
    if preco < 2:
        return "Muito barato"
    elif preco <= 3:
        return "Barato"
    else:
        return "Caro"

# Aplica a função em cada linha da coluna 'preco'
df["faixa"] = df["preco"].apply(classificar)

# Salva o novo DataFrame
df.to_csv("./7-pandas/frutas_categorizadas.csv", index=False)

print(df)
```

---

## 🎯 Conclusão

Agora você sabe:

- O que é um DataFrame (uma tabela com colunas e linhas)
- Como criar, salvar e carregar dados usando `.csv`
- Como ordenar com `.sort_values()`
- Como filtrar com condições (`df[condição]`)
- Como aplicar funções em colunas com `.apply()`
- Como calcular média com `.mean()`
- Como montar regras para **categorizar dados**

Esses conhecimentos são **fundamentais** para qualquer pessoa que quer trabalhar com **análise de dados, planilhas automáticas, relatórios ou dashboards** em Python.

---