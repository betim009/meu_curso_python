class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def exibir_resumo(self):
        return f"{self.titulo}, de {self.autor} ({self.ano})"


# Cada objeto Livro tem seus próprios dados.
livro_1 = Livro("Python Básico", "Ana Costa", 2024)
livro_2 = Livro("Automação com Python", "Bruno Lima", 2023)
livro_3 = Livro("Dados para Iniciantes", "Carla Mendes", 2025)

print(livro_1.exibir_resumo())
print(livro_2.exibir_resumo())
print(livro_3.exibir_resumo())
