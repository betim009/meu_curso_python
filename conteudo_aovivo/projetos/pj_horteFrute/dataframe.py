import pandas as pd
from entradas import entradas
from vendas import vendas

# GERAR entradas
df_entradas = pd.DataFrame(entradas)
df_entradas.to_csv('entradas.csv', index=False)

# GERAR vendas
df_vendas = pd.DataFrame(vendas)
df_vendas.to_csv('vendas.csv', index=False)