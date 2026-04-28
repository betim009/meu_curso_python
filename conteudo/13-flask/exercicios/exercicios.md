# Exercicios - Flask e APIs

Estes exercicios simulam tarefas reais de backend: criar rotas, retornar JSON, cadastrar dados e buscar informacoes especificas.

## Exercicios faceis

### 1. Rota de status

Crie uma API Flask com uma rota:

```text
GET /status
```

Ela deve retornar:

```json
{"status": "online"}
```

### 2. Listar clientes

Crie uma lista em memoria com 3 clientes.

Depois crie:

```text
GET /clientes
```

Retorne a lista em JSON.

### 3. Buscar cliente por ID

Crie:

```text
GET /clientes/<id>
```

Se encontrar o cliente, retorne os dados.  
Se nao encontrar, retorne erro com status `404`.

### 4. Listar produtos

Crie uma lista de produtos com:

- id;
- nome;
- preco;
- estoque.

Crie a rota:

```text
GET /produtos
```

### 5. Mensagem inicial

Crie a rota:

```text
GET /
```

Ela deve retornar uma mensagem dizendo que a API esta funcionando.

## Exercicios medios

### 6. Cadastrar cliente com POST

Crie:

```text
POST /clientes
```

O endpoint deve receber JSON com:

- nome;
- email;
- cidade.

Depois deve adicionar o cliente na lista em memoria e retornar status `201`.

### 7. Validar campo obrigatorio

No cadastro de cliente, valide se o campo `nome` foi enviado.

Se nao foi enviado, retorne:

```json
{"erro": "Nome e obrigatorio"}
```

com status `400`.

### 8. Filtrar produtos por categoria

Crie:

```text
GET /produtos?categoria=Perifericos
```

Se a categoria for enviada, retorne apenas produtos daquela categoria.

### 9. Buscar pedido por ID

Crie uma lista de pedidos e implemente:

```text
GET /pedidos/<id>
```

Retorne `404` se o pedido nao existir.

### 10. Criar pedido

Crie:

```text
POST /pedidos
```

Receba:

- cliente;
- produto;
- quantidade;
- valor_unitario.

Calcule o total do pedido e retorne o pedido criado.

## Exercicios desafiadores

### 11. API organizada por recurso

Crie uma API com endpoints:

- `GET /clientes`;
- `POST /clientes`;
- `GET /produtos`;
- `POST /produtos`;
- `GET /pedidos`;
- `POST /pedidos`.

Use listas em memoria.

### 12. Integração com MySQL

Crie uma rota:

```text
GET /clientes
```

Ela deve conectar ao MySQL, consultar a tabela `clientes` e retornar os dados em JSON.

Use o banco do projeto deste modulo ou o banco criado no modulo MySQL.

### 13. API com validação e status

Melhore os endpoints POST para:

- validar campos obrigatorios;
- retornar `400` para erro do usuario;
- retornar `201` quando criar;
- retornar `404` quando um id nao existir.
