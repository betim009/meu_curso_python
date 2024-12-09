import pandas as pd

# Ler o CSV original
df = pd.read_csv('arquivo.csv')

filtro = "Sicredi"

filtro_portador = df[df['Descrição - Portador'] == filtro]

# Salvar o novo DataFrame em um arquivo CSV
filtro_portador.to_csv('resultado_3.csv', index=False)
