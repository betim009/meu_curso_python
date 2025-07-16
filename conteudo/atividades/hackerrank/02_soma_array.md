# Soma Simples de Array (Simple Array Sum)

Você está desenvolvendo um sistema para processar listas de compras. Seu objetivo é somar todos os valores de uma lista de inteiros fornecida pelo usuário.

**Tarefa:**
Implemente uma função chamada `soma_array(arr)` que recebe uma lista de inteiros e retorna a soma de todos os elementos.

Seu programa deve:
- Ler um inteiro n da entrada padrão, representando o tamanho do array.
- Ler uma linha com n números inteiros separados por espaço.
- Chamar a função `soma_array(arr)` passando a lista lida.
- Imprimir o resultado retornado pela função.

---

## Assinatura da função
```python
def soma_array(arr: list) -> int:
```

---

## Formato de entrada
- A primeira linha contém um inteiro n (1 ≤ n ≤ 10^6), o tamanho do array.
- A segunda linha contém n números inteiros separados por espaço (cada um no intervalo -10^9 a 10^9).

## Formato de saída
- Imprima um único número inteiro, que é a soma de todos os elementos do array.

---

## Exemplos

### Exemplo 1
**Entrada:**
```
6
1 2 3 4 10 11
```
**Saída:**
```
31
```

### Exemplo 2
**Entrada:**
```
3
-5 0 5
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