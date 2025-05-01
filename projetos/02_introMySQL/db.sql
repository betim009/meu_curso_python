CREATE DATABASE my_db;

use my_db;

-- Tabela contratos_clientes
CREATE TABLE contratos_clientes (
    nr_cic VARCHAR(11) NOT NULL,             -- CPF do cliente (11 caracteres)
    nr_ctr INT NOT NULL,                     -- Número do contrato
    nr_adl INT NOT NULL,                     -- Identificador adicional do contrato
    nr_beneficio INT,                        -- Número do benefício
    vr_parcela DECIMAL(10, 2),               -- Valor da parcela
    vr_averbado DECIMAL(10, 2),              -- Valor averbado
    averb_completa TINYINT DEFAULT 0,        -- Indicador de averbação completa (0 ou 1)
    dt_ope DATE,                             -- Data da operação
    status_contrato VARCHAR(20),             -- Status do contrato (Ex: 'Ativo')
    bloqueado TINYINT DEFAULT 0,             -- Indicador de bloqueio (0 ou 1)
    elegivel TINYINT DEFAULT 1,              -- Indicador de elegibilidade (0 ou 1)
    PRIMARY KEY (nr_ctr, nr_adl)             -- Chave primária composta
);

-- Tabela detalhes_contratos
CREATE TABLE detalhes_contratos (
    nr_ctr INT NOT NULL,                     -- Número do contrato
    nr_adl INT NOT NULL,                     -- Identificador adicional do contrato
    qt_tit INT,                              -- Quantidade total de parcelas
    ID_SIT_CTR VARCHAR(2),                   -- Situação do contrato (Ex: 'AT', 'CE')
    PRIMARY KEY (nr_ctr, nr_adl),            -- Chave primária composta
    FOREIGN KEY (nr_ctr, nr_adl)             -- Chave estrangeira para contratos_clientes
        REFERENCES contratos_clientes (nr_ctr, nr_adl)
        ON DELETE CASCADE ON UPDATE CASCADE   -- Integridade referencial com ações de exclusão e atualização em cascata
);

-- Seed para inserir dados fictícios
INSERT INTO contratos_clientes (nr_cic, nr_ctr, nr_adl, nr_beneficio, vr_parcela, vr_averbado, averb_completa, dt_ope, status_contrato, bloqueado, elegivel)
VALUES 
    ('12345678901', 1001, 1, 789456, 100.50, 5000.00, 1, '2023-01-10', 'Ativo', 0, 1),
    ('98765432100', 1002, 1, 456123, 200.75, 8000.00, 0, '2023-03-15', 'Inativo', 1, 1),
    ('15975345682', 1003, 1, 852369, 150.25, 7500.00, 1, '2023-06-20', 'Ativo', 0, 1),
    ('75395185247', 1004, 2, 159357, 175.50, 9000.00, 0, '2023-07-05', 'Encerrado', 1, 0);

INSERT INTO detalhes_contratos (nr_ctr, nr_adl, qt_tit, ID_SIT_CTR)
VALUES 
    (1001, 1, 24, 'AT'),
    (1002, 1, 36, 'IN'),
    (1003, 1, 18, 'AT'),
    (1004, 2, 12, 'CE');
