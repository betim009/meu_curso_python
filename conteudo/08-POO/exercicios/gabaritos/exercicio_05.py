class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self._preco = preco
        self._estoque = estoque

    def adicionar_estoque(self, quantidade):
        if quantidade <= 0:
            print("Quantidade precisa ser positiva.")
            return

        self._estoque += quantidade

    def remover_estoque(self, quantidade):
        if quantidade <= 0:
            print("Quantidade precisa ser positiva.")
            return

        if quantidade > self._estoque:
            print("Estoque insuficiente.")
            return

        self._estoque -= quantidade

    def calcular_total_estoque(self):
        return self._preco * self._estoque

    def __str__(self):
        return f"{self.nome} - {self._estoque} unidades"


# As regras impedem que o estoque fique negativo.
produto = Produto("Monitor", 900.00, 5)
produto.remover_estoque(2)
produto.remover_estoque(10)
produto.adicionar_estoque(4)

print(produto)
print(f"Total em estoque: R$ {produto.calcular_total_estoque():.2f}")
