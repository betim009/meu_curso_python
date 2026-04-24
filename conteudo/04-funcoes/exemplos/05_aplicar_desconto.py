def aplicar_desconto(valor, percentual_desconto):
    desconto = valor * (percentual_desconto / 100)
    return valor - desconto


total_com_desconto = aplicar_desconto(1000.00, 15)

print(f"Total com desconto: R$ {total_com_desconto:.2f}")
