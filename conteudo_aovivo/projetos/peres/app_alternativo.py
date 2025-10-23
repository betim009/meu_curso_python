import pandas as pd

df = pd.read_csv("atletas_exportistas.csv")

contagens = df["esporte"].value_counts()

print(contagens)
