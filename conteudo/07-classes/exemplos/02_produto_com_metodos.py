class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total_estoque(self):
        return self.preco * self.quantidade

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto

    def exibir_resumo(self):
        total = self.calcular_total_estoque()
        return f"{self.nome} | {self.quantidade} unidades | Total: R$ {total:.2f}"


produto = Produto("Monitor", 900.00, 5)

print(produto.exibir_resumo())

produto.aplicar_desconto(10)

print(produto.exibir_resumo())
