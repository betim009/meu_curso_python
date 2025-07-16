# Gabarito - Escada (Staircase)

```python
def staircase(n):
    for i in range(1, n+1):
        print(' ' * (n - i) + '#' * i)

# Leitura de entrada
n = int(input())
# Chamada da função
staircase(n)
``` 