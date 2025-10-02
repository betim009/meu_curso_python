class Produto:
    def __init__(self, nome, preco, quantidade, tipo):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.tipo = tipo

    def descricao(self):
        return f"Nome: {self.nome}, Preço: R${self.preco:.2f}, Quantidade: {self.quantidade}, Tipo: {self.tipo}"


class Estoque:
    def __init__(self, produtos):
        self.produtos = produtos
        self.graos = []
        self.bebidas = []

    def listar_produtos(self):
        print("Produtos:")
        for produto in self.produtos:
            print(produto.descricao())

    def listar_graos(self):
        for produto in self.graos:
            print(produto.descricao())

    def listar_bebidas(self):
        for produto in self.bebidas:
            print(produto.descricao())

    def cadastrar_grao(self, produto):
        self.produtos.append(produto)
        if produto.tipo == "grão":
            self.graos.append(produto)

    def cadastrar_bebida(self, produto):
        self.produtos.append(produto)
        if produto.tipo == "bebida":
            self.bebidas.append(produto)


# Instancias
arroz = Produto("Arroz", 25.0, 5, "grão")
leite = Produto("Leite", 10.0, 2, "bebida")
cafe = Produto("Café", 15.0, 3, "grão")
suco = Produto("Suco", 8.0, 4, "bebida")

estoque = Estoque([])

estoque.cadastrar_grao(arroz)
estoque.cadastrar_bebida(leite)
estoque.cadastrar_grao(cafe)
estoque.cadastrar_bebida(suco)

estoque.listar_produtos()
estoque.listar_graos()
estoque.listar_bebidas()
