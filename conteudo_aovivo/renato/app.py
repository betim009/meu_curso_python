import pandas as pd

# Arquivos
arquivo = pd.read_csv("vendas_equipamentos.csv")

# Colunas
coluna_metodo_pagamento = arquivo["metodopagamento"]
coluna_preco= arquivo["preco"]

# Metodos
quantidade_metodos_pagamento = coluna_metodo_pagamento.value_counts()
media_preco = coluna_preco.mean()
mediana_preco = coluna_preco.median()
moda_preco = coluna_preco.mode()[0]
max_preco = coluna_preco.max()
min_preco = coluna_preco.min()

# Algoritmo
# for index, row in arquivo.iterrows():
#     if row["preco"] > 4000:
#         print(row)

for index, row in arquivo.iterrows():
    if row["metodopagamento"] == "Pix" and row["preco"] > 4000:
        print(row)

# Exibir
# print(max_preco, min_preco)