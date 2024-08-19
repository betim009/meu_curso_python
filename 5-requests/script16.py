import requests  # Importa a biblioteca requests

# URL da API
url = "https://www.themealdb.com/api/json/v1/1/categories.php"

# Faz a requisição GET para a API
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Converte a resposta em formato JSON
    data = response.json()
    # Imprime os dados recebidos
    print(data)
else:
    # Caso a requisição não tenha sido bem-sucedida
    print(f"Falha na requisição: {response.status_code}")
