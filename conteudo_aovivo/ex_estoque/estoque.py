from produtos import produtos
from vendas import vendas

produtos_vendidos = []
estoque = []

for produto in produtos:
    for venda in vendas:
        if produto["id"] == venda["id_produto"]:
            produtos_vendidos.append(produto)

for produto in produtos:
    if produto not in produtos_vendidos:
        estoque.append(produto)


print(estoque)