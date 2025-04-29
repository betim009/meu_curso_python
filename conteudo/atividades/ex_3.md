
# 🔢 Verificando se um número é Par ou Ímpar

## 📚 Objetivo da Atividade

Nesta atividade, o aluno irá criar um programa que:

- Solicita um número inteiro ao usuário.
- Verifica se o número é **par** ou **ímpar**.
- Exibe uma mensagem com o resultado.

---

## ✅ Requisitos para fazer esta atividade

Antes de fazer esta atividade, é importante saber:

- Como usar `input()` e `int()`.
- Como usar o operador **resto da divisão** (`%`).
- Como utilizar `if` e `else`.

---

## 🧠 Enunciado

1. Peça ao usuário que digite um número inteiro.
2. Se o número dividido por 2 tiver **resto 0**, ele é **par**.
3. Se tiver **resto diferente de 0**, é **ímpar**.

---

## 🧪 Código com explicações

```python
# Recebe um número inteiro do usuário
n = int(input("Digite um número: "))

# Verifica se o número é par (resto da divisão por 2 é 0)
if n % 2 == 0:
    print(f"{n} é par")
else:
    print(f"{n} é impar")
```

---

## ✅ Gabarito

```python
n = int(input("Digite um número: "))

if n % 2 == 0:
    print(f"{n} é par")
else:
    print(f"{n} é impar")
```
