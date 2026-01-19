import pandas as pd

tabela = pd.read_csv("raw.csv")
b = pd.read_excel("raw.xlsx")

print(tabela.info())
print(tabela.describe())

col_idade = tabela["idade"]

print(
    tabela[col_idade == 30]
)
iguais_30 = tabela[col_idade == 30]
iguais_30.to_csv("iguais_30.csv", index=False)

print(
    tabela[col_idade > 30]
)
maior_30 = tabela[col_idade > 30]
maior_30.to_csv("maior_30.csv", index=False)