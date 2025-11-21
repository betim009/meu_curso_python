import pandas as pd


csv = pd.read_csv("exemplo.csv") # DataFrame - Tipo de dado Tabulado

print(csv.loc[csv["data_contrato"] == "23/02/2023"])
print()
print(csv.loc[csv["data_contrato"] != "23/02/2023"])
print()
print(csv["data_contrato"].value_counts())

quantidade_data = csv["data_contrato"].value_counts()
quantidade_data.to_csv("quantidade_data.csv")