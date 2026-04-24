from abc import ABC, abstractmethod


class Produto(ABC):
    def __init__(self, nome, preco, quantidade, tipo):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.tipo = tipo

    @abstractmethod
    def valor_total(self):
        pass

    def descricao(self):
        return f"Nome: {self.nome} - Quantidade: {self.quantidade} - Preço: {self.preco} - Tipo: {self.tipo}"


class Grao(Produto):
    def __init__(self, nome, preco, quantidade, tipo, tipo_grao):
        super().__init__(nome, preco, quantidade, tipo)
        self.tipo_grao = tipo_grao

    def valor_total(self):
        return f"Valor total {self.preco * self.quantidade}"

    def descricao(self):
        return super().descricao() + f" | Tipo de grão: {self.tipo_grao}"


class Bebida(Produto):
    def __init__(self, nome, preco, quantidade, tipo, tipo_bebida):
        super().__init__(nome, preco, quantidade, tipo)
        self.tipo_bebida = tipo_bebida

    def valor_total(self):
        return f"Valor total {self.preco * self.quantidade}"

    def descricao(self):
        return super().descricao() + f" | Tipo de bebida: {self.tipo_bebida}"


class Estoque:
    def __init__(self):
        self.produtos = []
        self.graos = []
        self.bebidas = []

    def cadastrar(self, produto):
        self.produtos.append(produto)

    def cadastrar_grao(self, produto):
        self.produtos.append(produto)
        self.graos.append(produto)

    def cadastrar_bebida(self, produto):
        self.produtos.append(produto)
        self.bebidas.append(produto)

    def listar_produtos(self):
        print("Todos os produtos:")
        for p in self.produtos:
            print(p.descricao())

    def listar_graos(self):
        for g in self.graos:
            print(g.descricao())

    def listar_bebidas(self):
        for b in self.bebidas:
            print(b.descricao())


estoque = Estoque()

arroz = Grao("Arroz", 25.0, 5, tipo="grão", tipo_grao="salgado")
acucar = Grao("Acucar", 12.0, 4, tipo="grão", tipo_grao="doce")

leite = Bebida("Leite", 10.0, 2, tipo="bebida", tipo_bebida="não alcoólico")
suco = Bebida("Suco", 8.0, 3, tipo="bebida", tipo_bebida="não alcoólico")

print(leite, arroz)

# print(leite.valor_total())

estoque.cadastrar_grao(arroz)
estoque.cadastrar_grao(acucar)

estoque.cadastrar_bebida(leite)
estoque.cadastrar_bebida(suco)

estoque.listar_produtos()
estoque.listar_graos()
estoque.listar_bebidas()
