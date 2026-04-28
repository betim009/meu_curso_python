import requests

url = "https://jsonplaceholder.typicode.com/users"

resposta = requests.get(url, timeout=10)

if resposta.status_code == 200:
    usuarios = resposta.json()

    for usuario in usuarios:
        nome = usuario["name"]
        email = usuario["email"]
        cidade = usuario["address"]["city"]
        print(f"{nome} - {email} - {cidade}")
else:
    print("Erro ao buscar usuarios:", resposta.status_code)
