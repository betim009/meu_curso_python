import os

import mysql.connector


def conectar():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "curso_python_vendas"),
    )


def listar_estoque_baixo():
    try:
        conexao = conectar()
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("""
            SELECT nome, categoria, estoque
            FROM produtos
            WHERE estoque < 20
            ORDER BY estoque
        """)

        for produto in cursor.fetchall():
            print(produto["nome"], produto["categoria"], produto["estoque"])

    except mysql.connector.Error as erro:
        print("Erro:", erro)

    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


def cadastrar_cliente(nome, email, telefone, cidade):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            """
            INSERT INTO clientes (nome, email, telefone, cidade, data_cadastro)
            VALUES (%s, %s, %s, %s, CURDATE())
            """,
            (nome, email, telefone, cidade),
        )
        conexao.commit()
        print("Cliente cadastrado com id:", cursor.lastrowid)

    except mysql.connector.Error as erro:
        print("Erro ao cadastrar cliente:", erro)

    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


if __name__ == "__main__":
    listar_estoque_baixo()
