import pandas as pd

def limpar_arquivo(nome_arquivo, arquivo_saida):
    arquivo = pd.read_excel(
        nome_arquivo,
        sheet_name=2,
        header=None,
        keep_default_na=False,
        dtype=str,
    )

    # Remove espacos e padroniza marcadores de vazio
    arquivo = arquivo.apply(lambda coluna: coluna.str.strip())

    # Trata "", "-" e strings "nan"/"none" como vazio
    arquivo = arquivo.replace({"": pd.NA, "-": pd.NA, "nan": pd.NA, "None": pd.NA})

    # Remove linhas totalmente vazias
    arquivo = arquivo.dropna(how="all")

    # Salva o arquivo de volta
    arquivo.to_excel(arquivo_saida, index=False, header=False)


limpar_arquivo("quadro_janeiro.xlsx", "arquivo_limpo1.xlsx")
