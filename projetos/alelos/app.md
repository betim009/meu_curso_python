# Documentação da lógica (`app.py`)

## Objetivo
Ler a planilha `epitopes.xlsx` e, para cada `allele` repetido, manter apenas a linha com o menor valor na coluna `netmhciipan_el percentile`.

## Fluxo da solução
1. **Leitura dos dados**
   - O arquivo Excel é carregado com `pd.read_excel("epitopes.xlsx")`.
   - Resultado armazenado em `df_sheet1`.

2. **Ordenação pelo critério de melhor valor**
   - `sort_values("netmhciipan_el percentile")` ordena de forma crescente.
   - Assim, o menor `percentile` de cada `allele` fica primeiro.

3. **Remoção de duplicados por `allele`**
   - `drop_duplicates(subset="allele", keep="first")` remove repetições de `allele`.
   - Como o DataFrame já está ordenado, `keep="first"` preserva a linha com o menor `percentile`.

4. **Reorganização do índice**
   - `reset_index(drop=True)` recria o índice para `0, 1, 2, ...`.
   - `drop=True` evita que o índice antigo vire coluna.

5. **Saída**
   - O DataFrame final (`df_resultado`) é exibido com `print(df_resultado)`.

## Resumo da regra aplicada
Para cada `allele`, a linha selecionada é a que possui o menor valor em `netmhciipan_el percentile`.
