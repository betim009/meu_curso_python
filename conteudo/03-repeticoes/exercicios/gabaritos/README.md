# Gabaritos - Repetições

Compare sua solução com calma.

O objetivo é entender como loops automatizam tarefas repetitivas e processam dados.

---

## 1. Listar clientes

```python
clientes = ["Ana Souza", "Carlos Lima", "Juliana Martins"]

for cliente in clientes:
    print(cliente)
```

Explicação:

- O `for` percorre cada item da lista.
- A variável `cliente` recebe um nome por vez.

---

## 2. Somar vendas

```python
vendas = [100.00, 250.00, 400.00]
total = 0

for venda in vendas:
    total += venda

print(f"Total vendido: R$ {total:.2f}")
```

Explicação:

- `total` começa em zero.
- Cada venda é somada ao acumulador.

---

## 3. Contar produtos

```python
produtos = ["Notebook", "Monitor", "Teclado"]
quantidade = 0

for produto in produtos:
    quantidade += 1

print(f"Quantidade de produtos: {quantidade}")
```

Explicação:

- O contador aumenta uma vez para cada produto.

---

## 4. Gerar números de pedidos

```python
for numero in range(1, 6):
    print(f"Processando pedido {numero}")
```

Explicação:

- `range(1, 6)` gera os números de 1 até 5.

---

## 5. Tentativas de login

```python
tentativas = 0

while tentativas < 3:
    print(f"Tentativa {tentativas + 1}")
    tentativas += 1
```

Explicação:

- O contador evita loop infinito.
- O loop para quando `tentativas` chega a 3.

---

## 6. Contar clientes ativos

```python
clientes = [
    {"nome": "Ana Souza", "ativo": True},
    {"nome": "Carlos Lima", "ativo": False},
    {"nome": "Juliana Martins", "ativo": True},
]

ativos = 0

for cliente in clientes:
    if cliente["ativo"]:
        ativos += 1

print(f"Clientes ativos: {ativos}")
```

Explicação:

- O `if` verifica o status.
- O contador só aumenta para clientes ativos.

---

## 7. Somar vendas acima de R$ 500

```python
vendas = [150.00, 800.00, 1200.00, 320.00, 990.00]
total = 0

for venda in vendas:
    if venda >= 500:
        total += venda

print(f"Total das vendas acima de R$ 500: R$ {total:.2f}")
```

Explicação:

- O acumulador soma apenas vendas que passam pela condição.

---

## 8. Produtos sem estoque

```python
produtos = [
    {"nome": "Notebook", "estoque": 5},
    {"nome": "Monitor", "estoque": 0},
    {"nome": "Teclado", "estoque": 12},
]

for produto in produtos:
    if produto["estoque"] == 0:
        print(f"{produto['nome']} está sem estoque.")
```

Explicação:

- Cada produto é um dicionário.
- A chave `"estoque"` guarda a quantidade disponível.

---

## 9. Buscar cliente

```python
clientes = ["Ana Souza", "Carlos Lima", "Juliana Martins"]
cliente_procurado = "Carlos Lima"

for cliente in clientes:
    if cliente == cliente_procurado:
        print("Cliente encontrado.")
        break
```

Explicação:

- `break` interrompe o loop quando o cliente é encontrado.

---

## 10. Ignorar pedidos cancelados

```python
pedidos = [
    {"id": 101, "status": "aprovado"},
    {"id": 102, "status": "cancelado"},
    {"id": 103, "status": "aprovado"},
]

for pedido in pedidos:
    if pedido["status"] == "cancelado":
        continue

    print(f"Pedido aprovado: {pedido['id']}")
```

Explicação:

- `continue` pula pedidos cancelados.
- O `print` só roda para pedidos não cancelados.

---

## 11. Relatório de vendas

```python
vendas = [1200.00, 850.50, 399.90, 1500.00]

total = 0
quantidade = 0
maior_venda = 0

for venda in vendas:
    total += venda
    quantidade += 1

    if venda > maior_venda:
        maior_venda = venda

media = total / quantidade

print(f"Total vendido: R$ {total:.2f}")
print(f"Quantidade de vendas: {quantidade}")
print(f"Média de vendas: R$ {media:.2f}")
print(f"Maior venda: R$ {maior_venda:.2f}")
```

Explicação:

- `total` acumula valores.
- `quantidade` conta registros.
- `maior_venda` guarda o maior valor encontrado até o momento.

---

## 12. Validação de cadastros

```python
cadastros = [
    {"nome": "Ana Souza", "idade": 28, "email_confirmado": True},
    {"nome": "Carlos Lima", "idade": 16, "email_confirmado": True},
    {"nome": "Juliana Martins", "idade": 34, "email_confirmado": False},
]

for cadastro in cadastros:
    if cadastro["idade"] >= 18 and cadastro["email_confirmado"]:
        print(f"Cadastro aprovado: {cadastro['nome']}")
```

Explicação:

- A aprovação exige duas regras.
- Usamos `and` porque ambas precisam ser verdadeiras.

---

## 13. Análise de estoque

```python
produtos = [
    {"nome": "Notebook", "preco": 4200.00, "estoque": 5},
    {"nome": "Monitor", "preco": 950.00, "estoque": 0},
    {"nome": "Teclado", "preco": 180.00, "estoque": 3},
]

valor_total = 0
sem_estoque = 0

for produto in produtos:
    valor_total += produto["preco"] * produto["estoque"]

    if produto["estoque"] == 0:
        sem_estoque += 1

    if produto["estoque"] < 5:
        print(f"Estoque baixo: {produto['nome']}")

print(f"Valor total em estoque: R$ {valor_total:.2f}")
print(f"Produtos sem estoque: {sem_estoque}")
```

Explicação:

- O valor em estoque é preço vezes quantidade.
- O mesmo loop pode calcular métricas e exibir alertas.
