import time

def solution(n, ratings):
    from collections import defaultdict

    # Dicionários para armazenar soma das notas e contagem por ID
    soma = defaultdict(int)
    contagem = defaultdict(int)

    for dish_id, nota in ratings:
        soma[dish_id] += nota
        contagem[dish_id] += 1

    # Variáveis para rastrear o melhor prato
    melhor_id = None
    melhor_media = -1

    for dish_id in soma:
        media = soma[dish_id] / contagem[dish_id]

        # Se for uma média melhor ou empate com ID menor
        if (media > melhor_media) or (media == melhor_media and dish_id < melhor_id):
            melhor_media = media
            melhor_id = dish_id

    return melhor_id


mn1 = solution(4, [[123, 4], [133, 2], [423, 5], [100, 4]])
mn2 = solution(4, [[123, 5], [133, 2], [99, 5], [100, 4]])

print(mn1, mn2)


print("--------")


# 🔽 Testando tempo de execução
import random

# Gerando uma entrada grande de teste
n = 10**5
ratings = [[random.randint(1, 1000), random.randint(1, 5)] for _ in range(n)]

inicio = time.time()
res = solution(n, ratings)
fim = time.time()

print("Resultado:", res)
print("Tempo de execução:", fim - inicio, "segundos")