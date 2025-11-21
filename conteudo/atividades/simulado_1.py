vetor_tipo = []
vetor_quantidade = []
vetor_preco = []
vetor_codigo = []


def exibir_cliente(posicao, tipos, quantidades, precos, codigos):
    print(f"Posicao: {posicao}")
    print(f"Tipo de plano: {tipos[posicao]}")
    print(f"Dias de treino por semana: {quantidades[posicao]}")
    print(f"Preco do plano: {precos[posicao]}")
    print(f"Codigo do cliente: {codigos[posicao]}")


tipos_validos = {"CARDIO", "MAQUINAS", "PREMIUM"}

while True:
    preco = int(input("Preco do plano? (-1 para sair) "))
    if preco == -1:
        break
    if preco < 0:
        print("Preco invalido. Tente novamente.")
        continue

    tipo = input("Tipo do plano? ").strip().upper()
    while tipo not in tipos_validos:
        print("Tipo invalido. Use CARDIO, MAQUINAS ou PREMIUM.")
        tipo = input("Tipo do plano? ").strip().upper()

    quantidade = int(input("Quantidade de dias de treino (1 a 7)? "))
    while quantidade < 1 or quantidade > 7:
        print("Quantidade invalida. Digite um valor entre 1 e 7.")
        quantidade = int(input("Quantidade de dias de treino (1 a 7)? "))

    codigo = int(input("Codigo do cliente (1 a 5)? "))
    while codigo < 1 or codigo > 5:
        print("Codigo invalido. Digite um valor entre 1 e 5.")
        codigo = int(input("Codigo do cliente (1 a 5)? "))

    vetor_tipo.append(tipo)
    vetor_quantidade.append(quantidade)
    vetor_preco.append(preco)
    vetor_codigo.append(codigo)
