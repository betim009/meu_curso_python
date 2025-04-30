
# 🍓 Trabalhando com Listas e Repetições em Python

## 📚 Introdução

Em Python, **listas** são usadas para armazenar **múltiplos valores em uma única variável**.  
Elas podem ser percorridas com estruturas de repetição como `for` e `while`.

Este material vai te mostrar:

- Como percorrer listas com `for`
- Como acessar índices com `enumerate()` e `range()`
- Como controlar repetições com `while`
- Como usar comandos especiais: `break` e `continue`
- Como criar listas de forma rápida com **List Comprehension**

---

## 🔹 Percorrendo uma lista com `for`

Quando usamos `for` com uma lista, conseguimos acessar cada item dela, um por um.

```python
frutas = ["Morango", "Laranja", "Melancia", "Manga", "Goiaba"]

for item in frutas:
    print(item)
```

➡️ O `for` percorre todos os elementos da lista e exibe cada fruta.

---

## 🔹 Acessando índice e valor com `enumerate()`

Se quisermos saber a **posição de cada item**, usamos `enumerate()`.

```python
frutas = ["Morango", "Laranja", "Melancia", "Manga", "Goiaba"]
precos = [2.19, 3.0, 1.77, 3.5, 2.09]

for index, item in enumerate(frutas):
    print(f"A fruta: {item} custa {precos[index]}")
```

---

## 🔹 Trabalhando com um intervalo de índices: `range()`

Com `range()`, definimos um intervalo exato de índices.

```python
for index in range(0, 2):
    print(frutas[index])
```

➡️ O `range(0, 2)` gera os valores 0 e 1 — exibindo apenas os dois primeiros itens.

---

## 🔁 Repetição com `while`

O `while` executa enquanto a **condição for verdadeira**.

```python
contador = 1

while contador <= 3:
    print(f"Repetição número {contador}")
    contador += 1
```

---

## ✋ Interrompendo repetições com `break`

O `break` serve para **parar um loop imediatamente**.

```python
while True:
    texto = input("Digite 'sair' para encerrar: ")
    if texto == "sair":
        break
```

---

## 🔄 Pulando uma repetição com `continue`

O `continue` serve para **pular o restante do código daquela repetição** e ir para a próxima.

```python
for numero in range(5):
    if numero == 2:
        continue  # Pula o número 2
    print(numero)
```

---

## 🔂 Repetição infinita com `while True`

Você também pode usar `while True` quando quiser **controlar manualmente o encerramento** com `break`.

```python
while True:
    resposta = input("Deseja continuar? (s/n): ")
    if resposta == "n":
        break
```

---

## 🔹 List Comprehension: Criando listas de maneira rápida

**List comprehension** é uma forma **resumida** de criar listas.

### Exemplo básico:

```python
# Cria uma lista com números de 0 a 4
numeros = [i for i in range(5)]
print(numeros)  # [0, 1, 2, 3, 4]
```

➡️ Em vez de usar um `for` separado para adicionar elementos, fazemos tudo em uma linha.

---

### Exemplo aplicando condição:

```python
# Cria uma lista apenas com números pares de 0 a 9
pares = [i for i in range(10) if i % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
```

---

## 🧠 Quando usar List Comprehension?

- Para criar listas novas **baseadas** em uma sequência.
- Quando quiser um código mais **curto** e **mais rápido** de escrever.

> Dica: Se o código começar a ficar difícil de ler, é melhor usar `for` normal para manter a clareza!

---

# ✅ Fechamento

Agora você aprendeu:

- `for`
- `while`
- `while True`
- `range()`
- `enumerate()`
- `break`
- `continue`
- `list comprehension`

Essas ferramentas são **essenciais** para quem quer dominar as estruturas de repetição em Python!
