from generate_csv import generate_csv
from lista_rock import bandas
from lista_pagamentos import pagamentos
import pandas as pd

# Executando a funcao para criar os CSV's
csv_bandas = generate_csv(bandas, "bandas.csv")
csv_pagamentos = generate_csv(pagamentos, "pagamentos.csv")

# Lendo o csv
df_bandas = pd.read_csv("bandas.csv")

# Fazendo filtro
for index, row in df_bandas.iterrows():
    if row["qtd_album"] > 9:
        print(row["nome"])