# Gabarito - Soma Mínima e Máxima (Mini-Max Sum)

```python
def mini_max_sum(arr):
    min_sum = sum(arr) - max(arr)
    max_sum = sum(arr) - min(arr)
    print(min_sum, max_sum)

# Leitura de entrada
arr = list(map(int, input().split()))
# Chamada da função
mini_max_sum(arr)
``` 