import mysql.connector

# Configurar os detalhes da conexão
config = {
    "user": "root",
    "password": "1234",  # sua senha
    "host": "localhost",  # ou o IP do servidor MySQL
    "database": "my_db2",
    "raise_on_warnings": True,
}

# Estabelecer a conexão
connection = mysql.connector.connect(**config)

# Cria um cursor para executar consultas
cursor = connection.cursor()

# Exemplo de uma consulta simples
cursor.execute("SELECT DATABASE();")
result = cursor.fetchone()
print(f"Banco de dados conectado: {result}")

# Encerrando
cursor.close()
connection.close()
print("Conexão encerrada.")
