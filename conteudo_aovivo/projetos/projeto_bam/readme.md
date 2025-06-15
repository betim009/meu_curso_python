`pip install flask mysql-connector-python`

```sql
-- Criar o banco de dados
CREATE DATABASE IF NOT EXISTS db_1;

-- Usar o banco criado
USE db_1;

-- Criar a tabela de usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);
```