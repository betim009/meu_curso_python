# Exercicios - MySQL

Use o banco criado pelo script:

```text
../banco/sistema_vendas.sql
```

Os exercicios simulam tarefas reais de sistemas: criar tabelas, inserir registros, consultar dados, atualizar informacoes e gerar relatorios.

## Exercicios faceis

### 1. Listar clientes

Crie uma consulta SQL para listar todos os clientes.

Mostre:

- id;
- nome;
- email;
- cidade.

### 2. Produtos ativos

Liste todos os produtos ativos.

Mostre:

- id;
- nome;
- categoria;
- preco;
- estoque.

### 3. Inserir cliente

Insira um novo cliente na tabela `clientes`.

Use dados ficticios.

### 4. Atualizar telefone

Atualize o telefone de um cliente usando `id_cliente`.

### 5. Produtos com estoque baixo

Liste produtos com estoque menor que 20.

## Exercicios medios

### 6. Pedidos com nome do cliente

Crie uma consulta usando `INNER JOIN` para listar:

- id do pedido;
- nome do cliente;
- data do pedido;
- status;
- forma de pagamento.

### 7. Total de cada pedido

Crie uma consulta que calcule o total de cada pedido usando:

```text
quantidade * preco_unitario
```

### 8. Faturamento dos pedidos pagos

Calcule o faturamento total considerando apenas pedidos com status `Pago`.

### 9. Produtos mais vendidos

Liste os produtos mais vendidos em quantidade.

Use `itens_pedido` com `produtos`.

### 10. Inserir pedido completo

Insira:

- um pedido na tabela `pedidos`;
- pelo menos dois itens na tabela `itens_pedido`.

## Exercicios desafiadores

### 11. Relatorio por cliente

Crie uma consulta que mostre, por cliente:

- nome;
- quantidade de pedidos;
- total gasto.

Considere apenas pedidos pagos.

### 12. Sistema Python de consulta

Crie um script Python que:

- conecte ao MySQL;
- liste produtos com estoque baixo;
- mostre nome, categoria e estoque.

### 13. Cadastro via Python

Crie uma funcao Python `cadastrar_cliente(nome, email, telefone, cidade)` que insira um cliente no banco.

A funcao deve:

- usar parametros no SQL;
- chamar `commit()`;
- tratar erros;
- fechar a conexao.
