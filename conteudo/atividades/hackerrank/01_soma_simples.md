# Soma Simples (Solve Me First)

Imagine que você está desenvolvendo um sistema de caixa para uma pequena loja. O caixa precisa somar rapidamente dois valores inteiros informados pelo cliente e exibir o resultado.

**Tarefa:**
Implemente uma função chamada `soma_simples(a, b)` que recebe dois inteiros e retorna a soma deles.

Seu programa deve:
- Ler dois valores inteiros da entrada padrão, um por linha.
- Chamar a função `soma_simples(a, b)` passando os valores lidos.
- Imprimir o resultado retornado pela função.

---

## Assinatura da função
```python
def soma_simples(a: int, b: int) -> int:
```

---

## Formato de entrada
- A entrada consiste em duas linhas, cada uma contendo um número inteiro \(a\) e \(b\).

## Restrições
- \(-10^9 \leq a, b \leq 10^9\)

## Formato de saída
- Imprima um único número inteiro, que é a soma de \(a\) e \(b\).

---

## Exemplos

### Exemplo 1
**Entrada:**
```
3
5
```
**Saída:**
```
8
```

### Exemplo 2
**Entrada:**
```
-100
100
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