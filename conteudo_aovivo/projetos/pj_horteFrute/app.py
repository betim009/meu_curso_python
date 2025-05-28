import pandas as pd

tabela_vendas = pd.read_csv('./vendas.csv')
tabela_entradas = pd.read_csv('./entradas.csv')

while True:
    print("Bem vindo ao sistema") 
    print("\nEscolha a opcao que deseja:")
    print("\nDigite 0 para ENCERRAR o sistema")
    print("Digite 1 para CONSULTAR uma venda")
    print("Digite 2 para CADASTRAR uma venda")
    print("Digite 3 para CONSULTAR saldo de um produto")
    print("Digite 4 para CADASTRAR entrada no estoque")

    opcao = input("Escolha a opcao: ")

    if opcao == "0":
        print("Programa encerrado")
        break 

    elif opcao == "1": 
        print("\nConsulte uma venda")
        nome = input ("Produto vendido: ")
        print() # QUEBRA LINHA

        validacao = False
        for index, venda in tabela_vendas.iterrows():
            if venda["produto"] == nome: 
                print(venda)
                validacao = True
                print()   
        if validacao == False:
            print ("Produto nao encontrado")
        break

    elif opcao == "2":
        produto = input("Qual produto foi vendido: ")
        qtd = int(input("Quantas unidades foram vendidas: "))
        preco = float(input("Qual o preço da unidade: "))
        data = input("Qual a data da venda: ")

        venda = {
            "produto": produto,
            "quantidade": qtd,
            "preco_custo": preco,
            "data": data
        }
        venda = pd.DataFrame([venda])
        
        tabela_vendas = pd.concat([tabela_vendas, venda])
        tabela_vendas.to_csv('vendas.csv', index=False)
        break

    # elif opcao == "3":
    #     encontrado = False
    #     produto_procurado = input("Qual produto deseja consultar saldo ?")
    #     for produto in vendas:
    #         if produto ["produto"] == produto_procurado:
    #             print(F"Produto {produto_procurado} disponivel")
    #             encontrado = True
    #     if encontrado == False:          
    #         print( F"O produto {produto_procurado} não esta disponível em estoque")
    #     break


    # elif opcao == "4":
    #     produto_estoque = input("Qual produto deseja cadastrar no estoque ?")
    #     qtd_estoque = int(input("Qual quantidade ?"))
    #     preco_custo = float(input("Qual preco?"))
    #     total = round(qtd_estoque * preco_custo)
    #     data_compra = input("Qual a data?")
        
    #     estoque = {
    #         "produto": produto_estoque,
    #         "quantidade": qtd_estoque,
    #         "preco": preco_custo,
    #         "data": data_compra
    #     }
    #     print(estoque) # esse esta ok
    #     break

