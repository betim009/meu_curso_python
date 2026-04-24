def calcular_total_vendas(vendas):
    total = 0

    for venda in vendas:
        total += venda

    return total


vendas = [1200.00, 850.50, 399.90]
total = calcular_total_vendas(vendas)

print(f"Total vendido: R$ {total:.2f}")
