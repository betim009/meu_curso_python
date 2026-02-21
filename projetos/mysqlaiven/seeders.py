from db import connection


PRODUTOS_INICIAIS = [
    ("Dipirona 1g", "Analgésico", 8.50, 120),
    ("Paracetamol 750mg", "Analgésico", 12.90, 90),
    ("Vitamina C 1g", "Suplemento", 24.90, 60),
    ("Omeprazol 20mg", "Gastrointestinal", 19.90, 75),
    ("Soro Fisiológico 500ml", "Higiene", 7.80, 140),
]

VENDAS_INICIAIS = [
    ("Dipirona 1g", 2),
    ("Paracetamol 750mg", 1),
    ("Vitamina C 1g", 3),
    ("Omeprazol 20mg", 1),
]


def run_seeders():
    conn = connection()
    cursor = conn.cursor(dictionary=True)

    cursor.executemany(
        """
        INSERT INTO produtos (nome, categoria, preco, estoque)
        VALUES (%s, %s, %s, %s)
        """,
        PRODUTOS_INICIAIS,
    )

    cursor.execute("SELECT id, nome, preco FROM produtos")
    produtos = {item["nome"]: item for item in cursor.fetchall()}

    vendas = []
    for nome, quantidade in VENDAS_INICIAIS:
        produto = produtos.get(nome)
        if not produto:
            continue

        valor_total = float(produto["preco"]) * quantidade
        vendas.append((produto["id"], quantidade, valor_total))

    if vendas:
        cursor.executemany(
            """
            INSERT INTO vendas (produto_id, quantidade, valor_total)
            VALUES (%s, %s, %s)
            """,
            vendas,
        )

    conn.commit()
    cursor.close()
    conn.close()
    print("Seeders executados com sucesso.")


if __name__ == "__main__":
    run_seeders()
