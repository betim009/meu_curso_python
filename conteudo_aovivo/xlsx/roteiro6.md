### Comecando

1. Este trecho importa o pandas e lê a terceira aba (índice 2) do arquivo `quadro_janeiro.xlsx` mantendo os dados como texto.
```py
import pandas as pd

arquivo = pd.read_excel(
    "quadro_janeiro.xlsx",
    sheet_name=2,
    header=None,
    keep_default_na=False,
    dtype=str,
)
```

2. Este trecho usa a segunda linha (índice 1) como cabeçalho, redefine as colunas do DataFrame com essa linha e remove as duas primeiras linhas de dados.
```py
linha_das_colunas = arquivo.iloc[1].astype(str).str.strip()
arquivo.columns = linha_das_colunas
arquivo = arquivo[2:].copy()
```

3. Este trecho percorre as linhas e seleciona quem tem `DT_DESLIGAMENTO` vazio ou com data em janeiro de 2025.
```py
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
```

4. Este trecho cria um novo DataFrame com as linhas filtradas e salva o resultado em Excel.
```py
dataFrame = pd.DataFrame(linhas, columns=arquivo.columns)

dataFrame.to_excel("arquivo_dt.xlsx", index=False)
```
