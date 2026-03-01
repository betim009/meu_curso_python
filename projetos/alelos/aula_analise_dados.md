# 📘 Fundamentos de Estruturas de Dados em Python

---

# 📌 Capítulo 1 — O que é uma Lista?

## 🧠 Definição Simples

Uma **lista** em Python é uma estrutura que permite armazenar vários valores dentro de uma única variável.

Ela é:

- 📌 Ordenada (mantém a ordem dos elementos)
- 📌 Mutável (podemos alterar os valores)
- 📌 Indexada (cada item tem uma posição)

---

## 📦 Exemplo de Lista

```python
numeros = [10, 20, 30, 40]
```

---

## 🔢 Como acessar um item da lista?

⚠️ O índice começa em **0**.

```python
print(numeros[0])  # 10
print(numeros[2])  # 30
```

Se acessar um índice inexistente:

```python
print(numeros[10])  # IndexError
```

---

# 📌 Capítulo 2 — O que é um Dicionário?

## 🧠 Definição Simples

Um **dicionário** armazena dados no formato:

```
chave : valor
```

---

## 📦 Exemplo

```python
pessoa = {
    "nome": "Alberto",
    "idade": 30,
    "cidade": "Manhumirim"
}
```

---

## 🔑 Como acessar um item?

```python
print(pessoa["nome"])
print(pessoa["idade"])
```

Se a chave não existir:

```python
print(pessoa["altura"])  # KeyError
```

---

# 📌 Capítulo 3 — Diferença entre Lista x Dicionário

| Lista | Dicionário |
|-------|------------|
| Usa índice numérico | Usa chave |
| Ordem importa | Organização por nome |
| numeros[0] | pessoa["nome"] |

---

# 📌 Capítulo 4 — O que é uma Base de Dados?

## 🧠 Definição Simples

Uma **base de dados** é um conjunto organizado de informações.

Ela pode estar:

- Em um arquivo (Excel, CSV, JSON)
- Em um banco de dados (MySQL, PostgreSQL)
- Em memória (listas e dicionários no Python)

Basicamente:

> Base de dados é um conjunto estruturado de informações.

Exemplo simples:

| nome     | idade | cidade        |
|----------|-------|--------------|
| Ana      | 25    | Vitória      |
| João     | 30    | Belo Horizonte |

Isso já é uma base de dados.

---

# 📌 Capítulo 5 — O que é uma Lista de Dicionários?

## 🧠 Definição

Uma **lista de dicionários** é quando:

- Cada linha da base vira um dicionário
- Todos os dicionários ficam dentro de uma lista

Estrutura visual:

```
[
    {linha 1},
    {linha 2},
    {linha 3}
]
```

---

## 📦 Exemplo

```python
base = [
    {"nome": "Ana", "idade": 25},
    {"nome": "João", "idade": 30}
]
```

---

## 🔁 Como acessar?

### Acessar uma linha inteira:

```python
print(base[0])
```

### Acessar um valor específico:

```python
print(base[0]["nome"])   # Ana
print(base[1]["idade"])  # 30
```

⚠️ Primeiro acessamos a posição da lista.  
⚠️ Depois acessamos a chave do dicionário.

---

# 📌 Capítulo 6 — O que é um Dicionário de Listas?

## 🧠 Definição

Um **dicionário de listas** é quando:

- Cada coluna vira uma chave
- Cada chave contém uma lista de valores

Estrutura visual:

```
{
    "coluna1": [valor1, valor2],
    "coluna2": [valor1, valor2]
}
```

---

## 📦 Exemplo

```python
base = {
    "nome": ["Ana", "João"],
    "idade": [25, 30]
}
```

---

## 🔁 Como acessar?

### Acessar uma coluna inteira:

```python
print(base["nome"])
```

### Acessar um valor específico:

```python
print(base["nome"][0])   # Ana
print(base["idade"][1])  # 30
```

⚠️ Primeiro acessamos a chave.  
⚠️ Depois acessamos a posição da lista.

---

# 🔥 Diferença Importante

