
from flask import Blueprint, jsonify, request
from connection import get_connection
from middlewares.validate_users import validar_nome, validar_email, validar_senha
from models.user_model import check_user_email_exists

user_bp = Blueprint('user_bp', __name__)

@user_bp.route("/")
def hello_world():
    return jsonify({"message": "Hello, World!"})

@user_bp.route("/usuarios", methods=["GET"])
def get_usuarios():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    resultado = []
    for u in usuarios:
        resultado.append({
            "id": u[0],
            "name": u[1],
            "email": u[2],
            "password": u[3]
        })
    cursor.close()
    conn.close()
    return jsonify(resultado)

@user_bp.route("/usuarios/<int:id>", methods=["GET"])
def get_usuario_by_id(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM usuarios WHERE id = %s", (id,))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    if usuario:
        return jsonify({
            "id": usuario[0],
            "name": usuario[1],
            "email": usuario[2]
        })
    return jsonify({"error": "Usuário não encontrado"}), 404

@user_bp.route("/usuarios", methods=["POST"])
def create_usuario():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    nome_valido = validar_nome(name)
    email_valido = validar_email(email)
    senha_valida = validar_senha(password)

    if nome_valido["error"]:
        return jsonify(nome_valido), 400
    if email_valido["error"]:
        return jsonify(email_valido), 400
    if senha_valida["error"]:
        return jsonify(senha_valida), 400
    if check_user_email_exists(email):
        return jsonify({"error": "Email já cadastrado"}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    conn.commit()
    user_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return jsonify({"message": "Usuário criado com sucesso", "id": user_id}), 201

@user_bp.route("/usuarios/<int:id>", methods=["PUT"])
def update_usuario(id):
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
    usuario = cursor.fetchone()

    if not usuario:
        cursor.close()
        conn.close()
        return jsonify({"error": "Usuário não encontrado"}), 404

    cursor.execute("UPDATE usuarios SET name=%s, email=%s, password=%s WHERE id=%s", (name, email, password, id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Usuário atualizado", "id": id})

@user_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def delete_usuario(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
    usuario = cursor.fetchone()

    if not usuario:
        cursor.close()
        conn.close()
        return jsonify({"error": "Usuário não encontrado"}), 404

    cursor.execute("DELETE FROM usuarios WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Usuário deletado", "id": id})
