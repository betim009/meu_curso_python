
# 📊 Métodos do Pandas com Explicações, Exemplos e Saídas

Este material é ideal para quem está aprendendo Pandas do zero. Aqui você encontra, para cada método:

1. 📘 O que é o método  
2. ✅ Quando usar  
3. 🤔 Por que usar  
4. 👨‍💻 Exemplo prático  
5. 📤 Saída esperada  
6. ⚠️ Cuidados importantes  

---

## 1. `pd.read_csv()`

📘 **O que é:**  
Esse método lê um arquivo `.csv` (planilha de texto separada por vírgulas) e transforma em um DataFrame (tabela no Python).

✅ **Quando usar:**  
Quando você quer abrir arquivos `.csv` no seu código Python para analisar dados.

🤔 **Por que usar:**  
É uma das formas mais comuns de importar dados de planilhas para o Python.

👨‍💻 **Exemplo:**

```python
import pandas as pd

df = pd.read_csv("frutas.csv")
print(df)
```

📤 **Saída esperada:**
```
     fruta  preco
0  Morango   2.19
1  Laranja   3.00
2 Melancia   1.77
3    Manga   3.50
4   Goiaba   2.09
```

⚠️ **Cuidado:**  
Se o nome ou caminho do arquivo estiver errado, vai gerar erro.

---

## 2. `df.to_csv()`

📘 **O que é:**  
Esse método salva um DataFrame em um arquivo `.csv`.

✅ **Quando usar:**  
Quando você quer guardar sua tabela em um arquivo para reusar ou abrir em outro programa (como Excel).

🤔 **Por que usar:**  
Permite exportar os dados do seu código Python para serem usados em outros lugares.

👨‍💻 **Exemplo:**

```python
df.to_csv("saida.csv", index=False)
```

📤 Cria um arquivo com conteúdo assim:
```
fruta,preco
Morango,2.19
Laranja,3.0
...
```

⚠️ **Cuidado:**  
Sempre use `index=False` para não salvar o número da linha como coluna.

---

## 3. `df.head()`

📘 **O que é:**  
Mostra as primeiras linhas do DataFrame.

✅ **Quando usar:**  
Logo após carregar os dados para ter uma ideia rápida da estrutura.

🤔 **Por que usar:**  
É útil para visualizar uma amostra do começo da tabela.

👨‍💻 **Exemplo:**

```python
print(df.head(2))
```

📤 **Saída esperada:**
```
     fruta  preco
0  Morango   2.19
1  Laranja   3.00
```

---

## 4. `df.info()`

📘 **O que é:**  
Mostra o resumo das colunas, tipos de dados e valores não nulos.

✅ **Quando usar:**  
Sempre que carregar um DataFrame novo.

🤔 **Por que usar:**  
Ajuda a entender o formato dos dados, tipos e se tem dados ausentes.

👨‍💻 **Exemplo:**

```python
df.info()
```

📤 **Saída esperada:**
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   fruta   5 non-null      object 
 1   preco   5 non-null      float64
```

---

## 5. `df.describe()`

📘 **O que é:**  
Gera estatísticas descritivas das colunas numéricas do DataFrame.

✅ **Quando usar:**  
Para entender como estão distribuídos os dados numéricos (ex: preços, idades, quantidades).

🤔 **Por que usar:**  
Ajuda a ver valores como média, mínimo, máximo, etc.

👨‍💻 **Exemplo:**

```python
print(df.describe())
```

📤 **Saída esperada:**
```
          preco
count  5.000000
mean   2.510000
std    0.654920
min    1.770000
max    3.500000
```

---

## 6. `df["coluna"]`

📘 **O que é:**  
Seleciona uma coluna específica do DataFrame.

✅ **Quando usar:**  
Quando quiser trabalhar com apenas uma informação da tabela (ex: só os preços).

🤔 **Por que usar:**  
Permite manipular ou visualizar apenas uma parte dos dados.

👨‍💻 **Exemplo:**

```python
print(df["fruta"])
```

📤 **Saída esperada:**
```
0     Morango
1     Laranja
2    Melancia
3        Manga
4       Goiaba
Name: fruta, dtype: object
```

---

Se quiser que eu continue com os próximos métodos nesse mesmo formato, posso fazer agora mesmo! Deseja?
