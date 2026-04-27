class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self._email = email
        self.ativo = True

    def consultar_email(self):
        return self._email

    def alterar_email(self, novo_email):
        if "@" not in novo_email or "." not in novo_email:
            print("E-mail inválido. Alteração não realizada.")
            return

        self._email = novo_email
        print("E-mail alterado com sucesso.")

    def desativar(self):
        self.ativo = False

    def exibir_dados(self):
        status = "ativo" if self.ativo else "inativo"
        return f"{self.nome} - {self._email} - {status}"


cliente = Cliente("Bruno Lima", "bruno@email.com")

print(cliente.exibir_dados())

cliente.alterar_email("bruno.email.com")
cliente.alterar_email("bruno.lima@email.com")

print(cliente.exibir_dados())
