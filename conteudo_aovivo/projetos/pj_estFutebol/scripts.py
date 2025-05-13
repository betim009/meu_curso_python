from jogadores import jogadores  # resgatando os dados de jogadores.py


def todos_gols():
    for jogador in jogadores:  # laço de repetição
        print(jogador["nome"], len(jogador["gols"]))


def melhor_media_gols():
    nova_lista = []
    
    for jogador in jogadores:
        novo_jogador = {"nome": jogador['nome'], "jogos": len(jogador['partidas'])}
        
        contador_gol = 0
        for partida in jogador['partidas']:
            contador_gol += partida['gols'] # += ACRESCENTA GOL
        
        novo_jogador['gols'] = contador_gol
        nova_lista.append(novo_jogador)
    
    print(nova_lista)


melhor_media_gols()


def melhor_media_assist():
    pass
