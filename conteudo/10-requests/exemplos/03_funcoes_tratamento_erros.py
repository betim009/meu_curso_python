import requests


def buscar_json(url):
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.RequestException as erro:
        print("Erro ao buscar dados:", erro)
        return None


usuarios = buscar_json("https://jsonplaceholder.typicode.com/users")

if usuarios is not None:
    print("Usuarios encontrados:", len(usuarios))
    print("Primeiro usuario:", usuarios[0]["name"])
