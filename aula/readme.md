# Aula: Filtros com pandas (`app.py` e `app1.py`)

Este projeto mostra duas formas de aplicar filtros em um CSV de vendas:

- `app.py`: forma mais comum no pandas (vetorizada, mais curta e mais rápida).
- `app1.py`: forma didática com `for` e `if` (mais verbosa, boa para ensinar lógica).

Arquivo de dados usado nos dois casos: `arquivo.csv`.

## 1) O que o `app.py` faz

No `app.py`, nós:

1. Importamos o pandas.
2. Lemos o CSV em um DataFrame (`df`).
3. Criamos filtros booleanos (True/False).
4. Aplicamos esses filtros para gerar novos DataFrames (`resultado`, `resultado_1`, etc.).
5. Exibimos um resultado com `head()`.

### Filtros criados no `app.py`

- `f_simples`: categoria igual a `Alimentos`.
- `f_alimentos`: categoria contendo `alimentos` (sem diferenciar maiúscula/minúscula).
- `f_preco`: preço unitário maior ou igual a `19`.
- `f_eletronicos`: categoria contendo `eletronicos`.
- `f_online`: canal igual a `Online`.
- `f_sp`: estado igual a `SP`.
- `f_desconto`: desconto maior que `0`.
- `f_quantidade`: quantidade maior ou igual a `15`.
- `f_loja_fisica`: canal igual a `Loja Fisica`.

### Resultados gerados no `app.py`

- `resultado`: somente `Alimentos`.
- `resultado_1`: categoria contendo `alimentos`.
- `resultado_2`: `alimentos` **E** preço >= 19.
- `resultado_3`: `alimentos` **OU** preço >= 19.
- `resultado_4`: `eletronicos` **E** canal `Online`.
- `resultado_5`: estado `SP` **E** com desconto.
- `resultado_6`: quantidade >= 15 **E** `Loja Fisica`.
- `resultado_7`: (`eletronicos` e preço >= 19) **OU** (`alimentos` e desconto > 0).

## 2) O que o `app1.py` faz

O `app1.py` aplica os **mesmos filtros**, mas usando o estilo manual:

1. Cria listas vazias (`resultado`, `resultado_1`, ..., `resultado_7`).
2. Faz um `for` para cada filtro.
3. Em cada volta do loop, lê valores da linha (`row`).
4. Usa `if` para decidir se aquela linha entra no resultado.
5. Adiciona a linha com `append(row)`.
6. No final, converte a lista para DataFrame para imprimir.

Esse formato é útil para explicar lógica de programação antes de ensinar a forma vetorizada do pandas.

## 3) Diferença prática entre os dois

- `app.py`: melhor para uso real no dia a dia (mais limpo e performático).
- `app1.py`: melhor para ensinar como o filtro funciona “por baixo dos panos”.

## 4) Como executar

No terminal, dentro da pasta do projeto:

```bash
python3 app.py
```

ou

```bash
python3 app1.py
```

Observação: nos dois arquivos, apenas um `print(...)` está ativo. Para testar outros resultados, basta descomentar o `print` desejado.
