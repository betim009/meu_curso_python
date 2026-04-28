# Gabaritos Comentados - Requests e APIs

## 1. Primeira requisicao

```python
import requests

url = "https://jsonplaceholder.typicode.com/users"
resposta = requests.get(url, timeout=10)

dados = resposta.json()

print("Status:", resposta.status_code)
print("Tipo:", type(dados))
print("Quantidade:", len(dados))
```

Explicacao: `requests.get()` busca os dados e `.json()` converte a resposta em lista/dicionario Python.

## 2. Nome e email dos usuarios

```python
import requests

url = "https://jsonplaceholder.typicode.com/users"
resposta = requests.get(url, timeout=10)
usuarios = resposta.json()

for usuario in usuarios:
    print(usuario["name"], "-", usuario["email"])
```

Explicacao: a API retorna uma lista de usuarios. O `for` percorre cada usuario.

## 3. Acessando dados internos

```python
import requests

url = "https://jsonplaceholder.typicode.com/users"
resposta = requests.get(url, timeout=10)
usuarios = resposta.json()

for usuario in usuarios:
    nome = usuario["name"]
    cidade = usuario["address"]["city"]
    print(nome, "-", cidade)
```

Explicacao: `address` e um dicionario dentro do dicionario do usuario.

## 4. Consulta de CEP

```python
import requests

url = "https://brasilapi.com.br/api/cep/v1/01001000"
resposta = requests.get(url, timeout=10)
resposta.raise_for_status()

cep = resposta.json()

print("Rua:", cep["street"])
print("Bairro:", cep["neighborhood"])
print("Cidade:", cep["city"])
print("Estado:", cep["state"])
```

Explicacao: a BrasilAPI retorna um dicionario com os dados do endereco.

## 5. Produtos simples

```python
import requests

url = "https://dummyjson.com/products?limit=10"
resposta = requests.get(url, timeout=10)
resposta.raise_for_status()

dados = resposta.json()
produtos = dados["products"]

for produto in produtos:
    print(produto["title"], "-", produto["price"])
```

Explicacao: na DummyJSON, a lista de produtos fica dentro da chave `products`.

## 6. Funcao reutilizavel

```python
import requests


def buscar_json(url):
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.RequestException as erro:
        print("Erro na requisicao:", erro)
        return None


usuarios = buscar_json("https://jsonplaceholder.typicode.com/users")

if usuarios is not None:
    print("Quantidade de usuarios:", len(usuarios))
```

Explicacao: a funcao centraliza a chamada HTTP e evita repetir o mesmo tratamento de erro.

## 7. Filtrar usuarios por email

```python
import requests

url = "https://jsonplaceholder.typicode.com/users"
resposta = requests.get(url, timeout=10)
resposta.raise_for_status()

usuarios = resposta.json()

for usuario in usuarios:
    if usuario["email"].endswith(".biz"):
        print(usuario["name"], "-", usuario["email"])
```

Explicacao: `endswith()` verifica se o texto termina com uma parte especifica.

## 8. Calcular preco medio

```python
import requests

url = "https://dummyjson.com/products?limit=20"
resposta = requests.get(url, timeout=10)
resposta.raise_for_status()

produtos = resposta.json()["products"]

soma_precos = 0

for produto in produtos:
    soma_precos += produto["price"]

preco_medio = soma_precos / len(produtos)

print(f"Preco medio: US$ {preco_medio:.2f}")
```

Explicacao: somamos todos os precos e dividimos pela quantidade de produtos.

## 9. Produtos com estoque baixo

```python
import requests

url = "https://dummyjson.com/products?limit=100"
resposta = requests.get(url, timeout=10)
resposta.raise_for_status()

produtos = resposta.json()["products"]

for produto in produtos:
    if produto["stock"] < 30:
        print(
            produto["title"],
            produto["category"],
            produto["price"],
            produto["stock"],
        )
```

Explicacao: o filtro seleciona apenas produtos com estoque menor que 30.

## 10. API com pandas

```python
import pandas as pd
import requests

url = "https://dummyjson.com/products?limit=20"
resposta = requests.get(url, timeout=10)
resposta.raise_for_status()

produtos = resposta.json()["products"]
df = pd.DataFrame(produtos)

print(df[["title", "category", "price", "stock"]])
print(f"Preco medio: US$ {df['price'].mean():.2f}")
print("Estoque total:", df["stock"].sum())
```

Explicacao: pandas facilita calculos e selecao de colunas depois que os dados chegam da API.

## 11. Relatorio por categoria

```python
import pandas as pd
import requests

url = "https://dummyjson.com/products?limit=100"
resposta = requests.get(url, timeout=10)
resposta.raise_for_status()

produtos = resposta.json()["products"]
df = pd.DataFrame(produtos)

relatorio = df.groupby("category").agg(
    quantidade_produtos=("id", "count"),
    preco_medio=("price", "mean"),
    estoque_total=("stock", "sum"),
)

relatorio = relatorio.sort_values(by="estoque_total", ascending=False)

print(relatorio)
```

Explicacao: `groupby()` resume os produtos por categoria.

## 12. Consulta de clima

```python
import requests

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=-23.55&longitude=-46.63&current_weather=true"
)

resposta = requests.get(url, timeout=10)
resposta.raise_for_status()

dados = resposta.json()
clima_atual = dados["current_weather"]

print("Temperatura:", clima_atual["temperature"])
print("Velocidade do vento:", clima_atual["windspeed"])
print("Codigo do clima:", clima_atual["weathercode"])
print("Horario:", clima_atual["time"])
```

Explicacao: a Open-Meteo retorna os dados atuais dentro da chave `current_weather`.

## 13. Relatorio completo de produtos

```python
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


def carregar_produtos():
    dados = buscar_json("https://dummyjson.com/products?limit=100")

    if dados is None:
        return pd.DataFrame()

    return pd.DataFrame(dados["products"])


def gerar_relatorio(df):
    total_produtos = len(df)
    preco_medio = df["price"].mean()
    estoque_total = df["stock"].sum()
    produto_mais_caro = df.sort_values(by="price", ascending=False).iloc[0]
    produto_maior_desconto = df.sort_values(by="discountPercentage", ascending=False).iloc[0]
    categorias = sorted(df["category"].unique())
    estoque_baixo = df[df["stock"] < 20]

    print("Total de produtos:", total_produtos)
    print(f"Preco medio: US$ {preco_medio:.2f}")
    print("Estoque total:", estoque_total)
    print("Produto mais caro:", produto_mais_caro["title"])
    print("Produto com maior desconto:", produto_maior_desconto["title"])
    print("Categorias:", categorias)
    print("\nProdutos com estoque baixo:")
    print(estoque_baixo[["title", "category", "price", "stock"]])


produtos = carregar_produtos()

if not produtos.empty:
    gerar_relatorio(produtos)
```

Explicacao: o codigo foi dividido em funcoes para ficar mais organizado e proximo de um sistema real.
