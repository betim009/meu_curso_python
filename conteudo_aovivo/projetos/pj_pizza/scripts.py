import pandas as pd

def exibir_cardapio():
    data_frame = pd.read_csv("cardapio.csv")
    print(data_frame)

def procurar_pizza(nome):
    data_frame = pd.read_csv("cardapio.csv")
    filtro = data_frame[data_frame["sabor"].str.contains(nome, case=False, na=False)]
    print(filtro)
       
def retornar_pizzas(nome):
    retornar = []
    for pizza in cardapio:
        if nome == pizza['sabor']:
            retornar.append(pizza)
    return retornar
   ### return "Não existe essa pizza!" 

def selecionar_tamanho(nome,tamanho):
    for pizza in cardapio:
        if nome == pizza['sabor']:
            if tamanho == pizza['tamanho']:
                return pizza
    return "Não existe essa pizza!" 
    
def exibir_selecao(nome):
    for selecao in retornar_pizzas(nome):
        print(f"sabor: {selecao['sabor']} ,tamanho: {selecao['tamanho']} , preco: {selecao['preco']}")