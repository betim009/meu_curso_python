import pandas as pd  # Importa a biblioteca pandas com o alias pd

# Lê o DataFrame a partir do arquivo CSV
df = pd.read_csv("./7-pandas/frutas.csv")  # Lê o arquivo CSV e cria um DataFrame

# Filtra frutas com preço maior que 2.0
frutas_caro = df[df["preco"] > 2.0]  # Filtra as linhas onde o preço é maior que 2.0
print(frutas_caro)
