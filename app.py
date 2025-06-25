def verify(str, str1):
    contador = 0

    for index in range(0, len(str1), len(str)):
        print(str1[index])

        if index < len(str1) - 1:
            char = str1[index] + str1[index +1]
            
            if str == char:
                contador += 1 
    
    return contador

verify("pa", "papagaios")
verify("p", "papagaios")
verify("pap", "papagaios")
verify("pap", "p")

