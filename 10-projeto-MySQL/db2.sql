DROP DATABASE IF EXISTS my_db2;


CREATE DATABASE my_db2;

use my_db2;

-- Tabela contratos
CREATE TABLE contratos (
    id_contrato INT NOT NULL AUTO_INCREMENT,   -- ID único do contrato
    cpf_cliente VARCHAR(11) NOT NULL,          -- CPF do cliente (11 caracteres)
    valor_parcela DECIMAL(10, 2),              -- Valor da parcela
    data_contrato DATE,                        -- Data do contrato
    status VARCHAR(20),                        -- Status do contrato (Ex: 'Ativo', 'Inativo')
    PRIMARY KEY (id_contrato)                  -- Chave primária
);

-- Dados fictícios para a tabela contratos
INSERT INTO contratos (cpf_cliente, valor_parcela, data_contrato, status)
VALUES 
    ('12345678901', 120.50, '2023-01-10', 'Ativo'),
    ('98765432100', 200.75, '2023-03-15', 'Inativo'),
    ('15975345682', 150.25, '2023-06-20', 'Ativo'),
    ('75395185247', 175.50, '2023-07-05', 'Encerrado');
