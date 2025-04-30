import pandas as pd

# Leitura do csv
file = pd.read_csv('produtos_estoque.csv')
file_pacientes = pd.read_csv('pacientes.csv')


plot = file.plot()
plot

# Destruturando por colunas diretamente
cols_produto_preco = file[['Produto', 'Preco']]
cols_produto_preco_estoque = file[['Produto', 'Preco', 'Estoque']]

# métodos de localizar
loc_arroz = file.loc[0, 'Produto']
iloc_arroz = file.iloc[0, 1]


# exibir dados de alguma coluna com for
for index, paciente in file_pacientes.iterrows():
    paciente['nome']
    # print(paciente['nome'])
    # print(paciente.loc['nome'])
    
for produto in file.iterrows():
    produto[1].loc['Produto']
    # print(produto[1].loc['Produto'])