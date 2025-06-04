import pandas as pd # pip3 install pandas | pip install pandas | py -m pip install pandas
from cardapio import cardapio
from scripts import *

### interface
while True:
    print(""" Bem vindo a Pizzaria Python
          [1] ver o cardapio
          [2] Buscar por nome
          [3] selecionar sabor
          [4] registrar uma reclamacao
          [0] sair""")
    
    entrada = input('DIGITE UMA DAS OPÇÕES: ')
    
    if entrada == "1":
       exibir_cardapio()
       break


    elif entrada == "2":
        busca = input('digite o sabor procurado: ')
        procurar_pizza(busca)
        break

    elif entrada == "3":
      pedido = []
      exibir_cardapio()
      selecionar = input('digite o sabor que gostaria?')
      saborselecionado = retornar_pizzas(selecionar)
        # print(saborselecionado)
      exibir_selecao(selecionar)

      select_tamanho = input('qual tamanho gostaria?')

      pedido.append(selecionar_tamanho(selecionar,select_tamanho))
      for pizza in pedido:
         print(f' voce escolheu uma pizza', pizza['sabor'],'tamanho', pizza['tamanho'])

      input('Podemos confirmar o pedido? [s] ou [n]')
     # print(selecionar_tamanho(selecionar,select_tamanho))


      break

    elif entrada == "0":
       break