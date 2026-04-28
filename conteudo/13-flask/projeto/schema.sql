DROP DATABASE IF EXISTS curso_flask_api;
CREATE DATABASE curso_flask_api CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE curso_flask_api;

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    cidade VARCHAR(80)
);

CREATE TABLE produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(80) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    estoque INT NOT NULL DEFAULT 0
);

CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    data_pedido DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(30) NOT NULL DEFAULT 'Pago',
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

INSERT INTO clientes (nome, email, cidade) VALUES
('Ana Souza', 'ana@email.com', 'Sao Paulo'),
('Bruno Lima', 'bruno@email.com', 'Rio de Janeiro'),
('Carla Mendes', 'carla@email.com', 'Belo Horizonte');

INSERT INTO produtos (nome, categoria, preco, estoque) VALUES
('Notebook Pro', 'Computadores', 4299.00, 10),
('Mouse sem fio', 'Perifericos', 89.90, 40),
('Monitor 24', 'Monitores', 899.90, 15);

INSERT INTO pedidos (id_cliente, status) VALUES
(1, 'Pago'),
(2, 'Pago');

INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, preco_unitario) VALUES
(1, 1, 1, 4299.00),
(1, 2, 2, 89.90),
(2, 3, 1, 899.90);
