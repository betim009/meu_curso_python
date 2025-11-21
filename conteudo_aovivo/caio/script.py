# for i in range(0, 3):
#     print(i)

# print()

# i = 0
# while i < 3:
#     print(i)
#     i += 1

# print()

# entrada = int(input("Digite numero de 0 - 10: "))
# while entrada != 0:
#     print("Nao é diferente do zero")
#     entrada = int(input("Digite numero de 0 - 10: "))

v1 = ["A", "B", "C"]
v2 = [10, 20, 30]


# for i in range(len(v1)):
#     print(v1[i], v2[i])

# print()

# for i, item in enumerate(v1):
#     print(item, v2[i])

# print()

# j = 0
# for item in v1:
#     print(item, v2[j])
#     j += 1

# print()

# index = 0
# while index < len(v1):
#     print(v1[index], v2[index])
#     index += 1


def estoque(produtos, quantidades):
    estoque_completo = True
    for item in quantidades:
        if item == 0:
            estoque_completo = False

    if estoque_completo == True:
        print("Estoque Completo")
        return
        

    for i, item in enumerate(produtos):
        quantidade = quantidades[i]
        
        if quantidade == 0:
            print(f"{item} zerado.")



estoque(
    ["mouse", "teclado", "monitor"],
    [10, 0, 5]
)