# Mais e Menos (Plus Minus)

Você está desenvolvendo um sistema para análise estatística de listas de números inteiros. Seu objetivo é calcular a fração de números positivos, negativos e zeros em uma lista.

**Tarefa:**
Implemente uma função chamada `plus_minus(arr)` que recebe uma lista de inteiros e imprime, cada um em uma linha, a fração de números positivos, negativos e zeros, com 6 casas decimais.

Seu programa deve:
- Ler um inteiro n da entrada padrão, representando o tamanho do array.
- Ler uma linha com n números inteiros separados por espaço.
- Chamar a função `plus_minus(arr)` passando a lista lida.

---

## Assinatura da função
```python
def plus_minus(arr: list) -> None:
```

---

## Formato de entrada
- A primeira linha contém um inteiro n (1 ≤ n ≤ 10^5), o tamanho do array.
- A segunda linha contém n números inteiros separados por espaço (cada um no intervalo -100 ≤ valor ≤ 100).

## Formato de saída
- Imprima três linhas:
  - A fração de números positivos
  - A fração de números negativos
  - A fração de zeros
- Cada valor deve ser impresso com 6 casas decimais.

---

## Exemplos

### Exemplo 1
**Entrada:**
```
6
-4 3 -9 0 4 1
```
**Saída:**
```
0.500000
0.333333
0.166667
```

### Exemplo 2
**Entrada:**
```
4
0 0 0 0
```
**Saída:**
```
0.000000
0.000000
1.000000
```

---

## Observações
- Implemente a função exatamente como especificado.
- Não inclua mensagens adicionais na saída.
- O código de leitura de entrada e chamada da função deve estar fora da definição da função. 