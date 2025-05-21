def loop():
    n = int(input("Quantas x repetir? "))
    if n <= 1:
        return False

    return n

def n_impares():
    # EXECUTA A FUNCAO LOOP
    n = loop()
    resultado = []
    
    if n > 1:
        for i in range(1, n+1):
            x = int(input("Digite: "))
    
            if x < 0 and x % 2 == 1:
                resultado.append(x)
    
    return resultado     

def nao_multiplos():
    # EXECUTA A FUNCAO LOOP
    n = loop()
    resultado = []     
    if n > 1:
        for i in range(1, n+1):
            x = int(input("Digite: "))

            # O QUE MUDARÁ DE UMA FUNÇÂO PARA OUTRA
            if x % 7 == 0:
                resultado.append(x)
    
    return resultado
    
               
# INSTANCIA
a = n_impares()
print(a)