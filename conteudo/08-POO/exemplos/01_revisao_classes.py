class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_dados(self):
        return f"{self.nome} - {self.email}"


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_dados(self):
        return f"{self.nome} - R$ {self.preco:.2f}"


cliente = Cliente("Ana Souza", "ana@email.com")
produto = Produto("Teclado", 150.00)

print(cliente.exibir_dados())
print(produto.exibir_dados())
