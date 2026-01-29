### Comecando

1. Este trecho importa o pandas e lê a terceira aba (índice 2) do arquivo `quadro_janeiro.xlsx`.
```py
import pandas as pd

arquivo = pd.read_excel("quadro_janeiro.xlsx", sheet_name=2, header=None)
```

2. Este trecho usa a segunda linha (índice 1) como cabeçalho, redefine as colunas do DataFrame com essa linha e remove as duas primeiras linhas de dados.
```py
linha_das_colunas = arquivo.iloc[1]
arquivo.columns = linha_das_colunas
arquivo = arquivo[2:]
```

3. Este trecho percorre as linhas, valida a coluna `SUPERVISOR` e tenta extrair o nome depois da vírgula.
```py
for i, row in arquivo.iterrows():
    supervisor = row["SUPERVISOR"]
    
    if (
        not pd.isna(supervisor)
        and str(supervisor).strip() not in ["", "-"] 
    ):
        try:
            nome_supervisor = str(supervisor).split(",")[1]
            arquivo.at[i, "SUPERVISOR"] = nome_supervisor
        except Exception as e :
            print(e)
```

4. Este trecho salva o resultado em CSV.
```py
arquivo.to_csv("supervisores.csv")
```
