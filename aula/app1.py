import pandas as pd

df = pd.read_csv("arquivo.csv")

# Listas para montar os DataFrames no mesmo estilo
resultado = []
resultado_1 = []
resultado_2 = []
resultado_3 = []
resultado_4 = []
resultado_5 = []
resultado_6 = []
resultado_7 = []

# resultado
for index, row in df.iterrows():
    col_categoria = row["categoria"]
    try:
        if col_categoria == "Alimentos":
            resultado.append(row)
    except:
        continue

# resultado_1
for index, row in df.iterrows():
    col_categoria = row["categoria"]
    try:
        if "alimentos" in col_categoria.lower():
            resultado_1.append(row)
    except:
        continue

# resultado_2
for index, row in df.iterrows():
    col_categoria = row["categoria"]
    col_preco = row["preco_unitario"]
    try:
        if "alimentos" in col_categoria.lower() and col_preco >= 19:
            resultado_2.append(row)
    except:
        continue

# resultado_3
for index, row in df.iterrows():
    col_categoria = row["categoria"]
    col_preco = row["preco_unitario"]
    try:
        if "alimentos" in col_categoria.lower() or col_preco >= 19:
            resultado_3.append(row)
    except:
        continue

# resultado_4
for index, row in df.iterrows():
    col_categoria = row["categoria"]
    col_canal = row["canal"]
    try:
        if "eletronicos" in col_categoria.lower() and col_canal == "Online":
            resultado_4.append(row)
    except:
        continue

# resultado_5
for index, row in df.iterrows():
    col_estado = row["estado"]
    col_desconto = row["desconto_pct"]
    try:
        if col_estado == "SP" and col_desconto > 0:
            resultado_5.append(row)
    except:
        continue

# resultado_6
for index, row in df.iterrows():
    col_quantidade = row["quantidade"]
    col_canal = row["canal"]
    try:
        if col_quantidade >= 15 and col_canal == "Loja Fisica":
            resultado_6.append(row)
    except:
        continue

# resultado_7
for index, row in df.iterrows():
    col_categoria = row["categoria"]
    col_preco = row["preco_unitario"]
    col_desconto = row["desconto_pct"]
    try:
        if ("eletronicos" in col_categoria.lower() and col_preco >= 19) or ("alimentos" in col_categoria.lower() and col_desconto > 0):
            resultado_7.append(row)
    except:
        continue

# Exibindo Resultados
print(pd.DataFrame(resultado).head())
# print(pd.DataFrame(resultado_1).head())
# print(pd.DataFrame(resultado_2).head())
# print(pd.DataFrame(resultado_3).head())
# print(pd.DataFrame(resultado_4).head())
# print(pd.DataFrame(resultado_5).head())
# print(pd.DataFrame(resultado_6).head())
# print(pd.DataFrame(resultado_7).head())
