# importacoes
import pandas as pd


tabela = pd.read_csv("dados.csv")
print(tabela)

data = [
    {
        "nome": "Alberto"
    },
    {
        "nome": "Leticia"
    }
]
    
pd.DataFrame(data).to_csv("usuarios.csv")