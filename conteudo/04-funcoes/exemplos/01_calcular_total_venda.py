def calcular_total_venda(preco_unitario, quantidade):
    return preco_unitario * quantidade


total = calcular_total_venda(250.00, 3)

print(f"Total: R$ {total:.2f}")
