import mysql.connector

# Configurar os detalhes da conexão
config = {
    "user": "root",
    "password": "1234",  # sua senha
    "host": "localhost",  # ou o IP do servidor MySQL
    "database": "simple_user",
    "raise_on_warnings": True,
}

# Estabelecer a conexão
# Estabelecer a conexão
try:
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        print("Conexão estabelecida com sucesso!")

        # Cria um cursor para executar consultas
        cursor = connection.cursor()

        # Exemplo de uma consulta SELECT
        cursor.execute("SELECT * FROM users")

        # Recuperar todos os resultados da consulta
        resultados = cursor.fetchall()

        # Exibir os resultados
        for index, linha in enumerate(resultados):
            print(linha[1])

except mysql.connector.Error as err:
    print(f"Erro: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão encerrada.")
