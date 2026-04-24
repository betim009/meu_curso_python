class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        return self.preco * self.quantidade

    def mostrar_dados(self):
        return (
            f"{self.nome} - R$ {self.preco:.2f} - "
            f"{self.quantidade} unidades - Total: R$ {self.valor_total():.2f}"
        )


class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.mostrar_dados())

    def calcular_valor_total(self):
        total = 0

        for produto in self.produtos:
            total += produto.valor_total()

        return total


estoque = Estoque()

produto_1 = Produto("Arroz", 25.90, 10)
produto_2 = Produto("Feijao", 8.50, 20)
produto_3 = Produto("Macarrao", 4.75, 15)

estoque.adicionar_produto(produto_1)
estoque.adicionar_produto(produto_2)
estoque.adicionar_produto(produto_3)

estoque.listar_produtos()
print(f"Valor total do estoque: R$ {estoque.calcular_valor_total():.2f}")
