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

3. Este trecho define a coluna `DT_DESLIGAMENTO`, cria um filtro de linhas em branco e converte a coluna para datas.
```py
col_deslig = "DT_DESLIGAMENTO"
serie = arquivo[col_deslig]

# em branco (string vazia ou NaN, se existir)
mask_blank = serie.isna() | serie.astype(str).str.strip().eq("")

# mês vigente (mês/dia/ano)
datas = pd.to_datetime(serie)
print(datas)
```

4. Este trecho cria o filtro para o mês vigente, aplica no DataFrame, imprime amostras e salva o resultado em Excel.
```py
hoje = pd.Timestamp.today()
mask_mes_atual = (datas.dt.year == hoje.year) & (datas.dt.month == hoje.month)

filtro = mask_blank | mask_mes_atual
arquivo_filtrado = arquivo[filtro]

print(arquivo_filtrado.head(12))
arquivo_filtrado.to_excel("dt_desligamento.xlsx", index=False)
```
