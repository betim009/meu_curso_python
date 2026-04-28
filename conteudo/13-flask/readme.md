# 13 - Flask para Backend e APIs

Neste modulo voce vai aprender a criar aplicacoes web e APIs usando Python com Flask.

Ate aqui, voce consumiu APIs com `requests`, trabalhou com pandas, graficos e banco de dados MySQL. Agora voce vai aprender o outro lado: criar uma API para que outros sistemas possam consumir os seus dados.

O foco sera backend de sistemas reais: clientes, produtos e pedidos.

## Estrutura do modulo

```text
13-flask/
  README.md
  exemplos/
    01_primeira_rota.py
    02_api_clientes_get.py
    03_api_produtos_post.py
    04_parametros_e_erros.py
  exercicios/
    exercicios.md
    gabaritos/
      gabaritos.md
      gabaritos.py
  projeto/
    README.md
    app.py
    database.py
    schema.sql
```

## 1. Introducao

### O que e backend?

Backend e a parte do sistema que roda no servidor.

Ele geralmente cuida de:

- receber requisicoes;
- validar dados;
- consultar banco de dados;
- salvar informacoes;
- aplicar regras de negocio;
- devolver respostas para o frontend ou para outros sistemas.

Quando voce usa um aplicativo, a tela que voce ve e o frontend. A parte que salva cadastro, busca produtos e registra pedidos e o backend.

### O que e uma API?

API e uma forma padronizada de um sistema conversar com outro.

Exemplo:

- um frontend pede a lista de produtos;
- o backend consulta o banco;
- a API retorna os produtos em JSON.

Uma API nao precisa mostrar uma pagina HTML. Muitas vezes ela retorna dados.

### Como sistemas web funcionam?

Um fluxo simples:

1. O usuario ou sistema faz uma requisicao HTTP.
2. O Flask recebe essa requisicao em uma rota.
3. A funcao da rota executa uma regra.
4. O backend consulta ou altera dados.
5. A API devolve uma resposta, geralmente em JSON.

Exemplo:

```text
GET /clientes
```

Resposta:

```json
[
  {"id": 1, "nome": "Ana Souza"},
  {"id": 2, "nome": "Bruno Lima"}
]
```

## 2. Instalando Flask

Instale o Flask:

```bash
pip install flask
```

Para projetos com MySQL:

```bash
pip install flask mysql-connector-python
```

Para conferir:

```bash
python3 -c "import flask; print(flask.__version__)"
```

## 3. Criando aplicacao

Crie um arquivo `app.py`:

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "API Flask funcionando!"


if __name__ == "__main__":
    app.run(debug=True)
```

Execute:

```bash
python3 app.py
```

Acesse:

```text
http://127.0.0.1:5000
```

### Explicando o codigo

- `Flask(__name__)` cria a aplicacao.
- `@app.route("/")` define uma rota.
- `home()` e a funcao executada quando a rota for acessada.
- `return` envia a resposta.
- `app.run(debug=True)` inicia o servidor local.

## 4. Rotas ou endpoints

Rota e um endereco da API.

Endpoint e uma rota criada para uma finalidade especifica.

Exemplos:

| Metodo | Endpoint | Finalidade |
|---|---|---|
| GET | `/clientes` | listar clientes |
| GET | `/clientes/1` | buscar cliente por id |
| POST | `/clientes` | cadastrar cliente |
| GET | `/produtos` | listar produtos |
| POST | `/produtos` | cadastrar produto |

### GET

`GET` busca dados.

```python
from flask import Flask, jsonify

app = Flask(__name__)

clientes = [
    {"id": 1, "nome": "Ana Souza"},
    {"id": 2, "nome": "Bruno Lima"},
]


@app.route("/clientes", methods=["GET"])
def listar_clientes():
    return jsonify(clientes)
```

### GET por ID

```python
@app.route("/clientes/<int:id_cliente>", methods=["GET"])
def buscar_cliente(id_cliente):
    for cliente in clientes:
        if cliente["id"] == id_cliente:
            return jsonify(cliente)

    return jsonify({"erro": "Cliente nao encontrado"}), 404
```

`<int:id_cliente>` significa que a rota recebe um numero.

### POST

`POST` cria dados.

```python
from flask import request


@app.route("/clientes", methods=["POST"])
def cadastrar_cliente():
    dados = request.get_json()

    novo_cliente = {
        "id": len(clientes) + 1,
        "nome": dados["nome"],
        "email": dados["email"],
    }

    clientes.append(novo_cliente)

    return jsonify(novo_cliente), 201
```

`request.get_json()` pega o JSON enviado no corpo da requisicao.

## 5. Retorno de dados

APIs geralmente retornam JSON.

JSON e um formato de dados que combina bem com dicionarios e listas do Python.

```python
from flask import jsonify

