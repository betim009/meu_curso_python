from main import *
import pandas as pd

if __name__ == "__main__":
    instancia_df = load_excel("quadro_janeiro.xlsx", 2, None, False, str)

    # 1o Limpando e gerando novo arquivo
    # instancia_df = clean_xlsx(instancia_df)
    # instancia_df = create_cols(instancia_df, 1)
    # create_xlsx(instancia_df, "arquivo_limpo.xlsx")

    # globais:
    df = load_excel_limpo("arquivo_limpo.xlsx")
    

    # 2o a) coluna função pegar só operador
    # df = load_excel_limpo("arquivo_limpo.xlsx")
    # filtro_funcao = filtrar_coluna(df, "FUNCAO", "OPERADOR")
    # create_xlsx(filtro_funcao, "filtro_funcao.xlsx")

    # 3o b) desligamento coloca o filtro pra manter tudo o que é vazio e pegar também o que é do mês vigente
    df_corrigido = corrigir_coluna_vazia_xlsx(df, "DT_DESLIGAMENTO", "arquivo_limpo.xlsx")
    filtro_funcao = filtrar_coluna(df, "DT_DESLIGAMENTO", "2026-01")
    create_xlsx(filtro_funcao, "filtro_dtDesligamento.xlsx")
    