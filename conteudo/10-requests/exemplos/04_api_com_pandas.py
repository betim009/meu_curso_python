import pandas as pd
import requests

url = "https://dummyjson.com/products?limit=10"

resposta = requests.get(url, timeout=10)
resposta.raise_for_status()

dados = resposta.json()
produtos = dados["products"]

df = pd.DataFrame(produtos)

print(df[["title", "category", "price", "stock"]])

preco_medio = df["price"].mean()
estoque_total = df["stock"].sum()

print(f"\nPreco medio: US$ {preco_medio:.2f}")
print(f"Estoque total: {estoque_total}")
