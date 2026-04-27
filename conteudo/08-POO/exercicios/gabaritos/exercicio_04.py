class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def calcular_pagamento(self):
        return self.salario

    def __str__(self):
        return f"{self.nome} - {self.cargo} - R$ {self.calcular_pagamento():.2f}"


# calcular_pagamento permite evoluir a regra depois sem mudar o print.
funcionario = Funcionario("Carla Mendes", "Analista", 4200.00)
print(funcionario)
