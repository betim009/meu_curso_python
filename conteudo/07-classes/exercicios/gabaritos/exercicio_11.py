class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        return self.preco * self.quantidade

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.quantidade += quantidade

    def remover_estoque(self, quantidade):
        if 0 < quantidade <= self.quantidade:
            self.quantidade -= quantidade


class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(
                f"{produto.nome} | {produto.quantidade} unidades | "
                f"R$ {produto.valor_total():.2f}"
            )

    def calcular_valor_total(self):
        total = 0

        for produto in self.produtos:
            total += produto.valor_total()

        return total

    def buscar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                return produto

        return None


# Estoque gerencia vários produtos, por isso possui uma lista.
estoque = Estoque()
estoque.adicionar_produto(Produto("Monitor", 900.00, 4))
estoque.adicionar_produto(Produto("Teclado", 150.00, 10))

estoque.listar_produtos()
print(f"Valor total: R$ {estoque.calcular_valor_total():.2f}")

produto = estoque.buscar_produto("teclado")

if produto is not None:
    produto.remover_estoque(2)
    print("Após venda:")
    estoque.listar_produtos()
