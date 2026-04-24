class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_dados(self):
        return f"{self.nome} - R$ {self.preco:.2f} - {self.quantidade} unidades"


produto = Produto("Arroz", 25.90, 10)
print(produto.mostrar_dados())
