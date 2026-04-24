produtos = [
    {"nome": "Notebook", "preco": 4200.00, "estoque": 5},
    {"nome": "Monitor", "preco": 950.00, "estoque": 0},
    {"nome": "Teclado", "preco": 180.00, "estoque": 12},
]

for produto in produtos:
    if produto["estoque"] == 0:
        print(f"{produto['nome']} está sem estoque.")
