import pandas as pd

file = pd.read_csv("file.csv")

# Para cada posicao e linha do arquivo, intereja pelas linhas.
for index, row in file.iterrows():
    col_nome = row["nome"]
    col_preco = row["preco"]

    if pd.isna(col_preco):
        print(f"A linha {index+1} possui a coluna de preco vazio.")


for index, row in file.iterrows():
    col_nome = row["nome"]
    col_preco = row["preco"]

    if col_preco > 4:
        print(f"O produto {col_nome} custa {col_preco}")


for index, row in file.iterrows():
    col_nome = row["nome"]
    col_preco = row["preco"]

    if col_nome.lower() == "arroz":
        print(f"Temos o produto arroz na linha {index+1}")