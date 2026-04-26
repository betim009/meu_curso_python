# Exercicios - Arquivos em Python

Resolva os exercicios usando os arquivos da pasta `../dados`.

Antes de comecar:

- Use `with open(...)` para abrir arquivos.
- Use `encoding="utf-8"`.
- Para CSV, prefira `csv.DictReader`.
- Converta numeros antes de calcular: `int()` para quantidades e `float()` para valores.
- Salve os arquivos gerados dentro da pasta `dados` ou em uma pasta temporaria criada por voce.

## Faceis

### 1. Listar nomes de clientes

Leia o arquivo `dados/clientes.csv` e mostre apenas o nome de cada cliente.

Saida esperada aproximada:

```text
Ana Souza
Bruno Lima
Carla Mendes
...
```

### 2. Mostrar clientes ativos

Leia `dados/clientes.csv` e mostre nome e email apenas dos clientes em que a coluna `ativo` seja igual a `sim`.

### 3. Contar chamados

Leia `dados/chamados.txt` e conte quantas linhas existem no arquivo.

### 4. Criar arquivo de boas-vindas

Crie um arquivo chamado `boas_vindas.txt` contendo tres linhas:

```text
Bem-vindo ao sistema.
Seu cadastro foi recebido.
Em breve entraremos em contato.
```

### 5. Listar produtos com estoque

Leia `dados/produtos.csv` e mostre o nome de cada produto junto com a quantidade em estoque.

## Medios

### 6. Calcular total vendido

Leia `dados/vendas.csv` e calcule o total vendido.

Regra:

```text
subtotal = quantidade * preco_unitario
```

### 7. Calcular media por pedido

Leia `dados/vendas.csv`, calcule o total vendido e divida pela quantidade de pedidos.

### 8. Filtrar produtos com estoque baixo

Leia `dados/produtos.csv` e gere um arquivo `estoque_baixo.csv` contendo apenas os produtos com estoque menor que 10.

### 9. Contar clientes por cidade

Leia `dados/clientes.csv` e mostre quantos clientes existem em cada cidade.

Exemplo:

```text
Sao Paulo: 2
Curitiba: 2
```

### 10. Gerar resumo de clientes ativos

Leia `dados/clientes.csv` e gere um arquivo `clientes_ativos.txt` com nome, email e cidade de cada cliente ativo.

## Desafiadores

### 11. Relatorio de vendas por cliente

Leia `dados/vendas.csv` e calcule quanto cada cliente comprou no total.

Gere um arquivo `vendas_por_cliente.csv` com as colunas:

```csv
cliente,total
```

### 12. Produto mais vendido em quantidade

Leia `dados/vendas.csv` e descubra qual produto teve a maior quantidade total vendida.

Exiba:

```text
Produto mais vendido: Mouse
Quantidade vendida: 4
```

### 13. Relatorio completo de estoque

Leia `dados/produtos.csv` e gere um arquivo `relatorio_estoque.txt` contendo:

- quantidade total de produtos cadastrados
- soma total de unidades em estoque
- produto com menor estoque
- produto com maior preco
- lista de produtos com estoque menor que 10

## Como estudar com os gabaritos

Tente resolver sozinho antes de abrir os arquivos em `gabaritos/`.

Depois compare:

- O seu codigo abre os arquivos com `with`?
- O seu codigo converte numeros corretamente?
- O seu codigo separa leitura, processamento e escrita?
- O resultado gerado faz sentido com os dados de entrada?
