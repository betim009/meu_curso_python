class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        total = 0

        for produto in self.produtos:
            total += produto.preco

        return total

    def exibir_resumo(self):
        print(f"Cliente: {self.cliente}")

        for produto in self.produtos:
            print(f"- {produto.nome}: R$ {produto.preco:.2f}")

        print(f"Total: R$ {self.calcular_total():.2f}")


# O pedido guarda uma lista de objetos Produto.
pedido = Pedido("Ana Souza")
pedido.adicionar_produto(Produto("Mouse", 80.00))
pedido.adicionar_produto(Produto("Teclado", 150.00))

pedido.exibir_resumo()
