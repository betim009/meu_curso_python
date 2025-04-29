
# 🔢 Gerando Tabuadas com While

## 📚 Objetivo da Atividade

Neste exercício, o aluno irá:

- Pedir ao usuário um número.
- Utilizar dois `while` para exibir as tabuadas de **0 até esse número**, multiplicando de 1 até 10.

---

## ✅ Requisitos para fazer esta atividade

Você precisa saber:

- Como funciona o `while` (repetição com condição).
- Como fazer multiplicações.
- Como formatar strings com `f"{}"`.

---

## 🧠 Enunciado

1. Solicite ao usuário um número inteiro.
2. Use uma variável `c` que começa em 0 (contador da tabuada).
3. Para cada número `c`, use outro `while` para multiplicar `c` de 1 até 10.
4. Exiba a tabuada e repita o processo até o número digitado.

---

## 🧪 Código com explicações

```python
# Lê um número do usuário
n = int(input("Digite um número: "))
c = 0  # contador para controlar qual tabuada será mostrada
t = 1  # multiplicador

print()

# Enquanto c for menor ou igual a n
while c <= n:
    print(f"Tabuada do {c}:")  # título da tabuada

    # Exibe as multiplicações de 1 até 10
    while t <= 10:
        print(f"{c} x {t} = {c * t}")
        t = t + 1  # soma 1 ao t

    t = 0  # reinicia t para próxima tabuada
    c = c + 1  # passa para o próximo número
    print()
```

---

## ✅ Gabarito

```python
n = int(input("Digite um número: "))
c = 0
t = 1

print()

while c <= n:
    print(f"Tabuada do {c}:")
    while t <= 10:
        print(f"{c} x {t} = {c * t}")
        t = t + 1

    t = 0
    c = c + 1
    print()
```
