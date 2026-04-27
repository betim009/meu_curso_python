class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibir_dados(self):
        return f"{self.nome} - {self.cargo} - R$ {self.salario:.2f}"

    def calcular_salario_anual(self):
        return self.salario * 12


# A classe representa uma entidade comum em sistemas de RH.
funcionario = Funcionario("Carla Mendes", "Analista", 4200.00)

print(funcionario.exibir_dados())
print(f"Salário anual: R$ {funcionario.calcular_salario_anual():.2f}")
