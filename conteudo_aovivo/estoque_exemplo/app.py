from produtos import produtos
from vendas import vendas

copia_produtos = produtos
for venda in vendas:
    for produto in copia_produtos:
        if venda["produto_id"] == produto["id"]:
            copia_produtos.remove(produto)
            break

print(copia_produtos)