from enemys import enemy_list
from heros import hero_list
from items import item_list

ingame_hero_list = []
gold_bag = 50

def shop():
    print("   --SHOP--\n")
    print(f"\n - ouro disponivel: {gold_bag}\n")
    
    for i in range(len(item_list)):
        item = item_list[i]
        if item["type"] == "attack":
            print(f"{i + 1} - {item["name"]}, damage: {item["damage"]}, gold: {item["price"]}")
        elif item["type"] == "defense":
            print(f"{i + 1} - {item["name"]}, armor: {item["armor"]}, gold: {item["price"]}")
        
    command = input("digite o index do item que quer comprar: ")
    for i in range(len(item_list)):
        if item_list[int(command) - 1]["price"] > gold_bag:
            return None

    for i in range(len(ingame_hero_list)):
        hero = ingame_hero_list[i]
        print(f"{i + 1} - {hero["name"]}")

    command2 = int(input("\na qual heroi deseja atribuir o item?\ndigite o numero que corresponde o posição do heroi: "))

    if command2 > 4 or command2 < 1:
        print("é preciso digitar um número entre 1 e 4.")
        return None
    
    for i in range(len(item_list)):
        if int(command) - 1 == i:
            ingame_hero_list[command2 -1]["backpack"].append(item_list[i])

    print(ingame_hero_list)


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
        return "exit"
    else:
        print("erro inesperado,\ntenha certeza que o comando que digitou existe\n")
        main_menu()

main_menu()