
# 🔁 Criando uma REST API com Flask

Este material é uma continuação do conteúdo básico sobre Flask, agora focado em **criar APIs RESTful** – que são muito utilizadas em sistemas modernos para troca de dados entre frontend e backend.

---

## 🧠 O que é uma API REST?

**API (Application Programming Interface)** é uma forma de fazer dois sistemas conversarem.  
**REST (Representational State Transfer)** é um estilo de arquitetura que usa **rotas e métodos HTTP** para criar, ler, atualizar e excluir dados (o famoso **CRUD**).

### 🚦 Métodos principais da REST API

| Método HTTP | O que faz?         | Exemplo |
|-------------|--------------------|---------|
| `GET`       | Buscar dados       | `/users` |
| `POST`      | Criar dados        | `/users` |
| `PUT`       | Atualizar dados    | `/users/1` |
| `DELETE`    | Remover dados      | `/users/1` |

---

## 📦 Instalando o Flask com suporte a JSON

Se você já instalou o Flask, não precisa repetir.

```bash
pip install flask
```

---

## 🧱 Estrutura de Projeto para API

```
api_flask/
├── app.py
└── venv/
```

---

## 🧰 Exemplo de API REST com Flask

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados simulados
usuarios = [
    {"id": 1, "nome": "João"},
    {"id": 2, "nome": "Maria"}
]

# GET - Retorna todos os usuários
@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    return jsonify(usuarios)

# GET - Retorna 1 usuário por ID
@app.route("/usuarios/<int:id>", methods=["GET"])
def get_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

# POST - Adiciona novo usuário
@app.route("/usuarios", methods=["POST"])
def add_usuario():
    data = request.get_json()
    novo_usuario = {
        "id": len(usuarios) + 1,
        "nome": data["nome"]
    }
    usuarios.append(novo_usuario)
    return jsonify(novo_usuario), 201

# PUT - Atualiza usuário
@app.route("/usuarios/<int:id>", methods=["PUT"])
def update_usuario(id):
    data = request.get_json()
    for usuario in usuarios:
        if usuario["id"] == id:
            usuario["nome"] = data["nome"]
            return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

# DELETE - Remove usuário
@app.route("/usuarios/<int:id>", methods=["DELETE"])
def delete_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuarios.remove(usuario)
            return jsonify({"mensagem": "Usuário removido com sucesso"})
    return jsonify({"erro": "Usuário não encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 🧪 Testando a API

Você pode testar com ferramentas como:

- [Postman](https://www.postman.com/)
- [Insomnia](https://insomnia.rest/)
- Ou com `curl` no terminal:

```bash
curl http://localhost:5000/usuarios
```

---

## ⚠️ Cuidados importantes

- Sempre valide os dados antes de salvar (`data.get("nome")`)
- Use códigos de status corretos (`201`, `404`, `200`)
- Em projetos reais, os dados não ficam em memória, mas sim num banco de dados

---

## 🧠 Conclusão

Você aprendeu:

- A estrutura básica de uma API REST em Flask
- Como criar rotas com GET, POST, PUT e DELETE
- Como manipular dados simulados em memória

Se quiser, posso criar a continuação usando **banco de dados SQLite ou MySQL**. Deseja seguir?
