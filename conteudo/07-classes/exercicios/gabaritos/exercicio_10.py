class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def exibir_dados(self):
        return f"{self.nome} | {self.idade} anos | {self.email}"


class CadastroClientes:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente.exibir_dados())

    def buscar_por_email(self, email):
        for cliente in self.clientes:
            if cliente.email == email:
                return cliente

        return None


# CadastroClientes coordena uma coleção de clientes.
cadastro = CadastroClientes()
cadastro.adicionar_cliente(Cliente("Ana Souza", 29, "ana@email.com"))
cadastro.adicionar_cliente(Cliente("Bruno Lima", 35, "bruno@email.com"))

cadastro.listar_clientes()

cliente = cadastro.buscar_por_email("ana@email.com")

if cliente is not None:
    print("Encontrado:", cliente.exibir_dados())
else:
    print("Cliente não encontrado")
