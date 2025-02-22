import pandas as pd

# 1. fazer leitura de uma planilha
estoque_produtos = pd.read_csv('produtos_estoque.csv')

# 2. Resgatar dados apenas das colunas
produtos = estoque_produtos["Produto"]
estoque = estoque_produtos["Estoque"]
data = estoque_produtos["Data de Validade"]
preco = estoque_produtos["Preço"]

# 3. Criar uma nova planilha com os valores apenas de alguma coluna
planilha_nova = produtos.to_csv('produtos.csv')

# 4. Criar uma nova planilha com valores de duas colunas
# será necessário o uso do FOR
# o for percorre cada linha e executa o que você definir para ele

base_dados = []
for index, row in estoque_produtos.iterrows():
    if row['Preço'] > 10:
        base_dados.append({
            "Nome_Produto": row['Produto'],
            "Preço_Produto": row['Preço']
        })

data_frame = pd.DataFrame(base_dados)
data_frame.to_csv('produtos_preco.csv')