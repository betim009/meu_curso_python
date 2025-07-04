def getTotalTrainingTime(n, logs):
    result = [0] * n
    pilha = []
    prev_time = 0

    for log in logs:
        model, action, time = log.split(":")
        model, time = int(model), int(time)

        if pilha:
            ultima_pilha = pilha[-1]
            result[ultima_pilha] += time - prev_time

        if action == "start":
            pilha.append(model)
        else:
            pilha.pop()

        prev_time = time

    return result


logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
logs_1 = ["0:start:0", "1:start:2", "2:start:3", "2:end:4", "1:end:5", "0:end:6"]

print(getTotalTrainingTime(2, logs))  # [3, 3]
print(getTotalTrainingTime(3, logs_1)) # [3, 2, 1]
