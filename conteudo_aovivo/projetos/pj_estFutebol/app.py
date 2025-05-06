from scripts import todos_gols, melhor_media_gols

# interface
while True:
    print(
        """Opções:
    [1] - Todos gols dos jogadores    
    [2] - outra opção 
    ---
    [6] - Encerrar sistema 
    """
    )
    entrada = input("Digite uma opção: ")

    if entrada == "1":
        print("\n")  # quebra de linha no terminal
        todos_gols()
        print("\n")  # quebra de linha no terminal

    if entrada == "2":
        pass

    if entrada == "6":
        break
