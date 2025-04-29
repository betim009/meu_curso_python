
# 🔷 Identificando se a Figura é um Quadrado ou Retângulo

## 📚 Objetivo da Atividade

Nesta atividade, o aluno deverá criar um programa simples que:

- Solicita ao usuário duas medidas: **largura** e **comprimento** de uma figura.
- Verifica se essas medidas formam um **quadrado** ou um **retângulo**.
- Mostra uma mensagem apropriada com base nos valores informados.

---

## ✅ Requisitos para fazer esta atividade

Antes de resolver este exercício, é importante que você já conheça:

- Como usar `input()` para ler dados do usuário.
- Como converter uma entrada de texto em número (`float()`).
- Como usar **condições** com `if`, `elif` e `else`.
- Como usar **operadores lógicos** (`==`, `<=`, `or`).

---

## 🧠 Enunciado

Crie um programa que:

1. Peça ao usuário a **largura** e o **comprimento** de uma figura geométrica.
2. Verifique se as medidas informadas são **válidas** (devem ser maiores que zero).
3. Se forem inválidas, exiba: `"Medidas inválidas"`.
4. Se forem válidas:
   - Caso a largura e o comprimento sejam **iguais**, exiba: `"É um quadrado"`.
   - Caso sejam **diferentes**, exiba: `"É um retângulo"`.

---

## ℹ️ Como saber se é um quadrado ou um retângulo?

- **Quadrado**: possui todos os lados com **mesma medida**.  
  Exemplo: largura = 5 e comprimento = 5 → é um quadrado.

- **Retângulo**: possui **dois pares de lados iguais**, mas **largura diferente do comprimento**.  
  Exemplo: largura = 4 e comprimento = 6 → é um retângulo.

---

## 🧪 Código base com explicações

```python
# Pede a largura e converte para número decimal (float)
l = float(input("Informe a largura da figura: "))

# Pede o comprimento e converte para número decimal (float)
c = float(input("Informe o comprimento da figura: "))

# Verifica se algum valor é menor ou igual a zero
if l <= 0 or c <= 0:
    print("\nMedidas inválidas")  # Mostra mensagem de erro

else:
    # Se a largura e o comprimento forem iguais, é um quadrado
    if l == c:
        print("\nÉ um quadrado")
    else:
        # Se forem diferentes, é um retângulo
        print("\nÉ um retângulo")
```

---

## ✅ Gabarito

Este é o **código final correto**, com indentação e lógica adequada:

```python
l = float(input("Informe a largura da figura: "))
c = float(input("Informe o comprimento da figura: "))

if l <= 0 or c <= 0:
    print("\nMedidas inválidas")
else:
    if l == c:
        print("\nÉ um quadrado")
    else:
        print("\nÉ um retângulo")
```
