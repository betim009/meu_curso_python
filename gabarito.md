## Gabarito

### 1:

```python
nome = "Carlos"
idade = 30
altura = 1.75
print(nome)  # "Carlos"
print(idade)  # 30
print(altura)  # 1.75
```

### 2:

```python
print(type(nome))  # <class 'str'>
print(type(idade))  # <class 'int'>
print(type(altura))  # <class 'float'>
```

### 3:

```python
preco = 50.0
quantidade = 3
valor_total = preco * quantidade
print(valor_total)  # 150.0
```

### 4:

```python
produto = "notebook"
print(produto.upper())  # "NOTEBOOK"
```

### 5:

```python
disponivel = True
print(str(disponivel))  # "True"
```

### 6:

```python
produtos = ["Celular", "Notebook", "Tablet", "Fone de Ouvido"]
print(produtos[2])  # "Tablet"
```

### 7:

```python
usuarios = ["Ana", "Bruno", "Carlos"]
usuarios.append("Daniela")
print(usuarios)  # ['Ana', 'Bruno', 'Carlos', 'Daniela']
```

### 8:

```python
cores = ("vermelho", "azul", "verde")
print(cores[1])  # "azul"
```

### 9:

```python
categorias = {"Eletrônicos", "Roupas", "Livros"}
categorias.add("Roupas")
print(categorias)  # {'Eletrônicos', 'Roupas', 'Livros'}
```

### 10:

```python
usuario = {"nome": "Mariana", "idade": 25}
print(usuario["nome"])  # "Mariana"
```

### 11:

```python
usuario["email"] = "mariana@email.com"
print(usuario)  # {'nome': 'Mariana', 'idade': 25, 'email': 'mariana@email.com'}
```

### 12:

```python
del usuario["idade"]
print(usuario)  # {'nome': 'Mariana', 'email': 'mariana@email.com'}
```

### 13:

```python
usuarios = [
    {"nome": "Ana", "idade": 28},
    {"nome": "Carlos", "idade": 35}
]
print(usuarios[1]["nome"])  # "Carlos"
```

### 14:

```python
loja = {"Eletrônicos": ["Notebook", "Celular"], "Móveis": ["Mesa", "Cadeira"]}
print(loja["Eletrônicos"])  # ['Notebook', 'Celular']
```

### 15:

```python
loja = {"Eletrônicos": [{"produto": "Notebook", "preco": 3500.0}, {"produto": "Celular", "preco": 1200.0}]}
print(loja["Eletrônicos"][1]["preco"])  # 1200.0
```
