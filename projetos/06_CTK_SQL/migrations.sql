CREATE DATABASE IF NOT EXISTS ctk_sql;

USE ctk_sql;

CREATE TABLE IF NOT EXISTS vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    metodo_pagamento VARCHAR(100) NOT NULL,
    dia INT NOT NULL,
    mes ENUM(
        'janeiro',
        'fevereiro',
        'marco',
        'abril',
        'maio',
        'junho',
        'julho',
        'agosto',
        'setembro',
        'outubro',
        'novembro',
        'dezembro'
    ) NOT NULL,
    ano INT NOT NULL
);
