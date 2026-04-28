from flask import Flask, jsonify, request
from mysql.connector import Error

from database import conectar


app = Flask(__name__)


def resposta_erro(mensagem, status=400):
    return jsonify({"erro": mensagem}), status


def preparar_json(valor):
    if hasattr(valor, "isoformat"):
        return valor.isoformat()

    if hasattr(valor, "__float__") and valor.__class__.__name__ == "Decimal":
        return float(valor)

    return valor


def preparar_linha(linha):
    return {chave: preparar_json(valor) for chave, valor in linha.items()}


def preparar_lista(linhas):
    return [preparar_linha(linha) for linha in linhas]


@app.route("/")
def home():
    return jsonify({"mensagem": "API de vendas com Flask e MySQL"})


@app.route("/status")
def status():
    return jsonify({"status": "online"})


@app.route("/clientes", methods=["GET"])
def listar_clientes():
    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT id_cliente, nome, email, cidade FROM clientes ORDER BY nome")
        clientes = cursor.fetchall()
        return jsonify(preparar_lista(clientes))
    except Error as erro:
        return resposta_erro(f"Erro ao buscar clientes: {erro}", 500)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


@app.route("/clientes/<int:id_cliente>", methods=["GET"])
def buscar_cliente(id_cliente):
    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(
            "SELECT id_cliente, nome, email, cidade FROM clientes WHERE id_cliente = %s",
            (id_cliente,),
        )
        cliente = cursor.fetchone()

        if cliente is None:
            return resposta_erro("Cliente nao encontrado", 404)

        return jsonify(preparar_linha(cliente))
    except Error as erro:
        return resposta_erro(f"Erro ao buscar cliente: {erro}", 500)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


@app.route("/clientes", methods=["POST"])
def cadastrar_cliente():
    dados = request.get_json() or {}

    for campo in ["nome", "email"]:
        if not dados.get(campo):
            return resposta_erro(f"{campo} e obrigatorio", 400)

    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, email, cidade) VALUES (%s, %s, %s)",
            (dados["nome"], dados["email"], dados.get("cidade")),
        )
        conexao.commit()
        return jsonify({"id_cliente": cursor.lastrowid, "mensagem": "Cliente cadastrado"}), 201
    except Error as erro:
        return resposta_erro(f"Erro ao cadastrar cliente: {erro}", 500)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


@app.route("/produtos", methods=["GET"])
def listar_produtos():
    categoria = request.args.get("categoria")

    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)

        if categoria:
            cursor.execute(
                """
                SELECT id_produto, nome, categoria, preco, estoque
                FROM produtos
                WHERE categoria = %s
                ORDER BY nome
                """,
                (categoria,),
            )
        else:
            cursor.execute("""
                SELECT id_produto, nome, categoria, preco, estoque
                FROM produtos
                ORDER BY nome
            """)

        produtos = cursor.fetchall()
        return jsonify(preparar_lista(produtos))
    except Error as erro:
        return resposta_erro(f"Erro ao buscar produtos: {erro}", 500)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


@app.route("/produtos/<int:id_produto>", methods=["GET"])
def buscar_produto(id_produto):
    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT id_produto, nome, categoria, preco, estoque
            FROM produtos
            WHERE id_produto = %s
            """,
            (id_produto,),
        )
        produto = cursor.fetchone()

        if produto is None:
            return resposta_erro("Produto nao encontrado", 404)

        return jsonify(preparar_linha(produto))
    except Error as erro:
        return resposta_erro(f"Erro ao buscar produto: {erro}", 500)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


@app.route("/produtos", methods=["POST"])
def cadastrar_produto():
    dados = request.get_json() or {}

    for campo in ["nome", "categoria", "preco"]:
        if dados.get(campo) is None:
            return resposta_erro(f"{campo} e obrigatorio", 400)

    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            """
            INSERT INTO produtos (nome, categoria, preco, estoque)
            VALUES (%s, %s, %s, %s)
            """,
            (
                dados["nome"],
                dados["categoria"],
                dados["preco"],
                dados.get("estoque", 0),
            ),
        )
        conexao.commit()
        return jsonify({"id_produto": cursor.lastrowid, "mensagem": "Produto cadastrado"}), 201
    except Error as erro:
        return resposta_erro(f"Erro ao cadastrar produto: {erro}", 500)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


@app.route("/pedidos", methods=["GET"])
def listar_pedidos():
    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("""
            SELECT
                p.id_pedido,
                c.nome AS cliente,
                p.data_pedido,
                p.status,
                SUM(i.quantidade * i.preco_unitario) AS total
            FROM pedidos p
            INNER JOIN clientes c ON p.id_cliente = c.id_cliente
            INNER JOIN itens_pedido i ON p.id_pedido = i.id_pedido
            GROUP BY p.id_pedido, c.nome, p.data_pedido, p.status
            ORDER BY p.data_pedido DESC
        """)
        pedidos = cursor.fetchall()
        return jsonify(preparar_lista(pedidos))
    except Error as erro:
        return resposta_erro(f"Erro ao buscar pedidos: {erro}", 500)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


@app.route("/pedidos", methods=["POST"])
def criar_pedido():
    dados = request.get_json() or {}

    if not dados.get("id_cliente"):
        return resposta_erro("id_cliente e obrigatorio", 400)

    itens = dados.get("itens", [])
    if not itens:
        return resposta_erro("O pedido precisa ter pelo menos um item", 400)

    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)

        cursor.execute(
            "INSERT INTO pedidos (id_cliente, status) VALUES (%s, 'Pago')",
            (dados["id_cliente"],),
        )
        id_pedido = cursor.lastrowid

        for item in itens:
            id_produto = item.get("id_produto")
            quantidade = int(item.get("quantidade", 0))

            if not id_produto or quantidade <= 0:
                conexao.rollback()
                return resposta_erro("Item invalido no pedido", 400)

            cursor.execute(
                "SELECT preco, estoque FROM produtos WHERE id_produto = %s",
                (id_produto,),
            )
            produto = cursor.fetchone()

            if produto is None:
                conexao.rollback()
                return resposta_erro(f"Produto {id_produto} nao encontrado", 404)

            if produto["estoque"] < quantidade:
                conexao.rollback()
                return resposta_erro(f"Estoque insuficiente para produto {id_produto}", 400)

            cursor.execute(
                """
                INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, preco_unitario)
                VALUES (%s, %s, %s, %s)
                """,
                (id_pedido, id_produto, quantidade, produto["preco"]),
            )
            cursor.execute(
                "UPDATE produtos SET estoque = estoque - %s WHERE id_produto = %s",
                (quantidade, id_produto),
            )

        conexao.commit()

        return jsonify({"id_pedido": id_pedido, "mensagem": "Pedido criado"}), 201
    except Error as erro:
        if "conexao" in locals() and conexao.is_connected():
            conexao.rollback()
        return resposta_erro(f"Erro ao criar pedido: {erro}", 500)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


if __name__ == "__main__":
    app.run(debug=True)
