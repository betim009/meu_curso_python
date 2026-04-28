# Projeto - API de Sistema de Vendas com Flask e MySQL

Neste projeto, voce vai criar uma API simples para um sistema de vendas.

Ela simula o backend de uma empresa que precisa:

- cadastrar clientes;
- cadastrar produtos;
- listar clientes;
- listar produtos;
- buscar registros por ID;
- registrar pedidos;
- consultar pedidos com total.

## Estrutura

```text
projeto/
  app.py
  database.py
  schema.sql
```

## Preparando o banco

Execute o script `schema.sql` no MySQL:

```bash
mysql -u root -p < schema.sql
```

O banco criado se chama:

```text
curso_flask_api
```

## Instalando dependencias

```bash
pip install flask mysql-connector-python
```

Se sua senha do MySQL nao for vazia:

```bash
export MYSQL_PASSWORD="sua_senha"
```

No Windows PowerShell:

```powershell
$env:MYSQL_PASSWORD="sua_senha"
```

## Executando

Dentro da pasta `projeto`:

```bash
python3 app.py
```

Ou:

```bash
flask --app app run --debug
```

## Endpoints

| Metodo | Rota | Funcao |
|---|---|---|
| GET | `/status` | verificar se API esta online |
| GET | `/clientes` | listar clientes |
| GET | `/clientes/<id>` | buscar cliente por ID |
| POST | `/clientes` | cadastrar cliente |
| GET | `/produtos` | listar produtos |
| GET | `/produtos/<id>` | buscar produto por ID |
| POST | `/produtos` | cadastrar produto |
| GET | `/pedidos` | listar pedidos com total |
| POST | `/pedidos` | registrar pedido |

## Exemplo de POST cliente

```bash
curl -X POST http://127.0.0.1:5000/clientes \
  -H "Content-Type: application/json" \
  -d '{"nome": "Paula Nunes", "email": "paula@email.com", "cidade": "Sao Paulo"}'
```

## Exemplo de POST produto

```bash
curl -X POST http://127.0.0.1:5000/produtos \
  -H "Content-Type: application/json" \
  -d '{"nome": "Webcam HD", "categoria": "Perifericos", "preco": 219.90, "estoque": 20}'
```

## Exemplo de POST pedido

```bash
curl -X POST http://127.0.0.1:5000/pedidos \
  -H "Content-Type: application/json" \
  -d '{"id_cliente": 1, "itens": [{"id_produto": 1, "quantidade": 1}, {"id_produto": 2, "quantidade": 2}]}'
```

## Decisoes tomadas

- O projeto usa MySQL para persistencia real.
- As rotas retornam JSON porque o foco e API.
- As consultas usam parametros `%s` para evitar SQL injection.
- O cadastro de pedido usa transacao: se algum item falhar, nada e salvo.
- O codigo separa conexao (`database.py`) das rotas (`app.py`).
