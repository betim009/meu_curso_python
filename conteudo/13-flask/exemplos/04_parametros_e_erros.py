from flask import Flask, jsonify, request


app = Flask(__name__)

pedidos = [
    {"id": 1, "cliente": "Ana Souza", "status": "pago", "total": 4498.80},
    {"id": 2, "cliente": "Bruno Lima", "status": "pendente", "total": 899.90},
    {"id": 3, "cliente": "Carla Mendes", "status": "pago", "total": 1299.00},
]


@app.route("/pedidos", methods=["GET"])
def listar_pedidos():
    status = request.args.get("status")

    if status:
        filtrados = [pedido for pedido in pedidos if pedido["status"] == status]
        return jsonify(filtrados)

    return jsonify(pedidos)


@app.route("/pedidos/<int:id_pedido>", methods=["GET"])
def buscar_pedido(id_pedido):
    for pedido in pedidos:
        if pedido["id"] == id_pedido:
            return jsonify(pedido)

    return jsonify({"erro": "Pedido nao encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)
