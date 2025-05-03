from flask import Blueprint, jsonify

# Criando um Blueprint
contratos_bp = Blueprint("contratos", __name__)


# Rota GET simples
@contratos_bp.route("/contratos", methods=["GET"])
def listar_contratos():
    dados_exemplo = [
        {"id": 1, "cliente": "João"},
        {"id": 2, "cliente": "Maria"},
    ]
    return jsonify(dados_exemplo)