| Lista de Dicionários | Dicionário de Listas |
|----------------------|----------------------|
| Estrutura por linha  | Estrutura por coluna |
| Mais intuitivo       | Mais eficiente para análise |
| Ideal para APIs      | Ideal para cálculos e gráficos |

---

# 📌 Capítulo 7 — Estrutura de Repetição

## 🧠 O que é uma Estrutura de Repetição?

Uma **estrutura de repetição** é um recurso da programação que permite executar um bloco de código várias vezes.

Ela é usada quando:

- Precisamos percorrer uma lista
- Precisamos analisar vários dados
- Precisamos automatizar tarefas repetitivas

Em Python, a principal estrutura de repetição é o `for`.

---

# 📌 Como usar o `for`

## 🧠 Estrutura básica

```python
for elemento in lista:
    print(elemento)
```

### 📌 Regras do `for`

- O `for` percorre cada item da sequência.
- A variável (ex: `elemento`) recebe um valor por vez.
- O bloco identado será executado para cada item.

---

## 📦 Exemplo simples

```python
numeros = [10, 20, 30]

for numero in numeros:
    print(numero)
```

Saída:
```
10
20
30
```

---

# 📌 Como usar o `for in range`

## 🧠 O que é `range`?

A função `range()` gera uma sequência de números.

```python
range(inicio, fim)
```

⚠️ O número final NÃO é incluído.

---

## 📦 Exemplo

```python
for i in range(3):
    print(i)
```

Saída:
```
0
1
2
```

---

## 📌 Regras do `for in range`

- Começa em 0 se não especificar o início.
- O valor final nunca é incluído.
- Muito usado quando precisamos de índice.

---

# 📌 Usando `for` com Lista de Dicionários

Lembre da estrutura:

```python
base = [
    {"nome": "Ana", "idade": 25},
    {"nome": "João", "idade": 30}
]
```

---

## 🔁 Percorrendo corretamente

```python
for item in base:
    print(item["nome"], "-", item["idade"])
```

### 🧠 Como funciona?

- `item` recebe cada dicionário da lista.
- Depois acessamos as chaves normalmente.

---

# 📌 Usando `for in range` com Dicionário de Listas

Estrutura:

```python
base = {
    "nome": ["Ana", "João"],
    "idade": [25, 30]
}
```

---

## 🔁 Percorrendo com índice

```python
for i in range(len(base["nome"])):
    print(base["nome"][i], "-", base["idade"][i])
```

### 🧠 Como funciona?

- `len(base["nome"])` retorna o tamanho da lista.
- `i` representa o índice.
- Acessamos a mesma posição em ambas as listas.

---

# ⚠️ Cuidados Importantes

- Sempre verifique se as listas possuem o mesmo tamanho.
- Cuidado com índices fora do limite.
- Atenção à identação (Python depende dela).

---


# 🏁 Conclusão do Capítulo

Agora você sabe:

- O que é estrutura de repetição
- Como usar `for`
- Como usar `for in range`
- Como aplicar em lista de dicionários
- Como aplicar em dicionário de listas

---

# 📌 Capítulo 8 — Exercícios Práticos com Base de Dados de Alelos

Agora vamos usar a base de dados de alelos que construímos anteriormente.

Lembre da estrutura utilizada:

## 📦 Lista de Dicionários

```python
lista_de_dicionarios = [
    {
        "allele": "HLA-DPA1*02:01/DPB1*05:01",
        "netmhciipan_el percentile": 4.6
    },
    {
        "allele": "HLA-DPA1*03:01/DPB1*04:02",
        "netmhciipan_el percentile": 4.3
    },
    {
        "allele": "HLA-DRB1*01:01",
        "netmhciipan_el percentile": 3.8
    }
]
```

---

## 📦 Dicionário de Listas

```python
dicionario_com_listas = {
    "allele": [
        "HLA-DPA1*02:01/DPB1*05:01",
        "HLA-DPA1*03:01/DPB1*04:02",
        "HLA-DRB1*01:01"
    ],
    "netmhciipan_el percentile": [4.6, 4.3, 3.8]
}
```

