idade_texto = "32"
salario_texto = "4500.75"

idade = int(idade_texto)
salario = float(salario_texto)

print(type(idade))
print(type(salario))
print(f"Idade no próximo ano: {idade + 1}")
print(f"Salário informado: R$ {salario:.2f}")
