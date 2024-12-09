import pandas as pd


relatorio = pd.read_csv("./arquivo.csv")

col_nome = "GNRE"

result = []

for index, row in relatorio.iterrows():
    if row["Nome"] == col_nome:
        result.append(
            {
                "nome": row["Nome"],
                "situacao": row["Situação"],
            }
        )

pd.DataFrame(result).to_csv("resultado_2.csv", index=False)