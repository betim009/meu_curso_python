# 📘 Guia Prático: Performance e Testes Técnicos em Python

Este material é uma revisão completa e prática sobre performance em Python com foco em testes técnicos. Ele foi baseado em perguntas reais e explicações objetivas, como se fosse uma conversa. Ideal para quem quer mandar bem em desafios de código em entrevistas!

---

## ⚡ 1. O que é performance em Python?

Performance é a capacidade do seu código de rodar **rápido** e usando **pouca memória**.

Em testes técnicos, seu código precisa:

* ✅ Estar **correto** (responder certo)
* ✅ Ser **eficiente** (responder rápido com entradas grandes)

---

## 📏 2. Complexidade (Big-O)

Isso mede o tempo que seu algoritmo leva para crescer:

| Tipo     | Nome       | Crescimento    |
| -------- | ---------- | -------------- |
| `O(1)`   | Constante  | Sempre o mesmo |
| `O(n)`   | Linear     | Cresce com n   |
| `O(n^2)` | Quadrático | Cresce muito   |

Evite laços aninhados se n pode ser grande (ex: `10^5`).

```python
# Ruim: O(n^2)
for i in range(n):
    for j in range(n):
        ...

# Melhor: O(n)
for i in range(n):
    ...
```

---

## 🧠 3. Quando usar função e quando escrever direto?

| Situação                         | Melhor fazer         |
| -------------------------------- | -------------------- |
| Comparar dois números simples    | Lógica direta        |
| Lógica usada várias vezes        | Criar função (`def`) |
| Código se repete ou fica confuso | Criar variável       |

Exemplo:

```python
# Melhor com variável
preco_total = preco_unitario * quantidade
if preco_total > 1000:
    print(preco_total)
```

---

## 🧮 4. max(), min() ou lógica manual?

Use `max()`, `min()`, `sum()` etc. sempre que puder.
Eles são otimizados (escritos em C) e são muito rápidos.

```python
maior = max(lista)  # Melhor que percorrer manualmente
```

Evite escrever a mesma lógica do zero a não ser que precise de algo customizado (ex: maior nota par).

---

## 🧪 5. Erro comum em testes técnicos: ignorar repetição

Se a entrada pode conter o mesmo item várias vezes, **precisamos tratar isso**.

Exemplo de erro:

```js
// JavaScript
// Erro: compara só uma nota por vez
if (notaAtual > maiorNota) { ... }
```

Certo seria somar todas as notas de cada item e calcular a média.

Python:

```python
soma = defaultdict(int)
contagem = defaultdict(int)
for id, nota in notas:
    soma[id] += nota
    contagem[id] += 1
```

---

## 🚀 6. Potências de 10 na prática

Quando o enunciado diz:

```text
1 ≤ n ≤ 10^5
```

Significa: **até 100.000 entradas!**

Tabela de potências:

| Potência | Valor         | Significado |
| -------- | ------------- | ----------- |
| 10^1     | 10            | Dez         |
| 10^3     | 1.000         | Mil         |
| 10^5     | 100.000       | Cem mil     |
| 10^6     | 1.000.000     | Um milhão   |
| 10^9     | 1.000.000.000 | Um bilhão   |

Se `n = 10^5`, seu código precisa rodar com 100.000 dados sem travar.

---

## 🧩 Exemplo prático (Food Ratings)

Problema: encontrar o prato com **maior média de notas** (se empatar, retorna o de menor ID).

```python
def solution(n, ratings):
    from collections import defaultdict

    soma = defaultdict(int)
    contagem = defaultdict(int)

    for dish_id, nota in ratings:
        soma[dish_id] += nota
        contagem[dish_id] += 1

    melhor_id = None
    melhor_media = -1

    for dish_id in soma:
        media = soma[dish_id] / contagem[dish_id]
        if (media > melhor_media) or (media == melhor_media and dish_id < melhor_id):
            melhor_media = media
            melhor_id = dish_id

    return melhor_id
```

---

Se quiser incluir benchmark, medição de tempo ou versões em JavaScript também, é só pedir! 🚀
