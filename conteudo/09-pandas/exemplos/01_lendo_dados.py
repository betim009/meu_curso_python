import pandas as pd
from pathlib import Path

CAMINHO_DADOS = Path(__file__).resolve().parents[1] / "dados" / "vendas.csv"

df = pd.read_csv(CAMINHO_DADOS)

print("Primeiras linhas:")
print(df.head())

print("\nQuantidade de linhas e colunas:")
print(df.shape)

print("\nColunas:")
print(df.columns)

print("\nResumo tecnico:")
print(df.info())
