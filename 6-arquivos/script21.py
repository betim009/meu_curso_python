# Caminho para o arquivo
arquivo = "./6-arquivos/frutas_vazio.txt"  # Define o caminho para o arquivo frutas_vazio.txt dentro do diretório '6-arquivos'

# Lista de frutas e preços
frutas_precos = [
    {"fruta": "Morango", "preco": 2.19},
    {"fruta": "Laranja", "preco": 3.0},
    {"fruta": "Melancia", "preco": 1.77},
    {"fruta": "Manga", "preco": 3.5},
    {"fruta": "Goiaba", "preco": 2.09},
]  # Define uma lista de dicionários com frutas e seus preços

# Abre o arquivo para escrita
with open(arquivo, "w") as file:  # Abre o arquivo no modo escrita ('w'). Se o arquivo já existir, ele será sobrescrito
    # Itera sobre cada item na lista frutas_precos
    for item in frutas_precos:
        # Escreve a fruta e o preço no arquivo, separados por vírgula, seguido de uma nova linha
        file.write(f"{item['fruta']},{item['preco']}\n")

# ATENÇÃO MANTENHA O ARQUIVO frutas_vazio sem nada.
