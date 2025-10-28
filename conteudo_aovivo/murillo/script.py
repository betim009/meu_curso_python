# Objetivo: Manipulacao de metodos para strings
# 
ata_1 = "Documento n 3204, do dia 23/02/2025..."
ata_2 = "Documento n 3205, do dia 30/02/2025..."
ata_3 = "DOCUMENTO n 3206, do dia 06/03/2025..."
ata_4 = "Documento n 3207, do dia 12/03/2025..."
ata_5 = "Documento n 3208, do dia 20/03/2025..."
ata_6 = "documento n 3209, do dia 27/03/2025..."
ata_7 = "Documento n 3210, do dia 03/04/2025..."

# Utilizando metodo find para descobrir se tem algum texto escrito errado.
# Se for -1, nao encontrou.
# Se for maior que zero, encontrou.

print(ata_3.find("Documento"))

separador_ata_3 = ata_3.split(" ", 1)
txt_documento = separador_ata_3[0].capitalize()
txt_resto = separador_ata_3[1]
nova_ata_3 = txt_documento + txt_resto

print(nova_ata_3)
