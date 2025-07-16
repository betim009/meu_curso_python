# Soma Muito Grande (A Very Big Sum)

Você está desenvolvendo um sistema para processar grandes volumes de dados financeiros. Seu objetivo é somar todos os valores de uma lista de inteiros muito grandes fornecida pelo usuário.

**Tarefa:**
Implemente uma função chamada `soma_muito_grande(arr)` que recebe uma lista de inteiros e retorna a soma de todos os elementos.

Seu programa deve:
- Ler um inteiro n da entrada padrão, representando o tamanho do array.
- Ler uma linha com n números inteiros separados por espaço.
- Chamar a função `soma_muito_grande(arr)` passando a lista lida.
- Imprimir o resultado retornado pela função.

---

## Assinatura da função
```python
def soma_muito_grande(arr: list) -> int:
```

---

## Formato de entrada
- A primeira linha contém um inteiro n (1 ≤ n ≤ 10^6), o tamanho do array.
- A segunda linha contém n números inteiros separados por espaço (cada um no intervalo 0 ≤ valor ≤ 10^10).

## Formato de saída
- Imprima um único número inteiro, que é a soma de todos os elementos do array.

---

## Exemplos

### Exemplo 1
**Entrada:**
```
5
1000000001 1000000002 1000000003 1000000004 1000000005
```
**Saída:**
```
5000000015
```

### Exemplo 2
**Entrada:**
```
3
9999999999 1 1
```
**Saída:**
```
10000000001
```

---

## Observações
- Implemente a função exatamente como especificado.
- Não inclua mensagens adicionais na saída.
- O código de leitura de entrada e chamada da função deve estar fora da definição da função. 