# IGNORE - VOCE JA POSSUI =)
estudantes = [
    {
        "nome": "Ana",
        "idade": 20,
        "curso": "Engenharia",
        "periodo": "5 periodo",
        "genero": "Feminino"
    },
    {
        "nome": "Bruno",
        "idade": 22,
        "curso": "Direito",
        "periodo": "6 periodo",
        "genero": "Masculino"
    },
    {
        "nome": "Carla",
        "idade": 21,
        "curso": "Medicina",
        "periodo": "5 periodo",
        "genero": "Feminino"
    }
]

while True:
    # 
    print("Opcoes:")
    print("[1] - Listar estudantens por Idade")
    print("[2] - Listar estudantes por Curso")
    print("[3] - Listar estudantes por Periodo")
    print("[4] - Listar estudantes por Genero")
    print("[5] - Encontrar um estudante pelo nome")

    opcao = input("Digite a sua opcao: ") # numero 1 - 5

    if opcao == "1":
        print("Listando estudantes por idade")
        entrada = input("Digite a idade: ")
        # FOR
        for item in estudantes:
            if item["idade"] >= int(entrada):
                print(f"{item['nome']} {item['idade']}")

    elif opcao == "2":
        print("Listando estudantes por curso")
        entrada = input("Digite o curso: ")
        # FOR
        for item in estudantes:
            if item["curso"] == entrada:
                print(f"{item['nome']} {item['curso']}")

    elif opcao == "3":
        print("Listando estudantes por periodo")
        entrada = input("Digite o periodo: ")
        # FOR
        for item in estudantes:
            if item["periodo"] == entrada:
                print(f"{item['nome']} {item['periodo']}")

    elif opcao == "4":
        print("Listando estudantes por genero")
        entrada = input("Digite o genero: ")
        # GENERO
        for item in estudantes:
            if item["genero"] == entrada:
                print(f"{item['nome']} {item['genero']}")

    elif opcao == "5":
        print("Encontrando um usuario")
        entrada = input("Digite o nome")
        # NOME
        for item in estudantes:
            if item["nome"] == entrada:
                print(f"{item['nome']}")

    else:
        print("Encerrando.")
        break # Encerra
