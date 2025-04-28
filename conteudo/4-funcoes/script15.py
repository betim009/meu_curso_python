# Lista de dicionários contendo frutas e seus preços
frutas_precos = [
    {"fruta": "Morango", "preco": 2.19},
    {"fruta": "Laranja", "preco": 3.0},
    {"fruta": "Melancia", "preco": 1.77},
    {"fruta": "Manga", "preco": 3.5},
    {"fruta": "Goiaba", "preco": 2.09},
]


# Função para adicionar uma nova fruta e seu preço à lista
def adicionar(fruta, preco):
    frutas_precos.append(
        {"fruta": fruta, "preco": preco}
    )  # Adiciona um dicionário à lista


# Função para listar todas as frutas e seus preços
def listar():
    for item in frutas_precos:  # Percorre cada dicionário na lista
        print(item["fruta"], item["preco"])  # Imprime a fruta e o preço


# Função principal que controla o menu e as opções do usuário
def main():
    while True:  # Loop contínuo até que o usuário decida encerrar
        # Exibe as opções disponíveis para o usuário
        print("[1] - Para adicionar uma nova fruta")
        print("[2] - Para listar todas as frutas")
        print("[0] - Para encerrar \n")
        entrada = input("Sua opção: ")  # Recebe a opção do usuário

        if entrada == "0":
            break  # Encerra o loop e o programa

        if entrada == "1":
            # Recebe o nome e o preço da nova fruta
            entrada_fruta = input("Nome da fruta: ")
            entrada_preco = input("Preço da fruta:")
            # Adiciona a nova fruta à lista
            adicionar(entrada_fruta, entrada_preco)

        if entrada == "2":
            # Lista todas as frutas e preços
            listar()


# Chama a função principal para iniciar o programa
main()
