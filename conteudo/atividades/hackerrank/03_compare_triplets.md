# Comparando as Trincas (Compare the Triplets)

Alice e Bob estão participando de uma competição de avaliação em três critérios diferentes. Cada um recebe três notas, uma para cada critério. Para cada critério, quem tiver a nota mais alta recebe um ponto. Se as notas forem iguais, ninguém recebe ponto.

**Tarefa:**
Implemente uma função chamada `compare_triplets(a, b)` que recebe duas listas de três inteiros cada e retorna uma lista com dois inteiros: o primeiro é a pontuação de Alice, o segundo de Bob.

Seu programa deve:
- Ler uma linha com três inteiros (notas de Alice).
- Ler uma linha com três inteiros (notas de Bob).
- Chamar a função `compare_triplets(a, b)` passando as listas lidas.
- Imprimir os dois valores retornados pela função, separados por espaço.

---

## Assinatura da função
```python
def compare_triplets(a: list, b: list) -> list:
```

---

## Formato de entrada
- A primeira linha contém três inteiros separados por espaço (notas de Alice).
- A segunda linha contém três inteiros separados por espaço (notas de Bob).

## Restrições
- Cada nota está no intervalo 1 ≤ nota ≤ 100.

## Formato de saída
- Imprima dois inteiros separados por espaço: a pontuação de Alice e a de Bob.

---

## Exemplos

### Exemplo 1
**Entrada:**
```
5 6 7
3 6 10
```
**Saída:**
```
1 1
```

### Exemplo 2
**Entrada:**
```
17 28 30
99 16 8
```
**Saída:**
```
2 1
```

---

## Observações
- Implemente a função exatamente como especificado.
- Não inclua mensagens adicionais na saída.
- O código de leitura de entrada e chamada da função deve estar fora da definição da função. 