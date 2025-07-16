# Gabarito - Mais e Menos (Plus Minus)

```python
def plus_minus(arr):
    n = len(arr)
    pos = sum(1 for x in arr if x > 0)
    neg = sum(1 for x in arr if x < 0)
    zero = sum(1 for x in arr if x == 0)
    print(f"{pos/n:.6f}")
    print(f"{neg/n:.6f}")
    print(f"{zero/n:.6f}")

# Leitura de entrada
n = int(input())
arr = list(map(int, input().split()))
# Chamada da função
plus_minus(arr)
``` 