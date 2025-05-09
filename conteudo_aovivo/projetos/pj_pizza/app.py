from scripts import *

# INTERFACE
while True:
    print(""" OPÇÕES
    [1] - RESGATAR UMA PIZZA ESPECIFICA
    [2] - CADASTRAR UMA PIZZA
    
    [0] - ENCERRAR
    """)
    
    entrada = input('DIGITE UMA DAS OPÇÕES: ')
    
    if entrada == "1":
        print(""" 
        [1] - POR ID
        [2] - TODOS
        [3] - POR NOME      
        """)
        
        entrada_pizza = input('DIGITE: ')
        if entrada_pizza == "1":
            pizza_id = int(input("Digite o id da pizza que você deseja encontrar: "))
            resultado = get_pizza_id(pizza_id)
            print(resultado)
            break
        elif entrada_pizza == "2":
            pass
        
    elif entrada == "2":
        pass
    
    elif entrada == "2":
        pass
    
    if entrada == "0":
        break