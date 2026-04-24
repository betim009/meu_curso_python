
# 📄 Trabalhando com Arquivos CSV em Pandas: Pacientes e Produtos

Neste material vamos explorar como **ler arquivos CSV**, **selecionar colunas**, **acessar valores específicos** e **percorrer dados com `for`** usando a biblioteca Pandas.

Tudo será explicado passo a passo, com exemplos reais e **saídas esperadas ilustradas**.

---

## 🧠 Objetivo

Aprender a:

- Carregar arquivos `.csv` para o Python
- Acessar colunas específicas
- Utilizar `.loc[]` e `.iloc[]`
- Usar `iterrows()` para percorrer linha por linha

---

## 📥 Leitura dos Arquivos

```python
import pandas as pd

# Leitura dos arquivos CSV
file = pd.read_csv('produtos_estoque.csv')
file_pacientes = pd.read_csv('pacientes.csv')
```

📘 `pd.read_csv()` é o método que carrega um arquivo CSV para dentro do Python em formato de **DataFrame**, que é uma **tabela de dados** com colunas e linhas.

📤 Exemplo de visualização da tabela `produtos_estoque.csv`:

```
   id   Produto  Estoque Data de Validade  Preco
0   1     Arroz       50       2025-12-30  20.50
1   2    Feijão       30       2025-10-15  10.75
2   3  Macarrão       45       2026-02-01   5.30
...
```

---

## 🎯 Selecionando Colunas Específicas

```python
cols_produto_preco = file[['Produto', 'Preco']]
cols_produto_preco_estoque = file[['Produto', 'Preco', 'Estoque']]
```

📘 Quando queremos trabalhar com apenas algumas colunas, podemos selecionar elas com duplas colchetes (`[[ ]]`).

📤 Resultado de `cols_produto_preco`:
```
   Produto  Preco
0   Arroz   20.50
1  Feijão   10.75
2 Macarrão   5.30
...
```

---

## 🔍 Acessando Valores com `.loc[]` e `.iloc[]`

```python
loc_arroz = file.loc[0, 'Produto']
iloc_arroz = file.iloc[0, 1]
```

📘 `.loc[]` acessa usando **nomes (rótulos)**.  
📘 `.iloc[]` acessa usando **índices numéricos** (posição da célula).

📤 Ambos retornam:

```
'Arroz'
```

⚠️ `.loc[0, 'Produto']` → linha 0, coluna "Produto".  
⚠️ `.iloc[0, 1]` → linha 0, coluna na posição 1 (que também é "Produto").

---

## 🔁 Percorrendo os dados com `iterrows()`

### 👨‍⚕️ Exemplo com pacientes

```python
for index, paciente in file_pacientes.iterrows():
    print(paciente['nome'])
```

📤 Resultado esperado:
```
João Silva
Maria Oliveira
Pedro Santos
Ana Costa
...
```

⚠️ A linha `paciente.loc['nome']` não é necessária. Usar `paciente['nome']` já é o suficiente.

---

### 🛒 Exemplo com produtos

```python
for produto in file.iterrows():
    print(produto[1].loc['Produto'])
```

📤 Resultado esperado:
```
Arroz
Feijão
Macarrão
Óleo
Açúcar
```

📘 `produto[1]` representa a **linha** como uma pequena tabela, e `loc['Produto']` acessa a coluna "Produto".

✔️ Versão alternativa mais clara:

```python
for _, linha in file.iterrows():
    print(linha['Produto'])
```

---

## ✅ Conclusão

Neste exemplo você aprendeu:

- Como **ler arquivos CSV**
- Como **acessar colunas específicas**
- Como **acessar valores** com `.loc[]` e `.iloc[]`
- Como **percorrer tabelas linha por linha** com `iterrows()`

Essas são bases muito importantes para análise de dados reais.

Se quiser, posso criar **exercícios com gabarito** sobre este conteúdo. Deseja?
