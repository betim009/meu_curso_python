import mysql.connector


def get_connection():
    config = {
        "user": "root",
        "password": "1234",
        "host": "localhost",
        "database": "my_db2",
        "raise_on_warnings": True,
    }
    conn = mysql.connector.connect(**config)
    return conn, conn.cursor()
