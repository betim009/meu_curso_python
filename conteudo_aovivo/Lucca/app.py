meus_pokes = [
    {
        "nome": "Charmander",
        "tipo": "fogo",
        "vantangem": "planta",
        "desvantagem": "agua",
        "forca": 3,
        "vida": 10,
    },
    {
        "nome": "Bulbasaur",
        "tipo": "planta",
        "vantangem": "agua",
        "desvantagem": "fogo",
        "forca": 3,
        "vida": 10,
    }
]

adversario_pokes = [
    {
        "nome": "Squirtle",
        "tipo": "agua",
        "vantangem": "fogo",
        "desvantagem": "planta",
        "forca": 3,
        "vida": 10
    }
]

# 0 é primeiro, 1 é segundo... 

# Escolhe o pokemon do combate
meu_pokemon = meus_pokes[0] # charmander
adversario_pokemon = adversario_pokes[0] # squirtle


# Combate
print("Inciando o combate.")
print()
while True: # Loop 
    print("Meu pokemon atacando")
    adversario_pokemon["vida"] -= 2
    print(adversario_pokemon)
    print() # PULA LINHA

    if adversario_pokemon["vida"] <= 0:
        print("Adversario derrotado")
        break

    print("Pokemon do adversario atacando")
    meu_pokemon["vida"] -= 4
    print(meu_pokemon)
    print() # PULA LINHA

    if meu_pokemon["vida"] <= 0:
        print("Fui derrotado")
        break


    
