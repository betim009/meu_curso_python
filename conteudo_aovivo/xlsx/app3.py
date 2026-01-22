import pandas as pd

arquivo = pd.read_excel(
    "quadro_janeiro.xlsx",
    sheet_name=2,
    header=None,
    keep_default_na=False,
    dtype=str,
)
# print(arquivo.head(2))

linha_das_colunas = arquivo.iloc[1]
arquivo.columns = linha_das_colunas
arquivo = arquivo[2:]

col_social = "NOME SOCIAL"
col_func = "FUNCIONARIO"

arquivo[col_social] = arquivo[col_social].astype(str).str.strip()
mask_vazio = arquivo[col_social].eq("") | arquivo[col_social].eq("-")
arquivo.loc[mask_vazio, col_social] = arquivo.loc[mask_vazio, col_func]

arquivo.to_excel("nomes.xlsx", index=False)
