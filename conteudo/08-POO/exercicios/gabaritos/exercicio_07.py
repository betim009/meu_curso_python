class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"{self.nome} ({self.email})"


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
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
            print(f"- {produto}")

        print(f"Total: R$ {self.calcular_total():.2f}")


# Pedido tem um cliente e vários produtos.
cliente = Cliente("Ana Souza", "ana@email.com")
pedido = Pedido(cliente)

pedido.adicionar_produto(Produto("Mouse", 80.00))
pedido.adicionar_produto(Produto("Teclado", 150.00))

pedido.exibir_resumo()
