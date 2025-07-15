def media(n1, n2):
    nota = (n1 + n2) / 2
    return aprovado(nota)

def mediaSuperior(n1, n2, n3):
    nota = (n1 + n2 + n3) / 3
    return aprovado(nota)

def aprovado(nota):
    if nota > 5:
        return "Aprovado"
    else:
        return "Reprovado"
    
print(media(5, 10))