from infos import *
from interface import * 

# INCIAR O JOGO - INICIAR O LOOP:
while True:
    print(menu)
    
    # A ESCOLHA DA CLASSE
    print(menu_inicial)
    class_ = input("Your answer: ")

    if class_ == "1":
        print("You chose to be a wizard")
        print("What will your name be? ")
        class_ = class_mage
        name = input("Your answer: ")
    else:
        print("You chose to be a warrior")
        print("What will your name be? ")
        class_ = class_warrior
        name = input("Your answer: ")

    print("Welcome", name)

    # A ESCOLHA DO MAPA
    print(menu_mapa)
    location = input("Your answer: ")

    if location == "1":
        print(menu_attack_1)
        atack = input("Your answer:")

        # SE FOR ATACK BASICO
        if atack == "1":
            print("The life of monster is this: ", forest["life"] - class_["attack"])

        # SE FOR ATACK MAGICO
        else:
            print(
                "The life of monster is this: ",
                forest["life"] - class_["magic"] * class_["spell"]["hit"],
            )

    elif location == "2":
        print(menu_attack_2)
        atack = input("Your answer:")
        if atack == "1":
            print("The life of monster is this: ", desert["life"] - class_["attack"])
        else:
            print(
                "The life of monster is this: ",
                desert["life"] - class_["magic"] * class_["spell"]["hit"],
            )
    else:
        print(menu_attack_3)
        atack = input("Your answer:")
        if atack == "1":
            print("The life of monster is this: ", sewer["life"] - class_["attack"])
        else:
            print(
                "The life of monster is this: ",
                sewer["life"] - class_["magic"] * class_["spell"]["hit"],
            )

    break