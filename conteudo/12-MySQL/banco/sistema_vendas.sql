DROP DATABASE IF EXISTS curso_python_vendas;
CREATE DATABASE curso_python_vendas CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE curso_python_vendas;

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    telefone VARCHAR(20),
    cidade VARCHAR(80),
    data_cadastro DATE NOT NULL
);

CREATE TABLE produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(80) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    estoque INT NOT NULL DEFAULT 0,
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    data_pedido DATE NOT NULL,
    status VARCHAR(30) NOT NULL,
    forma_pagamento VARCHAR(30) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE itens_pedido (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);

INSERT INTO clientes (nome, email, telefone, cidade, data_cadastro) VALUES
('Ana Souza', 'ana.souza@email.com', '11999990001', 'Sao Paulo', '2026-01-05'),
('Bruno Lima', 'bruno.lima@email.com', '21999990002', 'Rio de Janeiro', '2026-01-07'),
('Carla Mendes', 'carla.mendes@email.com', '31999990003', 'Belo Horizonte', '2026-01-10'),
('Diego Alves', 'diego.alves@email.com', '11999990004', 'Sao Paulo', '2026-01-12'),
('Elisa Rocha', 'elisa.rocha@email.com', '41999990005', 'Curitiba', '2026-01-15');

INSERT INTO produtos (nome, categoria, preco, estoque, ativo) VALUES
('Notebook Pro', 'Computadores', 4299.00, 12, TRUE),
('Monitor 24', 'Monitores', 899.90, 18, TRUE),
('Mouse sem fio', 'Perifericos', 89.90, 55, TRUE),
('Teclado mecanico', 'Perifericos', 249.90, 25, TRUE),
('Headset USB', 'Perifericos', 159.90, 8, TRUE),
('Cadeira ergonomica', 'Mobiliario', 1299.00, 6, TRUE);

INSERT INTO pedidos (id_cliente, data_pedido, status, forma_pagamento) VALUES
(1, '2026-02-01', 'Pago', 'Cartao'),
(2, '2026-02-03', 'Pago', 'Pix'),
(3, '2026-02-05', 'Pendente', 'Boleto'),
(1, '2026-02-08', 'Pago', 'Pix'),
(4, '2026-02-10', 'Cancelado', 'Cartao');

INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, preco_unitario) VALUES
(1, 1, 1, 4299.00),
(1, 3, 2, 89.90),
(2, 2, 2, 899.90),
(2, 4, 1, 249.90),
(3, 6, 1, 1299.00),
(4, 5, 3, 159.90),
(4, 3, 1, 89.90),
(5, 1, 1, 4299.00);

-- Consultas uteis para testar
SELECT * FROM clientes;
SELECT * FROM produtos;

SELECT
    p.id_pedido,
    c.nome AS cliente,
    p.data_pedido,
    p.status,
    p.forma_pagamento
FROM pedidos p
INNER JOIN clientes c ON p.id_cliente = c.id_cliente;

SELECT
    p.id_pedido,
    c.nome AS cliente,
    SUM(i.quantidade * i.preco_unitario) AS total_pedido
FROM pedidos p
INNER JOIN clientes c ON p.id_cliente = c.id_cliente
INNER JOIN itens_pedido i ON p.id_pedido = i.id_pedido
WHERE p.status = 'Pago'
GROUP BY p.id_pedido, c.nome;
