from db import connection


def run_migrations():
    conn = connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS produtos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(120) NOT NULL,
            categoria VARCHAR(80) NOT NULL,
            preco DECIMAL(10, 2) NOT NULL,
            estoque INT NOT NULL DEFAULT 0,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS vendas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            produto_id INT NOT NULL,
            quantidade INT NOT NULL,
            valor_total DECIMAL(10, 2) NOT NULL,
            vendido_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_vendas_produto
                FOREIGN KEY (produto_id)
                REFERENCES produtos(id)
                ON DELETE RESTRICT
                ON UPDATE CASCADE
        )
        """
    )

    conn.commit()
    cursor.close()
    conn.close()
    print("Migrations executadas com sucesso.")


if __name__ == "__main__":
    run_migrations()
