
# 📚 Enunciado

Você foi convidado a ajudar na organização de uma viagem de lazer. Para que a viagem realmente aconteça, é necessário verificar alguns requisitos:

- O custo da viagem deve ser de **R$0,00 até R$30,00**.
- Além disso, a viagem **só ocorrerá** se atender a pelo menos uma das seguintes condições:
  - Ter **Wi-Fi** e **piscina**;
  - Se não tiver Wi-Fi e piscina, **obrigatoriamente deve ter churrasqueira**;
  - Se tiver Wi-Fi **ou** piscina e também tiver churrasqueira, a viagem também ocorrerá.

Se o valor estiver fora do intervalo ou se nenhuma dessas condições for satisfeita, a viagem **não ocorrerá**.

Construa um programa que:
- Solicite ao usuário:
  - O valor da viagem;
  - Se terá Wi-Fi (respostas possíveis: `"Sim"`, `"Não"`, `"Terá"`, `"Não terá"`);
  - Se terá piscina;
  - Se terá churrasqueira.
- Analise as condições e exiba o resultado:
  - `"A viagem ocorrerá"` ou
  - `"A viagem NÃO ocorrerá"`.

---

# 🧩 Código

```python
v = float(input("Quanto custará a viagem? R$"))
w = input("Terá wifi? ")
p = input("Terá piscina? ")
c = input("Terá churrasqueira? ")

if v < 0 or v > 30:
    print("\nA viagem NÃO ocorrerá")
else:
    if (w == "Não" or w == "Não terá") and (p == "Não" or p == "Não terá") and (c == "Não" or c == "Não terá"):
        print("\nA viagem NÃO ocorrerá")
    else:
        if (w == "Sim" or w == "Terá") and (p == "Sim" or p == "Terá"):
            print("\nA viagem ocorrerá")
        else:
            if (w == "Não" or w == "Não terá") or (p == "Não" or p == "Não terá") and (c == "Sim" or c == "Terá"):
                print("\nA viagem ocorrerá")
            else:
                if (w == "Sim" or w == "Terá") or (p == "Sim" or p == "Terá") and (c == "Sim" or c == "Terá"):
                    print("\nA viagem ocorrerá")
```

---

# 📌 Observação
- **Dica**: Tome cuidado com a prioridade dos operadores `and` e `or`.
- **Melhoria possível**: Normalizar as respostas para minúsculas (`lower()`) e retirar espaços, para tornar o programa mais robusto.
- **Exemplo de entrada válida**:

```
Quanto custará a viagem? R$25
Terá wifi? Sim
Terá piscina? Não
Terá churrasqueira? Sim
```

Resultado: **"A viagem ocorrerá"**
