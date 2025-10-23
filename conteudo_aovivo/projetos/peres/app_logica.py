import pandas as pd

contagem_esportes = {}

file = pd.read_csv("atletas_exportistas.csv")

for esporte in file["esporte"]:
    if esporte not in contagem_esportes:
        contagem_esportes[esporte] = 1
    else:
        contagem_esportes[esporte] += 1

print(contagem_esportes)
