import pandas as pd

arquivo = pd.read_excel(
        "arquivo_limpo1.xlsx",
        header=None,
        keep_default_na=False,
        dtype=str,
    )

linha_das_colunas = arquivo.iloc[0]
arquivo.columns = linha_das_colunas
arquivo = arquivo[1:]


for i, row in arquivo.iterrows():
    supervisor = row["SUPERVISOR"]

    try:
        nome_supervisor = str(supervisor).split(",")[1]
        arquivo.at[i, "SUPERVISOR"] = nome_supervisor
    except:
        continue
        

arquivo.to_excel("arquivo_limpo1.xlsx")