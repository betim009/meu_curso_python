class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []
        self.status = "aberto"

    def adicionar_produto(self, produto):
        if self.status != "aberto":
            print("Não é possível adicionar produto em pedido fechado.")
            return

        self.produtos.append(produto)

    def calcular_total(self):
        total = 0

        for produto in self.produtos:
            total += produto.preco

        return total

    def fechar_pedido(self):
        self.status = "fechado"

    def exibir_resumo(self):
        print(f"Cliente: {self.cliente.nome} ({self.cliente.email})")
        print(f"Status: {self.status}")

        for produto in self.produtos:
            print(f"- {produto.nome}: R$ {produto.preco:.2f}")

        print(f"Total: R$ {self.calcular_total():.2f}")


# A regra de não alterar pedido fechado fica dentro da classe Pedido.
cliente = Cliente("Ana Souza", "ana@email.com")
pedido = Pedido(cliente)

pedido.adicionar_produto(Produto("Mouse", 80.00))
pedido.adicionar_produto(Produto("Teclado", 150.00))
pedido.fechar_pedido()
pedido.adicionar_produto(Produto("Monitor", 900.00))

pedido.exibir_resumo()
