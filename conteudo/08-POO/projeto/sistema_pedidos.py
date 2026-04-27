class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self._email = email

    def email_valido(self):
        return "@" in self._email and "." in self._email

    def consultar_email(self):
        return self._email

    def alterar_email(self, novo_email):
        if "@" not in novo_email or "." not in novo_email:
            print("E-mail inválido. Alteração não realizada.")
            return

        self._email = novo_email

    def __str__(self):
        return f"{self.nome} ({self._email})"


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    def consultar_preco(self):
        return self._preco

    def alterar_preco(self, novo_preco):
        if novo_preco <= 0:
            print("Preço inválido. Alteração não realizada.")
            return

        self._preco = novo_preco

    def __str__(self):
        return f"{self.nome} - R$ {self._preco:.2f}"


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []
        self.status = "aberto"

    def adicionar_produto(self, produto):
        if self.status != "aberto":
            print("Não é possível adicionar produto em pedido fechado ou cancelado.")
            return

        self.produtos.append(produto)
        print(f"Produto adicionado: {produto.nome}")

    def calcular_total(self):
        total = 0

        for produto in self.produtos:
            total += produto.consultar_preco()

        return total

    def fechar_pedido(self):
        if len(self.produtos) == 0:
            print("Não é possível fechar um pedido vazio.")
            return

        self.status = "fechado"
        print("Pedido fechado.")

    def cancelar_pedido(self):
        if self.status == "fechado":
            print("Pedido fechado não pode ser cancelado neste exemplo.")
            return

        self.status = "cancelado"
        print("Pedido cancelado.")

    def exibir_resumo(self):
        print("Resumo do pedido")
        print(f"Cliente: {self.cliente}")
        print(f"Status: {self.status}")

        if len(self.produtos) == 0:
            print("Nenhum produto no pedido.")
        else:
            print("Produtos:")

            for produto in self.produtos:
                print(f"- {produto}")

        print(f"Total: R$ {self.calcular_total():.2f}")


class PagamentoCartao:
    def processar(self, valor):
        return f"Pagamento de R$ {valor:.2f} aprovado no cartão."


class PagamentoPix:
    def processar(self, valor):
        return f"Pagamento de R$ {valor:.2f} aprovado via Pix."


class PagamentoBoleto:
    def processar(self, valor):
        return f"Boleto de R$ {valor:.2f} gerado para pagamento."


def pagar_pedido(pedido, forma_pagamento):
    if pedido.status != "fechado":
        print("O pedido precisa estar fechado antes do pagamento.")
        return

    total = pedido.calcular_total()
    print(forma_pagamento.processar(total))


def executar_demonstracao():
    cliente = Cliente("Ana Souza", "ana@email.com")

    if not cliente.email_valido():
        print("Cliente com e-mail inválido.")
        return

    produto_1 = Produto("Mouse", 80.00)
    produto_2 = Produto("Teclado", 150.00)
    produto_3 = Produto("Monitor", 900.00)

    pedido = Pedido(cliente)
    pedido.adicionar_produto(produto_1)
    pedido.adicionar_produto(produto_2)
    pedido.adicionar_produto(produto_3)

    print()
    pedido.exibir_resumo()

    print()
    pedido.fechar_pedido()
    pedido.adicionar_produto(Produto("Cabo HDMI", 35.00))

    print()
    pedido.exibir_resumo()

    print()
    pagamento = PagamentoPix()
    pagar_pedido(pedido, pagamento)


if __name__ == "__main__":
    executar_demonstracao()
