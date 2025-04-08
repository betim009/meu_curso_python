#               \/ recebe
def nomeFuncao(paramRecebe):
    return paramRecebe # <- retorna/resultado

#                  \/ envia
print(nomeFuncao("envia para o parametro"))

#                \/ recebe
def outraFuncao(parametro):
    return parametro # <- retorna

#                 \/ envia
print(outraFuncao(4)) # Enviando 4 para o parametro