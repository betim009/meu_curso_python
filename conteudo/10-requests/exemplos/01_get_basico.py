import requests

url = "https://jsonplaceholder.typicode.com/users"

resposta = requests.get(url, timeout=10)

print("Status da resposta:", resposta.status_code)
print("Conteudo bruto:")
print(resposta.text[:500])
