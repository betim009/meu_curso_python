
# 🔺 Classificação de Triângulos com Base nos Lados

## 📚 Objetivo da Atividade

Nesta atividade, o aluno deve desenvolver um programa que:

- Solicite ao usuário as medidas de três lados de uma figura.
- Verifique se essas medidas **formam um triângulo válido**.
- Classifique o tipo de triângulo em:
  - **Equilátero**
  - **Isósceles**
  - **Escaleno**
- Caso as medidas **não possam formar um triângulo**, exiba uma mensagem apropriada.

---

## ✅ Requisitos para fazer esta atividade

Para resolver este exercício, o aluno precisa:

- Saber como usar `input()` e `float()`.
- Conhecer a estrutura condicional `if`, `elif`, `else`.
- Compreender a **regra de existência de triângulos**:
  > A soma de dois lados deve ser sempre **maior ou igual ao terceiro**.

---

## 🧠 Enunciado

Crie um programa que:

1. Peça ao usuário os valores dos três lados (A, B e C).
2. Verifique se os três lados **podem formar um triângulo válido**.
3. Se não puder formar, exiba: `"Não é um triângulo"`.
4. Se for um triângulo:
   - Se os três lados forem **iguais**, é um **triângulo equilátero**.
   - Se **dois lados forem iguais**, é um **triângulo isósceles**.
   - Se **todos os lados forem diferentes**, é um **triângulo escaleno**.

---

## ℹ️ Como saber o tipo de triângulo?

- **Equilátero**: todos os lados são **iguais** (A = B = C).
- **Isósceles**: dois lados são **iguais** (A = B, B = C ou C = A).
- **Escaleno**: **todos os lados são diferentes**.
- Para **formar um triângulo**, as medidas precisam respeitar a **regra**:
  - A < B + C
  - B < A + C
  - C < A + B

---

## 🧪 Código base com explicações

```python
# Solicita ao usuário as medidas dos lados A, B e C
a = float(input("Digite a medida do lado A: "))
b = float(input("Digite a medida do lado B: "))
c = float(input("Digite a medida do lado C: "))

# Verifica se os lados podem formar um triângulo
if a <= b + c and b <= a + c and c <= a + b:
    
    # Todos os lados iguais → equilátero
    if a == b == c:
        print("\nTriângulo equilátero")

    # Dois lados iguais → isósceles
    elif a == b or b == c or c == a:
        print("\nTriângulo isósceles")

    # Todos diferentes → escaleno
    else:
        print("\nTriângulo escaleno")

else:
    # Se não respeitar a condição, não é um triângulo
    print("\nNão é um triângulo")
```

---

## ✅ Gabarito

```python
a = float(input("Digite a medida do lado A: "))
b = float(input("Digite a medida do lado B: "))
c = float(input("Digite a medida do lado C: "))

if a <= b + c and b <= a + c and c <= a + b:
    if a == b == c:
        print("\nTriângulo equilátero")
    elif a == b or b == c or c == a:
        print("\nTriângulo isósceles")
    else:
        print("\nTriângulo escaleno")
else:
    print("\nNão é um triângulo")
```
