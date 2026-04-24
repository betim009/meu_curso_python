class Aluno:
    def __init__(self, nome, nota_1, nota_2):
        self.nome = nome
        self.nota_1 = nota_1
        self.nota_2 = nota_2

    def calcular_media(self):
        return (self.nota_1 + self.nota_2) / 2

    def verificar_situacao(self):
        media = self.calcular_media()

        if media >= 7:
            return "Aprovado"

        return "Reprovado"


aluno = Aluno("Maria", 8.0, 6.5)

print(f"Aluno: {aluno.nome}")
print(f"Media: {aluno.calcular_media():.1f}")
print(f"Situacao: {aluno.verificar_situacao()}")
