def calcular_bonus(salario_base, percentual_bonus):
    return salario_base * (percentual_bonus / 100)


def calcular_desconto(salario_base, percentual_desconto):
    return salario_base * (percentual_desconto / 100)


def calcular_salario_final(salario_base, bonus, desconto):
    return salario_base + bonus - desconto


def gerar_resumo_pagamento(nome_funcionario, salario_base, percentual_bonus, percentual_desconto):
    bonus = calcular_bonus(salario_base, percentual_bonus)
    desconto = calcular_desconto(salario_base, percentual_desconto)
    salario_final = calcular_salario_final(salario_base, bonus, desconto)

    return {
        "nome": nome_funcionario,
        "salario_base": salario_base,
        "bonus": bonus,
        "desconto": desconto,
        "salario_final": salario_final,
    }


resumo = gerar_resumo_pagamento("Juliana Martins", 5800.00, 10, 8)

print("Resumo da folha de pagamento")
print(f"Funcionário: {resumo['nome']}")
print(f"Salário base: R$ {resumo['salario_base']:.2f}")
print(f"Bônus: R$ {resumo['bonus']:.2f}")
print(f"Desconto: R$ {resumo['desconto']:.2f}")
print(f"Salário final: R$ {resumo['salario_final']:.2f}")
