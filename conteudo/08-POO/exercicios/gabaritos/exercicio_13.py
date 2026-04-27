class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def calcular_pagamento(self):
        return 0


class FuncionarioCLT(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario

    def calcular_pagamento(self):
        return self.salario


class FuncionarioPJ(Funcionario):
    def __init__(self, nome, valor_hora, horas_trabalhadas):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_pagamento(self):
        return self.valor_hora * self.horas_trabalhadas


class Estagiario(Funcionario):
    def __init__(self, nome, bolsa, auxilio_transporte):
        super().__init__(nome)
        self.bolsa = bolsa
        self.auxilio_transporte = auxilio_transporte

    def calcular_pagamento(self):
        return self.bolsa + self.auxilio_transporte


# A lista trata todos como funcionários, mesmo com regras diferentes.
funcionarios = [
    FuncionarioCLT("Carla", 4200.00),
    FuncionarioPJ("Roberto", 80.00, 120),
    Estagiario("Lucas", 1400.00, 250.00),
]

for funcionario in funcionarios:
    print(f"{funcionario.nome}: R$ {funcionario.calcular_pagamento():.2f}")
