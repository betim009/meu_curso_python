# Conceitos Básicos de Python

Este documento apresenta conceitos fundamentais de Python com exemplos práticos organizados visualmente, ideal para iniciantes.

---

## 1. Variáveis

Variáveis armazenam valores e não precisam de declaração explícita de tipo.

```python
nome = "Alberto"
print(nome)  # Saída: Alberto
```

### 1.1 Exibindo textos

```python
print("Alberto é professor de lógica")  # Saída: Alberto é professor de lógica
```

---

## 2. Tipos de Dados Simples

| Tipo               | Exemplo                 | Saída              |
|--------------------|-------------------------|--------------------|
| **String (`str`)** | `fruta = "Manga"`      | `Manga`            |
| **Inteiro (`int`)**| `quantidade = 10`       | `10`               |
| **Float (`float`)**| `preco = 4.10`          | `4.1`              |
| **Boolean (`bool`)**| `disponivel = True`    | `True`             |

```python
# Exemplo combinado:
fruta = "Manga"
preco = 4.10
disponivel = True

print(fruta, preco, disponivel)  # Saída: Manga 4.1 True
```

---

## 3. Tipos de Dados Compostos

### 3.1 Listas (`list`)

Listas são ordenadas, mutáveis e permitem valores duplicados.

- **Ordenadas:** Os itens têm uma posição definida (índice) e mantêm sua ordem original.
- **Mutáveis:** Permitem alteração, adição ou remoção de itens após a criação.

```python
frutas = ["Manga", "Uva", "Morango", "Goiaba"]
print(frutas)  # Saída: ['Manga', 'Uva', 'Morango', 'Goiaba']

# Iteração para exibir cada fruta separadamente:
for fruta in frutas:
    print(fruta)

# Saída:
# Manga
# Uva
# Morango
# Goiaba
```

### 3.2 Tuplas (`tuple`)

Tuplas são semelhantes às listas, porém são ordenadas e imutáveis.

- **Ordenadas:** Assim como nas listas, os itens mantêm uma ordem fixa e têm posição definida.
- **Imutáveis:** Após criadas, não permitem alteração, adição ou remoção de itens.

```python
coordenadas = (10.0, 20.0)
print(coordenadas)  # Saída: (10.0, 20.0)
```

### 3.3 Conjuntos (`set`)

Conjuntos não têm ordem definida e não permitem valores duplicados.

```python
letras = {"a", "b", "c", "a"}
print(letras)  # Saída: {'a', 'b', 'c'} (a ordem pode variar)
```

### 3.4 Dicionários (`dict`)

Dicionários armazenam pares chave-valor, facilitando o acesso rápido aos valores através das chaves.

```python
produto = {
    "nome": "Manga",
    "preco": 5.10,
    "quantidade": 10,
    "disponivel": True
}

print(produto)
# Saída: {'nome': 'Manga', 'preco': 5.1, 'quantidade': 10, 'disponivel': True}

# Exemplo prático de alteração:
produto["preco"] = 4.50        # atualizando o preço
produto["origem"] = "Brasil"  # adicionando nova chave
produto.pop("quantidade")      # removendo a chave quantidade

print(produto)
# Saída: {'nome': 'Manga', 'preco': 4.5, 'disponivel': True, 'origem': 'Brasil'}
```

---

## 4. Símbolos e Definições

| Símbolo | Uso em Python                 |
|---------|-------------------------------|
| `""`    | Define strings                |
| `()`    | Executa funções               |
| `.`     | Acessa métodos ou atributos   |
| `[]`    | Listas e índices              |
| `{}`    | Dicionários ou conjuntos      |

---

## 5. Boas Práticas

- **Case-sensitive:** `Variavel` ≠ `variavel`
- **Indentação:** Utilize 4 espaços por nível.
- **Comentários:** `#` para linha única; `'''` ou `"""` para multilinhas.
- **Strings multilinhas:** `'''texto'''`
- **Tipagem dinâmica:** não precisa declarar o tipo.
- **Nomes:** use `snake_case` para variáveis e funções.

---

## 6. Métodos Comuns

| Tipo         | Métodos Úteis                               |
|--------------|---------------------------------------------|
| **String**   | `.lower()`, `.upper()`, `.strip()`, `.split()`|
| **Número**   | `abs()`, `round()`, `pow()`                 |
| **Lista**    | `.append()`, `.pop()`, `.sort()`, `.reverse()`|
| **Dicionário**| `.get()`, `.keys()`, `.values()`, `.items()`|

---

## 7. Exemplos Adicionais

| Exemplo                 | Código                                  | Saída                              |
|-------------------------|-----------------------------------------|------------------------------------|
| Tamanho da lista        | `print(len(frutas))`                    | `4`                                |
| Slicing                 | `print(frutas[1:3])`                    | `['Uva', 'Morango']`               |
| Loop básico             | `for i in range(3): print(i)`           | `0 1 2`                            |
| Lista para conjunto     | `print(set(frutas))`                    | `{'Manga', 'Uva', 'Morango', 'Goiaba'}` (ordem pode variar)|

---

