produtos_cafe = [
    {
        "id": 1,
        "nome": "Café Arábica Gourmet",
        "tipo": "Grãos",
        "torra": "Média",
        "preco": 35.90,
        "peso_g": 250,
        "desconto": True
    },
    {
        "id": 2,
        "nome": "Café Robusta Tradicional",
        "tipo": "Moído",
        "torra": "Escura",
        "preco": 18.50,
        "peso_g": 500,
        "desconto": True
    },
    {
        "id": 3,
        "nome": "Café Orgânico Premium",
        "tipo": "Grãos",
        "torra": "Clara",
        "preco": 42.00,
        "peso_g": 250,
        "desconto": False
    },
    {
        "id": 4,
        "nome": "Café Descafeinado",
        "tipo": "Moído",
        "torra": "Média",
        "preco": 27.90,
        "peso_g": 250,
        "desconto": True
    },
    {
        "id": 5,
        "nome": "Café Solúvel Instantâneo",
        "tipo": "Solúvel",
        "torra": "Escura",
        "preco": 15.00,
        "peso_g": 100,
        "desconto": False
    }
]

for item in produtos_cafe:
    if "escu" in item["torra"].lower():
        print(item)


lista = [40, 100, 200, 300, 500, 100]

maior = min(lista)
print(maior)