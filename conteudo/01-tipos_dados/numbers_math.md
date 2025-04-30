
# 🔢 Métodos e Funções para Números em Python

## 📚 Objetivo

Apresentar os principais métodos e funções utilizados para **números inteiros e decimais** em Python. Você aprenderá:

- Como manipular números.
- Arredondamentos, conversões e cálculos comuns.
- Diferença entre `int`, `float`, `round`, `abs`, entre outros.

---

## ✅ Requisitos

Antes de começar, é importante saber:

- O que são `int` (inteiros) e `float` (números decimais).
- Como declarar e usar variáveis numéricas.
- A diferença entre números positivos, negativos e operações básicas.

---

## 🧠 Tipos Numéricos em Python

- **`int`** → número inteiro  
  Ex: `10`, `-3`, `0`

- **`float`** → número com ponto decimal  
  Ex: `3.14`, `-7.2`, `0.0`

---

## 🧮 Funções e Métodos Numéricos

### `abs()`
Retorna o **valor absoluto** (sem sinal) de um número.

```python
abs(-5)  # 5
```

---

### `round(numero, casas)`
Arredonda um número para um número específico de casas decimais.

```python
round(3.14159, 2)  # 3.14
round(7.5)         # 8
```

---

### `pow(x, y)`
Eleva o número `x` à potência `y`.

```python
pow(2, 3)  # 8
```

---

### `divmod(x, y)`
Retorna uma tupla com dois valores: **quociente inteiro** e **resto** da divisão.

```python
divmod(10, 3)  # (3, 1)
```

---

### `int()`
Converte um número ou string para **inteiro** (descarta decimais).

```python
int(5.7)      # 5
int("42")     # 42
```

---

### `float()`
Converte para número decimal.

```python
float(3)     # 3.0
float("4.2") # 4.2
```

---

## 📊 Funções da biblioteca `math`

Para acessar funções matemáticas mais avançadas, use:

```python
import math
```

---

### `math.sqrt(x)`
Calcula a **raiz quadrada** de `x`.

```python
math.sqrt(16)  # 4.0
```

---

### `math.ceil(x)`
Arredonda o número **para cima** (teto).

```python
math.ceil(2.3)  # 3
```

---

### `math.floor(x)`
Arredonda **para baixo** (chão).

```python
math.floor(2.9)  # 2
```

---

### `math.trunc(x)`
Descarta a parte decimal, sem arredondar.

```python
math.trunc(3.9)  # 3
```

---

### `math.factorial(x)`
Calcula o **fatorial** de um número inteiro positivo.

```python
math.factorial(5)  # 120
```

---

### `math.pi` e `math.e`
Constantes matemáticas: π e o número de Euler.

```python
math.pi  # 3.141592653589793
math.e   # 2.718281828459045
```

---

## 📌 Dica Final

Você pode usar esses métodos para **validação de dados**, **operações matemáticas em jogos**, **cálculos financeiros** e muito mais.

---

## ✅ Resumo Rápido

| Função/Método       | O que faz                          |
|---------------------|-------------------------------------|
| `abs()`             | Valor absoluto                      |
| `round()`           | Arredonda                          |
| `pow()`             | Potência                           |
| `divmod()`          | Quociente e resto                  |
| `int()` / `float()` | Converte para int ou float         |
| `math.sqrt()`       | Raiz quadrada                      |
| `math.ceil()`       | Arredonda para cima                |
| `math.floor()`      | Arredonda para baixo               |
| `math.trunc()`      | Trunca a parte decimal             |
| `math.factorial()`  | Fatorial de um número              |
| `math.pi`, `math.e` | Constantes matemáticas             |
