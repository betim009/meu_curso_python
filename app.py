import requests
credentials = {'username': 'johnd', 'password': 'm38rmF$'}
response = requests.post('https://fakestoreapi.com/auth/login', json=credentials)
print(response.json())