from jogadores import jogadores  # resgatando os dados de jogadores.py

def todos_gols():
    # PARA CADA JOGADOR
    for jogador in jogadores:  # laço de repetição
        nome = jogador["nome"]
        partidas = jogador["partidas"]
        quantidade_gols = 0

        # Paraca da partida desse jogodor
        for partida in partidas:
            # SOMANDO A QUANTIDADE DE GOLS
            quantidade_gols += partida["gols"]
        
        # EXIBINDO
        print(f"{nome} fez: {quantidade_gols} gols")


def criar_media_gols():
    nova_lista = []
    
    for jogador in jogadores:
        novo_jogador = {"nome": jogador['nome'], "jogos": len(jogador['partidas'])}
        
        contador_gol = 0
        for partida in jogador['partidas']:
            contador_gol += partida['gols'] # += ACRESCENTA GOL
        
        novo_jogador['gols'] = contador_gol
        nova_lista.append(novo_jogador)
    
    for jogador in nova_lista:
        jogador["media"] = round((jogador["gols"] / jogador["jogos"]), 2)

    return nova_lista

def melhor_media_assist():
    pass
