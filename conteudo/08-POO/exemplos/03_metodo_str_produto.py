class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self._preco = preco
        self.estoque = estoque

    def alterar_preco(self, novo_preco):
        if novo_preco <= 0:
            print("Preço precisa ser maior que zero.")
            return

        self._preco = novo_preco

    def calcular_total_estoque(self):
        return self._preco * self.estoque

    def __str__(self):
        return f"{self.nome} - R$ {self._preco:.2f} - {self.estoque} unidades"


produto = Produto("Monitor", 900.00, 4)

print(produto)
print(f"Total em estoque: R$ {produto.calcular_total_estoque():.2f}")

produto.alterar_preco(850.00)

print(produto)
