
# 🧵 Métodos de String em Python

## 📚 Objetivo

Este material apresenta os **principais métodos** disponíveis para manipulação de **strings** em Python. Você vai aprender:

- O que cada método faz.
- Como usar na prática.
- Quando usar cada um deles.

---

## ✅ Requisitos

Antes de estudar os métodos de string, você deve:

- Saber o que é uma string (`str`) em Python.
- Entender como declarar e imprimir uma string.
- Compreender que métodos são ações aplicadas sobre objetos.

---

## 🧠 O que é um método de string?

Um **método** é uma **função associada a um objeto**. No caso das strings, Python oferece diversos métodos prontos para **analisar**, **transformar**, **buscar**, **modificar**, entre outras ações.

Exemplo:

```python
texto = "alberto"
print(texto.upper())  # ALBERTO
```

---

## 🔤 Métodos de Modificação de Texto

### `.upper()`
Transforma todos os caracteres da string em **maiúsculas**.

```python
"alberto".upper()  # "ALBERTO"
```

**Quando usar:** quando quiser exibir ou comparar textos em caixa alta.

---

### `.lower()`
Transforma todos os caracteres da string em **minúsculas**.

```python
"ALBERTO".lower()  # "alberto"
```

**Quando usar:** ideal para padronizar antes de comparações.

---

### `.capitalize()`
Coloca a **primeira letra** da string em **maiúscula** e o restante em minúsculo.

```python
"alBERto".capitalize()  # "Alberto"
```

---

### `.title()`
Coloca a **primeira letra de cada palavra** em maiúscula.

```python
"curso de python".title()  # "Curso De Python"
```

---

### `.strip()`
Remove **espaços em branco** (ou caracteres específicos) do início e do fim da string.

```python
"  python  ".strip()  # "python"
```

---

### `.lstrip()` e `.rstrip()`
Remove espaços só da esquerda (`lstrip`) ou só da direita (`rstrip`).

```python
"  teste".lstrip()  # "teste"
"teste  ".rstrip()  # "teste"
```

---

### `.replace(antigo, novo)`
Substitui trechos da string.

```python
"olá mundo".replace("mundo", "Python")  # "olá Python"
```

---

## 🔍 Métodos de Busca e Verificação

### `.find(valor)`
Procura a posição de um trecho na string. Retorna `-1` se não encontrar.

```python
"banana".find("na")  # 2
"banana".find("x")   # -1
```

---

### `.index(valor)`
Igual ao `.find()`, mas gera erro se não encontrar.

```python
"banana".index("na")  # 2
```

---

### `.count(valor)`
Conta quantas vezes um trecho aparece na string.

```python
"banana".count("a")  # 3
```

---

### `.startswith(valor)` / `.endswith(valor)`
Verifica se a string começa ou termina com o trecho indicado.

```python
"python".startswith("py")  # True
"python".endswith("on")    # True
```

---

## 🔠 Métodos de Análise de Conteúdo

### `.isalpha()`
Retorna `True` se a string tiver **somente letras** (sem espaço ou número).

```python
"Python".isalpha()  # True
"Python 3".isalpha()  # False
```

---

### `.isdigit()`
Retorna `True` se a string for composta **só por números**.

```python
"12345".isdigit()  # True
```

---

### `.isalnum()`
Retorna `True` se for **letra ou número** (sem símbolos).

```python
"Python3".isalnum()  # True
```

---

### `.isspace()`
Verifica se a string tem apenas espaços.

```python
"   ".isspace()  # True
```

---

## 🧩 Outros Métodos Úteis

### `.split(separador)`
Divide a string em uma **lista** com base no separador.

```python
"banana,maçã,uva".split(",")  # ["banana", "maçã", "uva"]
```

---

### `.join(lista)`
Une uma lista de strings usando a string atual como **separador**.

```python
"-".join(["a", "b", "c"])  # "a-b-c"
```

---

### `.zfill(n)`
Adiciona zeros à esquerda até completar o tamanho `n`.

```python
"42".zfill(5)  # "00042"
```

---

### `.center(tamanho, caractere)`
Centraliza a string no meio do espaço indicado.

```python
"oi".center(10, "*")  # "****oi****"
```

---

## 📝 Dica Final

Você pode **testar todos esses métodos** abrindo o terminal interativo do Python ou criando um script `.py`. São ótimos para limpeza de dados, formatação de textos e análise de strings!

---

## ✅ Resumo Rápido

| Método        | Para que serve                     |
|---------------|------------------------------------|
| upper()       | Deixa tudo maiúsculo               |
| lower()       | Deixa tudo minúsculo               |
| capitalize()  | Primeira letra maiúscula           |
| title()       | Primeira letra de cada palavra     |
| strip()       | Remove espaços nas pontas          |
| replace()     | Substitui partes do texto          |
| find(), index() | Localiza um trecho               |
| count()       | Conta quantas vezes aparece        |
| startswith(), endswith() | Início ou fim da string |
| isalpha(), isdigit(), isalnum(), isspace() | Verificações |
| split(), join() | Separar ou juntar textos         |
| zfill(), center() | Preencher ou centralizar       |