---

# 📝 Exercício 1

Percorra a **lista de dicionários** e imprima apenas os alelos cujo percentile seja menor que 4.

---

# ✅ Gabarito Explicado

```python
for item in lista_de_dicionarios:
    if item["netmhciipan_el percentile"] < 4:
        print(item["allele"], "-", item["netmhciipan_el percentile"])
```

### 🧠 Explicação

- O `for` percorre cada dicionário.
- O `if` verifica se o percentile é menor que 4.
- Se for verdadeiro, imprime.

---

# 📝 Exercício 2

Usando o **dicionário de listas**, imprima apenas os alelos cujo percentile seja maior que 4.

---

# ✅ Gabarito Explicado

```python
for i in range(len(dicionario_com_listas["allele"])):
    if dicionario_com_listas["netmhciipan_el percentile"][i] > 4:
        print(
            dicionario_com_listas["allele"][i],
            "-",
            dicionario_com_listas["netmhciipan_el percentile"][i]
        )
```

### 🧠 Explicação

- `len()` pega o tamanho da lista.
- `i` representa a posição.
- O `if` compara o valor da mesma posição nas duas listas.

---

# 📝 Exercício 3

Conte quantos alelos possuem percentile menor que 4 usando lista de dicionários.

---

# ✅ Gabarito Explicado

```python
contador = 0

for item in lista_de_dicionarios:
    if item["netmhciipan_el percentile"] < 4:
        contador += 1

print("Total:", contador)
```

### 🧠 Explicação

- Criamos um contador iniciando em 0.
- Cada vez que a condição for verdadeira, somamos 1.
- No final imprimimos o total.

---

# 📝 Exercício 4 (Desafio)

Encontre o menor valor de percentile na lista de dicionários.

---

# ✅ Gabarito Explicado

```python
menor = lista_de_dicionarios[0]["netmhciipan_el percentile"]

for item in lista_de_dicionarios:
    if item["netmhciipan_el percentile"] < menor:
        menor = item["netmhciipan_el percentile"]

print("Menor percentile:", menor)
```

### 🧠 Explicação

- Começamos assumindo que o primeiro valor é o menor.
- Comparamos cada valor com o atual menor.
- Se encontrarmos um menor, atualizamos.

---

# 🎯 Conclusão dos Exercícios

Com esses exercícios você praticou:

- `for`
- `for in range`
- `if`
- Comparações numéricas
- Uso de contador
- Lógica de menor valor

Esses são fundamentos essenciais para análise de dados em Python.

---

# 📌 Capítulo 9 — Base de Dados: Registro de Doenças

Agora vamos criar uma nova base de dados simulando um **registro de doenças em um hospital**.

Cada registro possui:

- nome do paciente
- idade
- doença
- dias internado

---

# 📦 Modelo 1 — Lista de Dicionários

```python
registro_doencas_lista = [
    {"paciente": "Ana", "idade": 25, "doenca": "Dengue", "dias_internado": 3},
    {"paciente": "Carlos", "idade": 40, "doenca": "Covid-19", "dias_internado": 7},
    {"paciente": "Marina", "idade": 32, "doenca": "Pneumonia", "dias_internado": 5},
    {"paciente": "João", "idade": 60, "doenca": "Covid-19", "dias_internado": 10},
    {"paciente": "Fernanda", "idade": 29, "doenca": "Dengue", "dias_internado": 2}
]
```

---

# 📦 Modelo 2 — Dicionário de Listas

```python
registro_doencas_dict = {
    "paciente": ["Ana", "Carlos", "Marina", "João", "Fernanda"],
    "idade": [25, 40, 32, 60, 29],
    "doenca": ["Dengue", "Covid-19", "Pneumonia", "Covid-19", "Dengue"],
    "dias_internado": [3, 7, 5, 10, 2]
}
```

---

# 📝 Exercício 1

Imprima todos os pacientes com **Covid-19** usando lista de dicionários.

