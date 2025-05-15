import pandas as pd

usuarios = [
    {
        "nome": "Camilla",
        "idade": 28
    },
    {
        "nome": "Alberto",
        "idade": 30
    }
]

usuarios = pd.DataFrame(usuarios)
usuarios.to_csv('usuarios.csv')