import pandas as pd  # Importa a biblioteca pandas com o alias pd

# Dados das frutas e preços
dados = {
    "fruta": ["Morango", "Laranja", "Melancia", "Manga", "Goiaba"],
    "preco": [2.19, 3.0, 1.77, 3.5, 2.09],
}  # Define um dicionário com frutas e preços

# Cria um DataFrame a partir dos dados
df = pd.DataFrame(dados)  # Converte o dicionário em um DataFrame

# Exibe o DataFrame
print(df)  # Mostra o DataFrame no console

# Salva o DataFrame em um arquivo CSV
df.to_csv(
    "./7-pandas/new_frutas.csv", index=False
)  # Salva o DataFrame como 'frutas.csv', sem incluir o índice
