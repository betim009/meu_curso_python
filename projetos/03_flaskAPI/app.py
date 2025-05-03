from flask import Flask, jsonify, request
from connection import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mensagem": "API Flask + MySQL funcionando!"})

@app.route("/contratos", methods=["GET"])
def get_contratos():
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM contratos")
    result = cursor.fetchall()
    contratos = []
    for row in result:
        contratos.append({
            "id": row[0],
            "cpf_cliente": row[1],
            "valor_parcela": format(float(row[2]), ".2f"),
        })
    cursor.close()
    conn.close()
    return jsonify(contratos)

@app.route("/contratos/<int:id>", methods=["GET"])
def get_contrato_id(id):
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM contratos WHERE id_contrato = %s", (id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        contrato = {
            "id": result[0],
            "cpf_cliente": result[1],
            "valor_parcela": format(float(result[2]), ".2f"),
        }
        return jsonify(contrato)
    else:
        return jsonify({"erro": f"Contrato com id {id} não encontrado."}), 404

@app.route("/contratos", methods=["POST"])
def inserir_contrato():
    data = request.get_json()
    conn, cursor = get_connection()

    cursor.execute(
        "INSERT INTO contratos (cpf_cliente, valor_parcela, data_contrato, status) VALUES (%s, %s, %s, %s)",
        (data["cpf_cliente"], data["valor_parcela"], data["data_contrato"], data["status"])
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"mensagem": "Contrato inserido com sucesso!"}), 201

@app.route("/contratos/<int:id>", methods=["PUT"])
def alterar_contrato(id):
    data = request.get_json()
    novo_valor = data.get("valor_parcela")

    conn, cursor = get_connection()
    cursor.execute(
        "UPDATE contratos SET valor_parcela = %s WHERE id_contrato = %s",
        (novo_valor, id)
    )
    conn.commit()
    sucesso = cursor.rowcount > 0
    cursor.close()
    conn.close()

    if sucesso:
        return jsonify({"mensagem": f"Contrato com id {id} alterado para R$ {float(novo_valor):.2f}"})
    else:
        return jsonify({"erro": f"Contrato com id {id} não encontrado"}), 404

@app.route("/contratos/<int:id>", methods=["DELETE"])
def deletar_contrato(id):
    conn, cursor = get_connection()
    cursor.execute("DELETE FROM contratos WHERE id_contrato = %s", (id,))
    conn.commit()
    sucesso = cursor.rowcount > 0
    cursor.close()
    conn.close()

    if sucesso:
        return jsonify({"mensagem": f"Contrato com id {id} removido com sucesso."})
    else:
        return jsonify({"erro": f"Contrato com id {id} não encontrado."}), 404

if __name__ == "__main__":
    app.run(debug=True)