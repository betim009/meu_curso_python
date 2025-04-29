
# 📥 Inserindo Números Únicos em uma Lista

## 📚 Objetivo da Atividade

Criar um programa que:

- Receba vários números do usuário.
- Adicione **apenas os diferentes** (sem repetições) em uma lista.
- Pare quando o usuário digitar o número 0.
- Mostre quantos **números diferentes** foram digitados.

---

## ✅ Requisitos para fazer esta atividade

Você precisa saber:

- Como usar `while True` com `break`.
- Como usar listas e o método `append()`.
- Como verificar se um número **já está na lista** com `not in`.
- Como usar `len()` para contar os itens de uma lista.

---

## 🧠 Enunciado

1. Crie uma lista vazia.
2. Peça ao usuário que digite vários números.
3. O programa deve continuar até que o usuário digite 0.
4. Somente **adicione na lista os números que ainda não estão nela**.
5. Ao final, mostre quantos números **diferentes** foram digitados.

---

## 🧪 Código com explicações

```python
# Lista para armazenar números únicos
lista_num = []

# Loop infinito até o usuário digitar 0
while True:
    n = int(input("Insira números para a lista, ao terminar digite 0: "))
    
    if n == 0:
        break  # Sai do loop
    
    # Só adiciona se o número ainda não estiver na lista
    elif n not in lista_num:
        lista_num.append(n)

# Exibe a quantidade de números diferentes digitados
print(f"\n{len(lista_num)} números diferentes foram digitados")
```

---

## ✅ Gabarito

```python
lista_num = []

while True:
    n = int(input("Insira números para a lista, ao terminar digite 0: "))
    if n == 0:
        break
    elif n not in lista_num:
        lista_num.append(n)

print(f"\n{len(lista_num)} números diferentes foram digitados")
```
