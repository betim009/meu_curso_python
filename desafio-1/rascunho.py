from data import *

"""
    1 - Implementar a função getChamadoById.
    
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
    
    2 Implementar a função getChamadosByTitulo
        essa função deve retornar todos os chamados que possuir o mesmo
        nome de titulo.
        
        se estiver recebendo a palavra 'emitir'
        deve retonar:
        
        [
            {
                "id": 2,
                "titulo": "Não consigo emitir nota",
                "detalhes": "O sistema de vocês é uma porcaria.........",
                "id_usuario": 1,
                "status": "pendente"
            },
            {
                "id": 3,
                "titulo": "Não consigo emitir nota",
                "detalhes": "Vocês não me ajudam.........",
                "id_usuario": 1,
                "status": "pendente"
            }
        ]
        
    3 implemente a função getUsuarioById
        se a função receber 1, deve retornar:
        {
            "id": 1,
            "status": "ativo",
            "nome": "João Marcelo Rodrigues Gomes",
            "telefone":  "11 99887766"   
        }
        
    4 implemente a função getUsuariosByNome
        se a funcao receber João, deve retonar:
        [
            {
                "id": 1,
                "status": "ativo",
                "nome": "João Marcelo Rodrigues Gomes",
                "telefone":  "11 99887766"   
            },
            {
                "id": 3,
                "status": "ativo",
                "nome": "João Paulo Macedo",
                "telefone":  "11 91123456"   
            }
        ]

"""


def getChamadoById(id):
    for item in chamados:
        if item["id"] == id:
            return item
    return {"resultado": "Não foi encontrado nenhum chamado com o ID enviado"}


def getChamadosByTitulo(palavra):
    if len(palavra) <= 3:
        return {"resultado": "Digite uma palavra com mais de 3 letras"}

    resultado = []
    for item in chamados:
        if palavra in item["titulo"]:
            resultado.append(item)

    if len(resultado) == 0:
        return {"resultado": "Não foi encontrado nenhum chamado com essa palavra"}

    return resultado


def getUsuarioById(id):
    pass

def getUsuariosByNome(nome):
    pass



# print(getChamadosByTitulo("emitir"))


# print(
#     getChamadoById(1)
# ) # deve retornar o primerio dicionário


# print(getChamadoById(2)) # deve retornar o segundo dicionário