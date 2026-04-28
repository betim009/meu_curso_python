USE curso_python_vendas;

-- 1. Listar clientes
SELECT id_cliente, nome, email, cidade
FROM clientes
ORDER BY nome;

-- 2. Produtos ativos
SELECT id_produto, nome, categoria, preco, estoque
FROM produtos
WHERE ativo = TRUE
ORDER BY nome;

-- 3. Inserir cliente
INSERT INTO clientes (nome, email, telefone, cidade, data_cadastro)
VALUES ('Mariana Costa', 'mariana.costa@email.com', '11988887777', 'Sao Paulo', CURDATE());

-- 4. Atualizar telefone
UPDATE clientes
SET telefone = '11977776666'
WHERE id_cliente = 1;

-- 5. Produtos com estoque baixo
SELECT id_produto, nome, categoria, estoque
FROM produtos
WHERE estoque < 20
ORDER BY estoque;

-- 6. Pedidos com nome do cliente
SELECT
    p.id_pedido,
    c.nome AS cliente,
    p.data_pedido,
    p.status,
    p.forma_pagamento
FROM pedidos p
INNER JOIN clientes c ON p.id_cliente = c.id_cliente
ORDER BY p.data_pedido;

-- 7. Total de cada pedido
SELECT
    p.id_pedido,
    c.nome AS cliente,
    SUM(i.quantidade * i.preco_unitario) AS total_pedido
FROM pedidos p
INNER JOIN clientes c ON p.id_cliente = c.id_cliente
INNER JOIN itens_pedido i ON p.id_pedido = i.id_pedido
GROUP BY p.id_pedido, c.nome
ORDER BY total_pedido DESC;

-- 8. Faturamento dos pedidos pagos
SELECT
    SUM(i.quantidade * i.preco_unitario) AS faturamento_pago
FROM pedidos p
INNER JOIN itens_pedido i ON p.id_pedido = i.id_pedido
WHERE p.status = 'Pago';

-- 9. Produtos mais vendidos
SELECT
    pr.nome,
    pr.categoria,
    SUM(i.quantidade) AS unidades_vendidas
FROM itens_pedido i
INNER JOIN produtos pr ON i.id_produto = pr.id_produto
GROUP BY pr.id_produto, pr.nome, pr.categoria
ORDER BY unidades_vendidas DESC;

-- 10. Inserir pedido completo
INSERT INTO pedidos (id_cliente, data_pedido, status, forma_pagamento)
VALUES (2, CURDATE(), 'Pago', 'Pix');

SET @id_pedido = LAST_INSERT_ID();

INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, preco_unitario)
VALUES
(@id_pedido, 3, 2, 89.90),
(@id_pedido, 4, 1, 249.90);

-- 11. Relatorio por cliente
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
