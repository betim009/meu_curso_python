# BASE DE DADOS
esportistas = [
    {"id": 1, "nome": "Geraldo", "esporte": "Futebol", "idade": 23},
    {"id": 2, "nome": "Marcelo", "esporte": "Tenis", "idade": 33},
]

# ENTRADA DE DADOS
novo_esportista_id = input("Digite o ID: ")
novo_esportista_nome = input("Digite o nome do esportista: ")
novo_esportista_esporte = input("Digite o esporte: ")
novo_esportista_idade = int(input("Digite a idade: "))

# CADASTRO DE DADOS
esportistas.append({ "id": novo_esportista_id, "nome": novo_esportista_nome, "esporte": novo_esportista_esporte, "idade":  novo_esportista_idade})

# FILTROS
for item in esportistas:
    if item["esporte"] == "Futebol":
        print(item)

for item in esportistas:
    if item["nome"] == "Geraldo":
        print(item)

for item in esportistas:
    if item["idade"] > 30:
        print(item)