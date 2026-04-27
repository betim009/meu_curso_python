class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def exibir_dados(self):
        return f"{self.nome} | {self.idade} anos | {self.email}"

    def email_valido(self):
        return "@" in self.email and "." in self.email


cliente_1 = Cliente("Ana Souza", 29, "ana@email.com")
cliente_2 = Cliente("Bruno Lima", 17, "bruno.email.com")

print(cliente_1.exibir_dados())
print("E-mail válido?", cliente_1.email_valido())

print(cliente_2.exibir_dados())
print("E-mail válido?", cliente_2.email_valido())
