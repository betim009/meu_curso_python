frutas = [
    {"id": 1, "fruta": "Morango", "preco": 2.19, "quantidade": 1},
    {"id": 2, "fruta": "Laranja", "preco": 3.0, "quantidade": 59},
    {"id": 3, "fruta": "Melancia", "preco": 1.77, "quantidade": 13},
    {"id": 4, "fruta": "Manga", "preco": 3.5, "quantidade": 20},
    {"id": 5, "fruta": "Goiaba", "preco": 2.09, "quantidade": 10},
]

frutas[0]['preco'] = 2.39

for item in frutas:
    print(item)