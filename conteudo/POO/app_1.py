class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def descricao(self):
        return f"{self.nome}: R$ {self.preco:.2f} ({self.quantidade} unidades)"

    def preco_por_kg(self):
        return f"Preço por kg: R$ {self.preco / self.quantidade:.2f}"

    def preco_por_litro(self):
        return f"Preço por litro: R$ {self.preco / self.quantidade:.2f}"


# Exemplos de uso
p1 = Produto("Arroz", 25.0, 5)
p2 = Produto("Leite", 5.0, 10)
p3 = Produto("Café", 12.5, 20)

print(p1.descricao())
print(p2.descricao())
print(p3.descricao())

print(p1.preco_por_kg())
print(p2.preco_por_litro())
