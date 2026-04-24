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
connection = mysql.connector.connect(**config)

# Cria um cursor para executar consultas
cursor = connection.cursor()

# Exemplo de uma consulta SELECT
cursor.execute("SELECT * FROM users")

# Recuperar todos os resultados da consulta
result = cursor.fetchall()

print('resultado do result:', result)

# Exibindo em formato de lista de dicionário
for row in result:
    print({
        "id": row[0], "user": row[1], "url": row[2]
    })

# Encerrando
cursor.close()
connection.close()
print("Conexão encerrada.")
