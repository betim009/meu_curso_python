filmes = []
notas = []

# While eh um loop
# Ele vai sempre perguntar o filme que voce vai querer adicionar na lista filmes
while True:
    filme = input("Adicionar filme dentro da lista -filmes-\n")
    nota = input("Adicionar nota para o filme\n")

    if filme == "0":
        print("Loop encerrado!")
        break

    filmes.append(filme) # adicionando o filme dentro da lista
    notas.append(nota) # adicionar nota para a lista notas

# APOS o loop se encerrar!
# Vamos exibir o resultado
print(filmes)
print(notas)