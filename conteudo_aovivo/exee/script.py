import pandas as pd

df = pd.read_csv("file.csv")

df = df["cpf"]
print(df)