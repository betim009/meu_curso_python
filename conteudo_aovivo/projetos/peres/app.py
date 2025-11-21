import pandas as pd

file = pd.read_csv("atletas_exportistas.csv")

lista_esportes = [] 
quantidade_esportes = [] 

for index, row in file.iterrows(): 
    if row["esporte"] not in lista_esportes: 
        lista_esportes.append(row["esporte"]) 
        quantidade_esportes.append({ 
            "esporte": row["esporte"],
            "quantidade": 1
        })

    else: 
        for element in quantidade_esportes:
            if element["esporte"] == row["esporte"]:
                element["quantidade"] += 1 


# print(lista_esportes)
print(quantidade_esportes)
