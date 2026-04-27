class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade


# O cálculo fica dentro da classe porque depende dos dados do produto.
produto = Produto("Teclado", 150.00, 5)

print(f"Produto: {produto.nome}")
print(f"Total em estoque: R$ {produto.calcular_total():.2f}")
