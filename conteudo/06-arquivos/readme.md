
# 🍓 Leitura e Escrita de Arquivos em Python

Neste material, vamos aprender a **ler** e **escrever** arquivos `.txt` em Python com exemplos simples usando uma lista de frutas e seus preços.

---

## 🧠 Por que aprender isso?

Em muitos programas, é necessário **salvar dados** em arquivos ou **ler informações** previamente registradas. Esses dados podem ser de:

- Cadastros de usuários
- Resultados de vendas
- Logs de sistema
- Informações de produtos

Saber manipular arquivos é um passo essencial para tornar seu programa **útil no mundo real**.

---

## 📄 O conteúdo do nosso arquivo `frutas.txt`

```txt
Morango,2.19
Laranja,3.0
Melancia,1.77
Manga,3.5
Goiaba,2.09
```

Cada linha contém:
- O nome da fruta
- Seu preço

Eles estão separados por vírgula (`,`), o que é comum em arquivos `.csv`.

---

## 📥 Parte 1 – Lendo o arquivo linha por linha

Queremos **abrir o arquivo** e exibir cada linha, removendo os espaços extras e quebras de linha.

```python
# Nome do arquivo
arquivo = './6-arquivos/frutas.txt'

# Abre o arquivo para leitura
with open(arquivo, 'r') as file:
    for linha in file:
        print(linha.strip())  # Remove espaços e quebras de linha
```

### ✅ O que esse código faz?

- `open(arquivo, 'r')`: abre o arquivo no modo leitura
- `for linha in file`: percorre cada linha do arquivo
- `linha.strip()`: remove quebras de linha e espaços desnecessários

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

Agora vamos **separar as informações**, tratando o texto para extrair dados úteis.

---

### 🔹 Passo 1: Dividindo por vírgula

```python
with open(arquivo, "r") as file:
    for linha in file:
        print(linha.strip().split(","))
```

- `.split(",")`: separa a linha usando a vírgula como divisor
- Resultado: uma **lista com duas partes**: nome da fruta e preço

**Saída esperada:**
```
['Morango', '2.19']
['Laranja', '3.0']
['Melancia', '1.77']
['Manga', '3.5']
['Goiaba', '2.09']
```

---

### 🔹 Passo 2: Exibindo nome e preço separadamente

```python
with open(arquivo, "r") as file:
    for linha in file:
        fruta, preco = linha.strip().split(",")
        print(fruta, preco)
```

Aqui usamos **duas variáveis** para armazenar cada parte da linha.

**Saída esperada:**
```
Morango 2.19
Laranja 3.0
Melancia 1.77
Manga 3.5
Goiaba 2.09
```

---

### 🔹 Passo 3: Salvando como lista de dicionários

Agora vamos transformar os dados em **estrutura organizada**:

```python
frutas_precos = []

with open(arquivo, "r") as file:
    for linha in file:
        fruta, preco = linha.strip().split(",")
        frutas_precos.append({"fruta": fruta, "preco": float(preco)})

print(frutas_precos)
```

### ✅ O que acontece aqui?

- Criamos uma **lista vazia**
- Para cada linha do arquivo:
  - Separamos `fruta` e `preço`
  - Convertendo o preço para `float`
  - Adicionamos à lista um **dicionário com os dados**

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

Agora que temos a lista de frutas com preços, vamos **salvar isso em outro arquivo**.

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
        file.write(f"{item['fruta']},{item['preco']}")
```

### ⚠️ Cuidado!

- O modo `"w"` **apaga o conteúdo** anterior do arquivo.
- Use com cuidado quando for sobrescrever.

---

## ✅ Conclusão

Neste material, você aprendeu:

- Como **ler um arquivo** linha por linha em Python
- Como **tratar dados de texto** e extrair informações
- Como **organizar os dados em dicionários**
- Como **salvar esses dados** em um novo arquivo

Essas habilidades são úteis em muitos contextos: análise de dados, relatórios, automações, e sistemas que lidam com cadastros ou arquivos `.csv`.

---

Pronto para o próximo nível? Agora você pode integrar esses dados com **interfaces gráficas**, **bancos de dados** ou até **web APIs**!
