import pandas as pd  # Importa a biblioteca pandas com o alias pd

# Lê o DataFrame a partir do arquivo CSV
df = pd.read_csv("./7-pandas/frutas.csv")  # Lê o arquivo CSV e cria um DataFrame

# Exibe o DataFrame
print(df)  # Mostra o DataFrame no console

# Exibe estatísticas básicas do DataFrame
print("\nEstatísticas Básicas:")
print(
    df.describe()
)  # Mostra estatísticas básicas, como média e desvio padrão dos preços
