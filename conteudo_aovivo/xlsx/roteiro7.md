### Introducao

Neste roteiro, o objetivo e tratar valores vazios de uma coluna especifica da planilha e padronizar esses casos com `-`. Esse tipo de ajuste e comum quando precisamos entregar dados mais consistentes para relatorios, importacoes ou validacoes futuras.

A logica do script segue um fluxo simples: ler a aba correta, ajustar o cabecalho real, validar a existencia da coluna, preencher vazios e exportar o resultado para outro arquivo.

### Comecando

1. Este trecho importa a biblioteca pandas e declara a funcao principal.
```py
import pandas as pd


def corrigir_coluna_vazia(coluna, arquivo_saida):
```
Detalhes:
- `import pandas as pd`: importa o pandas com o alias `pd`, padrao de mercado para facilitar a escrita.
- `def corrigir_coluna_vazia(coluna, arquivo_saida):`: cria uma funcao reutilizavel.
- `coluna`: parametro com o nome exato da coluna que sera tratada.
- `arquivo_saida`: parametro com o caminho/nome do arquivo Excel de saida.

2. Este trecho le a terceira aba do arquivo Excel original.
```py
    arquivo = pd.read_excel(
        "quadro_janeiro.xlsx",
        sheet_name=2,
        header=None,
        keep_default_na=False,
        dtype=str,
    )
```
Detalhes:
- `pd.read_excel(...)`: metodo do pandas para leitura de arquivos `.xlsx`.
- `"quadro_janeiro.xlsx"`: arquivo de entrada.
- `sheet_name=2`: seleciona a aba de indice 2 (terceira aba).
- `header=None`: informa que nenhuma linha deve ser usada automaticamente como cabecalho.
- `keep_default_na=False`: impede conversao automatica de certos textos para valores nulos.
- `dtype=str`: forca todas as colunas para texto, evitando diferencas de tipo na comparacao.
- `arquivo`: variavel que recebe o DataFrame carregado.

3. Este trecho define o cabecalho real com base na segunda linha e remove as linhas tecnicas iniciais.
```py
    linha_das_colunas = arquivo.iloc[1]
    arquivo.columns = linha_das_colunas
    arquivo = arquivo[2:]
```
Detalhes:
- `arquivo.iloc[1]`: pega a linha de indice 1 por posicao (segunda linha).
- `arquivo.columns = ...`: substitui os nomes de colunas atuais por essa linha.
- `arquivo = arquivo[2:]`: remove as duas primeiras linhas (indices 0 e 1).

4. Este trecho valida se a coluna informada existe no DataFrame.
```py
    if coluna not in arquivo.columns:
        raise ValueError(f"Coluna '{coluna}' nao encontrada.")
```
Detalhes:
- `arquivo.columns`: objeto com todos os nomes de colunas.
- `if coluna not in ...`: verifica existencia antes de processar.
- `raise ValueError(...)`: interrompe a execucao com mensagem clara se a coluna nao existir.

5. Este trecho percorre as linhas e preenche com `-` os valores nulos ou vazios.
```py
    for index, row in arquivo.iterrows():
        col = row[coluna]
        if pd.isna(col) or str(col).strip() == "":
            arquivo.at[index, coluna] = "-"
```
Detalhes:
- `arquivo.iterrows()`: itera linha a linha retornando indice e conteudo da linha.
- `row[coluna]`: acessa o valor da coluna desejada na linha atual.
- `pd.isna(col)`: identifica valor nulo real (`NaN`, `None`, `pd.NA`).
- `str(col).strip() == ""`: detecta strings vazias ou com apenas espacos.
- `arquivo.at[index, coluna] = "-"`: atualiza uma celula especifica por indice/coluna.

6. Este trecho salva o resultado tratado em um novo arquivo Excel.
```py
    arquivo.to_excel(arquivo_saida, index=False)
```
Detalhes:
- `to_excel(...)`: exporta o DataFrame para `.xlsx`.
- `arquivo_saida`: nome/caminho definido por parametro.
- `index=False`: nao grava o indice do DataFrame como coluna no arquivo final.

7. Este trecho executa a funcao para a coluna `NOME SOCIAL`.
```py
corrigir_coluna_vazia("NOME SOCIAL", "NOMESOCIAL.xlsx")
```
Detalhes:
- `"NOME SOCIAL"`: coluna alvo para preenchimento dos vazios.
- `"NOMESOCIAL.xlsx"`: arquivo que recebera o resultado.

8. Codigo completo:
```py
import pandas as pd


def corrigir_coluna_vazia(coluna, arquivo_saida):
    arquivo = pd.read_excel(
        "quadro_janeiro.xlsx",
        sheet_name=2,
        header=None,
        keep_default_na=False,
        dtype=str,
    )

    linha_das_colunas = arquivo.iloc[1]
    arquivo.columns = linha_das_colunas
    arquivo = arquivo[2:]

    if coluna not in arquivo.columns:
        raise ValueError(f"Coluna '{coluna}' nao encontrada.")

    for index, row in arquivo.iterrows():
        col = row[coluna]
        if pd.isna(col) or str(col).strip() == "":
            arquivo.at[index, coluna] = "-"

    arquivo.to_excel(arquivo_saida, index=False)


corrigir_coluna_vazia("NOME SOCIAL", "NOMESOCIAL.xlsx")
```
