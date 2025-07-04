
# 🧠 Cálculo de Tempo de Execução de Modelos com Interrupções

Imagine que temos **3 modelos de IA** para serem treinados em **uma única GPU**, que só pode treinar **um por vez**.

A cada novo modelo iniciado, se ele tiver **prioridade igual ou maior** (ID mais alto), ele **aguarda**. Mas se tiver **ID menor**, ele **interrompe** o modelo atual.

Cada linha do log segue o formato:

```
"ID_DO_MODELO:acao:tempo"
```

---

## Exemplo de entrada

```python
logs = [
  "0:start:0",
  "1:start:2",
  "2:start:3",
  "2:end:4",
  "1:end:5",
  "0:end:6"
]
```

---

## Etapas da execução:

- **0:start:0** → modelo 0 começa no tempo 0
- **1:start:2** → modelo 1 entra e pausa o modelo 0 → modelo 0 rodou de 0 a 2 (2s)
- **2:start:3** → modelo 2 entra e pausa o modelo 1 → modelo 1 rodou de 2 a 3 (1s)
- **2:end:4** → modelo 2 termina → rodou de 3 a 4 (1s)
- **1:end:5** → modelo 1 volta e termina → rodou de 4 a 5 (1s)
- **0:end:6** → modelo 0 volta e termina → rodou de 5 a 6 (1s)

---

## Resultado final:

| Modelo | Tempo total (s) |
|--------|------------------|
|   0    | 2 + 1 = **3s**   |
|   1    | 1 + 1 = **2s**   |
|   2    | 1 = **1s**       |

---

## Saída da função:

```python
[3, 2, 1]
```
