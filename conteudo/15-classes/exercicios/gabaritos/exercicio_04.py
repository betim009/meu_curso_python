class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            return "Valor de deposito invalido."

        self.saldo += valor
        return "Deposito realizado com sucesso."

    def sacar(self, valor):
        if valor <= 0:
            return "Valor de saque invalido."

        if valor > self.saldo:
            return "Saldo insuficiente."

        self.saldo -= valor
        return "Saque realizado com sucesso."

    def mostrar_saldo(self):
        return f"Saldo atual: R$ {self.saldo:.2f}"


conta = ContaBancaria("Joao", 100)
conta.depositar(50)
conta.sacar(30)

print(conta.mostrar_saldo())
