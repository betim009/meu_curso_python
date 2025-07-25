import sys

hero_list = [
    {
        "name": "magnus",
        "class": "tank",
        "damage_type": "physical",
        "damage": 60,
        "health": 1200,
        "armor": 60,
        "magic_resistance": 5,
        "health_regen": 25,
        "backpack": [],
        "level": 1
    },
    {
        "name": "erin",
        "class": "bruiser",
        "damage_type": "physical",
        "damage": 130,
        "health": 800,
        "armor": 45,
        "magic_resistance": 5,
        "health_regen": 5,
        "backpack": [],
        "level": 1
    },
    {
        "name": "mikayla",
        "class": "support",
        "damage_type": "magic",
        "damage": 20,
        "cure": 40,
        "health": 400,
        "armor": 4,
        "magic_resistance": 12,
        "health_regen": 2,
        "backpack": [],
        "level": 1
    },
    {
        "name": "neruel",
        "class": "mage",
        "damage_type": "magic",
        "damage": 100,
        "health": 500,
        "armor": 5,
        "magic_resistance": 40,
        "health_regen": 2,
        "backpack": [],
        "level": 1
    },
]

enemy_list = [
    {
        "name": "wolf",
        "class": "creature",
        "damage_type": "physical",
        "damage": 20,
        "health": 200,
        "armor": 2,
        "magic_resistance": 0,
        "health_regen": 1,
        "level": 1
    },
    {
        "name": "troll",
        "class": "creature",
        "damage_type": "physical",
        "damage": 45,
        "health": 450,
        "armor": 5,
        "magic_resistance": 0,
        "health_regen": 2,
        "level": 1
    },
    {
        "name": "wolf mounted troll",
        "class": "creature",
        "damage_type": "physical",
        "damage": 65,
        "health": 650,
        "armor": 7,
        "magic_resistance": 0,
        "health_regen": 4,
        "level": 1
    },
    {
        "name": "troll warlord",
        "class": "creature",
        "damage_type": "physical",
        "damage": 120,
        "health": 700,
        "armor": 15,
        "magic_resistance": 8,
        "health_regen": 5,
        "level": 1
    },
    {
        "name": "king troll",
        "class": "creature",
        "damage_type": "physical",
        "damage": 170,
        "health": 1000,
        "armor": 30,
        "magic_resistance": 15,
        "health_regen": 10,
        "level": 1
    }
]

item_list = [
    {
        "name": "basic sword",
        "class": "item",
        "damage_type": "physical",
        "type": "attack",
        "damage": 10,
        "price": 50
    },
    {
        "name": "staff of wizard",
        "class": "item",
        "damage_type": "magic",
        "type": "attack",
        "damage": 80,
        "price": 350
    },
    {
        "name": "golden sword",
        "class": "item",
        "damage_type": "physical",
        "type": "attack",
        "damage": 25,
        "price": 125
    },
    {
        "name": "diamond sword",
        "class": "item",
        "damage_type": "physical",
        "type": "attack",
        "damage": 50,
        "price": 250
    },
    {
        "name": "basic shield",
        "class": "item",
        "type": "defense",
        "armor": 5,
        "price": 25
    },
    {
        "name": "iron shield",
        "class": "item",
        "type": "defense",
        "armor": 15,
        "price": 50
    }
]

ingame_hero_list = []

gold_bag = 50

def shop():
    print("   --SHOP--\n")

    i = 1
    i2 = 1

    for item in item_list:
        if item["type"] == "attack":
            print(f"{i} - {item["name"]}, damage: {item["damage"]}, gold: {item["price"]}")
        elif item["type"] == "defense":
            print(f"{i} - {item["name"]}, armor: {item["armor"]}, gold: {item["price"]}")
        i += 1

    print(f"\n - ouro disponivel: {gold_bag}\n")
    command = input("digite o nome do item que quer comprar: ")

    for hero in ingame_hero_list:
        print(f"{i2} - {hero["name"]}")
        i2 += 1

    command2 = int(input("\na qual heroi deseja atribuir o item?\n"
                     "digite o numero que corresponde o posição do heroi: "))

    if command2 > 4 or command2 < 1:
        print("é preciso digitar um número entre 1 e 4.")
        shop()
    #agora precisa pensar em como faz para atualizar o gold apos a compra
    #outro problema é que por algum motivo, quando se compra o iron shield,
    #o codigo caminha pro else
    for item in item_list:
        if item["name"] == command and item["price"] <= gold_bag:
            ingame_hero_list[command2 - 1]["backpack"] = item
            print(f"item comprado: {ingame_hero_list[command2 -1]["backpack"]["name"]}")
            break
        elif item["price"] > gold_bag:
            print("\nouro insuficiente")
            shop()
        else:
            print("tente novamente, talvez você tenha digitado errado, ou\n"
                  "o item não existe")
            shop()
def character_select():
    print("   --CHARACTER SELECT--\n")
    print(" - type 1 for: magnus\n")
    print(" - type 2 for: erin\n")
    print(" - type 3 for: mikayla\n")
    print(" - type 4 for: neruel\n")

    command = input("command: \n")

    if command == "1":
        ingame_hero_list.append(hero_list[0])
        print(ingame_hero_list[0])
    elif command == "2":
        ingame_hero_list.append(hero_list[1])
        print(ingame_hero_list[0])
    elif command == "3":
        ingame_hero_list.append(hero_list[2])
        print(ingame_hero_list[0])
    elif command == "4":
        ingame_hero_list.append(hero_list[3])
        print(ingame_hero_list[0])
    else:
        print(" - erro inesperado, tente novamente")
        character_select()

    shop()

def main_menu():
    print("   --MAIN MENU--\n")
    print(" - type 1 for: start new game\n"
          " - type 2 for: quit\n\n")

    command = input("command: \n")

    if command == "1":
        character_select()
    elif command == "2":
        sys.exit()
    else:
        print("erro inesperado,\ntenha certeza que o comando que digitou existe\n")
        main_menu()

main_menu()