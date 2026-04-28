# Gabaritos Comentados - MySQL

## 1. Listar clientes

```sql
SELECT id_cliente, nome, email, cidade
FROM clientes
ORDER BY nome;
```

Explicacao: `SELECT` busca colunas especificas e `ORDER BY` organiza o resultado.

## 2. Produtos ativos

```sql
SELECT id_produto, nome, categoria, preco, estoque
FROM produtos
WHERE ativo = TRUE
ORDER BY nome;
```

Explicacao: `WHERE ativo = TRUE` filtra apenas produtos disponiveis.

## 3. Inserir cliente

```sql
INSERT INTO clientes (nome, email, telefone, cidade, data_cadastro)
VALUES ('Mariana Costa', 'mariana.costa@email.com', '11988887777', 'Sao Paulo', CURDATE());
```

Explicacao: `INSERT INTO` adiciona uma nova linha na tabela.

## 4. Atualizar telefone

```sql
UPDATE clientes
SET telefone = '11977776666'
WHERE id_cliente = 1;
```

Explicacao: o `WHERE` garante que apenas um cliente seja alterado.

## 5. Produtos com estoque baixo

```sql
SELECT id_produto, nome, categoria, estoque
FROM produtos
WHERE estoque < 20
ORDER BY estoque;
```

Explicacao: o filtro encontra produtos que podem precisar de reposicao.

## 6. Pedidos com nome do cliente

```sql
SELECT
    p.id_pedido,
    c.nome AS cliente,
    p.data_pedido,
    p.status,
    p.forma_pagamento
FROM pedidos p
INNER JOIN clientes c ON p.id_cliente = c.id_cliente
ORDER BY p.data_pedido;
```

Explicacao: `JOIN` junta pedidos com clientes usando a chave `id_cliente`.

## 7. Total de cada pedido

```sql
SELECT
    p.id_pedido,
    c.nome AS cliente,
    SUM(i.quantidade * i.preco_unitario) AS total_pedido
FROM pedidos p
INNER JOIN clientes c ON p.id_cliente = c.id_cliente
INNER JOIN itens_pedido i ON p.id_pedido = i.id_pedido
GROUP BY p.id_pedido, c.nome
ORDER BY total_pedido DESC;
```

Explicacao: `SUM()` soma os itens de cada pedido e `GROUP BY` separa o calculo por pedido.

## 8. Faturamento dos pedidos pagos

```sql
SELECT
    SUM(i.quantidade * i.preco_unitario) AS faturamento_pago
FROM pedidos p
INNER JOIN itens_pedido i ON p.id_pedido = i.id_pedido
WHERE p.status = 'Pago';
```

Explicacao: o filtro considera apenas pedidos pagos.

## 9. Produtos mais vendidos

```sql
SELECT
    pr.nome,
    pr.categoria,
    SUM(i.quantidade) AS unidades_vendidas
FROM itens_pedido i
INNER JOIN produtos pr ON i.id_produto = pr.id_produto
GROUP BY pr.id_produto, pr.nome, pr.categoria
ORDER BY unidades_vendidas DESC;
```

Explicacao: agrupamos por produto e somamos as quantidades vendidas.

## 10. Inserir pedido completo

```sql
INSERT INTO pedidos (id_cliente, data_pedido, status, forma_pagamento)
VALUES (2, CURDATE(), 'Pago', 'Pix');

SET @id_pedido = LAST_INSERT_ID();

INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, preco_unitario)
VALUES
(@id_pedido, 3, 2, 89.90),
(@id_pedido, 4, 1, 249.90);
```

Explicacao: `LAST_INSERT_ID()` recupera o id do pedido criado para inserir os itens ligados a ele.

## 11. Relatorio por cliente

```sql
SELECT
    c.nome,
    COUNT(DISTINCT p.id_pedido) AS quantidade_pedidos,
    SUM(i.quantidade * i.preco_unitario) AS total_gasto
FROM clientes c
INNER JOIN pedidos p ON c.id_cliente = p.id_cliente
INNER JOIN itens_pedido i ON p.id_pedido = i.id_pedido
WHERE p.status = 'Pago'
GROUP BY c.id_cliente, c.nome
ORDER BY total_gasto DESC;
```

Explicacao: a consulta resume os pedidos pagos por cliente.

## 12. Sistema Python de consulta

```python
import os
import mysql.connector


def conectar():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "curso_python_vendas"),
    )


try:
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("""
        SELECT nome, categoria, estoque
        FROM produtos
        WHERE estoque < 20
        ORDER BY estoque
    """)

    for produto in cursor.fetchall():
        print(produto["nome"], produto["categoria"], produto["estoque"])

except mysql.connector.Error as erro:
    print("Erro:", erro)

finally:
    if "cursor" in locals():
        cursor.close()
    if "conexao" in locals() and conexao.is_connected():
        conexao.close()
```

Explicacao: o Python executa o mesmo SQL que voce rodaria no MySQL.

## 13. Cadastro via Python

```python
import os
import mysql.connector


def conectar():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "curso_python_vendas"),
    )


def cadastrar_cliente(nome, email, telefone, cidade):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(
            """
            INSERT INTO clientes (nome, email, telefone, cidade, data_cadastro)
            VALUES (%s, %s, %s, %s, CURDATE())
            """,
            (nome, email, telefone, cidade),
        )
        conexao.commit()
        print("Cliente cadastrado com id:", cursor.lastrowid)
    except mysql.connector.Error as erro:
        print("Erro ao cadastrar cliente:", erro)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conexao" in locals() and conexao.is_connected():
            conexao.close()


cadastrar_cliente("Paula Nunes", "paula.nunes@email.com", "11955554444", "Sao Paulo")
```

Explicacao: parametros deixam a insercao mais segura e evitam montar SQL por concatenacao.
