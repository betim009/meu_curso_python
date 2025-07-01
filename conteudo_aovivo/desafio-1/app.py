def contar_repeticoes(string=None, texto=None):
    if not string or not texto:
        return 0

    if not isinstance(string, str) or not isinstance(texto, str):
        raise ValueError("Ambos os parâmetros devem ser strings.")

    string = string.lower()
    texto = texto.lower()

    if len(string) > len(texto):
        return 0

    contador = 0
    for i in range(len(texto) - len(string) + 1):
        new_str = texto[i:i+len(string)]
        if  new_str == string:
            contador += 1
    return contador



print(contar_repeticoes("pa", "papagaio"))  # Saída: 2
print(contar_repeticoes("pap", "papagaio")) # Saída: 1
print(contar_repeticoes("a", "banana"))     # Saída: 3
print(contar_repeticoes("na", "banana"))    # Saída: 2

print(contar_repeticoes("nao", "ba"))    # Saída: 0
print(contar_repeticoes("nao"))    # Saída: 0
