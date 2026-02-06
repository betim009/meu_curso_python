### Comecando

1. Este trecho importa o pandas e lê a terceira aba (índice 2) do arquivo `quadro_janeiro.xlsx`.
```py
import pandas as pd

arquivo = pd.read_excel("quadro_janeiro.xlsx", sheet_name=2, header=None)
```

2. Este trecho usa a segunda linha (índice 1) como cabeçalho, redefine as colunas do DataFrame com essa linha e remove as duas primeiras linhas de dados.
```py
linha_das_colunas = arquivo.iloc[1].astype(str).str.strip()
arquivo.columns = linha_das_colunas
arquivo = arquivo[2:].copy()
```

3. Este trecho percorre as linhas e seleciona apenas quem tem `FUNCAO` contendo "OPERADOR" (ignorando maiúsculas e espaços).
```py
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
```

4. Este trecho cria um novo DataFrame com as linhas filtradas e salva o resultado em Excel.
```py
operadores = pd.DataFrame(linhas, columns=arquivo.columns)

operadores.to_excel("funcoes_operador.xlsx", index=False)
```
