### Introducao

Neste roteiro, o foco e limpeza de dados em planilha: remover espacos desnecessarios, padronizar marcadores de vazio e excluir linhas completamente sem informacao. Esse processo melhora a qualidade da base antes de filtros, analises ou cargas em outros sistemas.

A ideia central e transformar varios formatos de "vazio" em um unico padrao (`pd.NA`) e, depois, eliminar apenas o que realmente nao possui dado algum.

### Comecando

1. Este trecho importa o pandas e define a funcao de limpeza.
```py
import pandas as pd

def limpar_arquivo(nome_arquivo, arquivo_saida):
```
Detalhes:
- `import pandas as pd`: disponibiliza os recursos de manipulacao tabular.
- `def limpar_arquivo(nome_arquivo, arquivo_saida):`: funcao reutilizavel para qualquer arquivo no mesmo padrao.
- `nome_arquivo`: parametro de entrada.
- `arquivo_saida`: parametro para o arquivo final.

2. Este trecho le a terceira aba do Excel informado.
```py
    arquivo = pd.read_excel(
        nome_arquivo,
        sheet_name=2,
        header=None,
        keep_default_na=False,
        dtype=str,
    )
```
Detalhes:
- `pd.read_excel(...)`: leitura de planilha para DataFrame.
- `nome_arquivo`: arquivo recebido por parametro.
- `sheet_name=2`: terceira aba.
- `header=None`: mantem o arquivo sem definir cabecalho automatico.
- `keep_default_na=False`: evita que textos sejam convertidos para nulo sem controle.
- `dtype=str`: forca leitura textual para padronizar o tratamento.

3. Este trecho remove espacos no inicio e no fim de cada celula.
```py
    arquivo = arquivo.apply(lambda coluna: coluna.str.strip())
```
Detalhes:
- `apply(...)`: aplica uma funcao em cada coluna do DataFrame.
- `lambda coluna: ...`: funcao anonima usada para transformar cada coluna.
- `coluna.str.strip()`: remove espacos laterais de cada valor textual.

4. Este trecho padroniza marcadores de vazio para `pd.NA`.
```py
    arquivo = arquivo.replace({"": pd.NA, "-": pd.NA, "nan": pd.NA, "None": pd.NA})
```
Detalhes:
- `replace({...})`: substitui valores com base em um dicionario.
- `""`, `"-"`, `"nan"`, `"None"`: valores tratados como ausencia de informacao.
- `pd.NA`: valor nulo nativo do pandas para dados tabulares.

5. Este trecho remove linhas que ficaram totalmente vazias.
```py
    arquivo = arquivo.dropna(how="all")
```
Detalhes:
- `dropna(...)`: remove linhas/colunas com nulos.
- `how="all"`: remove apenas quando todas as colunas da linha sao nulas.

6. Este trecho salva o resultado limpo em outro arquivo Excel.
```py
    arquivo.to_excel(arquivo_saida, index=False, header=False)
```
Detalhes:
- `to_excel(...)`: exporta o DataFrame.
- `arquivo_saida`: destino informado na chamada.
- `index=False`: nao grava o indice.
- `header=False`: nao grava cabecalho de colunas no arquivo final.

7. Este trecho executa a limpeza do arquivo original.
```py
limpar_arquivo("quadro_janeiro.xlsx", "arquivo_limpo.xlsx")
```
Detalhes:
- `"quadro_janeiro.xlsx"`: entrada.
- `"arquivo_limpo.xlsx"`: saida com dados tratados.

8. Codigo completo:
```py
import pandas as pd

def limpar_arquivo(nome_arquivo, arquivo_saida):
    arquivo = pd.read_excel(
        nome_arquivo,
        sheet_name=2,
        header=None,
        keep_default_na=False,
        dtype=str,
    )

    # Remove espacos e padroniza marcadores de vazio
    arquivo = arquivo.apply(lambda coluna: coluna.str.strip())

    # Trata "", "-" e strings "nan"/"none" como vazio
    arquivo = arquivo.replace({"": pd.NA, "-": pd.NA, "nan": pd.NA, "None": pd.NA})

    # Remove linhas totalmente vazias
    arquivo = arquivo.dropna(how="all")

    # Salva o arquivo de volta
    arquivo.to_excel(arquivo_saida, index=False, header=False)


limpar_arquivo("quadro_janeiro.xlsx", "arquivo_limpo.xlsx")
```
