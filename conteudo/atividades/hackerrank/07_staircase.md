# Escada (Staircase)

Você está desenvolvendo um sistema para exibir padrões visuais em texto. Seu objetivo é imprimir uma escada de tamanho n, alinhada à direita, usando o caractere #.

**Tarefa:**
Implemente uma função chamada `staircase(n)` que recebe um inteiro n e imprime uma escada de n níveis, alinhada à direita.

Seu programa deve:
- Ler um inteiro n da entrada padrão.
- Chamar a função `staircase(n)` passando o valor lido.

---

## Assinatura da função
```python
def staircase(n: int) -> None:
```

---

## Formato de entrada
- Um inteiro n (1 ≤ n ≤ 100).

## Formato de saída
- Imprima n linhas, cada uma contendo espaços e caracteres #, formando uma escada alinhada à direita.

---

## Exemplos

### Exemplo 1
**Entrada:**
```
4
```
**Saída:**
```
   #
  ##
 ###
####
```

### Exemplo 2
**Entrada:**
```
2
```
**Saída:**
```
 #
##
```

---

## Observações
- Implemente a função exatamente como especificado.
- Não inclua mensagens adicionais na saída.
- O código de leitura de entrada e chamada da função deve estar fora da definição da função. 