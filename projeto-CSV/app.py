import pandas as pd

registros = pd.read_csv("./planilhas/registros.csv")

zona_sul = 0
resgistros_sul = []
nomes = []

# Estou percorrendo todas as linhas da planilha registros.csv
for index, row in registros.iterrows():
    # Verificando se existe "Sul" na coluna "zona"
    if "Sul" in row["zona"]:
        if row["paciente"] not in nomes:
            zona_sul += 1
            resgistros_sul.append({"id": zona_sul, "nome": row["paciente"]})
        nomes.append(row["paciente"])


pd.DataFrame(resgistros_sul).to_csv('./planilhas/zona_sul.csv')
