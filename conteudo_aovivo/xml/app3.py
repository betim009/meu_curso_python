import pandas as pd


df = pd.read_csv("exemplo.csv")

# coluna
coluna_cidade = df["cidade"]

rio_janeiro = df[coluna_cidade == "rj"]
