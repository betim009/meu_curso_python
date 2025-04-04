import pandas as pd

arquivo = pd.read_csv("data.csv")

nomes = arquivo["nome"]
nomes.to_csv("nomes.csv")

pessoas = [
    {
        "nome": "Carlos Alberto", 
        "idade": 20, 
        "estudante": True
    },
    {
        "nome": "Alberto", 
        "idade": 30, 
        "estudante": False
    }
]

data_frame = pd.DataFrame(pessoas)
data_frame.to_csv('pessoas.csv')


for index, row in arquivo.iterrows():
    if 'Alberto' in row['nome']:
        print(row['nome'])