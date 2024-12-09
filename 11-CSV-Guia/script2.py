import pandas as pd


relatorio = pd.read_csv("./arquivo.csv")

col_nome = "Bitrix"

result = []

for index, row in relatorio.iterrows():
    if row["Nome"] == col_nome and row['Situação'] == "Encerrado":
        result.append(
            {
                "nome": row["Nome"],
                "situacao": row["Situação"],
                "data_vencimento": row['Data de vencimento']
            }
        )

pd.DataFrame(result).to_csv("resultado_2.csv", index=False)