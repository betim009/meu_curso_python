import pandas as pd
from pathlib import Path

CAMINHO_DADOS = Path(__file__).resolve().parents[1] / "dados" / "vendas_com_problemas.csv"

df = pd.read_csv(CAMINHO_DADOS)

print("Valores ausentes antes da limpeza:")
print(df.isna().sum())

df = df.drop_duplicates()
df = df.dropna(subset=["cliente", "produto", "preco_unitario"])

df["desconto"] = df["desconto"].fillna(0)
df["vendedor"] = df["vendedor"].fillna("Nao informado")
df["data"] = pd.to_datetime(df["data"], errors="coerce")

df = df[df["quantidade"] > 0]
df["valor_total_recalculado"] = (df["preco_unitario"] * df["quantidade"]) - df["desconto"]

print("\nValores ausentes depois da limpeza:")
print(df.isna().sum())

print("\nDados limpos:")
print(df)
