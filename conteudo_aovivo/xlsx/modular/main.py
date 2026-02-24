import pandas as pd

def load_excel(file, sheet=0, header=None, clean=False, type=str):
    data_frame = pd.read_excel(
        file,
        sheet_name=sheet,
        header=header,
        keep_default_na=clean,
        dtype=type,
    )

    return data_frame

def load_csv(file, type_spe=","):
    data_frame = pd.read_csv(file, sep=type_spe)
    return data_frame

def create_xlsx(df, name_file):
    return df.to_excel(name_file, index=False)

def clean_xlsx(df):
    data_frame = df.apply(lambda coluna: coluna.str.strip())
    data_frame = data_frame.replace({"": pd.NA, "-": pd.NA, "nan": pd.NA, "None": pd.NA})
    data_frame = data_frame.dropna(how="all")

    return data_frame

def create_cols(data_frame, index_col):
    linha_das_colunas = data_frame.iloc[index_col]
    data_frame.columns = linha_das_colunas
    data_frame = data_frame[index_col+1:]

    return data_frame

def corrigir_coluna_vazia_xlsx(df, coluna, name_file):
    colunas = df.iloc[0]
    df.colums = colunas
    if coluna not in df.columns:
        raise ValueError(f"Coluna '{coluna}' nao encontrada.")

    for index, row in df.iterrows():
        col = row[coluna]
        if pd.isna(col) or str(col).strip() == "":
            df.at[index, coluna] = "-"

    df.to_excel(name_file, index=False)
    

if __name__ == "__main__":
    instancia_df = load_excel(
        "quadro_janeiro.xlsx",
        2,
        None,
        False,
        str
    )

    instancia_df = clean_xlsx(instancia_df)
    instancia_df = create_cols(instancia_df, 1)

    create_xlsx(instancia_df, "arquivo_limpo.xlsx")
    df_corrigido = corrigir_coluna_vazia_xlsx(instancia_df, "NOME SOCIAL","arquivo_limpo.xlsx")
    df_corrigido = corrigir_coluna_vazia_xlsx(instancia_df, "ONDA ORIGINAL","arquivo_limpo.xlsx")