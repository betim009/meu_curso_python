import pandas as pd

df = pd.read_csv("arquivo.csv")

# Filtros com recursos do pandas
f_simples = df["categoria"] == "Alimentos" # Simples
f_alimentos = df["categoria"].str.contains("alimentos", case=False, na=False) # Avancado
f_preco = df["preco_unitario"] >= 19
f_eletronicos = df["categoria"].str.contains("eletronicos", case=False, na=False)
f_online = df["canal"] == "Online"
f_sp = df["estado"] == "SP"
f_desconto = df["desconto_pct"] > 0
f_quantidade = df["quantidade"] >= 15
f_loja_fisica = df["canal"] == "Loja Fisica"

# Gerando os DataFrames
resultado = df[f_simples]
resultado_1 = df[f_alimentos]
resultado_2 = df[f_alimentos & f_preco] # Dois filtros com AND
resultado_3 = df[f_alimentos | f_preco] # Dois filtros com OR
resultado_4 = df[f_eletronicos & f_online] # Eletronicos vendidos no online
resultado_5 = df[f_sp & f_desconto] # Pedidos de SP com desconto
resultado_6 = df[f_quantidade & f_loja_fisica] # Vendas em volume na loja fisica
resultado_7 = df[(f_eletronicos & f_preco) | (f_alimentos & f_desconto)] # Combinacao simples

# Exibindo Resultados
print(resultado.head()) 
# print(resultado_1.head()) 
# print(resultado_2.head()) 
# print(resultado_3.head()) 
# print(resultado_4.head()) 
# print(resultado_5.head()) 
# print(resultado_6.head()) 
# print(resultado_7.head()) 
