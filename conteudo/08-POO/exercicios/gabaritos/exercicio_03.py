class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            print("Depósito precisa ser positivo.")
            return

        self._saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            print("Saque precisa ser positivo.")
            return

        if valor > self._saldo:
            print("Saldo insuficiente.")
            return

        self._saldo -= valor

    def consultar_saldo(self):
        return self._saldo


# O saldo só muda por métodos que aplicam regras.
conta = ContaBancaria("Rafael Alves", 1000.00)
conta.depositar(300.00)
conta.sacar(150.00)
conta.sacar(5000.00)

print(f"Saldo: R$ {conta.consultar_saldo():.2f}")
