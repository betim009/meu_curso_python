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
serie = arquivo[col_deslig]
# print(serie.head(12))

# em branco (string vazia ou NaN, se existir)
mask_blank = serie.isna() | serie.astype(str).str.strip().eq("")

# mês vigente (mês/dia/ano)
datas = pd.to_datetime(serie)
print(datas)

hoje = pd.Timestamp.today()
mask_mes_atual = (datas.dt.year == hoje.year) & (datas.dt.month == hoje.month)

filtro = mask_blank | mask_mes_atual
arquivo_filtrado = arquivo[filtro]

print(arquivo_filtrado.head(12))
arquivo_filtrado.to_excel("dt_desligamento.xlsx", index=False)
