def dividir(a, b):
    try:
        return a / b
    except ValueError:
        return "Erro ao converter para inteiro!"
    
print(dividir(4, "1"))