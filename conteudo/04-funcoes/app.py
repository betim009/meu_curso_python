lista = [{"nome": "Alberto", "idade": 92}, {"nome": "Jessica", "idade": 12},]
lista_1 = [
    (1, 0), # numero [0] 1
    (2, 1), # numero [0] 2
    (0, 1) # numero [0] 0
]

ordernar = sorted(lista, key=lambda item: item["idade"])
ordernar_1 = sorted(lista_1, key=lambda numero: numero[1])

print(lista_1[0][1])