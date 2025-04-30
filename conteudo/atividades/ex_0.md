## 1. Variáveis
Uma **variável** é um nome que se refere a um valor armazenado na memória do computador. Em Python, a variável é definida automaticamente pelo valor atribuído. Não é necessário declarar o tipo da variável antecipadamente, o Python faz isso de forma dinâmica.

### Exemplos:

```python
nome = "João"  # String
idade = 25  # Inteiro
altura = 1.75  # Float
```

### Quando usar?

Você deve usar variáveis quando precisar armazenar um valor temporário para manipulá-lo ou usá-lo ao longo do seu código. Exemplos incluem:

- Quando precisar realizar cálculos.
- Para armazenar informações temporárias (como nome de usuário, idade, preços, etc.).
- Para reutilizar valores ou resultados ao longo do código sem precisar duplicá-los.

### Por que usar?

Usar variáveis traz várias vantagens, como:

1. **Legibilidade**: O uso de variáveis permite que você dê nomes significativos aos dados, tornando o código mais fácil de entender.
2. **Reusabilidade**: Você pode armazenar um valor em uma variável e reutilizá-lo várias vezes sem precisar duplicá-lo no código.
3. **Facilidade de manutenção**: Caso precise alterar o valor de uma variável, basta modificar em um único lugar.

### Boas Práticas (Nomes de Variáveis)

- **Seja Descritivo**: Escolha nomes que façam sentido e descrevam o propósito da variável.

  - **Correto**: `idade`, `nome_usuario`, `altura_media`
  - **Errado**: `x`, `y`, `a1`

- **Use Notação PEP8**: A convenção do Python sugere o uso de `snake_case` para variáveis. Isso significa usar letras minúsculas e separar palavras com underscores (`_`).

  - **Correto**: `quantidade_produtos`, `preco_total`
  - **Errado**: `quantidadeProdutos`, `precoTotal`

- **Evite Palavras Reservadas**: Não use palavras reservadas do Python (como `class`, `def`, `for`, etc.) como nome de variáveis.
- **Seja Conciso, Mas Claro**: Use nomes curtos, mas que ainda façam sentido. Por exemplo, ao invés de `numero_de_items_na_lista`, use apenas `num_items`.

### Exemplos de boas práticas:

```python
# Variáveis com nomes descritivos
nome_usuario = "Maria"
idade_usuario = 30
altura_usuario = 1.65

# Evitar nomes confusos ou muito genéricos
x = "João"  # Confuso
preco_item = 10.5  # Claro
```

### Evite Variáveis Globais

Sempre que possível, prefira usar variáveis dentro de funções ou blocos específicos. Variáveis globais podem causar confusão e dificultar a manutenção do código.

```python
# Evite
contador = 0  # Variável global
```

### Resumo

- **Quando usar**: Para armazenar e manipular dados temporários.
- **Por que usar**: Torna o código mais legível, reutilizável e fácil de manter.
- **Boas práticas**: Use nomes descritivos, siga a convenção `snake_case`, evite variáveis globais e palavras reservadas.

## 2. Tipos de Dados
Em Python, os tipos de dados representam diferentes tipos de valores. Cada tipo de dado tem características próprias e operações que podem ser feitas sobre ele.

### Tipos Comuns em Python

#### Strings (str)
Usadas para representar textos.

```python
produto = "Notebook"
usuario = "Carlos Silva"
```

Métodos úteis para strings:

```python
# Convertendo para maiúsculas
print(produto.upper())  # NOTEBOOK

# Convertendo para minúsculas
print(usuario.lower())  # carlos silva

# Substituindo caracteres
print(produto.replace("Note", "Ultra"))  # Ultrabook
```

#### Números (int e float)
Usados para representar valores numéricos inteiros e decimais.

```python
preco = 1999.99  # Float
quantidade = 10  # Inteiro
```

Operações aritméticas básicas:

```python
# Soma
valor_total = preco * quantidade
print(valor_total)  # 19999.9

# Divisão inteira
parcelas = valor_total // 5
print(parcelas)  # 3999

# Módulo (resto da divisão)
resto = valor_total % 3
print(resto)  # 1.9
```

#### Booleanos (bool)
Usados para representar verdadeiro ou falso.

```python
estoque_disponivel = True
cliente_logado = False
```

Métodos úteis para booleanos:

```python
print(str(estoque_disponivel))  # 'True' (convertendo para string)
print(int(cliente_logado))  # 0 (convertendo para número)
```

#### Listas (list)
São coleções ordenadas e mutáveis de itens.

```python
usuarios = ["Maria", "João", "Carlos"]
produtos = ["Notebook", "Celular", "Tablet"]
```

Manipulação de listas:

```python
# Adicionar item
usuarios.append("Ana")
print(usuarios)  # ['Maria', 'João', 'Carlos', 'Ana']

# Remover item
produtos.remove("Tablet")
print(produtos)  # ['Notebook', 'Celular']
```

#### Tuplas (tuple)
Semelhantes às listas, mas imutáveis.

```python
cores = ("vermelho", "azul", "verde")
print(cores[1])  # azul
```

#### Conjuntos (set)
Usados para armazenar valores únicos e sem ordem definida.

```python
categorias = {"Eletrônicos", "Roupas", "Livros"}
categorias.add("Móveis")
print(categorias)  # {'Eletrônicos', 'Roupas', 'Livros', 'Móveis'}
```

#### Dicionários (dict)
Armazenam pares chave-valor.

```python
usuario_info = {
    "nome": "João",
    "idade": 25,
    "compras": ["Notebook", "Celular"]
}

# Acessando valores
print(usuario_info["nome"])  # João

# Adicionando um novo par
usuario_info["email"] = "joao@example.com"
print(usuario_info)
```

### Exemplos mais complexos

#### Lista de dicionários

```python
usuarios = [
    {"nome": "Maria", "idade": 28, "cidade": "São Paulo"},
    {"nome": "João", "idade": 35, "cidade": "Rio de Janeiro"}
]
print(usuarios[1]["cidade"])  # Rio de Janeiro
```

#### Dicionário com listas que contêm dicionários

```python
loja = {
    "eletronicos": [
        {"produto": "Notebook", "preco": 3500.0},
        {"produto": "Celular", "preco": 1200.0}
    ],
    "moveis": [
        {"produto": "Mesa", "preco": 450.0},
        {"produto": "Cadeira", "preco": 250.0}
    ]
}

print(loja["eletronicos"][0]["produto"])  # Notebook
```

### Quando escolher o tipo de dado correto?

- **Use listas** quando precisar armazenar múltiplos itens e a ordem for importante.
- **Use tuplas** quando quiser armazenar valores que não devem ser alterados.
- **Use conjuntos** quando precisar de valores únicos e sem ordem.
- **Use dicionários** quando precisar associar chaves a valores.
- **Use strings** para armazenar textos e nomes.
- **Use números inteiros e decimais** para cálculos e preços.
- **Use booleanos** para representar verdadeiro ou falso.

### Boas práticas para os tipos de dados

- Escolha sempre o tipo mais adequado para otimizar o desempenho.
- Evite modificar tuplas, pois elas são imutáveis.
- Utilize chaves descritivas em dicionários para facilitar a leitura.
- Para grandes coleções de dados, prefira listas ou dicionários em vez de muitas variáveis soltas.
- Quando for necessário armazenar dados únicos, prefira `set` ao invés de listas.
- Ao trabalhar com números que exigem alta precisão, utilize a biblioteca `decimal`.


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

-------

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
