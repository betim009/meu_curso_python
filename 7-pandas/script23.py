import pandas as pd  # Importa a biblioteca pandas com o alias pd

# Lê o DataFrame a partir do arquivo CSV
df = pd.read_csv("./7-pandas/frutas.csv")  # Lê o arquivo CSV e cria um DataFrame

# Exibe o DataFrame
print(df)  # Mostra o DataFrame no console

# Ordena o DataFrame por preço
df_ordenado = df.sort_values(by="preco")  # Ordena o DataFrame pela coluna 'preco'

# Exibe o DataFrame ordenado
print("\nLista de Frutas e Preços (Ordenado por Preço):")
print(df_ordenado)  # Mostra o DataFrame ordenado no console

# Exibe apenas os nomes das frutas
print("\nNomes das Frutas:")
print(df["fruta"])  # Mostra apenas a coluna 'fruta'
