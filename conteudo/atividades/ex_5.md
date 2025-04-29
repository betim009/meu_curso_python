
# 🔁 Exibindo Números Pares até 200 com While

## 📚 Objetivo da Atividade

Criar um programa que utilize a estrutura de repetição `while` para:

- Contar de 1 até 200.
- Exibir apenas os **números pares** nesse intervalo.

---

## ✅ Requisitos para fazer esta atividade

Você deve saber:

- Usar `while` para repetir ações.
- Utilizar o operador `%` para saber se o número é par.
- Incrementar variáveis com `n += 1`.

---

## 🧠 Enunciado

Crie um programa que:

1. Comece com a variável `n` valendo 1.
2. Use `while` para contar até 200.
3. Verifique se o número é **par** (`n % 2 == 0`).
4. Se for, exiba o número na tela.

---

## 🧪 Código com explicações

```python
# Começa com n valendo 1
n = 1

# Enquanto n for menor ou igual a 200
while n <= 200:
    n += 1  # Soma 1 ao n

    # Se o número for par, imprime
    if n % 2 == 0:
        print(n)
```

---

## ✅ Gabarito

```python
n = 1

while n <= 200:
    n += 1
    if n % 2 == 0:
        print(n)
```
