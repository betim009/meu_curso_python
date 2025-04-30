part 1
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


part2
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


part3
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
