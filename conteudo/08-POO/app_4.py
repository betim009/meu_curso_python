from abc import ABC, abstractmethod


class Produto(ABC):
    def __init__(self, nome, preco, quantidade, tipo):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.tipo = tipo

    @abstractmethod
    def descricao(self):
        pass


class Grao(Produto):
    def __init__(self, nome, preco, quantidade, tipo, tipo_grao):
        super().__init__(nome, preco, quantidade, tipo)
        self.tipo_grao = tipo_grao

    def descricao(self):
        return f"Grão - {self.nome} ({self.tipo_grao}): R$ {self.preco:.2f} ({self.quantidade} unidades)"


class Bebida(Produto):
    def __init__(self, nome, preco, quantidade, tipo, tipo_bebida):
        super().__init__(nome, preco, quantidade, tipo)
        self.tipo_bebida = tipo_bebida

    def descricao(self):
        return f"Bebida - {self.nome} ({self.tipo_bebida}): R$ {self.preco:.2f} ({self.quantidade} unidades)"


class Estoque:
    def __init__(self):
        self.produtos = []


class EstoqueGraos(Estoque):
    def __init__(self):
        super().__init__()

    def cadastrar(self, produto):
        if isinstance(produto, Grao):
            self.produtos.append(produto)

    def listar(self):
        for g in self.produtos:
            print(g.descricao())


class EstoqueBebidas(Estoque):
    def __init__(self):
        super().__init__()

    def cadastrar(self, produto):
        if isinstance(produto, Bebida):
            self.produtos.append(produto)

    def listar(self):
        for b in self.produtos:
            print(b.descricao())


estoque_graos = EstoqueGraos()
estoque_bebidas = EstoqueBebidas()

arroz = Grao("Arroz", 25.0, 5, tipo="grão", tipo_grao="salgado")
acucar = Grao("Acucar", 12.0, 4, tipo="grão", tipo_grao="doce")

leite = Bebida("Leite", 10.0, 2, tipo="bebida", tipo_bebida="não alcoólico")
suco = Bebida("Suco", 8.0, 3, tipo="bebida", tipo_bebida="não alcoólico")

estoque_graos.cadastrar(arroz)
estoque_graos.cadastrar(acucar)
estoque_bebidas.cadastrar(leite)
estoque_bebidas.cadastrar(suco)

print("Produtos no estoque de grãos:")
estoque_graos.listar()
print("\nProdutos no estoque de bebidas:")
estoque_bebidas.listar()
