import os

import mysql.connector


def conectar():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "curso_python_vendas"),
    )


try:
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("""
        SELECT id_cliente, nome, email, cidade
        FROM clientes
        ORDER BY nome
    """)

    clientes = cursor.fetchall()

    for cliente in clientes:
        print(f"{cliente['id_cliente']} - {cliente['nome']} - {cliente['email']} - {cliente['cidade']}")

except mysql.connector.Error as erro:
    print("Erro ao consultar clientes:", erro)

finally:
    if "cursor" in locals():
        cursor.close()
    if "conexao" in locals() and conexao.is_connected():
        conexao.close()
