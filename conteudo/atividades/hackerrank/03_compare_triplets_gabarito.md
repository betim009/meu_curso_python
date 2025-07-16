# Gabarito - Comparando as Trincas (Compare the Triplets)

```python
def compare_triplets(a, b):
    pontos_a = 0
    pontos_b = 0
    for i in range(3):
        if a[i] > b[i]:
            pontos_a += 1
        elif a[i] < b[i]:
            pontos_b += 1
    return [pontos_a, pontos_b]

# Leitura de entrada
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# Chamada da função e impressão do resultado
resultado = compare_triplets(a, b)
print(resultado[0], resultado[1])
``` 