import requests


def getApi():
    try:
        # URL da API
        url = "https://www.themealdb.com/api/json/v1/1/categories.php"

        # Faz a requisição GET para a API
        response = requests.get(url)

        # Verifica se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Converte a resposta em formato JSON
            data = response.json()
            return data
        else:
            # Retorna uma mensagem de erro se a resposta não for bem-sucedida
            return f"Falha na requisição: {response.status_code}"

    except requests.RequestException as e:
        # Retorna uma mensagem de erro em caso de exceção
        return f"Erro na requisição: {e}"


# Exemplo de uso da função
resultado = getApi()

# Depois de testar a linha abaixo comente ela, por conta do proximo arquivo
print(resultado)
