"""
- Listas quando usar [ ]
- Dicionario quando usar [ ]


- Você não lida apenas com 1 informão.
Sempre ira trabalhar com volume de informação.
-> LISTA

NAO é ideal:
venda1 = 250
data_venda1 = 30/01/2024
nome_venda = "João"

IDEAL:
Dicionario

venda = {
    "valor": 250,
    "data_venda": "30/01/24",
    "usuario": "João"
}


LISTA tem posição. 0, 1, 2 ...
DICIONARIO tem chave, nome, propriedade...


"""

# CONTINUA SENDO APENAS UMA UNICA INFORMAÇÃO DE VENDA
venda = {
    "valor": 250, 
    "data_venda": "30/01/24", 
    "usuario": "João",
    "assinante": True
}

lista_vendas = [
    {
        "valor": 250,  # chave valor
        "data_venda": "30/01/24", # chave data_venda
        "usuario": "João", 
        "assinante": True
    }, # 0
    {
        "valor": 350, 
        "data_venda": "30/01/24", 
        "usuario": "Guilherme",
        "assinante": False
    } # 1
]

## LOOOPS
## FOR -> ir do primeiro ao ultimo elemento e fazer alguma coisa
# PERCORRER - VARRER 

# EXIBE A LISTA INTEIRA
print(lista_vendas)

print()

# EXIBE CADA ELEMENTO DA LISTA
for x in lista_vendas: 
    print(x)