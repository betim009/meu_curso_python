

# 📘 Documentação — Funções de Leitura de Arquivos (Pandas)

Este arquivo documenta as funções `load_excel()` e `load_csv()` utilizadas para leitura de arquivos com a biblioteca **pandas**.

---

# 🔹 1️⃣ Função `load_excel()`

```python
def load_excel(file, sheet=0, header=None, clean=False, type=str):
    arquivo = pd.read_excel(
        file,
        sheet_name=sheet,
        header=header,
        keep_default_na=clean,
        dtype=type,
    )

    return arquivo
```

## 📌 Objetivo

Ler arquivos **Excel (.xlsx)** e retornar um `DataFrame`.

---

## 📂 Parâmetro: `file`

**Tipo:** `str`  
**Descrição:** Nome ou caminho do arquivo Excel.

### Exemplo:

```python
load_excel("quadro_janeiro.xlsx")
```

Pode ser:
- Arquivo na mesma pasta
- Caminho relativo (`./dados/arquivo.xlsx`)
- Caminho absoluto (`C:/pasta/arquivo.xlsx`)

---

## 📄 Parâmetro: `sheet`

**Tipo:** `int` ou `str`  
**Padrão:** `0`  

Define qual aba do Excel será lida.

### Exemplos:

```python
sheet=0  # primeira aba
sheet=2  # terceira aba
sheet="Vendas"  # pelo nome da aba
```

⚠ O pandas começa a contagem das abas a partir do zero.

---

## 🏷 Parâmetro: `header`

**Tipo:** `int` ou `None`  
**Padrão:** `None`

Define qual linha será usada como nome das colunas.

### Exemplos:

```python
header=0      # primeira linha vira cabeçalho
header=None   # nenhuma linha é cabeçalho
```

Se for `None`, o pandas cria colunas automáticas:

```
0 | 1 | 2 | 3 | ...
```

---

## 🚫 Parâmetro: `clean`

**Tipo:** `bool`  
**Padrão:** `False`

Internamente controla:

```python
keep_default_na=clean
```

Define se valores vazios serão transformados automaticamente em `NaN`.

### Comportamento:

- `clean=True` → valores vazios viram `NaN`
- `clean=False` → valores vazios permanecem como string vazia

⚠ Observação: O nome `clean` pode gerar confusão, pois a lógica está ligada ao parâmetro `keep_default_na`.

---

## 🔤 Parâmetro: `type`

**Tipo:** tipo Python (ex: `str`, `int`, `float`)  
**Padrão:** `str`

Define o tipo de dado das colunas.

### Exemplo:

```python
type=str
```

Significa:

> Todos os dados serão lidos como texto.

Isso evita erros de conversão automática de tipos.

---

# 🔹 2️⃣ Função `load_csv()`

```python
def load_csv(file, type_spe=","):
    arquivo = pd.read_csv(file, sep=type_spe)
    return arquivo
```

## 📌 Objetivo

Ler arquivos **CSV (.csv)** e retornar um `DataFrame`.

---

## 📂 Parâmetro: `file`

**Tipo:** `str`  
**Descrição:** Nome ou caminho do arquivo CSV.

### Exemplo:

```python
load_csv("dados.csv")
```

---

## 🔀 Parâmetro: `type_spe`

**Tipo:** `str`  
**Padrão:** `","`

Define qual separador o arquivo utiliza.

Internamente:

```python
sep=type_spe
```

---

## 📊 Exemplos comuns

### CSV padrão (vírgula)

```python
load_csv("dados.csv")
```

### CSV brasileiro (ponto e vírgula)

```python
load_csv("dados.csv", ";")
```

---

# 🎯 Comparação Geral

| Função        | Tipo de Arquivo | Complexidade |
|--------------|------------------|--------------|
| load_excel   | .xlsx            | Maior (pode ter múltiplas abas) |
| load_csv     | .csv             | Menor (apenas texto separado) |

---

# 🧠 Conclusão

- Use `load_excel()` quando precisar trabalhar com arquivos Excel estruturados.
- Use `load_csv()` quando trabalhar com arquivos simples separados por delimitador.
- Adicione parâmetros extras apenas quando necessário.