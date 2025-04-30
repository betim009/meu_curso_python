"""
- Analise do projeto

# Começando: 
1. Base de dados dos produtos
2. Base de dados das vendas
3. Base de dados das entradas


1. Informações de cada fruta, legume, verdura e etc. 
Nome? preço? tudo o que for importante de cada fruta

2. Informações de cada venda feita
quem comprou? quando foi feita a venda? o que foi vendido? total da venda? 

3. Quantas frutas eu comprei? quando eu comprei? por quanto eu comprei? 

# Temos que definir o máximo antes de iniciar o projeto

## imagina um pedreiro construindo um quarto onde ele não sabe o tamanho do quarto?
pode acontecer dele ter que derrubar uma parede, pq ele percebeu que era pequeno.

# PENSA o maximo antes de fazer para nao construir algo desnecessário.




4 . A nossa interface será o terminal.

- Cadastrar estoque(entrada)
- Cadastrar venda

- Consultar venda
- Consultar saldo
"""



# Para iniciar a interface

# A ideia é ter uma interface de como se fosse "PERGUNTA" e "RESPOSTA"
while True:
    print("###### Bem vindo ao programa #######\n")
    
    print("Digite 0 para encerrar.\n")
    print("Digite 1 para consultar uma venda.\n")
    resposta = input("- : ")
    
    ### Consultar vendas?
    if resposta == "1":
        print("Qual produto você deseja consultar?")
    
    ### Consultar saldo?
    
    ### Cadastrar uma venda?
    
    ### Cadastrar uma entrada?
    
    
    ### 0 para encerrar a interface
    if resposta == "0":
        print("Programa encerrado.")
        break
    