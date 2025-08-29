from heros import heros
import pandas as pd

while True:
    print("0 - New Game")
    print("1 - Load Game")
    print("X - Quit\n")

    entry = input("R: ")


    if entry == "0":
        for index, i in enumerate(heros):
            print(f"{index} | {i['name']} - {i['class']}")

        new_hero = input("\nR: ") # 0 ou 1

        load_game_csv = pd.read_csv("load_game.csv")
        load_game = []

        for index, row in load_game_csv.iterrows():
            load_game.append({
                "name": row["name"],
                "class": row["class"],
                "level": row["level"]
            })

        load_game.append(heros[int(new_hero)])
        pd.DataFrame(load_game).to_csv("load_game.csv")


        

    elif entry == "1":
        pass
    else:
        break