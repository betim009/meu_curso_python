import pandas as pd

file = pd.read_csv("atletas_exportistas.csv")

lista_esportes = [] # LISTA DE STRING
quantidade_esportes = [] # LISTA DE DICIONARIO

for index, row in file.iterrows(): # PERCORRENDO O ARQUIVO
    if row["esporte"] not in lista_esportes: # A COLUNA ESPORTE DO ARQUIVO se NAO EXISTE NA LISTA STRING
        lista_esportes.append(row["esporte"]) # ADICIONA A STRING
        quantidade_esportes.append({ # ADICIONA O DICIONARIO
            "esporte": row["esporte"],
            "quantidade": 1
        })

    else: # SE EXISTIR A STRING
        for element in quantidade_esportes: # PERCORRE CADA DICIONARIO
            if element["esporte"] == row["esporte"]: # ECONTRA O DICIONARIO COM MESMO NOME DE ESPORTE
                element["quantidade"] += 1 # ADICIONA +1 na quantidade


# print(lista_esportes)
print(quantidade_esportes)
