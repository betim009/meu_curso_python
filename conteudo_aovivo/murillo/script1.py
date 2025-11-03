lista = [
    "24/03/2025", # 0 Index - Indice - Ordem
    "22/06/2025", # 1
    "14/04/2025", # 2
    "25/05/2025", # 3
    "18/03/2024", # 4
    "18/03/2024", # 5
    "18/03/2024", # 6
    "18/03/2024", # 7
    "18/03/2024"  # 8
] 

print(lista)

print()

# Exibindo todas as datas manualmente
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print()
# ------- # ------------#

# Percorer Dinamicamente os dados de uma lista
for data in lista:
    print(data)

print()

for data in lista:
    # estrutura de condicao
    if data == "18/03/2024":
        print(data)