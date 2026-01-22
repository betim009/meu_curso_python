### Comecando

1. Este trecho importa o pandas, lê a terceira aba (índice 2) do arquivo `quadro_janeiro.xlsx` sem considerar cabeçalho e, em seguida, imprime as 5 primeiras linhas do DataFrame resultante.
```py
import pandas as pd

arquivo = pd.read_excel("quadro_janeiro.xlsx", sheet_name=2, header=None)
print(arquivo.head(5))
```


2. Este trecho usa a segunda linha (índice 1) como cabeçalho, redefine as colunas do DataFrame com essa linha, remove as duas primeiras linhas de dados e imprime amostras das colunas, do DataFrame e da coluna "FUNCAO".
```py
linha_das_colunas = arquivo.iloc[1]
arquivo.columns = linha_das_colunas
arquivo = arquivo[2:]

print(linha_das_colunas.head(5))
print(arquivo.head(5))
print(arquivo["FUNCAO"].head(5))

```

3. Este trecho cria um filtro booleano para linhas cuja coluna "FUNCAO" contém "OPERADOR" (sem diferenciar maiúsculas/minúsculas e ignorando valores nulos), filtra o DataFrame e salva o resultado em um novo Excel.
```py
filtro_operador = arquivo["FUNCAO"].str.contains("OPERADOR", case=False, na=False)
arquivo_operador = arquivo[filtro_operador]
arquivo_operador.to_excel("quadro_funcao.xlsx", index=False)

print(filtro_operador.head(5))
print(arquivo_operador.head(5))
```

4. Este trecho seleciona apenas a coluna "FUNCAO" do DataFrame filtrado e salva essa coluna em um novo arquivo Excel.
```py
col_funcao_filtro = arquivo_operador[["FUNCAO"]]
col_funcao_filtro.to_excel("quadro_coluna_funcao.xlsx", index=False)

print(col_funcao_filtro)
```

5. Codigo completo:
```py
import pandas as pd

arquivo = pd.read_excel("quadro_janeiro.xlsx", sheet_name=2, header=None)


linha_das_colunas = arquivo.iloc[1]
arquivo.columns = linha_das_colunas
arquivo = arquivo[2:]

filtro_operador = arquivo["FUNCAO"].str.contains("OPERADOR", case=False, na=False)
arquivo_operador = arquivo[filtro_operador]
arquivo_operador.to_excel("quadro_funcao.xlsx", index=False)


col_funcao_filtro = arquivo_operador[["FUNCAO"]]
col_funcao_filtro.to_excel("quadro_coluna_funcao.xlsx", index=False)
```