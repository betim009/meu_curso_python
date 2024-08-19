# indices:  0         1         2           3         4
frutas = ["Morango", "Laranja", "Melancia", "Manga", "Goiaba"]

# indices: 0    1    2     3    4
precos = [2.19, 3.0, 1.77, 3.5, 2.09]

# O range(0, 2) vai do índice 0 até o índice 1 (não inclui o 2)
for index in range(0, 2, 1):  # começa do 0, vai até a posição 2 de 1 em 1
    print(f"{frutas[index]} custa {precos[index]}")
