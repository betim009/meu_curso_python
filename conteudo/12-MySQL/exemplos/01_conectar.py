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

    cursor.execute("SELECT DATABASE() AS banco_conectado")
    print(cursor.fetchone())

except mysql.connector.Error as erro:
    print("Erro ao conectar no MySQL:", erro)

finally:
    if "cursor" in locals():
        cursor.close()
    if "conexao" in locals() and conexao.is_connected():
        conexao.close()
