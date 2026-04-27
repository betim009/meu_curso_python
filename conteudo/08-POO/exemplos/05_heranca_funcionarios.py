class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_pagamento(self):
        return self.salario

    def __str__(self):
        return f"{self.nome} - pagamento: R$ {self.calcular_pagamento():.2f}"


class Vendedor(Funcionario):
    def __init__(self, nome, salario, comissao):
        super().__init__(nome, salario)
        self.comissao = comissao

    def calcular_pagamento(self):
        return self.salario + self.comissao


class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def calcular_pagamento(self):
        return self.salario + self.bonus


funcionarios = [
    Funcionario("Carlos", 3000.00),
    Vendedor("Marina", 2500.00, 900.00),
    Gerente("Patrícia", 6000.00, 1500.00),
]

for funcionario in funcionarios:
    print(funcionario)
