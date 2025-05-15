lista = ["A", "B", "C", "A"]
lista2 = ["E", "F", "F", "G"]

# SE você tem que retorna mais de 1 resultado -> LISTA

# Toda função ela deve ser definida
def funcao(letra, letras):
    result = []
    for element in letras:
        if element == letra:
            result.append(element)
    
    if len(result) == 0:
        return "Não existe essa letra"
    
    return result
        

def exibir_letras(letras):
    for letra in letras:
        print(letra)

# Instancias       
x = funcao('A', lista)
exibir_letras(x)

y = funcao('F', lista2)
exibir_letras(y)