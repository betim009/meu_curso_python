
# 📅 Verificando se uma Data é Válida e se o Ano é Bissexto

## 📚 Objetivo da Atividade

Nesta atividade, o aluno irá criar um programa que:

- Solicita ao usuário uma data (dia, mês e ano).
- Verifica se essa data é **válida**.
- Informa se o ano é **bissexto**.

---

## ✅ Requisitos para fazer esta atividade

Você precisa saber:

- Como usar `input()` e `int()`.
- Como usar **condições compostas** (`and`, `or`).
- O que é um **ano bissexto**.

---

## 🧠 Enunciado

1. Solicite ao usuário o **dia**, **mês** e **ano**.
2. Verifique se os valores são possíveis (dia entre 1 e 31, mês entre 1 e 12, ano maior que 0).
3. Verifique se o ano é **bissexto**:
   - O ano é bissexto se for divisível por 4 **e** não for divisível por 100, **ou** se for divisível por 400.
4. Considere os meses com 30 dias (abril, junho, setembro, novembro).
5. Fevereiro pode ter 29 dias **apenas se for ano bissexto**.
6. Exiba se a data é válida ou inválida e diga se o ano é bissexto.

---

## 🧪 Código com explicações

```python
# Lê o dia, mês e ano
d = int(input("Digite o dia: "))
m = int(input("Digite o mês: "))
a = int(input("Digite o ano: "))

# Verifica se os valores estão dentro de uma faixa válida
if (d < 1 or d > 31) or (m < 1 or m > 12) or (a < 1):
    print("\nData inválida")
else:
    # Verifica se o ano é bissexto
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        b = "ano bissexto"
    else:
        b = "ano não é bissexto"

    # Trata o caso de fevereiro em ano bissexto
    if b == "ano bissexto" and m == 2 and d <= 29:
        print(f"\n{d}/0{m}/{a} - Data válida, {b}")
    else:
        # Verifica se fevereiro tem mais de 28 dias em ano normal
        if m == 2 and d > 28:
            print("\nData inválida")
        else:
            # Meses com 30 dias não podem ter 31
            if (m == 4 or m == 6 or m == 9 or m == 11) and d >= 31:
                print("\nData inválida")
            else:
                # Formata o dia e o mês para manter o padrão de data
                if d < 10:
                    d = "0" + str(d)
                if m <= 9:
                    print(f"\n{d}/0{m}/{a} - Data válida, {b}")
                else:
                    print(f"\n{d}/{m}/{a} - Data válida, {b}")
```

---

## ✅ Gabarito

```python
d = int(input("Digite o dia: "))
m = int(input("Digite o mês: "))
a = int(input("Digite o ano: "))

if (d < 1 or d > 31) or (m < 1 or m > 12) or (a < 1):
    print("\nData inválida")
else:
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        b = "ano bissexto"
    else:
        b = "ano não é bissexto"

    if b == "ano bissexto" and m == 2 and d <= 29:
        print(f"\n{d}/0{m}/{a} - Data válida, {b}")
    else:
        if m == 2 and d > 28:
            print("\nData inválida")
        else:
            if (m == 4 or m == 6 or m == 9 or m == 11) and d >= 31:
                print("\nData inválida")
            else:
                if d < 10:
                    d = "0" + str(d)
                if m <= 9:
                    print(f"\n{d}/0{m}/{a} - Data válida, {b}")
                else:
                    print(f"\n{d}/{m}/{a} - Data válida, {b}")
```
