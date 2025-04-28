# Trabalhando com Condições em Python

Este material apresenta o uso de **condicionais** em Python, explicações simples sobre operadores lógicos e exemplos aplicados.

---

## Tipos de Condições

| Operador | Descrição               |
|:--------:|:-------------------------|
| `==`     | Igual a                   |
| `!=`     | Diferente de               |
| `>`      | Maior que                  |
| `<`      | Menor que                  |
| `>=`     | Maior ou igual a           |
| `<=`     | Menor ou igual a           |

Esses operadores são usados para comparar dois valores e retornar um resultado **booleano** (`True` ou `False`).

---

## Exemplo: Verificando o estado de uma fruta

### Cenário 1: Fruta não está madura (valor `False`)

```python
# Variável com valor False
fruta_condicao = False

# Primeira forma de verificar
if fruta_condicao == False:
    print("Está verde a fruta")

# Forma mais ideal e simples
if not fruta_condicao:
    print("Está verde também")
```

**Saída:**
```
Está verde a fruta
Está verde também
```

### Cenário 2: Fruta está madura (valor `True`)

```python
# Variável com valor True
fruta_condicao = True

# Primeira forma de verificar
if fruta_condicao == True:
    print("Está madura")

# Forma mais ideal e simples
if fruta_condicao:
    print("Está madura também")
```

**Saída:**
```
Está madura
Está madura também
```

> 🔍 **Nota:** Sempre que possível, prefira escrever a condição de forma mais enxuta (sem comparar diretamente com `True` ou `False`).

---

## Trabalhando com Listas de Dicionários

Imagine que temos uma lista contendo várias frutas, onde cada fruta é representada por um **dicionário**:

```python
frutas = [
    {"nome": "Maçã", "cor": "Vermelha", "preço": 3.50},
    {"nome": "Banana", "cor": "Amarela", "preço": 2.00},
    {"nome": "Laranja", "cor": "Laranja", "preço": 2.50},
    {"nome": "Uva", "cor": "Roxa", "preço": 4.00},
    {"nome": "Manga", "cor": "Amarela", "preço": 5.00},
]
```

Agora queremos verificar se a fruta no **índice 1** tem o **nome** "banana".

```python
if frutas[1]["nome"] == "banana":
    print("Encontrei a fruta Banana")
```

**Resultado:** Nada será exibido.

**Motivo:**
- Em Python, a comparação é sensível à diferença entre maiúsculas e minúsculas (**case-sensitive**).
- A palavra armazenada é "Banana" (com "B" maiúsculo) e não "banana".

### Forma correta:

```python
if frutas[1]["nome"].lower() == "banana":
    print("Encontrei a fruta Banana")
```

**Saída correta:**
```
Encontrei a fruta Banana
```

> 🔄 Sempre que trabalhar com comparações de textos, para evitar erros, utilize `.lower()` ou `.upper()` para padronizar.

---


