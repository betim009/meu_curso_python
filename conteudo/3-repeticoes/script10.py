frutas = ["Morango", "Laranja", "Melancia", "Manga", "Goiaba"]

# Estrutura de repetição, que percorre a lista frutas
for item in frutas:
    print(item)  # Exibe cada item da fruta
    
# indeces:  0         1         2           3         4
frutas = ["Morango", "Laranja", "Melancia", "Manga", "Goiaba"]

# indices: 0    1    2     3    4
precos = [2.19, 3.0, 1.77, 3.5, 2.09]

# O enumerate gera o índice e o item da lista frutas
for index, item in enumerate(frutas):
    # exibe o item de frutas e o preço por index
    print(f"A fruta: {item} custa {precos[index]}")
