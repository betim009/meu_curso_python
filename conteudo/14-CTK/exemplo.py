import pandas as pd

pessoas = [
    {
        "nome": "Alberto",
        "idade": 30,
        "cidade": "Manhumirim",
        "admin": True 
    },
    {
        "nome": "Leticia",
        "idade": 25,
        "cidade": "Manhumirim"
    }
]

pd.DataFrame(pessoas).to_csv("exemplo.csv")