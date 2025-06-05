from scripts import todos_gols, criar_media_gols # resgatando funções do arquivo scripts.py

# cria a interface
while True: # mantem acontecendo a interface
    print(
        """Opções:
    [1] - Todos gols dos jogadores    
    [2] - Media de gols 
    ---
    [6] - Encerrar sistema 
    """
    )
    entrada = input("Digite uma opção: ")

    if entrada == "1":
        print("\n")  # quebra de linha no terminal
        print("Todos os gols da base de dados:")
        todos_gols()
        print("\n")  # quebra de linha no terminal

    if entrada == "2":
        media_gols = criar_media_gols()
        melhor_media = max(media_gols, key=lambda jogador: jogador["media"])
        print(melhor_media)



    if entrada == "6":
        break # encerra a interface
