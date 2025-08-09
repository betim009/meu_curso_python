usuarios = [
    {"id": 1, "nome": "Jean S.", "idade": 38}, # 0
    {"id": 2, "nome": "Carolina M.", "idade": 20}, # 1
    {"id": 3, "nome": "Marcelo A.", "idade": 38}, # 2
    {"id": 4, "nome": "Antoniela G.", "idade": 38}, # 3 
]

# Manipulando dados simplificadamente:
## Acessando o terceiro usuario. 
#print(usuarios[2])

## Exibir uma informacao especifica:
#print(usuarios[2]["id"])
#print(usuarios[2]["nome"])

## Exibir mais de uma informacao por linha:
#print(usuarios[2]["nome"], usuarios[2]["idade"])

## Alterar um dado da sua lista:
#usuarios[2]["nome"] = "Marcelo Albani"
#print(usuarios)

## Excluir um dado da lista:
#usuarios.pop(2)
#print(usuarios)
usuarios.remove({"id": 1, "nome": "Jean S.", "idade": 38})
print(usuarios)

## Adicionar um novo usuario
usuarios.append({"id": 5, "nome": "Marcos T.", "idade": 28})
print(usuarios)