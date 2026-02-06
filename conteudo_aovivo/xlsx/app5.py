import pandas as pd

arquivo = pd.read_excel("quadro_janeiro.xlsx", sheet_name=2, header=None)

linha_das_colunas = arquivo.iloc[1].astype(str).str.strip()
arquivo.columns = linha_das_colunas
arquivo = arquivo[2:].copy()

# usando for para coletar linhas com FUNCAO == "OPERADOR"
linhas = []
for i, row in arquivo.iterrows():
    funcao = row["FUNCAO"]
    try:
        if pd.isna(funcao):
            continue
        if "OPERADOR" in str(funcao).upper():
            linhas.append(row)
    except Exception:
        continue

operadores = pd.DataFrame(linhas, columns=arquivo.columns)

# salva em um novo arquivo
operadores.to_excel("funcoes_operador.xlsx", index=False)
