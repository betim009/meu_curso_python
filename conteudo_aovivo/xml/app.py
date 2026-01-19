import pandas as pd

df_pessoas = pd.read_xml("pessoas.xml")

#Localiza por indice
pessoa = df_pessoas.loc[0]

#localia por mais de um indice
pessoas_1 = df_pessoas.loc[[0, 1]]

# localiza indice + coluna
pessoa_idade = df_pessoas.loc[0, "cidade"]

# por condicao
pessoa_condicao = df_pessoas[df_pessoas["idade"] == 28]

# outra maneira por codincao
idade = df_pessoas["idade"]
pessao_condicao1 = df_pessoas[idade == 28]

nome = df_pessoas["nome"]

# gerando novo data frame
new_df = pd.concat([nome, idade], axis=1)

# Alterando
new_df.loc[new_df["nome"] == "Alberto", "nome"] = "Geraldo"

