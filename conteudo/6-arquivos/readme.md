
# 🍓 Leitura e Escrita de Arquivos em Python

Neste material, vamos aprender a **ler** e **escrever** arquivos `.txt` em Python com exemplos simples usando uma lista de frutas e seus preços.

---

## 📄 O conteúdo do nosso arquivo frutas.txt

```txt
Morango,2.19
Laranja,3.0
Melancia,1.77
Manga,3.5
Goiaba,2.09
```

Cada linha contém uma fruta e seu preço separados por vírgula.

---

## 📥 Parte 1 – Lendo o arquivo linha por linha

Aqui vamos **abrir** o arquivo e exibir cada linha removendo espaços e quebras de linha.

```python
# Nome do arquivo
arquivo = './6-arquivos/frutas.txt'  # Caminho para o arquivo frutas.txt dentro do diretório '6-arquivos'

# Abre o arquivo para leitura
with open(arquivo, 'r') as file:  # Modo leitura
    for linha in file:  # Percorre cada linha
        print(linha.strip())  # Remove espaços e quebras de linha
```

**Saída esperada:**
```
Morango,2.19
Laranja,3.0
Melancia,1.77
Manga,3.5
Goiaba,2.09
```

---

## 📤 Parte 2 – Processando os dados do arquivo

Vamos ler, separar os valores e transformar em dados utilizáveis.

### 🔹 Passo 1: Dividindo por vírgula

```python
arquivo = "./6-arquivos/frutas.txt"

# Lê o arquivo e mostra os dados divididos
with open(arquivo, "r") as file:
    for linha in file:
        print(linha.strip().split(","))  # Exibe como lista
```

**Saída esperada:**
```
['Morango', '2.19']
['Laranja', '3.0']
['Melancia', '1.77']
['Manga', '3.5']
['Goiaba', '2.09']
```

---

### 🔹 Passo 2: Exibindo fruta e preço separadamente

```python
with open(arquivo, "r") as file:
    for linha in file:
        fruta, preco = linha.strip().split(",")
        print(fruta, preco)
```

**Saída esperada:**
```
Morango 2.19
Laranja 3.0
Melancia 1.77
Manga 3.5
Goiaba 2.09
```

---

### 🔹 Passo 3: Salvando os dados em uma lista de dicionários

```python
frutas_precos = []

with open(arquivo, "r") as file:
    for linha in file:
        fruta, preco = linha.strip().split(",")
        frutas_precos.append({"fruta": fruta, "preco": float(preco)})

print(frutas_precos)
```

**Saída esperada:**

```python
[
    {'fruta': 'Morango', 'preco': 2.19},
    {'fruta': 'Laranja', 'preco': 3.0},
    {'fruta': 'Melancia', 'preco': 1.77},
    {'fruta': 'Manga', 'preco': 3.5},
    {'fruta': 'Goiaba', 'preco': 2.09}
]
```

---

## 📝 Parte 3 – Escrevendo em um novo arquivo

Agora vamos criar um novo arquivo e escrever os dados nele.

```python
# Caminho do novo arquivo
arquivo = "./6-arquivos/frutas_vazio.txt"

# Lista de frutas
frutas_precos = [
    {"fruta": "Morango", "preco": 2.19},
    {"fruta": "Laranja", "preco": 3.0},
    {"fruta": "Melancia", "preco": 1.77},
    {"fruta": "Manga", "preco": 3.5},
    {"fruta": "Goiaba", "preco": 2.09},
]

# Abre o arquivo para escrita
with open(arquivo, "w") as file:
    for item in frutas_precos:
        file.write(f"{item['fruta']},{item['preco']}
")
```

> ⚠️ **Atenção**: esse código irá **sobrescrever** o conteúdo do arquivo `frutas_vazio.txt`. Mantenha ele **vazio** antes de testar.

---

## ✅ Conclusão

Com esses passos, você aprendeu a:

- Ler arquivos `.txt` linha por linha.
- Separar valores e convertê-los.
- Armazenar os dados em uma estrutura organizada.
- Escrever arquivos novos a partir de listas.

Esse conhecimento é essencial para trabalhar com **dados externos**, como planilhas, logs ou relatórios em Python.

---
