## Comandos basicos

#### Pip 
1. pandas (bibliteoca de arquivos)

`python3 -m pip install pandas`


2. streamlit (biblioteca de interface)

`python3 -m pip install streamlit`


<hr>

#### Arquivos
Existe dois tipos populares de arquivos para planilhas:
- CSV
- XLSX (formato do excel)

Priorize o formato CSV - causa menos problemas!

<hr>

#### Modo de uso
*Pandas*
```py

lista = [
    {"nome": "Alberto", "idade": 30},
    {"nome": "Marcia", "idade": 31},
    {"nome": "Alex", "idade": 29},
    {"nome": "Airtom", "idade": 50},
    {"nome": "Daniela", "idade": 10},
]

# Convertendo a lista de dicionarios em DataFrame
data_frame = pd.DataFrame(lista) 



dicionario = {
    "nome": ["Alberto", "Maria", "Leticia"],
    "idade": [22, 21, 30]
}

# Convertendo o dicionario em DataFrame
data_frame2 = pd.DataFrame(dicionario)

```


```py
# to_csv ou to_xlsx geram arquivos.
data_frame.to_csv("raw.csv", index=False)
data_frame.to_excel("raw.xlsx", index=False, header=["Nome", "Idade"])
```


```py
#leitura de arquivos existentes
a = pd.read_csv("raw.csv")
b = pd.read_excel("raw.xlsx")
```


```py
#lendo os arquivos
tabela = pd.read_csv("raw.csv")
b = pd.read_excel("raw.xlsx")

# info mostra relacao de linhas, colunas e valores nulos(vazios)
print(tabela.info())
# describe mostra dados relacionados a estatistica basica
print(tabela.describe())

# acessando uma coluna
col_idade = tabela["idade"]

# exibindo filtro por coluna
print(
    tabela[col_idade == 30]
)
# armazena
iguais_30 = tabela[col_idade == 30]
# gera novo arquivo filtrado
iguais_30.to_csv("iguais_30.csv", index=False)

# filtro
print(
    tabela[col_idade > 30]
)
# armazena filtro
maior_30 = tabela[col_idade > 30]
#gera novo arquivo filtrado
maior_30.to_csv("maior_30.csv", index=False)

```