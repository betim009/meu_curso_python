class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def aplicar_aumento(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento

    def salario_anual(self):
        return self.salario * 12

    def exibir_dados(self):
        return f"{self.nome} | {self.cargo} | R$ {self.salario:.2f}"


funcionario = Funcionario("Carla Mendes", "Analista", 4200.00)

print(funcionario.exibir_dados())
print(f"Salário anual: R$ {funcionario.salario_anual():.2f}")

funcionario.aplicar_aumento(8)

print(funcionario.exibir_dados())
