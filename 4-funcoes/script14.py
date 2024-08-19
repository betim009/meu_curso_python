# Define a função chamada 'media' que recebe dois parâmetros: 'nota1' e 'nota2'
def media(nota1, nota2):
    # Calcula a média das duas notas fornecidas e retorna o resultado
    return (nota1 + nota2) / 2


# Chama a função 'media' com os valores 9.4 e 5, e imprime o resultado da média calculada
print(media(9.4, 5))

# Comentário sobre a prática ideal:
# Para tornar o código mais claro e a saída mais informativa, armazena o resultado em uma variável
media_alberto = media(
    9.4, 5
)  # Armazena o resultado da chamada da função 'media' na variável 'media_alberto'

# Imprime a média calculada com uma mensagem explicativa
print(f"A média de notas do Alberto é: {media_alberto}")
