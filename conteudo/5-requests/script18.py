from script17 import getApi  # Importa a função getApi do módulo script17

# Chama a função getApi e armazena o resultado na variável 'resultado'
resultado = getApi()

# Acessa o primeiro item da lista associada à chave 'categories' no dicionário 'resultado'
resultado_1 = resultado['categories'][0]

# Imprime o primeiro item da lista de categorias
print(resultado_1)
