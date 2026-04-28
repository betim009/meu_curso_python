from flask import Flask, jsonify


app = Flask(__name__)

clientes = [
    {"id": 1, "nome": "Ana Souza", "email": "ana@email.com", "cidade": "Sao Paulo"},
    {"id": 2, "nome": "Bruno Lima", "email": "bruno@email.com", "cidade": "Rio de Janeiro"},
    {"id": 3, "nome": "Carla Mendes", "email": "carla@email.com", "cidade": "Belo Horizonte"},
]


@app.route("/clientes", methods=["GET"])
def listar_clientes():
    return jsonify(clientes)


@app.route("/clientes/<int:id_cliente>", methods=["GET"])
def buscar_cliente(id_cliente):
    for cliente in clientes:
        if cliente["id"] == id_cliente:
            return jsonify(cliente)

    return jsonify({"erro": "Cliente nao encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)
