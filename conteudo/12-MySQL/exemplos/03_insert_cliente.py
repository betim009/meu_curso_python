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
    cursor = conexao.cursor()

    sql = """
        INSERT INTO clientes (nome, email, telefone, cidade, data_cadastro)
        VALUES (%s, %s, %s, %s, CURDATE())
    """
    valores = ("Fernanda Torres", "fernanda.torres@email.com", "51999990006", "Porto Alegre")

    cursor.execute(sql, valores)
    conexao.commit()

    print("Cliente cadastrado com id:", cursor.lastrowid)

except mysql.connector.Error as erro:
    print("Erro ao inserir cliente:", erro)

finally:
    if "cursor" in locals():
        cursor.close()
    if "conexao" in locals() and conexao.is_connected():
        conexao.close()
