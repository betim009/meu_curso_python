valor_total = 0

while True:
    print("[1] - CADASTRAR COMPRA")
    print("[0] - ENCERRAR")
    
    entrada = input("Digite a opção desejada: ")
    if entrada == "0":
        print(f"O valor total da minha compra foi de: R$ {valor_total:.2f}")
        break
    elif entrada == "1":
        nome_produto = input('Digite o nome do produto: ')
        preco_produto = float(input('Digite o preço do produto: '))
        if preco_produto <= 0:
            print("O preço do produto deve ser maior que zero.")
            continue
        quantidade_produto = int(input('Digite a quantidade do produto: '))
        if quantidade_produto <= 0:
            print("A quantidade do produto deve ser maior que zero.")
            continue
        
        valor_total += preco_produto * quantidade_produto