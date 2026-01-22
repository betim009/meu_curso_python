import pandas as pd

arquivo = pd.read_excel("quadro_janeiro.xlsx", sheet_name=2, header=None)
# print(arquivo.head(2))

linha_das_colunas = arquivo.iloc[1]
arquivo.columns = linha_das_colunas
arquivo = arquivo[2:]

# print(linha_das_colunas.head(5))
# print(arquivo.head(5))
# print(arquivo["FUNCAO"].head(5))

filtro_operador = arquivo["FUNCAO"].str.contains("OPERADOR", case=False, na=False)
arquivo_operador = arquivo[filtro_operador]
arquivo_operador.to_excel("quadro_funcao.xlsx", index=False)

print(filtro_operador.head(5))
print(arquivo_operador.head(5))

col_funcao_filtro = arquivo_operador[["FUNCAO"]]
col_funcao_filtro.to_excel("quadro_coluna_funcao.xlsx", index=False)

print(col_funcao_filtro)