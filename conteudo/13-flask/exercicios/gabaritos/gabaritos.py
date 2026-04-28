from flask import Flask, jsonify, request


app = Flask(__name__)

clientes = [
    {"id": 1, "nome": "Ana Souza", "email": "ana@email.com", "cidade": "Sao Paulo"},
    {"id": 2, "nome": "Bruno Lima", "email": "bruno@email.com", "cidade": "Rio de Janeiro"},
]

produtos = [
    {"id": 1, "nome": "Notebook Pro", "categoria": "Computadores", "preco": 4299.0, "estoque": 12},
    {"id": 2, "nome": "Mouse sem fio", "categoria": "Perifericos", "preco": 89.9, "estoque": 55},
]

pedidos = [
    {"id": 1, "cliente": "Ana Souza", "produto": "Notebook Pro", "quantidade": 1, "total": 4299.0},
]


def buscar_por_id(lista, id_item):
    for item in lista:
        if item["id"] == id_item:
            return item
    return None


@app.route("/")
def home():
    return jsonify({"mensagem": "API de exercicios Flask"})


@app.route("/status")
def status():
    return jsonify({"status": "online"})


@app.route("/clientes", methods=["GET"])
def listar_clientes():
    return jsonify(clientes)


@app.route("/clientes/<int:id_cliente>", methods=["GET"])
def buscar_cliente(id_cliente):
    cliente = buscar_por_id(clientes, id_cliente)

    if cliente is None:
        return jsonify({"erro": "Cliente nao encontrado"}), 404

    return jsonify(cliente)


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


@app.route("/produtos", methods=["GET"])
def listar_produtos():
    categoria = request.args.get("categoria")

    if categoria:
        filtrados = [produto for produto in produtos if produto["categoria"] == categoria]
        return jsonify(filtrados)

    return jsonify(produtos)


@app.route("/produtos", methods=["POST"])
def cadastrar_produto():
    dados = request.get_json() or {}

    campos_obrigatorios = ["nome", "categoria", "preco"]
    for campo in campos_obrigatorios:
        if dados.get(campo) is None:
            return jsonify({"erro": f"{campo} e obrigatorio"}), 400

    novo_produto = {
        "id": len(produtos) + 1,
        "nome": dados["nome"],
        "categoria": dados["categoria"],
        "preco": float(dados["preco"]),
        "estoque": int(dados.get("estoque", 0)),
    }

    produtos.append(novo_produto)

    return jsonify(novo_produto), 201


@app.route("/pedidos", methods=["GET"])
def listar_pedidos():
    return jsonify(pedidos)


@app.route("/pedidos/<int:id_pedido>", methods=["GET"])
def buscar_pedido(id_pedido):
    pedido = buscar_por_id(pedidos, id_pedido)

    if pedido is None:
        return jsonify({"erro": "Pedido nao encontrado"}), 404

    return jsonify(pedido)


@app.route("/pedidos", methods=["POST"])
def criar_pedido():
    dados = request.get_json() or {}

    campos_obrigatorios = ["cliente", "produto", "quantidade", "valor_unitario"]
    for campo in campos_obrigatorios:
        if dados.get(campo) is None:
            return jsonify({"erro": f"{campo} e obrigatorio"}), 400

    quantidade = int(dados["quantidade"])
    valor_unitario = float(dados["valor_unitario"])

    novo_pedido = {
        "id": len(pedidos) + 1,
        "cliente": dados["cliente"],
        "produto": dados["produto"],
        "quantidade": quantidade,
        "valor_unitario": valor_unitario,
        "total": quantidade * valor_unitario,
    }

    pedidos.append(novo_pedido)

    return jsonify(novo_pedido), 201


if __name__ == "__main__":
    app.run(debug=True)
