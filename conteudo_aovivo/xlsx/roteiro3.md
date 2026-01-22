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

3. Este trecho normaliza a coluna `NOME SOCIAL`, tratando vazio e “-” como ausente.
```py
col_social = "NOME SOCIAL"
col_func = "FUNCIONARIO"

arquivo[col_social] = arquivo[col_social].astype(str).str.strip()
mask_vazio = arquivo[col_social].eq("") | arquivo[col_social].eq("-")
```

4. Este trecho preenche `NOME SOCIAL` com `FUNCIONARIO` quando o nome social estiver vazio e salva o resultado em Excel.
```py
arquivo.loc[mask_vazio, col_social] = arquivo.loc[mask_vazio, col_func]

arquivo.to_excel("nomes.xlsx", index=False)
```
