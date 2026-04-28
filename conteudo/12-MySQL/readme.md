# 12 - MySQL com Python

Neste modulo voce vai aprender como sistemas armazenam dados de forma organizada usando banco de dados MySQL.

Ate aqui, voce trabalhou com arquivos, pandas, APIs e graficos. Agora voce vai aprender uma parte essencial de sistemas reais: salvar, consultar, atualizar e excluir dados em um banco.

O foco sera um exemplo parecido com uma empresa pequena: clientes, produtos e pedidos.

## Estrutura do modulo

```text
12-MySQL/
  README.md
  banco/
    sistema_vendas.sql
  exemplos/
    01_conectar.py
    02_select_clientes.py
    03_insert_cliente.py
    04_update_delete.py
  exercicios/
    exercicios.md
    gabaritos/
      gabaritos.md
      gabaritos.sql
      gabaritos.py
  projeto/
    README.md
    app_sistema_vendas.py
```

## 1. Introducao

### O que e banco de dados?

Banco de dados e um lugar organizado para armazenar informacoes.

Em vez de guardar tudo em arquivos soltos, sistemas usam bancos de dados para manter dados com estrutura, seguranca e facilidade de consulta.

Exemplos de dados que um sistema pode guardar:

- clientes cadastrados;
- produtos no estoque;
- pedidos realizados;
- pagamentos;
- usuarios do sistema;
- historico de compras.

### Por que sistemas usam banco?

Sistemas usam banco de dados porque precisam:

- salvar dados mesmo depois que o programa fecha;
- buscar informacoes rapidamente;
- evitar dados perdidos ou baguncados;
- relacionar informacoes;
- permitir relatorios;
- controlar alteracoes.

### Exemplo real

Em um ecommerce:

- a tabela `clientes` guarda quem compra;
- a tabela `produtos` guarda o catalogo;
- a tabela `pedidos` guarda cada venda;
- a tabela `itens_pedido` guarda quais produtos foram vendidos em cada pedido.

Quando o cliente compra, o sistema salva dados no banco. Depois, a empresa pode consultar:

- total vendido;
- produtos mais vendidos;
- pedidos de um cliente;
- clientes por cidade;
- produtos com estoque baixo.

## 2. Conceitos basicos

### Tabela

Tabela e uma estrutura parecida com uma planilha.

Exemplo de tabela `clientes`:

| id_cliente | nome | email | cidade |
|---:|---|---|---|
| 1 | Ana Souza | ana@email.com | Sao Paulo |
| 2 | Bruno Lima | bruno@email.com | Rio de Janeiro |

### Coluna ou campo

Coluna e cada tipo de informacao.

Na tabela `clientes`, temos:

- `id_cliente`;
- `nome`;
- `email`;
- `cidade`.

### Linha ou registro

Linha e um item cadastrado.

Cada cliente ocupa uma linha na tabela.

### Chave primaria

Chave primaria identifica uma linha de forma unica.

Exemplo:

```sql
id_cliente INT AUTO_INCREMENT PRIMARY KEY
```

Cada cliente tem um `id_cliente` unico.

### Chave estrangeira

Chave estrangeira liga uma tabela a outra.

Exemplo: um pedido pertence a um cliente.

Na tabela `pedidos`, a coluna `id_cliente` aponta para a tabela `clientes`.

## 3. SQL basico

SQL e a linguagem usada para conversar com bancos relacionais como MySQL.

### SELECT

Busca dados.

```sql
SELECT * FROM clientes;
```

Busca algumas colunas:

```sql
SELECT nome, email FROM clientes;
```

Busca com filtro:

```sql
SELECT * FROM clientes WHERE cidade = 'Sao Paulo';
```

### INSERT

Insere dados.

```sql
INSERT INTO clientes (nome, email, cidade)
VALUES ('Mariana Costa', 'mariana@email.com', 'Curitiba');
```

### UPDATE

Atualiza dados existentes.

```sql
UPDATE clientes
SET cidade = 'Campinas'
WHERE id_cliente = 1;
```

O `WHERE` e muito importante. Sem ele, voce pode atualizar todas as linhas.

### DELETE

Exclui dados.

```sql
DELETE FROM clientes
WHERE id_cliente = 3;
```

O `WHERE` tambem e essencial no `DELETE`.

## 4. Criacao de tabela

Para criar uma tabela, usamos `CREATE TABLE`.

```sql
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    cidade VARCHAR(80),
    data_cadastro DATE NOT NULL
);
```

### Tipos de dados comuns

| Tipo | Uso |
|---|---|
| `INT` | numeros inteiros |
| `VARCHAR(100)` | texto curto |
| `DECIMAL(10,2)` | valores financeiros |
| `DATE` | datas |
| `DATETIME` | data e hora |

### Regras comuns

| Regra | Significado |
|---|---|
| `PRIMARY KEY` | identifica cada linha |
| `AUTO_INCREMENT` | gera numero automaticamente |
| `NOT NULL` | campo obrigatorio |
| `UNIQUE` | nao permite repeticao |
| `FOREIGN KEY` | cria relacionamento |

## 5. Relacionamento simples

Em sistemas reais, os dados ficam separados em tabelas.

Exemplo:

- `clientes`: dados dos clientes;
- `pedidos`: dados dos pedidos.

Um cliente pode ter varios pedidos.

```sql
CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    data_pedido DATE NOT NULL,
    status VARCHAR(30) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);
```

