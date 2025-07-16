# Soma Mínima e Máxima (Mini-Max Sum)

Você está desenvolvendo um sistema para análise de listas de números inteiros. Seu objetivo é calcular a soma mínima (a soma de 4 dos 5 números, excluindo o maior) e a soma máxima (excluindo o menor).

**Tarefa:**
Implemente uma função chamada `mini_max_sum(arr)` que recebe uma lista de 5 inteiros e imprime dois valores: a soma mínima e a soma máxima, separados por espaço.

Seu programa deve:
- Ler uma linha com 5 números inteiros separados por espaço.
- Chamar a função `mini_max_sum(arr)` passando a lista lida.

---

## Assinatura da função
```python
def mini_max_sum(arr: list) -> None:
```

---

## Formato de entrada
- Uma linha com 5 números inteiros separados por espaço (cada um no intervalo 1 ≤ valor ≤ 10^9).

## Formato de saída
- Imprima dois inteiros separados por espaço: a soma mínima e a soma máxima.

---

## Exemplos

### Exemplo 1
**Entrada:**
```
1 2 3 4 5
```
**Saída:**
```
10 14
```

### Exemplo 2
**Entrada:**
```
7 69 2 221 8974
```
**Saída:**
```
299 9271
```

---

## Observações
- Implemente a função exatamente como especificado.
- Não inclua mensagens adicionais na saída.
- O código de leitura de entrada e chamada da função deve estar fora da definição da função. 