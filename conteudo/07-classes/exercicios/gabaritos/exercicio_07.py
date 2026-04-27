class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def aplicar_aumento(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento

    def exibir_dados(self):
        return f"{self.nome} | {self.cargo} | R$ {self.salario:.2f}"


# O aumento muda o salário guardado dentro do objeto.
funcionario = Funcionario("Marina Rocha", "Desenvolvedora", 5000.00)

print(funcionario.exibir_dados())
funcionario.aplicar_aumento(10)
print(funcionario.exibir_dados())
