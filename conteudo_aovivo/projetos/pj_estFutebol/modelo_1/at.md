
# 🏅 Exercícios com Dados de Esportes em Python

Este material apresenta diferentes bases de dados simuladas de esportes,
onde cada jogador tem estatísticas por partida. O objetivo é praticar
listas de dicionários, laços e lógica em Python.

---

## 🏀 Base de Dados: Jogadores de Basquete
***Faça as a media dos jogadores de rebote, pontos e assistencias.***

```python
jogadores_basquete = [
    {
        "id": 1,
        "nome": "LeBron James",
        "partidas": [
            {
                "id": 1,
                "time": "Lakers",
                "minuto": 38,
                "data": "01/01/2025",
                "campeonato": "NBA",
                "pontos": 30,
                "rebotes": 10,
                "assistencias": 8
            },
            {
                "id": 2,
                "time": "Warriors",
                "minuto": 35,
                "data": "03/01/2025",
                "campeonato": "NBA",
                "pontos": 25,
                "rebotes": 12,
                "assistencias": 7
            }
        ]
    },
    {
        "id": 2,
        "nome": "Stephen Curry",
        "partidas": [
            {
                "id": 1,
                "time": "Lakers",
                "minuto": 36,
                "data": "01/01/2025",
                "campeonato": "NBA",
                "pontos": 28,
                "rebotes": 4,
                "assistencias": 6
            },
            {
                "id": 2,
                "time": "Celtics",
                "minuto": 40,
                "data": "05/01/2025",
                "campeonato": "NBA",
                "pontos": 32,
                "rebotes": 5,
                "assistencias": 9
            }
        ]
    }
]


```




---

## 🏐 Vôlei: Bloqueios e Pontos

***Faça media pontos, bloqueios e saques***

### Base de dados

```python
jogadores_volei = [
    {
        "nome": "Thaisa",
        "partidas": [
            {"pontos": 18, "bloqueios": 5, "saques": 3},
            {"pontos": 22, "bloqueios": 7, "saques": 4}
        ]
    },
    {
        "nome": "Sheilla",
        "partidas": [
            {"pontos": 25, "bloqueios": 2, "saques": 5},
            {"pontos": 20, "bloqueios": 3, "saques": 6}
        ]
    }
]
```

---

## 🎾 Tênis: Aces e Erros

***Faça media de aces e erros***

### Base de dados

```python
jogadores_tenis = [
    {
        "nome": "Nadal",
        "partidas": [
            {"aces": 5, "erros": 3},
            {"aces": 8, "erros": 1}
        ]
    },
    {
        "nome": "Federer",
        "partidas": [
            {"aces": 10, "erros": 2},
            {"aces": 7, "erros": 4}
        ]
    }
]
```

---

## 🏁 Corrida: Tempos e Posições

***Faça media tempo, posição***

### Base de dados

```python
corredores = [
    {
        "nome": "Usain",
        "provas": [
            {"tempo": 9.58, "posicao": 1},
            {"tempo": 9.70, "posicao": 1}
        ]
    },
    {
        "nome": "Gatlin",
        "provas": [
            {"tempo": 9.74, "posicao": 2},
            {"tempo": 9.80, "posicao": 2}
        ]
    }
]
```

---

## 🏋️ Crossfit: Peso e Repetições

***Faça media peso, tempo e repetições ***

### Base de dados

```python
atletas = [
    {
        "nome": "Mat Fraser",
        "treinos": [
            {"peso": 100, "tempo": 30, "repeticoes": 80},
            {"peso": 120, "tempo": 28, "repeticoes": 85}
        ]
    },
    {
        "nome": "Rich Froning",
        "treinos": [
            {"peso": 110, "tempo": 29, "repeticoes": 75},
            {"peso": 130, "tempo": 27, "repeticoes": 80}
        ]
    }
]
```

---

Cada exemplo serve para treinar:

- Listas de dicionários
- Laços de repetição
- Funções
- Uso de `sum`, `len`, `max`, `min`, etc.

