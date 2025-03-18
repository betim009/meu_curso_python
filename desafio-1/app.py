from data import *
"""
    Implementar a função getChamadoById.
    
    A função deve encontrar o id RECEBIDO na chamada,
    dentro da list chamados.
    
    Se estiver recebendo 1, deve retornar:
    {
        "id": 1,
        "titulo": "Estou com problema no pagamento da minha fatura.",
        "detalhes": "Não estou conseguindo efetuar o pagamento..........",
        "id_usuario": 2,
        "status": "resolvido"
    }
    
    Se estiver recebendo 2, deve retornar:
    {
        "id": 2,
        "titulo": "Não consigo emitir nota",
        "detalhes": "O sistema de vocês é uma porcaria.........",
        "id_usuario": 1,
        "status": "pendente"
    }

"""

def getChamadoById(id):
    pass



print(getChamadoById(1)) # deve retornar o primerio dicionário
print(getChamadoById(2)) # deve retornar o segundo dicionário
