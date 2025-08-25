import pandas as pd
from heros import hero_list


def main():
    while True:
        print("[0] - New Game")
        print("[1] - Load Game")
        print("[2] - Quit\n")

        entry = input("R: ")

        if entry == "2":
            break

        if entry == "0":
            print("\n")
            for index, hero in enumerate(hero_list):
                print(f'[{index}] - {hero["name"]} | {hero["class"]}')

            entry_1 = input("R: ")

            loaded_game = pd.read_csv("load_games.csv")

            games = []
            for index, row in loaded_game.iterrows():
                games.append(
                    {
                        "id_game": row["id_game"],
                        "name": row["name"],
                        "class": row["class"],
                    }
                )

            new_game = {
                "id_game": len(games) + 1,
                "name": hero_list[int(entry_1)]["name"],
                "class": hero_list[int(entry_1)]["class"],
                "level": 1,
                "health": hero_list[int(entry_1)]["health"],
                "damage": hero_list[int(entry_1)]["damage"],
                "exp": 0
            }
            games.append(new_game)

            pd.DataFrame(games).to_csv("load_games.csv")

        if entry == "1":
            loaded_game = pd.read_csv("load_games.csv")

            for index, row in loaded_game.iterrows():
                print(f'[{row["id_game"]}] - {row["name"]} | {row["class"]}')

            print("Choice by number: ")
            entry_2 = input("R: ")

            games = []
            for index, row in loaded_game.iterrows():
                games.append(
                    {
                        "id_game": row["id_game"],
                        "name": row["name"],
                        "class": row["class"],
                    }
                )
            
            in_game = games[int(entry_2 ) - 1]
            print(f"\nFaca a sua escolha {in_game["name"]}\n")

            print("[0] - Shop")
            print("[1] - Dungeons")
            print("[2] - Quit")

            entry_3 = input("R: ")
        break


main()
