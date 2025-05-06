from jogadores import jogadores

def todos_gols():
    for jogador in jogadores:
        print(jogador["nome"], len(jogador["gols"]))

def melhor_media_gols():
    # criar uma nova lista
    # dentro dessa nova lista a gente vai adicionar um dicionario
    # esse novo dicionario vai ter data e quantidade
    # se a data nao existe, adicona a data e quantidade = 1
    # se a data existe, quantidade +=1
    
    nova_lista = []
    for jogador in jogadores:
        gols = jogador['gols']
        for gol in gols:
            print(gol)
            if gol['data'] not in nova_lista:
                nova_lista.append(gol['data'])
    print(nova_lista)
    

melhor_media_gols()



def melhor_media_assist():
    pass