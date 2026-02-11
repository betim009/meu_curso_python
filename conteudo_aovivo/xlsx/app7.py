import pandas as pd


def corrigir_coluna_vazia(coluna, arquivo_entrada, arquivo_saida):
    arquivo = pd.read_excel(
        arquivo_entrada,
        # sheet_name=2,
        header=None,
        keep_default_na=False,
        dtype=str,
    )

    linha_das_colunas = arquivo.iloc[1]
    arquivo.columns = linha_das_colunas
    arquivo = arquivo[2:]

    if coluna not in arquivo.columns:
        raise ValueError(f"Coluna '{coluna}' nao encontrada.")

    for index, row in arquivo.iterrows():
        col = row[coluna]
        if pd.isna(col) or str(col).strip() == "":
            arquivo.at[index, coluna] = "-"

    arquivo.to_excel(arquivo_saida, index=False)


corrigir_coluna_vazia("SUPERVISOR", "arquivo_limpo1.xlsx", "arquivo_limpo1.xlsx")
# corrigir_coluna_vazia("EMAIL", "ex_1.xlsx")
# corrigir_coluna_vazia("DT_AFASTAMENTO", "ex_1.xlsx")

