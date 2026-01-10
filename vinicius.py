class Pessoa:
    def __init__(self, name):
        self.name = name

    def dizer_ola(self):
        print("Ola", self.name)


pessoa_1 = Pessoa("Alberto")
pessoa_2 = Pessoa("Vinicius")

pessoa_1.dizer_ola()
pessoa_2.dizer_ola()