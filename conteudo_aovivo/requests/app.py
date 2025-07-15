import requests # pip install requests 

req_products = requests.get('https://fakestoreapi.com/products')
req_users = requests.get('https://fakestoreapi.com/users')
req_user = requests.get('https://fakestoreapi.com/users/1')

if req_products.status_code == 200:
    res = req_products.json()

    for item in res:
        print(item)
        print()

if req_users.status_code == 200:
    res = req_users.json()

    for item in res:
        print(item)
        print()

if req_user.status_code == 200:
    res = req_user.json()

    print(res)