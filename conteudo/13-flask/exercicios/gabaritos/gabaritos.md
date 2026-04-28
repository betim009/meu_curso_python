# Gabaritos Comentados - Flask

## 1. Rota de status

```python
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/status")
def status():
    return jsonify({"status": "online"})
```

Explicacao: `jsonify()` transforma o dicionario Python em resposta JSON.

## 2. Listar clientes

```python
clientes = [
    {"id": 1, "nome": "Ana Souza"},
    {"id": 2, "nome": "Bruno Lima"},
    {"id": 3, "nome": "Carla Mendes"},
]


@app.route("/clientes", methods=["GET"])
def listar_clientes():
    return jsonify(clientes)
```

Explicacao: `GET` e usado para buscar dados.

## 3. Buscar cliente por ID

```python
@app.route("/clientes/<int:id_cliente>", methods=["GET"])
def buscar_cliente(id_cliente):
    for cliente in clientes:
        if cliente["id"] == id_cliente:
            return jsonify(cliente)

    return jsonify({"erro": "Cliente nao encontrado"}), 404
```

Explicacao: se o item nao existe, a API deve retornar `404`.

## 4. Listar produtos

```python
produtos = [
    {"id": 1, "nome": "Notebook Pro", "preco": 4299.0, "estoque": 12},
    {"id": 2, "nome": "Mouse sem fio", "preco": 89.9, "estoque": 55},
]


@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)
```

Explicacao: uma lista de dicionarios vira uma lista JSON.

## 5. Mensagem inicial

```python
@app.route("/")
def home():
    return jsonify({"mensagem": "API funcionando"})
```

Explicacao: a rota `/` costuma ser usada como entrada da API.

## 6. Cadastrar cliente com POST

```python
from flask import request


@app.route("/clientes", methods=["POST"])
def cadastrar_cliente():
    dados = request.get_json()

    novo_cliente = {
        "id": len(clientes) + 1,
        "nome": dados["nome"],
        "email": dados["email"],
        "cidade": dados["cidade"],
    }

    clientes.append(novo_cliente)

    return jsonify(novo_cliente), 201
```

Explicacao: `request.get_json()` le o corpo JSON enviado pelo cliente da API.

## 7. Validar campo obrigatorio

```python
@app.route("/clientes", methods=["POST"])
def cadastrar_cliente():
    dados = request.get_json() or {}

    if not dados.get("nome"):
        return jsonify({"erro": "Nome e obrigatorio"}), 400

    novo_cliente = {
        "id": len(clientes) + 1,
        "nome": dados["nome"],
        "email": dados.get("email"),
        "cidade": dados.get("cidade"),
    }

    clientes.append(novo_cliente)

    return jsonify(novo_cliente), 201
```

Explicacao: `.get()` evita erro quando a chave nao existe.

## 8. Filtrar produtos por categoria

```python
@app.route("/produtos", methods=["GET"])
def listar_produtos():
    categoria = request.args.get("categoria")

    if categoria:
        filtrados = [produto for produto in produtos if produto["categoria"] == categoria]
        return jsonify(filtrados)

    return jsonify(produtos)
```

Explicacao: `request.args` acessa parametros da URL.

## 9. Buscar pedido por ID

```python
@app.route("/pedidos/<int:id_pedido>", methods=["GET"])
def buscar_pedido(id_pedido):
    for pedido in pedidos:
        if pedido["id"] == id_pedido:
            return jsonify(pedido)

    return jsonify({"erro": "Pedido nao encontrado"}), 404
```

Explicacao: o padrao e o mesmo da busca de cliente por id.

## 10. Criar pedido

```python
@app.route("/pedidos", methods=["POST"])
def criar_pedido():
    dados = request.get_json() or {}

    quantidade = int(dados["quantidade"])
    valor_unitario = float(dados["valor_unitario"])

    pedido = {
        "id": len(pedidos) + 1,
        "cliente": dados["cliente"],
        "produto": dados["produto"],
        "quantidade": quantidade,
        "valor_unitario": valor_unitario,
        "total": quantidade * valor_unitario,
    }

    pedidos.append(pedido)

    return jsonify(pedido), 201
```

Explicacao: o backend pode calcular dados antes de salvar.

## 11. API organizada por recurso

Veja o arquivo `gabaritos.py`. Ele contem uma API completa com clientes, produtos e pedidos em memoria.

## 12. Integração com MySQL

```python
import os
import mysql.connector


def conectar():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "curso_flask_api"),
    )


@app.route("/clientes", methods=["GET"])
def listar_clientes_mysql():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT id_cliente, nome, email, cidade FROM clientes")
    clientes = cursor.fetchall()
    cursor.close()
    conexao.close()
    return jsonify(clientes)
```

Explicacao: a rota consulta o banco e transforma o resultado em JSON.

## 13. API com validação e status

O gabarito completo usa:

- `400` quando faltam campos;
- `404` quando recurso nao existe;
- `201` quando cria um registro;
- `200` quando consulta com sucesso.
