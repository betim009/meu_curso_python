# 🔧 Construindo uma API REST com Flask e MySQL (sem ORM)

Este material ensina como criar uma API REST básica usando Flask com integração direta ao banco de dados MySQL, **sem uso de ORM** como SQLAlchemy. A ideia aqui é usar o `mysql.connector`, ideal para quem está aprendendo e quer ver o funcionamento "na unha".

---

## 📦 O que vamos aprender:

- Como criar uma estrutura básica com Flask
- Como conectar ao MySQL em Python
- Como implementar rotas GET, POST, PUT e DELETE
- Como retornar dados no formato JSON
- Como tratar conexão e evitar erros comuns
- Como organizar o código com separação de conexão

---

## 🛠 Requisitos

Antes de começar, você precisa:

### 1. Ter o MySQL instalado e um banco criado

No exemplo usamos um banco chamado `my_db2` com uma tabela `contratos`.

### 2. Instalar os pacotes:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows

pip install flask mysql-connector-python
```

---

## 🧩 Estrutura sugerida de arquivos

```
meu_projeto_api/
├── app.py           # Arquivo principal com as rotas Flask
├── connection.py    # Função de conexão com o MySQL
├── venv/            # Ambiente virtual Python
```

---

## ⚙️ Arquivo `connection.py` (refatorado)

```python
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
```

---

## 🚀 Arquivo `app.py` – Criando as Rotas da API

```python
from flask import Flask, jsonify, request
from connection import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"mensagem": "API Flask + MySQL funcionando!"})

@app.route("/contratos", methods=["GET"])
def get_contratos():
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM contratos")
    result = cursor.fetchall()
    contratos = []
    for row in result:
        contratos.append({
            "id": row[0],
            "cpf_cliente": row[1],
            "valor_parcela": format(float(row[2]), ".2f"),
        })
    cursor.close()
    conn.close()
    return jsonify(contratos)

@app.route("/contratos/<int:id>", methods=["GET"])
def get_contrato_id(id):
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM contratos WHERE id_contrato = %s", (id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        contrato = {
            "id": result[0],
            "cpf_cliente": result[1],
            "valor_parcela": format(float(result[2]), ".2f"),
        }
        return jsonify(contrato)
    else:
        return jsonify({"erro": f"Contrato com id {id} não encontrado."}), 404

@app.route("/contratos", methods=["POST"])
def inserir_contrato():
    data = request.get_json()
    conn, cursor = get_connection()

    cursor.execute(
        "INSERT INTO contratos (cpf_cliente, valor_parcela, data_contrato, status) VALUES (%s, %s, %s, %s)",
        (data["cpf_cliente"], data["valor_parcela"], data["data_contrato"], data["status"])
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"mensagem": "Contrato inserido com sucesso!"}), 201

@app.route("/contratos/<int:id>", methods=["PUT"])
def alterar_contrato(id):
    data = request.get_json()
    novo_valor = data.get("valor_parcela")

    conn, cursor = get_connection()
    cursor.execute(
        "UPDATE contratos SET valor_parcela = %s WHERE id_contrato = %s",
        (novo_valor, id)
    )
    conn.commit()
    sucesso = cursor.rowcount > 0
    cursor.close()
    conn.close()

    if sucesso:
        return jsonify({"mensagem": f"Contrato com id {id} alterado para R$ {float(novo_valor):.2f}"})
    else:
        return jsonify({"erro": f"Contrato com id {id} não encontrado"}), 404

@app.route("/contratos/<int:id>", methods=["DELETE"])
def deletar_contrato(id):
    conn, cursor = get_connection()
    cursor.execute("DELETE FROM contratos WHERE id_contrato = %s", (id,))
    conn.commit()
    sucesso = cursor.rowcount > 0
    cursor.close()
    conn.close()

    if sucesso:
        return jsonify({"mensagem": f"Contrato com id {id} removido com sucesso."})
    else:
        return jsonify({"erro": f"Contrato com id {id} não encontrado."}), 404

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 🧪 Como testar

Você pode usar o **Postman** ou **Insomnia**:

- `GET /contratos`
- `GET /contratos/1`
- `PUT /contratos/1` com body:

```json
{
  "valor_parcela": 250.44
}
```

---



### POST (inserir contrato)

```
POST http://localhost:5000/contratos
```

```json
{
  "cpf_cliente": "12345678900",
  "valor_parcela": 199.90,
  "data_contrato": "2024-09-01",
  "status": "Ativo"
}
```

---

### DELETE (remover contrato)

```
DELETE http://localhost:5000/contratos/1
```

---

## ✅ Conclusão

Você aprendeu a:

- Criar uma API com Flask
- Conectar ao MySQL com `mysql.connector`
- Evitar problemas fechando conexões dentro das rotas
- Implementar os métodos principais do CRUD

Esse projeto é base para qualquer sistema de gestão que use Python + MySQL!

[Acesse o projeto completo clicando aqui](https://github.com/betim009/meu_curso_python/tree/main/projetos/03_flaskAPI)