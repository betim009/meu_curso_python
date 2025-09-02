# BASE DE DADOS

# Lista
usuarios = [
    # Dicionario
    {
        "id_user": 1, # Chave
        "nome": "Geraldo Marcelo da Silva",
        "idade": 69
    },
    {
        "id_user": 2,
        "nome": "Maria Fernandes Gomes",
        "idade": 43
    }
]

saques = [
    {
        "id_saque": 1,
        "id_usuario": 2,
        "valor": 100,
        "data": "23-01",
    },
    {
        "id_saque": 2,
        "id_usuario": 2,
        "valor": 120,
        "data": "24-01",
    },
    {
        "id_saque": 3,
        "id_usuario": 1,
        "valor": 60,
        "data": "24-01",
    }
]

depositos = [
    {
        "id_deposito": 1,
        "id_usuario": 1,
        "valor": 1500,
        "data": "23-01",
    },
    {
        "id_deposito": 2,
        "id_usuario": 2,
        "valor": 400,
        "data": "25-01",
    }
]

while True:

    print("1 - Listar Depositos")
    print("2 - Listar Saques")
    print("3 - Listar Usuarios")
    print("4 - Cadastrar Usuario")
    print("5 - Cadastrar um Saque")
    print("6 - Cadastrar um Deposito")


    entrada = input("Informe: ")

    if entrada == "1":
        print("Informe o ID do usuario que deseja saber o deposito")
    elif entrada == "2":
        print("Informe o ID do usuario que deseja saber o saque")
    else:
        print("Lista dos nossos usuarios.")

    break # ENCERRA