vendas = [
    {"data": "01/02", "preco": 300},
    {"data": "02/02", "preco": 310},
    {"data": "03/02", "preco": 299},
    {"data": "04/02", "preco": 540},
    {"data": "05/02", "preco": 120},
]

quantidade_vendas = len(vendas)

valor_total_vendas = 0
for item in vendas:
    valor_total_vendas += item["preco"]

print(valor_total_vendas / quantidade_vendas)