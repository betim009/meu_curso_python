### Comecando

1. Este trecho importa o pandas e define a função que vai corrigir valores vazios de uma coluna específica.
```py
import pandas as pd


def corrigir_coluna_vazia(coluna, arquivo_saida):
```

2. Este trecho lê a terceira aba (índice 2) do arquivo `quadro_janeiro.xlsx` e carrega tudo como texto.
```py
    arquivo = pd.read_excel(
        "quadro_janeiro.xlsx",
        sheet_name=2,
        header=None,
        keep_default_na=False,
        dtype=str,
    )
```

3. Este trecho usa a segunda linha como cabeçalho e remove as duas primeiras linhas da planilha.
```py
    linha_das_colunas = arquivo.iloc[1]
    arquivo.columns = linha_das_colunas
    arquivo = arquivo[2:]
```

4. Este trecho valida se a coluna informada realmente existe no DataFrame.
```py
    if coluna not in arquivo.columns:
        raise ValueError(f"Coluna '{coluna}' nao encontrada.")
```

5. Este trecho percorre a coluna escolhida e substitui valores nulos ou vazios por `-`.
```py
    for index, row in arquivo.iterrows():
        col = row[coluna]
        if pd.isna(col) or str(col).strip() == "":
            arquivo.at[index, coluna] = "-"
```

6. Este trecho salva o resultado em um novo arquivo Excel e executa a função para a coluna `NOME SOCIAL`.
```py
    arquivo.to_excel(arquivo_saida, index=False)


corrigir_coluna_vazia("NOME SOCIAL", "NOMESOCIAL.xlsx")
```
