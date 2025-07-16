def media(n1, n2):
    nota = (n1 + n2) / 2
    situacao = resultado(nota)
    return f"Nota: {nota} e foi {situacao}"

def media_avancada(notas):
    somar = sum(notas)
    nota = somar / len(notas)
    situacao = resultado(nota)
    return f"Nota: {nota} e foi {situacao}"

def resultado(nota_final):
    if nota_final > 5:
        return "Aprovado"
    else:
        return "Reprovado"
    

m1 = media_avancada([3, 5, 10, 9])
