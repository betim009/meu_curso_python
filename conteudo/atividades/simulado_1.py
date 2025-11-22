vetor_tipo = ["CARDIO", "MAQUINAS"]
vetor_quantidade = [5, 7]
vetor_preco = [10, 20]
vetor_codigo = [1, 2]


def exibir_cliente(posicao, tipos, quantidades, precos, codigos):
    print(f"Posicao: {posicao}")
    print(f"Tipo de plano: {tipos[posicao]}")
    print(f"Dias de treino por semana: {quantidades[posicao]}")
    print(f"Preco do plano: {precos[posicao]}")
    print(f"Codigo do cliente: {codigos[posicao]}")


def loop_preco():
    preco = int(input("Preco do plano? (-1 para sair) "))
    if preco == -1:
        return False

    vetor_preco.append(preco)
    return preco


def loop_plano():
    tipos_validos = {"CARDIO", "MAQUINAS", "PREMIUM"}
    tipo = input("Tipo do plano? ")
    while tipo not in tipos_validos:
        print("Tipo invalido. Use CARDIO, MAQUINAS ou PREMIUM.")
        tipo = input("Tipo do plano? ")

    vetor_tipo.append(tipo)
    return tipo


def loop_quantidade():
    quantidade = int(input("Quantidade de dias de treino (1 a 7)? "))
    while quantidade < 1 or quantidade > 7:
        print("Quantidade invalida. Digite um valor entre 1 e 7.")
        quantidade = int(input("Quantidade de dias de treino (1 a 7)? "))

    vetor_quantidade.append(quantidade)
    return quantidade


def loop_codigo():
    codigo = int(input("Codigo do cliente (1 a 5)? "))
    while codigo < 1 or codigo > 5:
        print("Codigo invalido. Digite um valor entre 1 e 5.")
        codigo = int(input("Codigo do cliente (1 a 5)? "))

    vetor_codigo.append(codigo)
    return codigo


def exibir_cliente(index):
    print(vetor_preco[index])
    print(vetor_tipo[index])
    print(vetor_quantidade[index])
    print(vetor_codigo[index])
    print("######################################")

    return None


preco = loop_preco()
while preco:
    plano = loop_plano()
    quantidade = loop_quantidade()
    codigo = loop_codigo()
    preco = loop_preco()

print("RESULTADO DOS VETORES CONSTRUIDOS: ")
print(vetor_preco)
print(vetor_tipo)
print(vetor_quantidade)
print(vetor_codigo)
print("######################################")

while True:
    print(
        """
[1] - SAIR
[2] - Exibir dados de um Cliente
[3] - Buscar cliente por Codigo      
"""
    )

    entrada = int(input("Qual opcao? "))
    print("######################################")

    if entrada == 1:
        break

    if entrada == 2:
        parametro = int(
            input(f"Digite um numero inteiro entra 0 a {len(vetor_preco) - 1}: ")
        )
        print("######################################")

        while parametro < 0 or parametro >= len(vetor_preco):
            parametro = int(
                input(f"Digite um numero inteiro entra 0 a {len(vetor_preco) - 1}: ")
            )
            print("######################################")
        exibir = exibir_cliente(parametro)
        print("######################################")
