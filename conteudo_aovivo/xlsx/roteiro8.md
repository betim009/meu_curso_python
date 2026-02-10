### Comecando

1. Este trecho importa o pandas e cria a função para limpar o arquivo.
```py
import pandas as pd

def limpar_arquivo(nome_arquivo, arquivo_saida):
```

2. Este trecho lê a terceira aba (índice 2) do Excel de entrada, mantendo os dados como texto.
```py
    arquivo = pd.read_excel(
        nome_arquivo,
        sheet_name=2,
        header=None,
        keep_default_na=False,
        dtype=str,
    )
```

3. Este trecho remove espaços extras de cada célula para padronizar os dados.
```py
    arquivo = arquivo.apply(lambda coluna: coluna.str.strip())
```

4. Este trecho transforma marcadores de vazio (`""`, `"-"`, `"nan"`, `"None"`) em valor nulo (`pd.NA`).
```py
    arquivo = arquivo.replace({"": pd.NA, "-": pd.NA, "nan": pd.NA, "None": pd.NA})
```

5. Este trecho remove linhas totalmente vazias (todas as colunas nulas).
```py
    arquivo = arquivo.dropna(how="all")
```

6. Este trecho salva o resultado limpo em Excel e executa a função.
```py
    arquivo.to_excel(arquivo_saida, index=False, header=False)


limpar_arquivo("quadro_janeiro.xlsx", "arquivo_limpo.xlsx")
```
