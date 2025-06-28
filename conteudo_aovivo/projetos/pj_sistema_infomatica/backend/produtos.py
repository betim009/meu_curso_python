produtos = [
    {"id_produto": 1, "produto": "Intel i9, 10ª geração", "preco": 1200.00},
    {"id_produto": 2, "produto": "AMD Ryzen 7 5800X", "preco": 950.00},
    {"id_produto": 3, "produto": "Placa-mãe ASUS B550", "preco": 750.00},
    {"id_produto": 4, "produto": "Memória RAM 16GB DDR4", "preco": 320.00},
    {"id_produto": 5, "produto": "SSD NVMe 1TB", "preco": 600.00},
    {"id_produto": 6, "produto": "Fonte Corsair 650W", "preco": 420.00},
    {"id_produto": 7, "produto": "Gabinete Gamer RGB", "preco": 350.00},
    {"id_produto": 8, "produto": "Monitor LG 24'' Full HD", "preco": 900.00},
    {"id_produto": 9, "produto": "Teclado Mecânico Redragon", "preco": 250.00},
    {"id_produto": 10, "produto": "Mouse Gamer Logitech G203", "preco": 180.00},
    {"id_produto": 11, "produto": "Headset HyperX Cloud Stinger", "preco": 320.00},
    {"id_produto": 12, "produto": "HD Seagate 2TB", "preco": 400.00},
]

# Formas ESTATICA de acessar
# Acessar todos os produtos, e exibir o nome de cada um deles.
# print(produtos[0]["produto"])
# print(produtos[1]["produto"])
# print(produtos[3]["produto"])
# print(produtos[4]["produto"])
# print(produtos[5]["produto"])
# print(produtos[6]["produto"])
# print(produtos[7]["produto"])
# print(produtos[8]["produto"])
# print(produtos[9]["produto"])
# print(produtos[10]["produto"])
# print(produtos[11]["produto"])

# Acessar todos os produtos, e exibir o nome e preco de cada um deles.
# print(produtos[0]["produto"], produtos[0]["preco"])
# print(produtos[1]["produto"], produtos[1]["preco"])
# print(produtos[2]["produto"], produtos[2]["preco"])


## AGORA de maneira DINAMICA
## Para fazer dinamicamente, utilizaremos o FOR
# For eh uma estrutura de repeticao

# for item in produtos:
#     print(item["produto"], item["preco"])


# ## Melhorando a exibicao
# for item in produtos:
#     print(f"Nome: {item['produto']}\nPreço: {item['preco']}\n")


## Dinamico com condicao
## Unir for com if para criar filtros

# VERIFICA EXATAMENTE IGUAL
for item in produtos:
    if item["produto"] == "Intel i9, 10ª geração":
        print(item)

# VERIFICA PARCIALMENTE CONTEM DENTRO
# for item in produtos:
#     if "HD" in item["produto"]:
#         print(item)

# VERIFICA TODOS QUE NAO TEM HD DENTRO DE PRODUTO
for item in produtos:
    if "HD" not in item["produto"]:
        print(item)

# VERIFICA produtos por PRECO
# for item in produtos:
#     if item["preco"] > 500:
#         print(item)


''''
Simbolo          Definicao
=                armazenar
==               Comparacao
>                Maior
>=               Maior Igual
<
<=
+=               Incrementacao
-=               Decrementacao
%                Resto da divisao
in
not in
'''
