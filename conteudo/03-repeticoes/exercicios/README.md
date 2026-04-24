# Exercícios - Repetições

Resolva os exercícios em ordem.

Eles simulam tarefas comuns em empresas: processar listas, gerar relatórios, contar registros, filtrar dados e automatizar validações.

Faça primeiro sem olhar o gabarito. Depois compare com [`gabaritos/README.md`](gabaritos/README.md).

---

## Exercícios fáceis

### 1. Listar clientes

Crie uma lista com três nomes de clientes.

Use `for` para mostrar cada cliente no terminal.

---

### 2. Somar vendas

Crie uma lista com valores de vendas.

Use `for` para calcular o total vendido.

---

### 3. Contar produtos

Crie uma lista de produtos.

Use `for` para contar quantos produtos existem na lista.

---

### 4. Gerar números de pedidos

Use `range()` para mostrar os pedidos de 1 até 5.

Saída esperada:

```text
Processando pedido 1
Processando pedido 2
...
```

---

### 5. Tentativas de login

Use `while` para mostrar três tentativas de login.

---

## Exercícios médios

### 6. Contar clientes ativos

Use a lista:

```python
clientes = [
    {"nome": "Ana Souza", "ativo": True},
    {"nome": "Carlos Lima", "ativo": False},
    {"nome": "Juliana Martins", "ativo": True},
]
```

Conte quantos clientes estão ativos.

---

### 7. Somar vendas acima de R$ 500

Use a lista:

```python
vendas = [150.00, 800.00, 1200.00, 320.00, 990.00]
```

Some apenas as vendas maiores ou iguais a `500`.

---

### 8. Produtos sem estoque

Use uma lista de produtos com nome e estoque.

Mostre apenas os produtos com estoque igual a zero.

---

### 9. Buscar cliente

Percorra uma lista de clientes e pare a busca com `break` quando encontrar o cliente procurado.

---

### 10. Ignorar pedidos cancelados

Use a lista:

```python
pedidos = [
    {"id": 101, "status": "aprovado"},
    {"id": 102, "status": "cancelado"},
    {"id": 103, "status": "aprovado"},
]
```

Use `continue` para ignorar pedidos cancelados e mostrar apenas os aprovados.

---

## Exercícios desafiadores

### 11. Relatório de vendas

Use uma lista de vendas.

Calcule:

- total vendido;
- quantidade de vendas;
- média de vendas;
- maior venda.

---

### 12. Validação de cadastros

Use a lista:

```python
cadastros = [
    {"nome": "Ana Souza", "idade": 28, "email_confirmado": True},
    {"nome": "Carlos Lima", "idade": 16, "email_confirmado": True},
    {"nome": "Juliana Martins", "idade": 34, "email_confirmado": False},
]
```

Mostre quais cadastros foram aprovados.

Regra:

- idade maior ou igual a 18;
- email confirmado.

---

### 13. Análise de estoque

Use uma lista de produtos com:

- nome;
- preço;
- estoque.

Calcule:

- valor total em estoque;
- quantidade de produtos sem estoque;
- produtos com estoque abaixo de 5.
