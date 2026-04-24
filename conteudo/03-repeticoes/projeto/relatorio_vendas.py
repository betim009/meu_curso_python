vendas = [1200.00, 850.50, 399.90, 1500.00, 220.00, 990.00]

total = 0
quantidade = 0
maior_venda = 0
vendas_acima_meta = 0
meta = 1000

for venda in vendas:
    total += venda
    quantidade += 1

    if venda > maior_venda:
        maior_venda = venda

    if venda >= meta:
        vendas_acima_meta += 1

media = total / quantidade

print("Relatório de vendas")
print(f"Total vendido: R$ {total:.2f}")
print(f"Quantidade de vendas: {quantidade}")
print(f"Média por venda: R$ {media:.2f}")
print(f"Maior venda: R$ {maior_venda:.2f}")
print(f"Vendas acima da meta: {vendas_acima_meta}")
