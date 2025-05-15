def menu_local_dor():
    # ARMAZENA as POSSIVEIS DOECENAS DO PACIENTE
    doencas_paciente = []

    print(""" Local da dor:
    [1] Flanco Direito
    [2] Flanco Esquerdo
    [3] Fossa Ilíaca Direita
    [4] Fossa Ilíaca Esquerda
    [5] Hipocôndrio Direito
    [6] Hipocôndrio Esquerdo
    [7] Região Epigástrica
    [8] Região Hipogástrica
    [9] Região Mesogástrica
    [10] Difusa
    [11] MAIS DE UMA REGIÃO *******

    [0] ENCERRAR       
    """)
    
    local_dor = input('Digite: ')
    if local_dor == "1":
        print('Flanco Direito')
        doencas_paciente.append('Abscesso hepático')
        
    elif local_dor == "2":
        print('Flanco Esquerdo')
        doencas_paciente.append('Abscesso esplênico')
         
    elif local_dor == "3":
        print('Fossa Ilíaca Direita')
        doencas_paciente.append('Adenite mesentérica (hiperplasia linfonodular)')  
        doencas_paciente.append('Apendicite')
        
    print(doencas_paciente)

        