class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_pagamento(self):
        return self.salario


class Vendedor(Funcionario):
    def __init__(self, nome, salario, comissao):
        super().__init__(nome, salario)
        self.comissao = comissao

    def calcular_pagamento(self):
        return self.salario + self.comissao


# Vendedor é um tipo de Funcionario, por isso a herança faz sentido.
funcionario = Funcionario("Carlos", 3000.00)
vendedor = Vendedor("Marina", 2500.00, 900.00)

print(f"{funcionario.nome}: R$ {funcionario.calcular_pagamento():.2f}")
print(f"{vendedor.nome}: R$ {vendedor.calcular_pagamento():.2f}")
