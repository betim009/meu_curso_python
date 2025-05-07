from jogadores import jogadores  # resgatando os dados de jogadores.py


def todos_gols():
    for jogador in jogadores:  # laço de repetição
        print(jogador["nome"], len(jogador["gols"]))


def melhor_media_gols():
    # criar uma nova lista
    # dentro dessa nova lista a gente vai adicionar um dicionario
    # esse novo dicionario vai ter data e quantidade e nome do jogador
    # se a data nao existe, adicona a data e quantidade = 1
    # se a data existe, quantidade +=1

    nova_lista = []

    for jogador in jogadores:
        novo_dict = {"nome": jogador["nome"], "datas": {}}

        for gol in jogador["gols"]:
            data = gol["data"]
            if data in novo_dict["datas"]:
                novo_dict["datas"][data] += 1
                print(novo_dict)
            else:
                novo_dict["datas"][data] = 1

        nova_lista.append(novo_dict)

    # Exibindo os resultados
    for jogador in nova_lista:
        print(f"\n{jogador['nome']}")
        for data, qtd in jogador["datas"].items():
            print(f"Data: {data} | Gols: {qtd}")


melhor_media_gols()


def melhor_media_assist():
    pass
