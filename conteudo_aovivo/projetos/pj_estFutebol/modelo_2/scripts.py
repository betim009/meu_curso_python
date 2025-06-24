import pandas as pd
import os

def cria_tabela():
    # Precisa verificar se o arquivo ja existe
    if os.path.exists("partidas_jogadores.csv"):
        # Se Existir -> leia o arquivo
        partidas_jogadores = pd.read_csv("partidas_jogadores.csv")

    # Se nao existir -> crie a tabela
    else: 
        colunas = ["id_partida", "id_jogador", "gols", "assistencias"]
        partidas_jogadores = pd.DataFrame(columns=colunas)
        partidas_jogadores.to_csv("partidas_jogadores.csv", index=False)

    # Retorne o resultado do arquivo
    return partidas_jogadores


print(cria_tabela())