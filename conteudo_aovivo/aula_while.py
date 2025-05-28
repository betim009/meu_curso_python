saidas = [
    {"id": 1, "data": "13/03/2025", "valor": 487.12},
    {"id": 2, "data": "14/03/2025", "valor": 87.00},
    {"id": 3, "data": "15/03/2025", "valor": 123.00},
    {"id": 4, "data": "16/03/2025", "valor": 400.00},
]



while True:
    print('Bem vindo ao sistema')
    print('[1] - Consultar saldo')
    print('[2] - Consultar saidas')
    print('[3] - Consultar entradas')
    print('[0] - Encerrar')
    entrada = input('Digite um valor: ')
    print() # quebra de linha

    if entrada == '1':
        # logica de consultar saldo
        print(""" 
        [1] - Janeiro
        [2] - Fevereiro
        [3] - Março
    """)
        opcao = input('Qual mes deseja ver o saldo: ')
    
    if entrada == '2':
        # logica de consultar saidas
        somar_saidas = 0
        for item in saidas:
            somar_saidas += item["valor"]
        print("O total das saidas foram de:",somar_saidas)

    if entrada == "0":
        break

    