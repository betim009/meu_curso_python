# Uma lista de dicionário
frutas = [
    {"nome": "Maçã", "cor": "Vermelha", "preço": 3.50},
    {"nome": "Banana", "cor": "Amarela", "preço": 2.00},
    {"nome": "Laranja", "cor": "Laranja", "preço": 2.50},
    {"nome": "Uva", "cor": "Roxa", "preço": 4.00},
    {"nome": "Manga", "cor": "Amarela", "preço": 5.00},
]

# Verificando se a fruta do index 1 e chave nome é igual a "banana"
if frutas[1]["nome"] == "banana":
    # Não vai exibir nada pois não atende a condição
    print("Encontrei a fruta Banana")
