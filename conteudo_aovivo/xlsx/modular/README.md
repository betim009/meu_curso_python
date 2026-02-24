# 📘 Documentação — `main.py`

Este arquivo documenta o fluxo principal e as funções presentes em `main.py`, usando como base o estilo de documentação do `loads.md`.

---

# 🔹 Visão Geral

O `main.py` faz o processamento de uma planilha Excel em etapas:

1. Lê uma aba específica do arquivo.
2. Faz limpeza dos dados.
3. Define a linha de colunas.
4. Exporta o resultado para um novo `.xlsx`.
5. Corrige valores vazios em uma coluna específica.

---

# 🔹 Função `load_excel()`

```python
def load_excel(file, sheet=0, header=None, clean=False, type=str):
```

## 📌 Objetivo

Ler arquivo Excel (`.xlsx`) e retornar um `DataFrame`.

## 📂 Parâmetros

- `file` (`str`): nome/caminho do arquivo.
- `sheet` (`int` ou `str`, padrão `0`): aba a ser lida.
- `header` (`int` ou `None`, padrão `None`): linha usada como cabeçalho.
- `clean` (`bool`, padrão `False`): ligado ao `keep_default_na`.
- `type` (tipo Python, padrão `str`): tipo dos dados lidos.

Referência detalhada: `loads.md`.

---

# 🔹 Função `load_csv()`

```python
def load_csv(file, type_spe=","):
```

## 📌 Objetivo

Ler arquivo CSV (`.csv`) e retornar um `DataFrame`.

## 📂 Parâmetros

- `file` (`str`): nome/caminho do arquivo.
- `type_spe` (`str`, padrão `","`): separador do CSV.

Referência detalhada: `loads.md`.

---

# 🔹 Função `create_xlsx()`

```python
def create_xlsx(df, name_file):
```

## 📌 Objetivo

Salvar um `DataFrame` em arquivo Excel sem índice.

## 📂 Parâmetros

- `df` (`DataFrame`): dados a serem exportados.
- `name_file` (`str`): nome/caminho do arquivo de saída.

---

# 🔹 Função `clean_xlsx()`

```python
def clean_xlsx(df):
```

## 📌 Objetivo

Limpar dados do `DataFrame`:

- Remove espaços extras nas strings (`strip`).
- Substitui valores vazios ou inválidos por `pd.NA`.
- Remove linhas totalmente vazias.

## 📂 Parâmetros

- `df` (`DataFrame`): dados de entrada.

## ✅ Retorno

`DataFrame` limpo.

---

# 🔹 Função `create_cols()`

```python
def create_cols(data_frame, index_col):
```

## 📌 Objetivo

Definir os nomes das colunas com base em uma linha do próprio `DataFrame`.

## 📂 Parâmetros

- `data_frame` (`DataFrame`): dados de entrada.
- `index_col` (`int`): índice da linha que contém os nomes das colunas.

## ✅ Retorno

`DataFrame` com colunas ajustadas e sem as linhas anteriores ao cabeçalho real.

---

# 🔹 Função `corrigir_coluna_vazia_xlsx()`

```python
def corrigir_coluna_vazia_xlsx(df, coluna, name_file):
```

## 📌 Objetivo

Verificar uma coluna específica e preencher valores vazios com `"-"`, depois salvar no Excel.

## 📂 Parâmetros

- `df` (`DataFrame`): dados a corrigir.
- `coluna` (`str`): nome da coluna alvo.
- `name_file` (`str`): arquivo de saída.

## ⚠ Observação

No código atual existe `df.colums`, mas o correto no pandas é `df.columns`.

---

# 🔹 Fluxo do Bloco Principal (`if __name__ == "__main__":`)

No bloco principal, o script executa:

1. `load_excel("quadro_janeiro.xlsx", 2, None, False, str)`
2. `clean_xlsx(instancia_df)`
3. `create_cols(instancia_df, 1)`
4. `create_xlsx(instancia_df, "arquivo_limpo.xlsx")`
5. `corrigir_coluna_vazia_xlsx(instancia_df, "NOME SOCIAL", "arquivo_limpo.xlsx")`

---

# 🧠 Resumo

O `main.py` implementa um pipeline de leitura, limpeza, organização e exportação de planilhas com pandas, reutilizando os conceitos de leitura documentados em `loads.md`.
