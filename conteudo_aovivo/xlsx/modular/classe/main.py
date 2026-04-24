from app import DataFrameCleaner, DataFrameFilter, ExcelLoader


def main():
    arquivo_entrada = "entrada.xlsx"
    arquivo_saida = "saida.xlsx"

    loader = ExcelLoader()
    df = loader.carregar_excel(arquivo_entrada).get_df()

    df_limpo = (
        DataFrameCleaner(df)
        .limpar()
        # .criar_colunas(0)
        # .corrigir_coluna_vazia("Nome da coluna")
        .get_df()
    )

    df_filtrado = (
        DataFrameFilter(df_limpo)
        # .filtrar_coluna("Nome da coluna", "valor")
        # .filtrar_coluna_null("Nome da coluna", "valor")
        # .remover_matricula("Nome da coluna")
        .get_df()
    )

    ExcelLoader(df_filtrado).salvar_excel(arquivo_saida)


if __name__ == "__main__":
    main()
