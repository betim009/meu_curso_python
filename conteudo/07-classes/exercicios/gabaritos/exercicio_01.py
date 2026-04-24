class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


produto = Produto("Caderno", 18.50, 3)

print(produto.nome)
print(produto.preco)
print(produto.quantidade)
