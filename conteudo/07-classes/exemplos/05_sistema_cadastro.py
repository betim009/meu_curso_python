class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.ativo = True

    def email_valido(self):
        return "@" in self.email and "." in self.email

    def desativar(self):
        self.ativo = False

    def exibir_dados(self):
        status = "ativo" if self.ativo else "inativo"
        return f"{self.nome} | {self.idade} anos | {self.email} | {status}"


class CadastroClientes:
    def __init__(self):
        self.clientes = []

    def cadastrar(self, cliente):
        if not cliente.email_valido():
            print(f"Cliente não cadastrado: e-mail inválido para {cliente.nome}")
            return

        self.clientes.append(cliente)
        print(f"Cliente cadastrado: {cliente.nome}")

    def listar(self):
        print("Clientes cadastrados:")

        for cliente in self.clientes:
            print(cliente.exibir_dados())

    def buscar_por_email(self, email):
        for cliente in self.clientes:
            if cliente.email == email:
                return cliente

        return None


cadastro = CadastroClientes()

cadastro.cadastrar(Cliente("Ana Souza", 29, "ana@email.com"))
cadastro.cadastrar(Cliente("Bruno Lima", 35, "bruno.email.com"))
cadastro.cadastrar(Cliente("Carla Mendes", 41, "carla@email.com"))

cadastro.listar()

cliente_encontrado = cadastro.buscar_por_email("carla@email.com")

if cliente_encontrado is not None:
    print("Encontrado:", cliente_encontrado.exibir_dados())
