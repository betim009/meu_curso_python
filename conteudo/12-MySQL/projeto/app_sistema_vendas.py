import os

import mysql.connector


def conectar():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "curso_python_vendas"),
    )


def cadastrar_cliente(nome, email, telefone, cidade):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO clientes (nome, email, telefone, cidade, data_cadastro)
            VALUES (%s, %s, %s, %s, CURDATE())
            """,
            (nome, email, telefone, cidade),
        )
        conexao.commit()
        print("Cliente cadastrado com id:", cursor.lastrowid)
    finally:
        cursor.close()
        conexao.close()


def cadastrar_produto(nome, categoria, preco, estoque):
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO produtos (nome, categoria, preco, estoque, ativo)
            VALUES (%s, %s, %s, %s, TRUE)
            """,
            (nome, categoria, preco, estoque),
        )
        conexao.commit()
        print("Produto cadastrado com id:", cursor.lastrowid)
    finally:
        cursor.close()
        conexao.close()


def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT id_cliente, nome, email, cidade
            FROM clientes
            ORDER BY nome
        """)
        for cliente in cursor.fetchall():
            print(cliente)
    finally:
        cursor.close()
        conexao.close()


def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT id_produto, nome, categoria, preco, estoque
            FROM produtos
            WHERE ativo = TRUE
            ORDER BY nome
        """)
        for produto in cursor.fetchall():
            print(produto)
    finally:
        cursor.close()
        conexao.close()


def registrar_pedido(id_cliente, forma_pagamento, itens):
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute(
            """
            INSERT INTO pedidos (id_cliente, data_pedido, status, forma_pagamento)
            VALUES (%s, CURDATE(), 'Pago', %s)
            """,
            (id_cliente, forma_pagamento),
        )
        id_pedido = cursor.lastrowid

        for item in itens:
            id_produto = item["id_produto"]
            quantidade = item["quantidade"]

            cursor.execute(
                "SELECT preco, estoque FROM produtos WHERE id_produto = %s",
                (id_produto,),
            )
            produto = cursor.fetchone()

            if produto is None:
                raise ValueError(f"Produto {id_produto} nao encontrado.")

            if produto["estoque"] < quantidade:
                raise ValueError(f"Estoque insuficiente para o produto {id_produto}.")

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
        print("Pedido registrado com id:", id_pedido)

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()


def listar_pedidos_com_total():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
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
        for pedido in cursor.fetchall():
            print(pedido)
    finally:
        cursor.close()
        conexao.close()


def relatorio_faturamento_por_produto():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("""
            SELECT
                pr.nome,
                pr.categoria,
                SUM(i.quantidade) AS unidades_vendidas,
                SUM(i.quantidade * i.preco_unitario) AS faturamento
            FROM itens_pedido i
            INNER JOIN produtos pr ON i.id_produto = pr.id_produto
            INNER JOIN pedidos p ON i.id_pedido = p.id_pedido
            WHERE p.status = 'Pago'
            GROUP BY pr.id_produto, pr.nome, pr.categoria
            ORDER BY faturamento DESC
        """)
        for linha in cursor.fetchall():
            print(linha)
    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    print("=== CLIENTES ===")
    listar_clientes()

    print("\n=== PRODUTOS ===")
    listar_produtos()

    print("\n=== PEDIDOS COM TOTAL ===")
    listar_pedidos_com_total()

    print("\n=== FATURAMENTO POR PRODUTO ===")
    relatorio_faturamento_por_produto()
