import pandas as pd


relatorio = pd.read_csv("./arquivo.csv")

# Data para busca
col_data = "17/02/2025"

result = []

for index, row in relatorio.iterrows():
    if row["Data de vencimento original"] == col_data:
        print(row["Data de vencimento original"])
        result.append(
            {
                "Nome": row["Nome"],
                "data_vencimento_original": row["Data de vencimento original"],
            }
        )


pd.DataFrame(result).to_csv("resultado_1.csv", index=False)
