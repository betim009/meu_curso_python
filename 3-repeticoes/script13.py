condicao = True  # Define a condição inicial como True

while condicao:  # Enquanto a condição for True, o loop continuará
    print("Vou continuar até a condição ficar falsa.")  # Exibe mensagem

    entrada = input("Digite X para encerrar:  ")  # Solicita input do usuário

    if entrada == "X":  # Se o usuário digitar "X"
        condicao = False  # Altera a condição para False, encerrando o loop
