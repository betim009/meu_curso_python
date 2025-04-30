# Exercícios de Python - Variáveis e Tipos de Dados

A seguir, uma série de exercícios para praticar os conceitos de variáveis e tipos de dados em Python.

## Exercícios

### 1. Criando variáveis

Crie três variáveis: `nome`, `idade` e `altura`, e atribua valores a elas.

**Exemplo de saída:**

```python
print(nome)  # "Carlos"
print(idade)  # 30
print(altura)  # 1.75
```

### 2. Tipos de Dados

Imprima os tipos das variáveis criadas no exercício anterior.

**Exemplo de saída:**

```python
print(type(nome))  # <class 'str'>
print(type(idade))  # <class 'int'>
print(type(altura))  # <class 'float'>
```
### 3. Operações com Números

Crie duas variáveis `preco` e `quantidade`, realize uma multiplicação entre elas e exiba o resultado.

**Exemplo de saída:**

```python
print(valor_total)  # 150.0
```

### 4. Métodos de String

Dada uma variável `produto`, converta seu valor para letras maiúsculas e exiba o resultado.

**Exemplo de saída:**

```python
print(produto.upper())  # "NOTEBOOK"
```

### 5. Trabalhando com Booleanos

Crie uma variável `disponivel` com valor `True` e converta-a para uma string.

**Exemplo de saída:**

```python
print(str(disponivel))  # "True"
```

### 6. Listas e Índices

Crie uma lista de produtos e exiba o terceiro item.

**Exemplo de saída:**

```python
print(produtos[2])  # "Tablet"
```

### 7. Adicionando e Removendo Itens

Crie uma lista de usuários e adicione um novo usuário.

**Exemplo de saída:**

```python
print(usuarios)  # ['Ana', 'Bruno', 'Carlos', 'Daniela']
```

### 8. Tuplas

Crie uma tupla com três cores e exiba a segunda cor.

**Exemplo de saída:**

```python
print(cores[1])  # "azul"
```

### 9. Conjuntos e Unicidade

Crie um conjunto de categorias e tente adicionar um item duplicado.

**Exemplo de saída:**

```python
print(categorias)  # {'Eletrônicos', 'Roupas', 'Livros'}
```

### 10. Dicionários e Acesso

Crie um dicionário representando um usuário com nome e idade e exiba o nome.

**Exemplo de saída:**

```python
print(usuario["nome"])  # "Mariana"
```

### 11. Dicionários e Adição de Dados

Adicione uma nova chave `email` ao dicionário do exercício anterior.

**Exemplo de saída:**

```python
print(usuario)  # {'nome': 'Mariana', 'idade': 25, 'email': 'mariana@email.com'}
```

### 12. Removendo Itens de um Dicionário

Remova a chave `idade` do dicionário do exercício anterior.

**Exemplo de saída:**

```python
print(usuario)  # {'nome': 'Mariana', 'email': 'mariana@email.com'}
```

### 13. Lista de Dicionários

Crie uma lista contendo dois dicionários representando usuários e exiba o nome do segundo usuário.

**Exemplo de saída:**

```python
print(usuarios[1]["nome"])  # "Carlos"
```

### 14. Dicionário com Listas

Crie um dicionário onde as chaves são categorias e os valores são listas de produtos.

**Exemplo de saída:**

```python
print(loja["Eletrônicos"])  # ['Notebook', 'Celular']
```

### 15. Acessando Dados em Estruturas Complexas

Dado um dicionário de produtos, exiba o preço do segundo item da categoria "Eletrônicos".

**Exemplo de saída:**

```python
print(loja["Eletrônicos"][1]["preco"])  # 1200.0
```