def calcular_salario_final(salario_base, bonus, desconto):
    return salario_base + bonus - desconto


salario = calcular_salario_final(3000.00, 500.00, 200.00)

print(f"Salário final: R$ {salario:.2f}")
