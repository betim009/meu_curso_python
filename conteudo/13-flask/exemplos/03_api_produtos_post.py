from flask import Flask, jsonify, request


app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Notebook Pro", "preco": 4299.0, "estoque": 12},
    {"id": 2, "nome": "Mouse sem fio", "preco": 89.9, "estoque": 55},
]


@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)


@app.route("/produtos", methods=["POST"])
def cadastrar_produto():
    dados = request.get_json() or {}

    if not dados.get("nome"):
        return jsonify({"erro": "Nome e obrigatorio"}), 400

    if dados.get("preco") is None:
        return jsonify({"erro": "Preco e obrigatorio"}), 400

    novo_produto = {
        "id": len(produtos) + 1,
        "nome": dados["nome"],
        "preco": float(dados["preco"]),
        "estoque": int(dados.get("estoque", 0)),
    }

    produtos.append(novo_produto)

    return jsonify(novo_produto), 201


if __name__ == "__main__":
    app.run(debug=True)
