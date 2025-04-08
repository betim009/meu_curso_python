
### 🐍 Exercícios de Funções em Python

#### 1. Função `hello_world`

Implemente a função `hello_world`.  
Ela deve **retornar exatamente** a string:

```
Hello World
```

**Exemplo:**

```python
print(hello_world())  # Saída esperada: Hello World
```

---

#### 2. Função `hello_name`

Crie a função `hello_name` que recebe um parâmetro `name` (uma string).  
Ela deve retornar a seguinte frase:

```
Hello <name>
```

**Exemplo:**

```python
print(hello_name("Janaina"))  # Saída esperada: Hello Janaina
```

---

#### 3. Função `some`

Implemente uma função chamada `some` que recebe dois parâmetros `n1` e `n2`, ambos inteiros.  
A função deve retornar a **soma dos dois números**.

**Exemplo:**

```python
print(some(10, 10))  # Saída esperada: 20
```

---

#### 4. Maior número de um array

Escreva uma função que recebe **uma lista de números inteiros** e retorna o **maior número da lista**.

**Exemplo:**

```python
print(maior_numero([4, 3, 10, 54, 100, 1]))  # Saída esperada: 100
```

---

#### 5. Verificação de números repetidos

Modifique a função anterior para que **retorne `False` caso existam números repetidos** na lista.

**Exemplo:**

```python
print(maior_numero([4, 3, 2, 2, 100, 10]))  # Saída esperada: False
```

---

#### 6. Conversor de moedas

Crie uma função que recebe um dicionário no seguinte formato:

```python
{"reais": 4.50}
```

E deve retornar:

```python
{"reais": 5.0, "dolar": 30.0}
```

**Regras**:
- A chave `"reais"` deve ser arredondada para cima (para o inteiro mais próximo).
- O valor em `"dolar"` será `"reais"` multiplicado por 6.


https://www.w3schools.com/python/python_functions.asp