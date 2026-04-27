class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.ativo = True

    def email_valido(self):
        return "@" in self.email and "." in self.email

    def idade_valida(self):
        return self.idade >= 18

    def desativar(self):
        self.ativo = False

    def ativar(self):
        self.ativo = True

    def exibir_dados(self):
        status = "ativo" if self.ativo else "inativo"
        return f"{self.nome} | {self.idade} anos | {self.email} | {status}"


class SistemaCadastro:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, cliente):
        if not cliente.email_valido():
            print(f"Erro: e-mail inválido para {cliente.nome}.")
            return

        if not cliente.idade_valida():
            print(f"Erro: {cliente.nome} precisa ser maior de idade.")
            return

        if self.buscar_por_email(cliente.email) is not None:
            print(f"Erro: já existe cliente com o e-mail {cliente.email}.")
            return

        self.clientes.append(cliente)
        print(f"Cliente cadastrado com sucesso: {cliente.nome}")

    def listar_clientes(self):
        if len(self.clientes) == 0:
            print("Nenhum cliente cadastrado.")
            return

        print("Clientes cadastrados:")

        for cliente in self.clientes:
            print(cliente.exibir_dados())

    def listar_clientes_ativos(self):
        print("Clientes ativos:")

        for cliente in self.clientes:
            if cliente.ativo:
                print(cliente.exibir_dados())

    def buscar_por_email(self, email):
        for cliente in self.clientes:
            if cliente.email == email:
                return cliente

        return None

    def desativar_cliente(self, email):
        cliente = self.buscar_por_email(email)

        if cliente is None:
            print("Cliente não encontrado.")
            return

        cliente.desativar()
        print(f"Cliente desativado: {cliente.nome}")


def executar_demonstracao():
    sistema = SistemaCadastro()

    cliente_1 = Cliente("Ana Souza", 29, "ana@email.com")
    cliente_2 = Cliente("Bruno Lima", 35, "bruno.email.com")
    cliente_3 = Cliente("Carla Mendes", 17, "carla@email.com")
    cliente_4 = Cliente("Daniel Rocha", 42, "daniel@email.com")

    sistema.cadastrar_cliente(cliente_1)
    sistema.cadastrar_cliente(cliente_2)
    sistema.cadastrar_cliente(cliente_3)
    sistema.cadastrar_cliente(cliente_4)

    print()
    sistema.listar_clientes()

    print()
    cliente = sistema.buscar_por_email("daniel@email.com")

    if cliente is not None:
        print("Cliente encontrado:")
        print(cliente.exibir_dados())

    print()
    sistema.desativar_cliente("ana@email.com")

    print()
    sistema.listar_clientes()

    print()
    sistema.listar_clientes_ativos()


if __name__ == "__main__":
    executar_demonstracao()
