"""
- Codigo:
    escreve no arquivo.
- Comando:
    escreve no terminal

    comando para instalar bibliotecas/ferramentas do python:
    # python3 -m pip install nome-ferramenta
"""

import pandas as pd

# Lista de dicionario 
# Dicionario com listas

"""
Lista -> acessa por indice
Dicionario -> acessa por chave
"""

lista_dicionario = [
    {
        "nome": "Alberto",
        "profissao": "Professor"
    },
    {
        "nome": "Jean",
        "profissao": "Dev FrontEnd"
    },
    {
        "nome": "Maria",
        "profissao": "Dev BackEnd"
    },
]

dicionario_lista = {
    #       0           1       2
    "nome": ["Alberto", "Jean", "Maria"],
    #            0             1               2
    "profissao": ["Professor", "Dev FrontEnd", "BackEnd"]
}

print(lista_dicionario[0]["nome"], lista_dicionario[0]["profissao"])
print(dicionario_lista["nome"][0], dicionario_lista["profissao"][0])

tabela_1 = pd.DataFrame(lista_dicionario)
tabela_1.to_csv("raw1.csv")

tabela_2 = pd.DataFrame(dicionario_lista)
tabela_2.to_csv("raw2.csv")

print(tabela_1)
print(tabela_2)