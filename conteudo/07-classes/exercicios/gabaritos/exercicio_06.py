class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco if preco >= 0 else 0
        self.quantidade = quantidade if quantidade >= 0 else 0

    def valor_total(self):
        return self.preco * self.quantidade

    def exibir_dados(self):
        return (
            f"{self.nome} | R$ {self.preco:.2f} | "
            f"{self.quantidade} unidades | Total: R$ {self.valor_total():.2f}"
        )


# A validação impede que o objeto nasça com dados inválidos.
produto = Produto("Notebook", -3500.00, 3)
print(produto.exibir_dados())
