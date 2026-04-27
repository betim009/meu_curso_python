class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def exibir_dados(self):
        return f"{self.nome} - {self.idade} anos - {self.email}"


# A classe Cliente agrupa os dados que pertencem ao mesmo cadastro.
cliente_1 = Cliente("Ana Souza", 29, "ana@email.com")
cliente_2 = Cliente("Bruno Lima", 35, "bruno@email.com")

print(cliente_1.exibir_dados())
print(cliente_2.exibir_dados())
