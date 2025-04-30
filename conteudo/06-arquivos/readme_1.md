
# 🍓 Leitura e Escrita de Arquivos em Python – Versão Avançada

Nesta versão ampliada do material, além de ler e escrever arquivos `.txt`, você também aprenderá a:

- Tratar erros ao acessar arquivos
- Diferenciar modos de abertura (`w`, `a`, `x`)
- Usar outras formas de leitura (`read()`, `readlines()`)
- Salvar dados como JSON
- Realizar desafios de prática

Tudo com o mesmo tema: frutas! 🍍🍇🍉

---

## 📄 Arquivo frutas.txt

```txt
Morango,2.19
Laranja,3.0
Melancia,1.77
Manga,3.5
Goiaba,2.09
```

---

## 📥 Parte 1 – Lendo o arquivo com segurança

### ✅ Com `try/except`

```python
arquivo = './6-arquivos/frutas.txt'

try:
    with open(arquivo, 'r') as file:
        for linha in file:
            print(linha.strip())
except FileNotFoundError:
    print("⚠️ Arquivo não encontrado.")
except Exception as erro:
    print(f"⚠️ Erro ao ler: {erro}")
```

---

## 📖 Outras formas de leitura

### `.readlines()`: Lê todas as linhas como uma lista

```python
with open(arquivo, 'r') as file:
    linhas = file.readlines()
    print(linhas)
```

### `.read()`: Lê todo o conteúdo como uma string única

```python
with open(arquivo, 'r') as file:
    conteudo = file.read()
    print(conteudo)
```

---

## 📝 Parte 2 – Gravando dados em arquivos

```python
frutas_precos = [
    {"fruta": "Morango", "preco": 2.19},
    {"fruta": "Laranja", "preco": 3.0},
    {"fruta": "Melancia", "preco": 1.77}
]
```

### `w`: sobrescreve
```python
with open("frutas_vazio.txt", "w") as file:
    for item in frutas_precos:
        file.write(f"{item['fruta']},{item['preco']}
")
```

### `a`: adiciona sem apagar o conteúdo

```python
with open("frutas_vazio.txt", "a") as file:
    file.write("Manga,3.5
")
```

### `x`: cria um novo arquivo, se ele não existir

```python
try:
    with open("novo_arquivo.txt", "x") as file:
        file.write("Goiaba,2.09
")
except FileExistsError:
    print("Arquivo já existe.")
```

---

## 💾 Salvando como JSON

Quando temos uma lista de dicionários, é muito comum usar JSON.

```python
import json

with open("frutas.json", "w") as arquivo_json:
    json.dump(frutas_precos, arquivo_json, indent=2)
```

### E para ler de volta?

```python
with open("frutas.json", "r") as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados)
```

---

## 🧠 Desafios para praticar

### 1. Média de preços

Crie um código que:

- Leia o arquivo `frutas.txt`
- Calcule a **média de preços** das frutas

### 2. Somente frutas com preço acima de 2.50

Filtrar e exibir só as frutas mais caras.

### 3. Gerar um novo arquivo `caros.txt`

- Deve conter apenas as frutas com preço acima de R$2.50
- Ex: `Melancia,2.90`

---

## ✅ Conclusão

Agora você conhece:

- Leitura simples e segura de arquivos
- Diferenças entre `read`, `readlines`, `strip`, `split`
- Gravação em arquivos com `w`, `a`, `x`
- Armazenamento e leitura de dados com `json`
- Como aplicar esse conhecimento em tarefas reais

Esse é um dos blocos fundamentais de qualquer projeto em Python profissional!

---
