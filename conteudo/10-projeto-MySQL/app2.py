import pandas as pd
from connection import connection, cursor


# Buscar todos contratos
def get_contratos():
    cursor.execute("SELECT * FROM contratos")

    # Recuperar todos os resultados da consulta
    result = cursor.fetchall()

    # Definir as colunas para o DataFrame
    colunas = ["id_contrato", "cpf_cliente", "valor_parcela", "data_contrato", "status"]

    # Converter para DataFrame
    df = pd.DataFrame(result, columns=colunas)

    # Exibindo o DataFrame
    print(df)

    # Converter o DataFrame para um array de dicionários
    contratos = df.to_dict(orient="records")

    # Encerrando a conexão
    cursor.close()
    connection.close()
    print("Conexão encerrada.")

    # Retornando o array de dicionários
    return contratos

# Buscar contrato por ID
def get_contrato_por_id(id_contrato):
    cursor.execute("SELECT * FROM contratos WHERE id_contrato = %s", (id_contrato,))
    result = cursor.fetchone()

    if result:
        colunas = ["id_contrato", "cpf_cliente", "valor_parcela", "data_contrato", "status"]
        contrato = pd.DataFrame([result], columns=colunas).to_dict(orient="records")[0]
        print(contrato)
        return contrato
    else:
        print(f"Contrato com id {id_contrato} não encontrado.")
        return None

def criar_contrato(cpf_cliente, valor_parcela, data_contrato, status):
    try:
        # Inserindo os dados na tabela
        cursor.execute(
            """
            INSERT INTO contratos (cpf_cliente, valor_parcela, data_contrato, status) 
            VALUES (%s, %s, %s, %s)
            """,
            (cpf_cliente, valor_parcela, data_contrato, status)
        )

        # Confirmando a inserção no banco de dados
        connection.commit()

        # Recuperando o ID do contrato inserido
        id_contrato = cursor.lastrowid
        print(f"Contrato criado com sucesso. ID do contrato: {id_contrato}")

        return id_contrato
    except Exception as e:
        print("Erro ao criar contrato:", e)
        return None

# Alterar contrato por ID
def alterar_contrato_por_id(id_contrato, novo_valor):
    cursor.execute("UPDATE contratos SET valor_parcela = %s WHERE id_contrato = %s", (novo_valor, id_contrato))
    connection.commit()

    if cursor.rowcount > 0:
        print(f"Contrato com id {id_contrato} alterado com sucesso. Novo valor: {novo_valor:.2f}")
    else:
        print(f"Contrato com id {id_contrato} não encontrado ou não foi alterado.")

# Deletar contrato por ID
def deletar_contrato_por_id(id_contrato):
    cursor.execute("DELETE FROM contratos WHERE id_contrato = %s", (id_contrato,))
    connection.commit()

    if cursor.rowcount > 0:
        print(f"Contrato com id {id_contrato} deletado com sucesso.")
    else:
        print(f"Contrato com id {id_contrato} não encontrado ou não foi deletado.")

    # Encerrando a conexão
    cursor.close()
    connection.close()
    print("Conexão encerrada.")

# Exemplos de uso

# Buscar todos
# get_contratos()

# Buscar por ID
# get_contrato_por_id(1)

# Alterar contrato
# alterar_contrato_por_id(1, 350.50)

# Deletar contrato
# deletar_contrato_por_id(1)

# Exemplo de uso
# novo_id = criar_contrato(
#     cpf_cliente="12345678901", 
#     valor_parcela=200.50, 
#     data_contrato="2024-11-27", 
#     status="Ativo"
# )
# print(f"Novo contrato criado com ID: {novo_id}")
