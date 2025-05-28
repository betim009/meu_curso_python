from clientes import lista

def encontrar_cliente_nome(nome):
    for item in lista:
        if item['nome'] == nome:
            return item
    return "Nao foi encontrado"    

resultado_1 = encontrar_cliente_nome("João")
resultado_2 = encontrar_cliente_nome("Maria Oliveira")

print(resultado_2)
print(resultado_1)
