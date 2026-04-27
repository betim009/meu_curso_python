class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"{self.nome} ({self.email})"


# __str__ controla como o objeto aparece no print.
cliente = Cliente("Ana Souza", "ana@email.com")
print(cliente)
