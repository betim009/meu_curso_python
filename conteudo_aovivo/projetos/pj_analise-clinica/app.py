from menu_local_dor import menu_local_dor
from menu_intensidade_dor import menu_intensidade_dor

# INTERFACE:
while True:
    menu_local_dor()
    
    pergunta = input('Deseja verificar local da dor? s/n')
    if pergunta == 's':
        menu_intensidade_dor()
    else:
        break
