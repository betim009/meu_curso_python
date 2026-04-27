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
        self.status = "aberto"

    def adicionar_produto(self, produto):
        if self.status != "aberto":
            print("Não é possível adicionar produto em pedido fechado ou cancelado.")
            return

        self.produtos.append(produto)

    def calcular_total(self):
        total = 0

        for produto in self.produtos:
            total += produto.preco

        return total

    def fechar_pedido(self):
        if len(self.produtos) == 0:
            print("Não é possível fechar pedido vazio.")
            return

        self.status = "fechado"

    def cancelar_pedido(self):
        self.status = "cancelado"

    def exibir_resumo(self):
        print(f"Cliente: {self.cliente}")
        print(f"Status: {self.status}")

        for produto in self.produtos:
            print(f"- {produto}")

        print(f"Total: R$ {self.calcular_total():.2f}")


# O status controla o que pode acontecer com o pedido.
pedido = Pedido(Cliente("Ana Souza", "ana@email.com"))
pedido.adicionar_produto(Produto("Mouse", 80.00))
pedido.adicionar_produto(Produto("Teclado", 150.00))
pedido.fechar_pedido()
pedido.adicionar_produto(Produto("Monitor", 900.00))

pedido.exibir_resumo()
