import pandas as pd

arquivo = pd.read_excel("quadro_janeiro.xlsx", sheet_name=2, header=None)
# print(arquivo.head(2))

linha_das_colunas = arquivo.iloc[1]
arquivo.columns = linha_das_colunas
arquivo = arquivo[2:]


for i, row in arquivo.iterrows():
    supervisor = row["SUPERVISOR"]
    
    if (
        not pd.isna(supervisor)
        and str(supervisor).strip() not in ["", "-"] 
    ):
        try:
            nome_supervisor = str(supervisor).split(",")[1]
            arquivo.at[i, "SUPERVISOR"] = nome_supervisor
        except Exception as e :
            print(e)
        

arquivo.to_csv("supervisores.csv")
        