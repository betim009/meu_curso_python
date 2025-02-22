from connection import connection, cursor


def get_contratos():
    cursor.execute("SELECT * FROM contratos")

    # Recuperar todos os resultados da consulta
    result = cursor.fetchall()

    # Exibindo em formato de lista de dicionário
    for row in result:
        print({
            "id": row[0],
            "cpf_cliente": row[1], 
            "valor_parcela": format(float(row[2]), ".2f")
        })

    # Encerrando
    cursor.close()
    connection.close()
    print("Conexão encerrada.")


def get_contrato_id(id):
    # Executando a consulta para buscar o contrato pelo id
    cursor.execute("SELECT * FROM contratos WHERE id_contrato = %s", (id,))

    # Recuperar o primeiro resultado da consulta (um único contrato)
    result = cursor.fetchone()

    # Verificar se o contrato foi encontrado
    if result:
        # Exibindo em formato de lista de dicionário
        print({
            "id": result[0],
            "cpf_cliente": result[1], 
            "valor_parcela": format(float(result[2]), ".2f")
        })
    else:
        print(f"Contrato com id {id} não encontrado.")

    # Encerrando a conexão
    cursor.close()
    connection.close()
    print("Conexão encerrada.")

def alterar_contrato(id, novo_valor):
    # Executando a consulta para atualizar o valor da parcela do contrato
    cursor.execute("UPDATE contratos SET valor_parcela = %s WHERE id_contrato = %s", (novo_valor, id))

    # Confirmando a alteração no banco de dados
    connection.commit()

    # Verificando se o contrato foi alterado
    if cursor.rowcount > 0:
        print(f"Contrato com id {id} alterado com sucesso. Novo valor da parcela: {novo_valor:.2f}")
    else:
        print(f"Contrato com id {id} não encontrado ou não foi alterado.")

    # Encerrando a conexão
    cursor.close()
    connection.close()
    print("Conexão encerrada.")


# get_contratos()
# get_contrato_id(1)
alterar_contrato(1, 250.44)