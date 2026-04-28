import pandas as pd
import requests


def buscar_json(url):
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.RequestException as erro:
        print("Erro na requisicao:", erro)
        return None


def exercicio_1():
    url = "https://jsonplaceholder.typicode.com/users"
    resposta = requests.get(url, timeout=10)
    dados = resposta.json()
    print("Status:", resposta.status_code)
    print("Tipo:", type(dados))
    print("Quantidade:", len(dados))


def exercicio_2():
    usuarios = buscar_json("https://jsonplaceholder.typicode.com/users")
    if usuarios is None:
        return
    for usuario in usuarios:
        print(usuario["name"], "-", usuario["email"])


def exercicio_3():
    usuarios = buscar_json("https://jsonplaceholder.typicode.com/users")
    if usuarios is None:
        return
    for usuario in usuarios:
        print(usuario["name"], "-", usuario["address"]["city"])


def exercicio_4():
    cep = buscar_json("https://brasilapi.com.br/api/cep/v1/01001000")
    if cep is None:
        return
    print("Rua:", cep["street"])
    print("Bairro:", cep["neighborhood"])
    print("Cidade:", cep["city"])
    print("Estado:", cep["state"])


def exercicio_5():
    dados = buscar_json("https://dummyjson.com/products?limit=10")
    if dados is None:
        return
    for produto in dados["products"]:
        print(produto["title"], "-", produto["price"])


def exercicio_6():
    usuarios = buscar_json("https://jsonplaceholder.typicode.com/users")
    if usuarios is not None:
        print("Quantidade de usuarios:", len(usuarios))


def exercicio_7():
    usuarios = buscar_json("https://jsonplaceholder.typicode.com/users")
    if usuarios is None:
        return
    for usuario in usuarios:
        if usuario["email"].endswith(".biz"):
            print(usuario["name"], "-", usuario["email"])


def exercicio_8():
    dados = buscar_json("https://dummyjson.com/products?limit=20")
    if dados is None:
        return
    produtos = dados["products"]
    soma_precos = 0
    for produto in produtos:
        soma_precos += produto["price"]
    preco_medio = soma_precos / len(produtos)
    print(f"Preco medio: US$ {preco_medio:.2f}")


def exercicio_9():
    dados = buscar_json("https://dummyjson.com/products?limit=100")
    if dados is None:
        return
    for produto in dados["products"]:
        if produto["stock"] < 30:
            print(produto["title"], produto["category"], produto["price"], produto["stock"])


def exercicio_10():
    dados = buscar_json("https://dummyjson.com/products?limit=20")
    if dados is None:
        return
    df = pd.DataFrame(dados["products"])
    print(df[["title", "category", "price", "stock"]])
    print(f"Preco medio: US$ {df['price'].mean():.2f}")
    print("Estoque total:", df["stock"].sum())


def exercicio_11():
    dados = buscar_json("https://dummyjson.com/products?limit=100")
    if dados is None:
        return
    df = pd.DataFrame(dados["products"])
    relatorio = df.groupby("category").agg(
        quantidade_produtos=("id", "count"),
        preco_medio=("price", "mean"),
        estoque_total=("stock", "sum"),
    )
    print(relatorio.sort_values(by="estoque_total", ascending=False))


def exercicio_12():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=-23.55&longitude=-46.63&current_weather=true"
    )
    dados = buscar_json(url)
    if dados is None:
        return
    clima_atual = dados["current_weather"]
    print("Temperatura:", clima_atual["temperature"])
    print("Velocidade do vento:", clima_atual["windspeed"])
    print("Codigo do clima:", clima_atual["weathercode"])
    print("Horario:", clima_atual["time"])


def exercicio_13():
    dados = buscar_json("https://dummyjson.com/products?limit=100")
    if dados is None:
        return

    df = pd.DataFrame(dados["products"])
    produto_mais_caro = df.sort_values(by="price", ascending=False).iloc[0]
    produto_maior_desconto = df.sort_values(by="discountPercentage", ascending=False).iloc[0]
    estoque_baixo = df[df["stock"] < 20]

    print("Total de produtos:", len(df))
    print(f"Preco medio: US$ {df['price'].mean():.2f}")
    print("Estoque total:", df["stock"].sum())
    print("Produto mais caro:", produto_mais_caro["title"])
    print("Produto com maior desconto:", produto_maior_desconto["title"])
    print("Categorias:", sorted(df["category"].unique()))
    print(estoque_baixo[["title", "category", "price", "stock"]])


if __name__ == "__main__":
    exercicio_1()
