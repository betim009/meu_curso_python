# Nome do arquivo
arquivo = "./6-arquivos/frutas.txt"  # Caminho para o arquivo frutas.txt localizado no diretório '6-arquivos'

# Lista para armazenar os dados lidos
frutas_precos = []  # Inicializa uma lista vazia para armazenar os dados lidos do arquivo

# Abre o arquivo para leitura
with open(arquivo, "r") as file:  # Abre o arquivo no modo leitura ('r')
    for linha in file:  # Itera sobre cada linha do arquivo
        print(
            linha.strip().split(",")
        )  # Remove espaços extras e quebras de linha, divide a linha por vírgula e imprime a lista resultante

print()  # Adiciona uma linha em branco para separar a saída dos blocos de código

# Abre o arquivo para leitura
with open(arquivo, "r") as file:  # Reabre o arquivo para leitura
    for linha in file:  # Itera sobre cada linha do arquivo
        fruta, preco = linha.strip().split(
            ","
        )  # Divide a linha em duas partes: fruta e preço, removendo espaços extras
        print(fruta, preco)  # Imprime a fruta e o preço separados por um espaço

print()  # Adiciona uma linha em branco para separar a saída dos blocos de código

# Abre o arquivo para leitura
with open(arquivo, "r") as file:  # Reabre o arquivo para leitura
    for linha in file:  # Itera sobre cada linha do arquivo
        fruta, preco = linha.strip().split(
            ","
        )  # Divide a linha em duas partes: fruta e preço, removendo espaços extras
        frutas_precos.append(
            {"fruta": fruta, "preco": float(preco)}
        )  # Adiciona um dicionário com a fruta e o preço (convertido para float) à lista frutas_precos

print(frutas_precos)  # Imprime a lista de dicionários contendo frutas e preços
