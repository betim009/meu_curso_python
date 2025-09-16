def calc_media(p1, p2, nome):
    calcular = (p1 + p2) / 2
    
    if calcular >= 6:
        return f"Aprovado {nome}"
    else:
        return f"Reprovado {nome}"

# exeutando a funcao 3x
cal1 = calc_media(8, 8, "Andre")
cal2 = calc_media(9, 9, "Maria")
cal3 = calc_media(9, 9, "Geralda")

# exibir o resultado
print(cal1)
print(cal2)
print(cal3)
