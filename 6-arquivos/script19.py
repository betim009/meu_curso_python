# Nome do arquivo
arquivo = './6-arquivos/frutas.txt'  # Caminho para o arquivo frutas.txt dentro do diretório '6-arquivos'

# Abre o arquivo para leitura
with open(arquivo, 'r') as file:  # Abre o arquivo no modo leitura ('r')
    # Itera sobre cada linha do arquivo
    for linha in file:  # Percorre cada linha do arquivo
        print(linha.strip())  # Remove espaços extras e quebras de linha e exibe o conteúdo da linha
