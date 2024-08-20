import pandas as pd  # Importa a biblioteca pandas com o alias pd

# Lê o DataFrame a partir do arquivo CSV
df = pd.read_csv("./7-pandas/frutas.csv")  # Lê o arquivo CSV e cria um DataFrame

# Filtra frutas com preço menor que 3.0
frutas_baratas = df[df["preco"] < 3.0]  # Filtra as frutas com preço menor que 3.0

# Exibe as frutas mais baratas
print("Frutas com preço menor que 3.0:")
print(frutas_baratas)  # Mostra as frutas filtradas no console

# Adiciona uma coluna indicando se a fruta é barata ou cara
df["categoria"] = df["preco"].apply(lambda x: "Barato" if x < 3.0 else "Caro")

# Exibe o DataFrame com a nova coluna
print("\nFrutas com Categorias:")
print(df)  # Mostra o DataFrame atualizado no console

# Calcula a média dos preços das frutas
media_precos = df["preco"].mean()

# Exibe a média dos preços
print(f"\nMédia dos Preços das Frutas: {media_precos:.2f}")
