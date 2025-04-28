Documentação - Gestão de Contratos
## Requisitos:
1. Função get_contratos
Essa função busca no banco de dados todos os contratos registrados.

Passos principais:
- Criar um cursor e executar a consulta SQL SELECT * FROM contratos.
- Recuperar todos os resultados da consulta com fetchall().
- Definir os nomes das colunas para o DataFrame.
- Converter os resultados para um pandas.DataFrame com as colunas apropriadas.
- Exibir o DataFrame para depuração (opcional).
- Converter o DataFrame para um array de dicionários usando .to_dict(orient="records").
- Fechar o cursor e a conexão com o banco de dados.
- Retornar o array de dicionários.


2. Função get_contrato_por_id
Essa função busca um contrato específico no banco de dados com base no ID fornecido.

Parâmetros:
id_contrato (int): ID do contrato a ser buscado.
Passos principais:

- Criar um cursor e executar a consulta SQL SELECT * FROM contratos WHERE id_contrato = %s, passando o parâmetro.
- Recuperar o resultado único da consulta com fetchone().
- Se o contrato for encontrado:
- Definir as colunas para o DataFrame.
- Converter o resultado para um dicionário usando .to_dict(orient="records")[0].
- Exibir o dicionário para depuração (opcional).
- Retornar o dicionário do contrato.
- Caso contrário, informar que o contrato não foi encontrado e retornar None.


3. Função criar_contrato
Essa função insere um novo contrato no banco de dados.

Parâmetros:

- cpf_cliente (str): CPF do cliente.
- valor_parcela (float): Valor da parcela do contrato.
- data_contrato (str): Data do contrato no formato YYYY-MM-DD.
- status (str): Status atual do contrato (exemplo: "Ativo").

Passos principais:
Criar um cursor e executar a consulta SQL para inserção:
INSERT INTO contratos (cpf_cliente, valor_parcela, data_contrato, status) 
VALUES (%s, %s, %s, %s)

- Confirmar a inserção no banco com connection.commit().
- Recuperar o ID do contrato recém-criado com cursor.lastrowid.
- Exibir o ID do contrato para depuração (opcional).
- Retornar o ID do contrato criado.
- Em caso de erro, exibir a mensagem de erro e retornar None.


4. Função alterar_contrato_por_id
Essa função altera o valor da parcela de um contrato com base no ID.

Parâmetros:

- id_contrato (int): ID do contrato a ser alterado.
- novo_valor (float): Novo valor para a parcela.
- Passos principais:

Criar um cursor e executar a consulta SQL para alteração:
- UPDATE contratos SET valor_parcela = %s WHERE id_contrato = %s
- Confirmar a alteração no banco com connection.commit().
- Verificar se a alteração foi bem-sucedida com cursor.rowcount.
- Exibir mensagens informando o sucesso ou falha da alteração.

5. Função deletar_contrato_por_id
Essa função exclui um contrato com base no ID fornecido.

Parâmetros:

- id_contrato (int): ID do contrato a ser excluído.
Passos principais:

- Criar um cursor e executar a consulta SQL para exclusão:
- DELETE FROM contratos WHERE id_contrato = %s
- Confirmar a exclusão no banco com connection.commit().
- Verificar se a exclusão foi bem-sucedida com cursor.rowcount.
- Exibir mensagens informando o sucesso ou falha da exclusão.
- Fechar o cursor e a conexão com o banco de dados.

