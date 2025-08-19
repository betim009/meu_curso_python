maps = [
    {"name": "Dungeon A"},
    {"name": "Dungeon B"},
    {"name": "Dungeon C"},
    {"name": "Dungeon D"}
]

def show_maps():
    for i in range(len(maps)):
        print(f'{i+1} {maps[i]["name"]}')

    entry = int(input("Escolha: "))
    
    if entry == 0 or entry > len(maps):
        return "Error"
    
    return entry - 1 

def main():
    while True:

        map = show_maps()
        print(map)

        break

main()