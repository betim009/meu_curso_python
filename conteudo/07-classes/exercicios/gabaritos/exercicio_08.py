class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.ativo = True

    def desativar(self):
        self.ativo = False

    def ativar(self):
        self.ativo = True

    def exibir_status(self):
        status = "ativo" if self.ativo else "inativo"
        return f"{self.nome} está {status}"


# O status é um atributo porque faz parte do estado do cadastro.
cliente = Cliente("Pedro Martins", "pedro@email.com")

print(cliente.exibir_status())
cliente.desativar()
print(cliente.exibir_status())
cliente.ativar()
print(cliente.exibir_status())
