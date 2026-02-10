import pandas as pd


def corrigir_coluna_vazia(coluna, arquivo_saida):
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

    if coluna not in arquivo.columns:
        raise ValueError(f"Coluna '{coluna}' nao encontrada.")

    for index, row in arquivo.iterrows():
        col = row[coluna]
        if pd.isna(col) or str(col).strip() == "":
            arquivo.at[index, coluna] = "-"

    arquivo.to_excel(arquivo_saida, index=False)


corrigir_coluna_vazia("NOME SOCIAL", "NOMESOCIAL.xlsx")
