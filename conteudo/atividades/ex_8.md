
# ➕ Soma Máxima de Números Ímpares Consecutivos

## 📚 Objetivo da Atividade

Criar um programa que:

- Solicita vários números do usuário e armazena em uma lista.
- Calcula a **maior soma possível** entre **números ímpares consecutivos**.
- Exibe o resultado.

---

## ✅ Requisitos para fazer esta atividade

Você deve saber:

- Como usar `while True` com `break`.
- Como usar listas, `for` e estruturas condicionais.
- Como acumular somas com uma variável auxiliar.

---

## 🧠 Enunciado

1. Crie uma lista que receba números digitados pelo usuário.
2. O programa encerra quando o número 0 for digitado.
3. Percorra a lista com um `for`:
   - Se o número for **ímpar**, some-o à variável `soma_atual`.
   - Se o número for **par**, compare `soma_atual` com `maior_soma`.
     - Se for maior, atualize `maior_soma`.
     - Depois, zere `soma_atual`.
4. Ao final, exiba a **maior soma obtida entre ímpares consecutivos**.

---

## 🧪 Código com explicações

```python
# Lista para armazenar os números
lista_num = []

# Leitura de números até digitar 0
while True:
    n = int(input("Insira números para a lista, ao terminar digite 0: "))
    if n == 0:
        print()
        break
    else:
        lista_num.append(n)

# Inicializa variáveis de soma
soma_atual = 0
maior_soma = 0

# Percorre a lista
for n in lista_num:
    # Se for ímpar, soma ao total atual
    if n % 2 != 0:
        soma_atual += n
    else:
        # Se achar um par, compara e zera a soma atual
        if soma_atual > maior_soma:
            maior_soma = soma_atual
        soma_atual = 0

# Após o loop, verifica se a última sequência foi a maior
if soma_atual > maior_soma:
    maior_soma = soma_atual

# Exibe o resultado
print(f"A maior soma entre os números ímpares consecutivos foi de: {maior_soma}")
```

---

## ✅ Gabarito

```python
lista_num = []

while True:
    n = int(input("Insira números para a lista, ao terminar digite 0: "))
    if n == 0:
        print()
        break
    else:
        lista_num.append(n)

soma_atual = 0
maior_soma = 0

for n in lista_num:
    if n % 2 != 0:
        soma_atual += n
    else:
        if soma_atual > maior_soma:
            maior_soma = soma_atual
        soma_atual = 0
    
if soma_atual > maior_soma:
    maior_soma = soma_atual

print(f"A maior soma entre os números ímpares consecutivos foi de: {maior_soma}")
```
