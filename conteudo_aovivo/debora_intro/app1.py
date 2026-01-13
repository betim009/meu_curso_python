import pandas as pd

file = pd.read_csv("file.csv")

print(file.head(2)) # exibe apenas as duas primeiras linhas
print(file.max())
print(file.min())

print(file.info())

print(file.describe())