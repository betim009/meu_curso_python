class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def apresentar(self):
        return f"Meu nome é {self.nome}, tenho {self.idade} anos e estudo {self.curso}."


aluno = Aluno("Ana", 20, "Python")
print(aluno.apresentar())
