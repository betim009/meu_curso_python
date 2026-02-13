# BASE DE DADOS
esportistas = [
    {"id": 1, "nome": "Geraldo", "esporte": "Futebol", "idade": 23},
    {"id": 2, "nome": "Marcelo", "esporte": "Tenis", "idade": 33},
    {"id": 3, "nome": "Vini", "esporte": "Futebol", "idade": 25},
    {"id": 4, "nome": "Mbappe", "esporte": "Futebol", "idade": 26},
]

for esportista in esportistas:
    if esportista["esporte"] == "Futebol" and esportista["idade"] > 25:
        print(esportista["nome"], esportista["esporte"])

print("------------------------------------------")

for item in esportistas:
    if item["esporte"] == "Tenis" or item["idade"] < 25:
        print(item["nome"])

print("------------------------------------------")

esporte = input("Digite o esporte: ")
for esportista in esportistas:
    if esportista["esporte"].lower() == esporte.lower():
        print(esportista)

print("------------------------------------------")

idade = int(input("Digite a idade: "))
for esportista in esportistas:
    if esportista["idade"] > idade:
        print(esportista)