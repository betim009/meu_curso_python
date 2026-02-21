from db import connection


def select_all_produtos():
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT id, nome, categoria, preco, estoque, criado_em
        FROM produtos
        ORDER BY id
        """
    )
    produtos = cursor.fetchall()

    cursor.close()
    conn.close()

    return produtos

def showTables():
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
    """
    SHOW TABLES
    """)

    for table in cursor.fetchall():
        print(table)
    
    conn.close()    
