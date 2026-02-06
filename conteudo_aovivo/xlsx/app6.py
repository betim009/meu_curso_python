import pandas as pd

arquivo = pd.read_excel(
    "quadro_janeiro.xlsx",
    sheet_name=2,
    header=None,
    keep_default_na=False,
    dtype=str,
)

linha_das_colunas = arquivo.iloc[1].astype(str).str.strip()
arquivo.columns = linha_das_colunas
arquivo = arquivo[2:].copy()

linhas = []
for i, row in arquivo.iterrows():
    col_deslig = row["DT_DESLIGAMENTO"]
    try:
        if pd.isna(col_deslig) or str(col_deslig).strip() == "":
            linhas.append(row)
            continue

        year = str(col_deslig).split("-")[0]
        mounth = str(col_deslig).split("-")[1]

        if year == "2025" and mounth == "01":
            linhas.append(row)


    except Exception:
        continue

dataFrame = pd.DataFrame(linhas, columns=arquivo.columns)

# salva em um novo arquivo
dataFrame.to_excel("arquivo_dt.xlsx", index=False)
