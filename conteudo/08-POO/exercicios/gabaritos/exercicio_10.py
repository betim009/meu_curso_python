class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R$ {self.preco:.2f}"


class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto_por_nome(self, nome):
        for produto in self.produtos:
            if produto.nome.lower() == nome.lower():
                self.produtos.remove(produto)
                return

        print("Produto não encontrado.")

    def calcular_total(self):
        total = 0

        for produto in self.produtos:
            total += produto.preco

        return total

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto)


# Carrinho é responsável por organizar produtos antes do pedido.
carrinho = Carrinho()
carrinho.adicionar_produto(Produto("Mouse", 80.00))
carrinho.adicionar_produto(Produto("Teclado", 150.00))
carrinho.adicionar_produto(Produto("Cabo HDMI", 35.00))

carrinho.remover_produto_por_nome("cabo hdmi")
carrinho.listar_produtos()
print(f"Total: R$ {carrinho.calcular_total():.2f}")
