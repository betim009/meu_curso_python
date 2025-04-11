classe_mago = {"vida": 100, "mana": 200, "magia": 2, "ataque": 1, "defesa": 50}

classe_guerreiro = {"vida": 100, "mana": 100, "magia": 1, "ataque": 2, "defesa": 100}

magia_mago_bola_fogo = {"custo_mana": 30, "dano": 20}

magia_guerreiro_corte_duplo = {"custo_mana": 15, "dano": 15}

locais = ["Floresta dos Elfos", "Deserto dos Assassinos", "Esgoto dos Crocodilos"]

itens_icial = {
    "arma_mago": "cajado de madeira",
    "arma_guerreiro": "espada de ferro",
    "defesa_armadura_mago": 4,
    "defesa_armadura_guerreiro": 8 
}

monstro_1 = {
    "vida": 0,
    "dano": 0,
    "defesa": 0
}

monstro_2 = {
    "vida": 0,
    "dano": 0,
    "defesa": 0
}

monstro_3 = {
    "vida": 0,
    "dano": 0,
    "defesa": 0
}
# INCIAR O JOGO - INICIAR O LOOP:

while True:
    print("Bem vindo!")
    print("Escolha a sua classe!")
    print("[1] - Mago | [2] - Guerreiro")

    classe = input("Sua resposta: ")

    if classe == "1":
        print("Você escolheu ser um mago")
        print("Qual sera o seu nome? ")
        nome = input("Sua resposta: ")
    else:
        print("Você escolheu ser um guerreiro")
        print("Qual sera o seu nome? ")
        nome = input("Sua resposta: ")

    print("Seja bem vindo", nome)
    
    print("Informe qual mapa você gostaria de explorar: ")
    print("[1] - Floresta dos Elfos | [2] - Deserto dos Assassinos | [3] - Esgoto dos Crocodilos")
    local = input("Sua resposta: ")
    break