return jsonify({"mensagem": "Cliente cadastrado"})
```

### Codigo de status

Uma resposta de API deve informar se deu certo ou errado.

Codigos comuns:

| Codigo | Significado |
|---:|---|
| 200 | sucesso |
| 201 | criado |
| 400 | erro nos dados enviados |
| 404 | nao encontrado |
| 500 | erro interno |

Exemplo:

```python
return jsonify({"erro": "Nome e obrigatorio"}), 400
```

## 6. Integracao com banco

Em projetos reais, dados nao ficam em listas dentro do codigo. Eles ficam no banco.

Com MySQL:

```python
import os
import mysql.connector


def conectar():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "curso_flask_api"),
    )
```

### Buscar dados no banco

```python
@app.route("/clientes", methods=["GET"])
def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT id_cliente, nome, email, cidade FROM clientes")
    clientes = cursor.fetchall()

    cursor.close()
    conexao.close()

    return jsonify(clientes)
```

### Inserir dados no banco

```python
@app.route("/clientes", methods=["POST"])
def cadastrar_cliente():
    dados = request.get_json()

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO clientes (nome, email, cidade)
        VALUES (%s, %s, %s)
        """,
        (dados["nome"], dados["email"], dados["cidade"]),
    )

    conexao.commit()
    id_cliente = cursor.lastrowid

    cursor.close()
    conexao.close()

    return jsonify({"id_cliente": id_cliente}), 201
```

Use parametros `%s` para evitar SQL injection e problemas com textos.

## 7. Organizacao do codigo

Para aprender, um arquivo unico funciona. Para projeto real, separe responsabilidades.

Exemplo:

```text
projeto/
  app.py        # rotas da API
  database.py   # conexao com MySQL
  schema.sql    # criacao do banco
```

No `database.py`, coloque a conexao.

No `app.py`, coloque as rotas.

Essa separacao evita repeticao e deixa o codigo mais facil de manter.

## 8. Boas praticas

### Use rotas claras

Prefira:

```text
/clientes
/clientes/1
/produtos
/pedidos
```

Evite:

```text
/pegar
/dados
/coisas
```

### Valide dados de entrada

Antes de salvar:

```python
if not dados.get("nome"):
    return jsonify({"erro": "Nome e obrigatorio"}), 400
```

### Retorne status correto

- `200`: consulta OK;
- `201`: cadastro criado;
- `400`: dados invalidos;
- `404`: item nao encontrado.

### Feche conexoes

Sempre feche cursor e conexao com banco.

### Nao exponha senha no codigo

Use variaveis de ambiente:

```bash
export MYSQL_PASSWORD="sua_senha"
```

## 9. Erros comuns

### Rota mal definida

Erro:

```python
@app.route("clientes")
```

Certo:

```python
@app.route("/clientes")
```

### Retorno errado

Erro comum: retornar lista Python diretamente em versões antigas ou retornar tipos que nao viram JSON.

Use:

```python
return jsonify(lista)
```

### Esquecer methods no POST

```python
@app.route("/clientes", methods=["POST"])
```

Sem isso, a rota aceita `GET` por padrao.

### Problemas de conexao

Causas comuns:

- MySQL desligado;
- banco nao criado;
- senha errada;
- biblioteca nao instalada.

### Esquecer commit

Depois de `INSERT`, `UPDATE` ou `DELETE`:

```python
conexao.commit()
```

## 10. Mini desafios

### Mini desafio 1

Crie uma rota `/status` que retorne:

```json
{"status": "online"}
```

### Mini desafio 2

Crie uma rota `GET /clientes` que retorne uma lista em memoria.

### Mini desafio 3

Crie uma rota `GET /clientes/<id>` que busque um cliente pelo id.

### Mini desafio 4

Crie uma rota `POST /clientes` que cadastre um cliente em uma lista.

### Mini desafio 5

Crie uma rota `GET /produtos` que retorne produtos com nome, preco e estoque.

### Mini desafio 6

Valide se o campo `nome` foi enviado no POST.

### Mini desafio 7

Crie uma rota `GET /pedidos` que retorne pedidos com nome do cliente e total.

## 11. Resumo

Neste modulo voce aprendeu que:

- backend roda no servidor e processa regras;
- API permite que sistemas conversem;
- Flask cria rotas e respostas HTTP com Python;
- endpoints representam recursos como clientes, produtos e pedidos;
- `GET` busca dados;
- `POST` cria dados;
- APIs retornam JSON;
- codigos de status ajudam a comunicar sucesso ou erro;
- MySQL guarda dados reais da aplicacao;
- organizar conexao e rotas separadamente melhora o projeto.

Ao final deste modulo, voce ja consegue criar uma API simples com Flask, retornar JSON e conectar o backend a um banco MySQL.
