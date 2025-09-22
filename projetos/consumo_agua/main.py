import pandas as pd

dados = [
    {
        "nome": "Alberto", 
        "idade": 30
    },

    {
        "nome": "Leticia", 
        "idade": 27
    }
]

pd.DataFrame(dados).to_csv("seliga.csv")
