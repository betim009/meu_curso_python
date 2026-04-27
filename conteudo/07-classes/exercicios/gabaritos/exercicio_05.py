class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def exibir_saldo(self):
        return f"Titular: {self.titular}\nSaldo: R$ {self.saldo:.2f}"


# O método depositar altera o estado da conta.
conta = ContaBancaria("Rafael Alves", 1000.00)
conta.depositar(250.00)

print(conta.exibir_saldo())
