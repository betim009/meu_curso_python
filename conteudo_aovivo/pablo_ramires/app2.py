import pandas as pd

file = pd.read_csv("raw.csv")

data = []
for index, row in file.iterrows():
    data.append({
        "id": row["id"],
        "nome": row["nome"],
        "genero": row["genero"]
    })

for item in data:
    if item["nome"] == "jean":
        item["nome"] = "Jean"

pd.DataFrame(data).to_csv("new_raw.csv")
        