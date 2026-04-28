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

    cursor.execute(
        "UPDATE produtos SET estoque = estoque - %s WHERE id_produto = %s",
        (1, 3),
    )
    conexao.commit()
    print("Produtos atualizados:", cursor.rowcount)

    cursor.execute(
        "DELETE FROM clientes WHERE email = %s",
        ("cliente.teste@email.com",),
    )
    conexao.commit()
    print("Clientes excluidos:", cursor.rowcount)

except mysql.connector.Error as erro:
    print("Erro ao alterar dados:", erro)

finally:
    if "cursor" in locals():
        cursor.close()
    if "conexao" in locals() and conexao.is_connected():
        conexao.close()
