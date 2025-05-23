from produtos import *
from vendas import *
from estoque import *
import pandas as pd

# For -> Vai do primeiro ao ultimo elemento da lista
for produto in produtos:
    for venda in vendas:
        if produto["id"] != venda["id_produto"]:
            estoque.append(produto)
        
estoque_tabela = pd.DataFrame(estoque)
estoque_tabela.to_csv("estoque.csv", index=False)