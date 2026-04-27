class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_preco_final(self):
        return self.preco

    def __str__(self):
        return f"{self.nome} - R$ {self.calcular_preco_final():.2f}"


class ProdutoFisico(Produto):
    def __init__(self, nome, preco, frete):
        super().__init__(nome, preco)
        self.frete = frete

    def calcular_preco_final(self):
        return self.preco + self.frete


class ProdutoDigital(Produto):
    def __init__(self, nome, preco, taxa_plataforma):
        super().__init__(nome, preco)
        self.taxa_plataforma = taxa_plataforma

    def calcular_preco_final(self):
        return self.preco + self.taxa_plataforma


# Produtos diferentes compartilham uma base, mas mudam o cálculo final.
produtos = [
    ProdutoFisico("Livro impresso", 60.00, 15.00),
    ProdutoDigital("Curso online", 200.00, 20.00),
]

for produto in produtos:
    print(produto)
