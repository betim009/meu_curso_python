# Gabarito - Diferença Diagonal (Diagonal Difference)

```python
def diferenca_diagonal(matriz):
    n = len(matriz)
    diag1 = sum(matriz[i][i] for i in range(n))
    diag2 = sum(matriz[i][n-1-i] for i in range(n))
    return abs(diag1 - diag2)

# Leitura de entrada
n = int(input())
matriz = [list(map(int, input().split())) for _ in range(n)]
# Chamada da função e impressão do resultado
print(diferenca_diagonal(matriz))
``` 