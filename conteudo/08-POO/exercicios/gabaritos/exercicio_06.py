class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self._email = email
        self.ativo = True

    def consultar_email(self):
        return self._email

    def alterar_email(self, novo_email):
        if "@" not in novo_email or "." not in novo_email:
            print("E-mail inválido.")
            return

        self._email = novo_email

    def desativar(self):
        self.ativo = False

    def __str__(self):
        status = "ativo" if self.ativo else "inativo"
        return f"{self.nome} - {self._email} - {status}"


class CadastroClientes:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)

    def buscar_por_email(self, email):
        for cliente in self.clientes:
            if cliente.consultar_email() == email:
                return cliente

        return None


# CadastroClientes gerencia a coleção; Cliente gerencia seus próprios dados.
cadastro = CadastroClientes()
cadastro.adicionar_cliente(Cliente("Ana Souza", "ana@email.com"))
cadastro.adicionar_cliente(Cliente("Bruno Lima", "bruno@email.com"))

cadastro.listar_clientes()

cliente = cadastro.buscar_por_email("bruno@email.com")

if cliente is not None:
    cliente.desativar()

cadastro.listar_clientes()
