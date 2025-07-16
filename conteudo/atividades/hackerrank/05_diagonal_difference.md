# Diferença Diagonal (Diagonal Difference)

Você está desenvolvendo um sistema para análise de matrizes quadradas. Seu objetivo é calcular a diferença absoluta entre as somas das diagonais principal e secundária de uma matriz.

**Tarefa:**
Implemente uma função chamada `diferenca_diagonal(matriz)` que recebe uma matriz quadrada (lista de listas) e retorna a diferença absoluta entre as somas das diagonais principal e secundária.

Seu programa deve:
- Ler um inteiro n da entrada padrão, representando o tamanho da matriz.
- Ler n linhas, cada uma contendo n números inteiros separados por espaço, representando as linhas da matriz.
- Chamar a função `diferenca_diagonal(matriz)` passando a matriz lida.
- Imprimir o resultado retornado pela função.

---

## Assinatura da função
```python
def diferenca_diagonal(matriz: list) -> int:
```

---

## Formato de entrada
- A primeira linha contém um inteiro n (2 ≤ n ≤ 100), o tamanho da matriz.
- As próximas n linhas contêm n inteiros cada, separados por espaço.

## Formato de saída
- Imprima um único número inteiro, que é a diferença absoluta entre as somas das diagonais.

---

## Exemplos

### Exemplo 1
**Entrada:**
```
3
11 2 4
4 5 6
10 8 -12
```
**Saída:**
```
15
```

### Exemplo 2
**Entrada:**
```
2
1 2
3 4
```
**Saída:**
```
0
```

---

## Observações
- Implemente a função exatamente como especificado.
- Não inclua mensagens adicionais na saída.
- O código de leitura de entrada e chamada da função deve estar fora da definição da função. 