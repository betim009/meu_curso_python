# Explicação completa do `sheet.py`

## Objetivo do script
O arquivo `sheet.py` lê 15 abas do arquivo `epitopes.xlsx`, filtra os melhores resultados por alelo e gera dois arquivos:

1. `alelos_filtrados.xlsx`  
Arquivo consolidado em uma aba única (`resultado_unico`) com os dados filtrados.
2. `alelos_percentile_colunas.xlsx`  
Arquivo no formato "matriz", onde cada coluna é um `allele` e os valores são `netmhciipan_el percentile`.

---

## Código e lógica, linha a linha

### `import pandas as pd`
- Importa a biblioteca `pandas`.
- `pd` é o alias usado para chamar funções como `pd.read_excel`, `pd.concat`, etc.

### `if __name__ == "__main__":`
- Garante que o bloco principal só rode quando o arquivo for executado diretamente (`python3 sheet.py`).
- Evita execução automática caso o arquivo seja importado por outro módulo.

### `resultados = []`
- Cria uma lista vazia para armazenar o resultado filtrado de cada aba.

### `for i in range(15):`
- Loop de `0` até `14` (15 iterações).
- Cada valor de `i` representa o índice de uma aba do Excel.

### `df_sheet = pd.read_excel("epitopes.xlsx", sheet_name=i)`
Método: `pd.read_excel(...)`
- Lê uma aba do Excel e retorna um `DataFrame`.

Parâmetros usados:
- `"epitopes.xlsx"`: caminho/nome do arquivo de entrada.
- `sheet_name=i`: seleciona a aba pelo índice numérico atual do loop.

### Bloco de filtro principal
```python
df_resultado = (
    df_sheet.sort_values("netmhciipan_el percentile")
    .drop_duplicates(subset="allele", keep="first")
    .reset_index(drop=True)
)
```

#### `sort_values("netmhciipan_el percentile")`
Método: `DataFrame.sort_values(by, ...)`
- Ordena do menor para o maior valor de `netmhciipan_el percentile`.
- Como menor percentile costuma ser melhor, o melhor fica primeiro por alelo.

Parâmetro usado:
- `"netmhciipan_el percentile"`: coluna usada para ordenação (`by`).

#### `drop_duplicates(subset="allele", keep="first")`
Método: `DataFrame.drop_duplicates(...)`
- Remove linhas duplicadas considerando apenas a coluna `allele`.
- Mantém a primeira ocorrência de cada alelo.
- Como já foi ordenado antes, essa primeira ocorrência é o menor percentile daquele alelo.

Parâmetros usados:
- `subset="allele"`: coluna usada para detectar duplicidade.
- `keep="first"`: mantém a primeira linha encontrada de cada grupo.

#### `reset_index(drop=True)`
Método: `DataFrame.reset_index(...)`
- Reorganiza o índice do DataFrame para `0, 1, 2, ...`.
- Evita carregar índices antigos após ordenação/remoção de duplicatas.

Parâmetro usado:
- `drop=True`: descarta o índice anterior em vez de virar uma coluna.

### `df_resultado["origem_sheet"] = i`
- Cria a coluna `origem_sheet` informando de qual aba cada linha veio.

### `resultados.append(df_resultado)`
- Adiciona o DataFrame filtrado da aba atual à lista `resultados`.

### `df_final = pd.concat(resultados, ignore_index=True)`
Método: `pd.concat(...)`
- Junta todos os DataFrames da lista em um DataFrame único (linhas empilhadas).

Parâmetros usados:
- `resultados`: sequência de DataFrames a combinar.
- `ignore_index=True`: cria índice novo contínuo no DataFrame final.

### `df_final.to_excel("alelos_filtrados.xlsx", sheet_name="resultado_unico", index=False)`
Método: `DataFrame.to_excel(...)`
- Salva o consolidado em Excel.

Parâmetros usados:
- `"alelos_filtrados.xlsx"`: arquivo de saída.
- `sheet_name="resultado_unico"`: nome da aba gerada.
- `index=False`: não escreve a coluna de índice no arquivo.

---

## Segunda etapa: transformar em colunas por alelo

### `df_gerado = pd.read_excel("alelos_filtrados.xlsx", sheet_name="resultado_unico")`
- Lê o arquivo consolidado recém-gerado.
- Usa especificamente a aba `resultado_unico`.

### `df_pivot = df_gerado[["allele", "netmhciipan_el percentile"]].copy()`
- Seleciona apenas as duas colunas necessárias para a matriz.
- `.copy()` evita efeitos colaterais no DataFrame original.

### `df_pivot["ordem"] = df_pivot.groupby("allele").cumcount()`
Métodos: `groupby(...)` + `cumcount()`
- Agrupa por `allele`.
- `cumcount()` cria uma contagem crescente dentro de cada grupo: `0,1,2,...`.
- Essa coluna `ordem` é necessária para montar linhas na pivot sem perder valores repetidos por alelo.

Parâmetro usado:
- `"allele"` no `groupby`: define o agrupamento por alelo.

### Bloco de pivot
```python
df_saida = (
    df_pivot.pivot(
        index="ordem",
        columns="allele",
        values="netmhciipan_el percentile",
    )
    .reset_index(drop=True)
)
```

#### `pivot(index="ordem", columns="allele", values="netmhciipan_el percentile")`
Método: `DataFrame.pivot(...)`
- Converte linhas em colunas.
- Cada valor único de `allele` vira nome de coluna.
- Os valores preenchidos nessas colunas vêm de `netmhciipan_el percentile`.
- As linhas são organizadas por `ordem` (0,1,2... por alelo).

Parâmetros usados:
- `index="ordem"`: define a estrutura das linhas.
- `columns="allele"`: define os nomes das colunas de saída.
- `values="netmhciipan_el percentile"`: define os valores que entram na matriz.

#### `.reset_index(drop=True)`
- Remove o índice `ordem` da saída final para deixar apenas as colunas dos alelos.

### `df_saida.to_excel("alelos_percentile_colunas.xlsx", index=False)`
- Salva o arquivo final no formato desejado.
- `index=False` evita escrever índice auxiliar no Excel.

---

## Resumo da regra de negócio aplicada
1. Para cada uma das 15 abas:
   - ordenar por `netmhciipan_el percentile` (menor primeiro),
   - manter só a melhor linha de cada `allele`.
2. Consolidar tudo em `alelos_filtrados.xlsx`.
3. Transformar o consolidado em matriz:
   - colunas = `allele`,
   - valores = `netmhciipan_el percentile`,
   - salvar em `alelos_percentile_colunas.xlsx`.

## Como executar
```bash
python3 sheet.py
```
