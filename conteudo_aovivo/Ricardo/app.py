nome_variavel = input("Digite o seu nome: ")
idade_variavel = 28
time_variavel = input("Digite o seu time: ")

if time_variavel.lower() == "fluminense":
    print(f"{nome_variavel} é tricolor".upper())
elif time_variavel.lower() == "flamengo":
    print(f"{nome_variavel} é rubronegro!")
else:
    print(f"{nome_variavel} nao é tricolor e nem rubro negro")