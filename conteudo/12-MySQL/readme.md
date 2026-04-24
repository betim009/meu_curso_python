
# 🛠️ Conectando Python com Banco de Dados MySQL – Material Didático Completo

Este guia é feito especialmente para quem está começando a usar banco de dados com Python.  
Vamos aprender desde a **criação do banco no MySQL**, até **como conectar**, **fazer consultas** e **exibir resultados no terminal**.

---

## 🧱 Parte 0 – Criando o banco de dados no MySQL

Antes de conectar com o Python, é fundamental que o banco de dados **já exista** no MySQL.

### 📘 Script para criar o banco e uma tabela de exemplo:

```sql
DROP DATABASE IF EXISTS users_cont;

CREATE DATABASE users_cont;
USE users_cont;

CREATE TABLE contratos (
    id_contrato INT NOT NULL AUTO_INCREMENT,
    cpf_cliente VARCHAR(11) NOT NULL,
    valor_parcela DECIMAL(10, 2),
    data_contrato DATE,
    status VARCHAR(20),
    PRIMARY KEY (id_contrato)
);

INSERT INTO contratos (cpf_cliente, valor_parcela, data_contrato, status)
VALUES 
    ('12345678901', 120.50, '2023-01-10', 'Ativo'),
    ('98765432100', 200.75, '2023-03-15', 'Inativo'),
    ('15975345682', 150.25, '2023-06-20', 'Ativo'),
    ('75395185247', 175.50, '2023-07-05', 'Encerrado');
```

---

## 📦 Parte 1 – Instalando a biblioteca `mysql-connector-python`

Antes de começar, você precisa instalar o conector do MySQL:

### Com ambiente virtual (recomendado):

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install mysql-connector-python
```

---

## 🔌 Parte 2 – Conexão simples com MySQL

```python
import mysql.connector

config = {
    "user": "root",
    "password": "1234",  # sua senha do MySQL
    "host": "localhost",
    "database": "users_cont",
    "raise_on_warnings": True,
}

# Estabelece a conexão
connection = mysql.connector.connect(**config)

# Cria um cursor
cursor = connection.cursor()

# Consulta simples
cursor.execute("SELECT DATABASE();")
result = cursor.fetchone()
print(f"Banco de dados conectado: {result}")

# Finaliza
cursor.close()
connection.close()
print("Conexão encerrada.")
```

---

## ✅ Parte 3 – Conexão com tratamento de erro (`try/except`)

```python
import mysql.connector

config = {
    "user": "root",
    "password": "1234",
    "host": "localhost",
    "database": "users_cont",
    "raise_on_warnings": True,
}

try:
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        print("Conexão estabelecida com sucesso!")
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        result = cursor.fetchone()
        print(f"Banco de dados conectado: {result}")

except mysql.connector.Error as err:
    print(f"Erro: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão encerrada.")
```

### 🧠 Por que usar `try/except`?

- Para **capturar erros** como: senha errada, banco inexistente, servidor desligado.
- O programa não quebra e você vê **mensagens claras no terminal**.

---

## 📋 Parte 4 – SELECT com fetchall()

```python
import mysql.connector

config = {
    "user": "root",
    "password": "1234",
    "host": "localhost",
    "database": "users_cont",
    "raise_on_warnings": True,
}

# Conexão
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

# Executa SELECT
cursor.execute("SELECT * FROM contratos")
result = cursor.fetchall()

print("resultado do result:", result)

# Exibindo os dados linha por linha
for row in result:
    print({
        "id_contrato": row[0],
        "cpf_cliente": row[1],
        "valor_parcela": row[2],
        "data_contrato": row[3],
        "status": row[4]
    })

cursor.close()
connection.close()
print("Conexão encerrada.")
```

📤 Saída esperada no terminal:

```
resultado do result: [(1, '12345678901', 120.5, datetime.date(2023, 1, 10), 'Ativo'), ...]
{'id_contrato': 1, 'cpf_cliente': '12345678901', 'valor_parcela': 120.5, 'data_contrato': datetime.date(2023, 1, 10), 'status': 'Ativo'}
...
```

---

## ⚠️ Dicas e Cuidados

- Sempre feche a conexão e o cursor com `close()`.
- Use `try/except` para evitar travamentos por erro.
- Sempre confira se o banco e a tabela realmente existem no MySQL.
- Use `fetchall()` para várias linhas e `fetchone()` se espera um único valor.

---

Se quiser, posso continuar com `INSERT`, `UPDATE`, `DELETE`, filtros com `WHERE`, ou até paginação com `LIMIT`. Deseja?
