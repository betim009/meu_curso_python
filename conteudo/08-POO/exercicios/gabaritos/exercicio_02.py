class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    def alterar_preco(self, novo_preco):
        if novo_preco <= 0:
            print("Preço inválido.")
            return

        self._preco = novo_preco

    def consultar_preco(self):
        return self._preco

    def __str__(self):
        return f"{self.nome} - R$ {self._preco:.2f}"


# O preço é alterado por método para manter a validação em um lugar só.
produto = Produto("Teclado", 150.00)
print(produto)

produto.alterar_preco(-20)
produto.alterar_preco(180.00)

print(produto)
