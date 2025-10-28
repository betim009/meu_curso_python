import pandas as pd

df = pd.read_csv("nomes.csv")


for index, row in df.iterrows():
    print(row["nome"], row["idade"])