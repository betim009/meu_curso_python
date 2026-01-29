### Comecando

1. Este trecho importa o pandas e lê a terceira aba (índice 2) do arquivo `quadro_janeiro.xlsx`, mantendo tudo como texto para não alterar os valores das colunas.
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
linha_das_colunas = arquivo.iloc[1]
arquivo.columns = linha_das_colunas
arquivo = arquivo[2:]
```

3. Este trecho converte a coluna `DT_DESLIGAMENTO` para data com segurança, cria um filtro para janeiro/2026 ou vazio e aplica o filtro no DataFrame.
```py
col_deslig = "DT_DESLIGAMENTO"

datas = pd.to_datetime(arquivo[col_deslig], errors="coerce")
mask_blank = arquivo[col_deslig].astype(str).str.strip().eq("")

filtro = ((datas.dt.month == 1) & (datas.dt.year == 2026)) | mask_blank
arquivo = arquivo[filtro]
```

4. Este trecho imprime o resultado final.
```py
print(arquivo)
```
