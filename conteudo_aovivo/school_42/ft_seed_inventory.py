def ft_seed_inventory():
    seeds = {
        "Tomato": 25,     # int → quantidade de pacotes
        "Lettuce": 40,
        "Carrot": 30
    }

    print("Seed Inventory")
    for seed_type, quantity in seeds.items():
        print(f"Seed type: {seed_type} | Packets available: {quantity}")