---

# ✅ Gabarito Explicado

```python
for item in registro_doencas_lista:
    if item["doenca"] == "Covid-19":
        print(item["paciente"], "-", item["dias_internado"], "dias")
```

---

# 📝 Exercício 2

Imprima todos os pacientes com mais de 5 dias internados usando dicionário de listas.

---

# ✅ Gabarito Explicado

```python
for i in range(len(registro_doencas_dict["paciente"])):
    if registro_doencas_dict["dias_internado"][i] > 5:
        print(
            registro_doencas_dict["paciente"][i],
            "-",
            registro_doencas_dict["dias_internado"][i],
            "dias"
        )
```

---

# 📝 Exercício 3

Conte quantos pacientes tiveram Dengue (usando lista de dicionários).

---

# ✅ Gabarito Explicado

```python
contador = 0

for item in registro_doencas_lista:
    if item["doenca"] == "Dengue":
        contador += 1

print("Total de casos de Dengue:", contador)
```

---

# 📝 Exercício 4 (Desafio)

Descubra qual foi o maior número de dias internado.

---

# ✅ Gabarito Explicado

```python
maior = registro_doencas_lista[0]["dias_internado"]

for item in registro_doencas_lista:
    if item["dias_internado"] > maior:
        maior = item["dias_internado"]

print("Maior tempo de internação:", maior)
```

---

# 🎯 Objetivo do Capítulo

Com esse novo conjunto de dados você praticou novamente:

- Estrutura de base de dados
- Lista de dicionários
- Dicionário de listas
- Estrutura de repetição
- Condicionais
- Lógica de contagem
- Lógica de maior valor

Agora você já consegue analisar pequenos conjuntos de dados manualmente em Python.

---

# 📌 Capítulo Final — Revisão Geral e Próximos Passos

## 🧠 Resumo do que você aprendeu

Durante este material você construiu uma base sólida em:

### 1️⃣ Estruturas Fundamentais
- O que é uma **lista**
- O que é um **dicionário**
- Diferença entre acessar por índice e por chave

### 2️⃣ Representação de Base de Dados
- O que é uma base de dados
- Como representar dados como **lista de dicionários** (modelo por linha)
- Como representar dados como **dicionário de listas** (modelo por coluna)

### 3️⃣ Estruturas de Repetição
- Como funciona o `for`
- Como funciona o `for in range`
- Como percorrer listas
- Como percorrer dicionários
- Como usar `len()` para trabalhar com índices

### 4️⃣ Estrutura Condicional
- Como usar `if`
- Como fazer comparações numéricas
- Como contar registros
- Como encontrar maior e menor valor

---

# 🎯 O que você já consegue fazer agora?

Você já consegue:

- Percorrer bases de dados
- Filtrar informações
- Contar registros específicos
- Encontrar valores extremos
- Analisar pequenos conjuntos de dados manualmente

Isso já é o começo da **análise de dados em Python**.

---

# 🤖 Como pedir uma base de dados para praticar com IA

Você pode usar um agente de IA (como ChatGPT ou outro assistente) para gerar novas bases de dados para treinar.

## 📌 Exemplo de Prompt

```
Crie uma base de dados fictícia com pelo menos 10 registros sobre vendas de uma loja.

Quero os dados nos dois formatos:

1) Lista de dicionários
2) Dicionário de listas

Cada registro deve ter:
- produto
- preço
- quantidade vendida
- vendedor

Depois crie 5 exercícios usando for e if para eu praticar filtros, contagem e maior valor.

Inclua gabarito explicativo.
```

---

# 🚀 Próximo Nível

Se quiser evoluir ainda mais, os próximos passos naturais são:

- Aprender funções (`def`)
- Aprender a organizar código em módulos
- Trabalhar com arquivos CSV
- Aprender a usar Pandas

---

# 🏁 Encerramento

Se você entendeu tudo até aqui, significa que já domina a base lógica necessária para trabalhar com dados em Python.

Continue praticando.
A prática é o que transforma conhecimento em habilidade.