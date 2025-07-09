# Atividade: Análise de Dados de um Processo Seletivo

Nesta atividade, você irá trabalhar com uma base de dados representada por uma lista de dicionários em Python. Cada dicionário representa um candidato de um concurso público, contendo informações como nome, idade e notas em diferentes disciplinas.

## Exemplo de base de dados:

```python
candidatos = [
    {"nome": "Ana", "idade": 25, "nota_matematica": 8.5, "nota_portugues": 7.0, "nota_informatica": 9.0},
    {"nome": "Bruno", "idade": 30, "nota_matematica": 6.0, "nota_portugues": 8.0, "nota_informatica": 7.5},
    {"nome": "Carla", "idade": 22, "nota_matematica": 9.0, "nota_portugues": 6.5, "nota_informatica": 8.0},
    {"nome": "Diego", "idade": 28, "nota_matematica": 5.5, "nota_portugues": 7.5, "nota_informatica": 6.0}
]
```

## Exercícios

1. **Tipos de Dados**
   - a) Qual o tipo de dado da variável `candidatos`?
   - b) Qual o tipo de dado de cada valor dentro dos dicionários (nome, idade, nota_matematica, etc)?

2. **Condições Simples**
   - a) Escreva um código para verificar se a nota de matemática do primeiro candidato é maior que 7.
   - b) Escreva um código para verificar se a idade do segundo candidato é maior ou igual a 30.
   - c) Escreva um código para verificar se a nota de informática do terceiro candidato é menor que 8.

3. **Condições Compostas**
   - a) Escreva um código para verificar se o primeiro candidato tirou nota maior que 7 em matemática **e** em informática.
   - b) Escreva um código para verificar se o segundo candidato tirou nota maior que 7 em português **ou** em informática.

> **Atenção:** Não utilize funções nem estruturas de repetição (for, while). Resolva cada exercício acessando diretamente os elementos da lista e dos dicionários.

---

Preencha suas respostas abaixo de cada exercício. 

---

## Gabarito

### 1. Tipos de Dados
- a) O tipo de dado da variável `candidatos` é uma lista (`list`).
- b) Dentro dos dicionários:
  - "nome": string (`str`)
  - "idade": inteiro (`int`)
  - "nota_matematica", "nota_portugues", "nota_informatica": ponto flutuante (`float`)

### 2. Condições Simples
- a)
```python
candidatos[0]["nota_matematica"] > 7  # True
```
- b)
```python
candidatos[1]["idade"] >= 30  # True
```
- c)
```python
candidatos[2]["nota_informatica"] < 8  # False
```

### 3. Condições Compostas
- a)
```python
candidatos[0]["nota_matematica"] > 7 and candidatos[0]["nota_informatica"] > 7  # True
```
- b)
```python
candidatos[1]["nota_portugues"] > 7 or candidatos[1]["nota_informatica"] > 7  # True
``` 