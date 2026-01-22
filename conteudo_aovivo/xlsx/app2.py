import pandas as pd

arquivo = pd.read_excel(
    "quadro_janeiro.xlsx",
    sheet_name=2,
    header=None,
    keep_default_na=False,
    dtype=str,
)

linha_das_colunas = arquivo.iloc[1]
arquivo.columns = linha_das_colunas
arquivo = arquivo[2:]

col_deslig = "DT_DESLIGAMENTO"

# converte para data com segurança (valores inválidos viram NaT)
datas = pd.to_datetime(arquivo[col_deslig], errors="coerce")
mask_blank = arquivo[col_deslig].astype(str).str.strip().eq("")

# filtro: janeiro/2026 ou vazio
filtro = ((datas.dt.month == 1) & (datas.dt.year == 2026)) | mask_blank

arquivo = arquivo[filtro]

arquivo.to_excel("dt_desligamento_1.xlsx")
print(arquivo)
