class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_dados(self):
        return f"{self.nome} - R$ {self.preco:.2f}"


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
            print(produto.exibir_dados())

        print(f"Total do pedido: R$ {self.calcular_total():.2f}")


pedido = Pedido("Ana Souza")

pedido.adicionar_produto(Produto("Mouse", 80.00))
pedido.adicionar_produto(Produto("Teclado", 150.00))
pedido.adicionar_produto(Produto("Cabo HDMI", 35.00))

pedido.exibir_resumo()
