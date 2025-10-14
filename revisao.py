animais = [
    {"nome": "Leão", "classe": "Mamífero", "habitat": "Savana", "alimentacao": "Carnívoro"},
    {"nome": "Elefante", "classe": "Mamífero", "habitat": "Floresta e Savana", "alimentacao": "Herbívoro"},
    {"nome": "Tartaruga", "classe": "Réptil", "habitat": "Terrestre e Aquático", "alimentacao": "Onívoro"},
    {"nome": "Águia", "classe": "Ave", "habitat": "Montanhas", "alimentacao": "Carnívoro"},
    {"nome": "Tubarão", "classe": "Peixe", "habitat": "Oceano", "alimentacao": "Carnívoro"},
    {"nome": "Sapo", "classe": "Anfíbio", "habitat": "Lagos e Pântanos", "alimentacao": "Insetívoro"},
    {"nome": "Pinguim", "classe": "Ave", "habitat": "Regiões Polares", "alimentacao": "Carnívoro"},
    {"nome": "Girafa", "classe": "Mamífero", "habitat": "Savana", "alimentacao": "Herbívoro"},
    {"nome": "Jacaré", "classe": "Réptil", "habitat": "Rios e Lagos", "alimentacao": "Carnívoro"},
    {"nome": "Golfinho", "classe": "Mamífero", "habitat": "Oceano", "alimentacao": "Carnívoro"}
]

# Exibe todos os dicionarios
for item in animais:
    print(item)

# Exibe um dos valores do dicionario
for item in animais:
    print(item["nome"])
    
# Filtro de animais da classe mamifero
for item in animais:
    if item["classe"] == "Mamífero":
        print(item)