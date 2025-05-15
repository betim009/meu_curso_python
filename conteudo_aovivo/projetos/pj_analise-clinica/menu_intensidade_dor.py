def menu_intensidade_dor():
    doencas_paciente = []
    print(""" Marque uma das opções da intensidade da dor:
       [1] Fraca
       [2] Média   
       [3] Forte   
    """)
    intensidade_dor = input('Digite: ')
    
    if intensidade_dor == '1':
        doencas_paciente.append('Constipação')
    elif intensidade_dor == '2':
        pass
    elif intensidade_dor == '3':
        pass
    
    print(doencas_paciente)