Para buscar pedido com nome do cliente, usamos `JOIN`.

```sql
SELECT
    pedidos.id_pedido,
    clientes.nome,
    pedidos.data_pedido,
    pedidos.status
FROM pedidos
INNER JOIN clientes ON pedidos.id_cliente = clientes.id_cliente;
```

Leia assim:

- pegue pedidos;
- junte com clientes;
- use a ligacao `pedidos.id_cliente = clientes.id_cliente`;
- mostre dados das duas tabelas.

## 6. Integracao com Python

Para conectar Python ao MySQL, use `mysql-connector-python`.

### Instalacao

```bash
pip install mysql-connector-python
```

### Configurando conexao

Neste modulo, os exemplos leem credenciais de variaveis de ambiente.

Valores padrao:

- usuario: `root`;
- senha: vazia;
- host: `localhost`;
- banco: `curso_python_vendas`.

Se sua senha for diferente, configure no terminal:

```bash
export MYSQL_PASSWORD="sua_senha"
```

No Windows PowerShell:

```powershell
$env:MYSQL_PASSWORD="sua_senha"
```

### Conexao simples

```python
import os
import mysql.connector

conexao = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.getenv("MYSQL_USER", "root"),
    password=os.getenv("MYSQL_PASSWORD", ""),
    database=os.getenv("MYSQL_DATABASE", "curso_python_vendas"),
)

cursor = conexao.cursor(dictionary=True)
cursor.execute("SELECT DATABASE() AS banco_conectado")
print(cursor.fetchone())

cursor.close()
conexao.close()
```

### Executando SELECT

```python
cursor.execute("SELECT id_cliente, nome, email FROM clientes")
clientes = cursor.fetchall()

for cliente in clientes:
    print(cliente["nome"], cliente["email"])
```

### Executando INSERT com parametros

Use parametros para evitar SQL injection e erros com textos.

```python
sql = """
INSERT INTO clientes (nome, email, telefone, cidade, data_cadastro)
VALUES (%s, %s, %s, %s, CURDATE())
"""

valores = ("Joana Freitas", "joana@email.com", "11999990000", "Sao Paulo")

cursor.execute(sql, valores)
conexao.commit()
```

`commit()` confirma alteracoes feitas por `INSERT`, `UPDATE` e `DELETE`.

## 7. Boas praticas

### Use nomes claros

Prefira:

```sql
clientes
produtos
pedidos
itens_pedido
```

Evite nomes genericos como:

```sql
tabela1
dados
coisas
```

### Evite duplicidade

Nao repita dados sem necessidade.

Exemplo ruim: guardar nome do cliente em todos os pedidos.

Melhor: guardar `id_cliente` no pedido e buscar o nome com `JOIN`.

### Use tipos adequados

Valores financeiros devem usar `DECIMAL`, nao `VARCHAR`.

Datas devem usar `DATE` ou `DATETIME`.

### Sempre use WHERE em UPDATE e DELETE

Antes de atualizar ou excluir, faca um SELECT com o mesmo filtro:

```sql
SELECT * FROM clientes WHERE id_cliente = 1;
```

Depois:

```sql
UPDATE clientes SET cidade = 'Campinas' WHERE id_cliente = 1;
```

### Feche conexoes

Em Python, sempre feche cursor e conexao.

## 8. Erros comuns

### Esquecer WHERE

Perigoso:

```sql
UPDATE produtos SET preco = 99.90;
```

Isso altera todos os produtos.

Certo:

```sql
UPDATE produtos SET preco = 99.90 WHERE id_produto = 2;
```

### Dados inconsistentes

Exemplo: pedido apontando para cliente inexistente.

Chaves estrangeiras ajudam a evitar isso.

### Duplicacao

Exemplo: cadastrar o mesmo email varias vezes.

Use `UNIQUE` em campos que nao devem repetir.

### Esquecer commit

Em Python, comandos de alteracao precisam de:

```python
conexao.commit()
```

### Erro de conexao

Possiveis causas:

- MySQL desligado;
- senha errada;
- banco nao criado;
- biblioteca nao instalada;
- usuario sem permissao.

## 9. Mini desafios

Use o script `banco/sistema_vendas.sql` para criar o banco.

### Mini desafio 1

Liste todos os clientes cadastrados.

### Mini desafio 2

Liste produtos com estoque menor que 20.

### Mini desafio 3

Insira um novo cliente.

### Mini desafio 4

Atualize o telefone de um cliente.

### Mini desafio 5

Crie uma consulta que mostre pedidos com nome do cliente.

### Mini desafio 6

Calcule o faturamento total dos pedidos pagos.

### Mini desafio 7

Liste os produtos mais vendidos usando `itens_pedido`.

## 10. Resumo

Neste modulo voce aprendeu que:

- banco de dados armazena informacoes de sistemas;
- tabelas organizam dados em linhas e colunas;
- SQL e usado para consultar e modificar dados;
- `SELECT`, `INSERT`, `UPDATE` e `DELETE` sao comandos essenciais;
- `CREATE TABLE` cria estruturas;
- chaves primarias identificam registros;
- chaves estrangeiras criam relacoes entre tabelas;
- Python pode se conectar ao MySQL com `mysql-connector-python`;
- `commit()` salva alteracoes;
- `WHERE` evita alteracoes perigosas;
- `JOIN` permite consultar dados relacionados.

Ao final deste modulo, voce ja consegue criar um banco simples e conectar Python com MySQL para construir sistemas reais.
