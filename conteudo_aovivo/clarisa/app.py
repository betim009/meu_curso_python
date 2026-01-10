variantes = [
    {"sinonimo1":'MPXV_Rivers', "sinonimo2": 'MPXV_Rivers_IIbA', "tipo_virus": "MPXV"},
    {"sinonimo1":'MPXV_USA_2022_B1', "sinonimo2": 'MPXV_USA2022_B1', "tipo_virus": "MPXV"},
    {"sinonimo1":'MPXV_Kamituga_2024', "sinonimo2": 'MPXV_Kamituga2024_Ibsh2023', "tipo_virus": "MPXV"},
    {"sinonimo1":'MPXV_Kamituga2024_Ib_sh2023', "sinonimo2":'MPXV_Kamituga2024_Ibsh2023',"tipo_virus": "MPXV"},
    {"sinonimo1":'MPXV_Kamituga2024', "sinonimo2":'MPXV_Kamituga2024_Ibsh2023',"tipo_virus": "MPXV"},
    {"sinonimo1":'MPXV_Zaire_96_I_16', "sinonimo2":'MPXV_Zaire96_I_16',"tipo_virus": "MPXV"},
    {"sinonimo1":'VARV_India_67_major', "sinonimo2":'VARV_India67_major',"tipo_virus": "VARV"},
    {"sinonimo1":'VARV_India67', "sinonimo2":'VARV_India67_major',"tipo_virus": "VARV"},
    {"sinonimo1":'VARV_Bangladesh75_major', "sinonimo2":'VARV_Bangla75_major',"tipo_virus": "VARV"},
    {"sinonimo1":'VARV_Bangladesh_75_major', "sinonimo2":'VARV_Bangla75_major',"tipo_virus": "VARV"},
    {"sinonimo1":'VARV_Bangla_75_major', "sinonimo2":'VARV_Bangla75_major',"tipo_virus": "VARV"},
    {"sinonimo1":'CP_GRI_90', "sinonimo2":'CPXV_GRI-90',"tipo_virus": "CPXV"},
    {"sinonimo1":'CPXV_GRI_90', "sinonimo2":'CPXV_GRI-90',"tipo_virus": "CPXV"},
    {"sinonimo1":'CPXV_GER_91_3', "sinonimo2":'CPXV_GER91_3',"tipo_virus": "CPXV"},
    {"sinonimo1":'VACV_Western_Reserve', "sinonimo2":'VACV_WR',"tipo_virus": "VACV"},
    {"sinonimo1":'VACV-Western-Reserve', "sinonimo2":'VACV_WR',"tipo_virus": "VACV"},
    {"sinonimo1":'VACV_WR_Ref', "sinonimo2":'VACV_WR',"tipo_virus": "VACV"},
    {"sinonimo1":'VACV_Cop', "sinonimo2":'VACV_Copenhagen',"tipo_virus": "VACV"},
    {"sinonimo1":'VACV_Copenhagen_Ref', "sinonimo2":'VACV_Copenhagen',"tipo_virus": "VACV"},
    {"sinonimo1":'VACV_Ankara', "sinonimo2":'VACV_MVA',"tipo_virus": "VACV"},
    {"sinonimo1":'VACV_Modified_Vaccinia_Ankara', "sinonimo2":'VACV_MVA',"tipo_virus": "VACV"}
]

x = input("Digite o tipo de virus: ")
for variante in variantes:
    if variante["tipo_virus"] == x:
        print(variante)

valor_digitado = input("Digite sinonimo: ")
for variante in variantes:
    if valor_digitado in variante["sinonimo1"]:
        print(variante)

valor_digitado2 = input("Digite sinonimo: ")
for variante in variantes:
    if valor_digitado2 not in variante["sinonimo1"]:
        print(variante)
