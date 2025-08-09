# Base de dados de Usuarios
usuarios = [
    {"id": 1, "nome": "Jean S.", "idade": 38},
    {"id": 2, "nome": "Carolina M.", "idade": 20},
    {"id": 3, "nome": "Marcelo A.", "idade": 38},
    {"id": 4, "nome": "Antoniela G.", "idade": 38},
]

# Base de dados de movimentacao
movimentacao = [
    {
        "id": 1, 
        "id_usuario": 1, 
        "tipo": "saque", 
        "valor": 100
    },
    {
        "id": 2, 
        "id_usuario": 1, 
        "tipo": "deposito", 
        "valor": 300
    },
    {
        "id": 3, 
        "id_usuario": 4, 
        "tipo": "deposito", 
        "valor": 1000
    },
]

