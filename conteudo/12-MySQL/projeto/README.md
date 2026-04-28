# Projeto - Sistema Simples de Vendas com MySQL

Neste projeto, voce vai criar um sistema simples conectado ao MySQL.

Ele simula uma empresa que precisa:

- cadastrar clientes;
- cadastrar produtos;
- registrar pedidos;
- listar dados;
- atualizar estoque;
- gerar relatorios.

## Estrutura do banco

O banco esta no arquivo:

```text
../banco/sistema_vendas.sql
```

Tabelas:

- `clientes`: dados dos clientes;
- `produtos`: catalogo e estoque;
- `pedidos`: cabecalho das vendas;
- `itens_pedido`: produtos dentro de cada pedido.

## Como preparar o banco

No terminal, execute:

```bash
mysql -u root -p < ../banco/sistema_vendas.sql
```

Ou abra o arquivo no MySQL Workbench e execute o script.

## Como instalar a biblioteca

```bash
pip install mysql-connector-python
```

Se sua senha do MySQL nao for vazia, configure:

```bash
export MYSQL_PASSWORD="sua_senha"
```

No Windows PowerShell:

```powershell
$env:MYSQL_PASSWORD="sua_senha"
```

## Como executar

Dentro da pasta `projeto`, rode:

```bash
python3 app_sistema_vendas.py
```

## Funcionalidades do projeto

O arquivo `app_sistema_vendas.py` contem funcoes para:

- conectar ao banco;
- cadastrar cliente;
- cadastrar produto;
- listar clientes;
- listar produtos;
- registrar pedido;
- atualizar estoque;
- listar pedidos com total;
- gerar relatorio de faturamento por produto.

## Decisoes importantes

### Uso de parametros

As consultas usam `%s` e tuplas de valores.

Isso evita montar SQL por concatenacao e reduz riscos de erro e SQL injection.

### Uso de commit

Toda operacao que altera dados usa:

```python
conexao.commit()
```

Sem `commit()`, o MySQL pode nao salvar a alteracao.

### Uso de relacionamento

Pedidos usam `id_cliente`.

Itens usam `id_pedido` e `id_produto`.

Essa estrutura evita duplicacao e deixa os dados mais organizados.
