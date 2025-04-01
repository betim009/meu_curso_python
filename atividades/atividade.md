# Exercícios de Python

## 1. Exibir todos os nomes

Percorra a lista de nomes utilizando um loop `for` e exiba cada um deles na tela. Esse exercício ajudará a entender a estrutura básica de um loop `for` e a manipulação de listas em Python.

**Lista de nomes:**

```python
nomes = ["Creusa", "Adriana", "Alexander", "Fernando"]
```

**Saída esperada:**

```
Creusa
Adriana
Alexander
Fernando
```

---

## 2. Encontrar um nome específico

Utilize um loop `for` combinado com `if` para verificar se um nome específico ("Adriana") está presente na lista e exiba-o. Esse exercício é útil para aprender sobre condições dentro de loops.

**Saída esperada:**

```
Adriana
```

---

## 3. Exibir todos os nomes exceto "Creusa"

Percorra a lista de nomes e exiba todos, exceto "Creusa". Aqui, você aprenderá a filtrar elementos dentro de um loop usando condições.

**Saída esperada:**

```
Adriana
Alexander
Fernando
```

---

## 4. Verificar se "João" está na lista

Crie um loop que percorra a lista de nomes e tente encontrar "João". Se ele não estiver presente, exiba uma mensagem informando que ele não foi encontrado. Caso esteja, exiba o nome.

**Saída esperada:**

```
Não foi possível encontrar o João
```

(se "João" estivesse na lista, a saída seria apenas "João")

---

## 5. Exibir idades maiores que 25

Percorra a lista de idades e exiba apenas os valores superiores a 25. Isso ajudará a praticar a combinação de loops e condições para filtrar dados.

**Lista de idades:**

```python
idades = [20, 17, 65, 32, 41]
```

**Saída esperada:**

```
65
32
41
```

---

## 6. Encontrar a maior idade

Crie uma variável `maior` inicializada com 0. Em seguida, percorra a lista de idades utilizando um loop `for` e atribua a `maior` o maior número encontrado. Esse exercício é essencial para entender como armazenar e comparar valores em loops.

**Saída esperada:**

```
65
```

---

## 7. Exibir informações das pessoas, exceto o ID

Percorra a lista de dicionários `pessoas` e exiba todas as informações de cada pessoa, exceto o ID. Aqui, você aprenderá a trabalhar com dicionários dentro de loops.

**Lista de pessoas:**

```python
pessoas = [
    {"id": "1", "nome": "Creusa", "idade": 20, "aposentado": True},
    {"id": "2", "nome": "Adriana", "idade": 17, "aposentado": False},
    {"id": "3", "nome": "Alexander", "idade": 65, "aposentado": True},
    {"id": "4", "nome": "Fernando", "idade": 41, "aposentado": False},
]
```

**Saída esperada:**

```
Creusa 20 aposentado
Adriana 17 não-aposentado
Alexander 65 aposentado
Fernando 41 não-aposentado
```

---

## 8. Corrigir a informação da pessoa com ID 1

Altere a informação da chave `aposentado` para `False` na pessoa que possui `id` igual a "1". Isso ajudará a entender como modificar elementos dentro de uma lista de dicionários.

**Saída esperada:**

```python
[
    {"id": "1", "nome": "Creusa", "idade": 20, "aposentado": False},
    {"id": "2", "nome": "Adriana", "idade": 17, "aposentado": False},
    {"id": "3", "nome": "Alexander", "idade": 65, "aposentado": True},
    {"id": "4", "nome": "Fernando", "idade": 41, "aposentado": False},
]
```
