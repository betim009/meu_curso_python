
# Função `contar_repeticoes` em Python — Versões Didáticas

Este documento mostra, passo a passo, a construção de uma função que conta quantas vezes uma substring aparece em uma string maior. Ao final, temos uma explicação detalhada de cada parte da lógica usada.

---

## 🔹 Versão 1: Sem nenhuma validação

```python
def contar_repeticoes(string, texto):
    contador = 0
    for i in range(len(texto) - len(string) + 1):
        if texto[i:i+len(string)] == string:
            contador += 1
    return contador
```

---

## 🔹 Versão 2: Validação — `string` maior que `texto`

```python
def contar_repeticoes(string, texto):
    if len(string) > len(texto):
        return 0

    contador = 0
    for i in range(len(texto) - len(string) + 1):
        if texto[i:i+len(string)] == string:
            contador += 1
    return contador
```

---

## 🔹 Versão 3: Ignorando maiúsculas/minúsculas com `.lower()`

```python
def contar_repeticoes(string, texto):
    if len(string) > len(texto):
        return 0

    string = string.lower()
    texto = texto.lower()

    contador = 0
    for i in range(len(texto) - len(string) + 1):
        if texto[i:i+len(string)] == string:
            contador += 1
    return contador
```

---

## 🔹 Versão 4: Validando se os argumentos são `str`

```python
def contar_repeticoes(string, texto):
    if not isinstance(string, str) or not isinstance(texto, str):
        raise ValueError("Ambos os parâmetros devem ser strings.")

    if len(string) > len(texto):
        return 0

    string = string.lower()
    texto = texto.lower()

    contador = 0
    for i in range(len(texto) - len(string) + 1):
        if texto[i:i+len(string)] == string:
            contador += 1
    return contador
```

---

## 🔹 Versão 5: Tratando valores `None` ou strings vazias

```python
def contar_repeticoes(string=None, texto=None):
    if not string or not texto:
        return 0

    if not isinstance(string, str) or not isinstance(texto, str):
        raise ValueError("Ambos os parâmetros devem ser strings.")

    string = string.lower()
    texto = texto.lower()

    if len(string) > len(texto):
        return 0

    contador = 0
    for i in range(len(texto) - len(string) + 1):
        if texto[i:i+len(string)] == string:
            contador += 1
    return contador
```

---

# 🧠 Explicação de cada parte do código (versão final)

### `if not string or not texto:`
Evita que a função processe valores `None` ou strings vazias. Se isso acontecer, retorna 0.

---

### `if not isinstance(string, str) or not isinstance(texto, str):`
Garante que ambos os parâmetros sejam do tipo `str`. Caso contrário, levanta um erro.

---

### `string = string.lower()` e `texto = texto.lower()`
Transforma tudo para minúsculo, garantindo que "PA" e "pa" sejam tratados como iguais.

---

### `if len(string) > len(texto):`
Evita gasto desnecessário de processamento se a string de busca for maior que o texto.

---

### Loop principal:

```python
for i in range(len(texto) - len(string) + 1):
    if texto[i:i+len(string)] == string:
        contador += 1
```

#### Explicação:

- `range(len(texto) - len(string) + 1)`  
  Garante que só serão testadas posições válidas para comparação.  
  Exemplo: se `texto` tem 9 letras e `string` tem 2, o range será `range(8)`.

- `texto[i:i+len(string)]`  
  Esse é o **fatiamento**. Ele pega um pedaço do `texto` com o mesmo tamanho da `string`, começando na posição `i`.

- `if texto[i:i+len(string)] == string:`  
  Compara se a fatia atual do texto é **igual à string que estamos procurando**.

- `contador += 1`  
  Se for igual, soma 1 no contador.

---

Pronto! Com essas versões, você pode ensinar passo a passo como construir uma função segura, clara e eficiente.
