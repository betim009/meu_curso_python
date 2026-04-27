# Projeto - Sistema simples de pedidos

## Objetivo

Criar um sistema simples de pedidos usando programação orientada a objetos.

O projeto simula uma parte básica de um ecommerce:

- cadastrar um cliente;
- criar produtos;
- abrir um pedido;
- adicionar produtos ao pedido;
- calcular o total;
- fechar ou cancelar o pedido;
- escolher uma forma de pagamento.

O foco é praticar organização de código com classes, não criar uma loja completa.

## O que você vai praticar

- Classes representando entidades reais.
- Encapsulamento simples.
- Método especial `__str__`.
- Separação de responsabilidades.
- Herança simples.
- Polimorfismo simples.
- Lista de objetos.
- Regras de negócio dentro das classes corretas.

## Visão geral das classes

```text
Cliente
  - representa quem compra
  - guarda nome e email
  - valida email

Produto
  - representa um item vendido
  - guarda nome e preço
  - controla alteração de preço

Pedido
  - pertence a um cliente
  - guarda uma lista de produtos
  - calcula total
  - controla status

PagamentoCartao / PagamentoPix / PagamentoBoleto
  - processam o pagamento de formas diferentes
  - usam o mesmo método: processar
```

## Passo 1 - Criar a classe Cliente

```python
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self._email = email
```

O e-mail fica como `_email` porque queremos alterar esse dado somente com validação.

## Passo 2 - Criar validação de e-mail

```python
def email_valido(self):
    return "@" in self._email and "." in self._email
```

Essa regra fica no cliente porque pertence ao cadastro do cliente.

## Passo 3 - Criar a classe Produto

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco
```

O preço também fica protegido por convenção. Assim, o sistema pode controlar alterações.

## Passo 4 - Criar a classe Pedido

```python
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []
        self.status = "aberto"
```

Um pedido começa aberto e sem produtos.

## Passo 5 - Adicionar produtos ao pedido

```python
def adicionar_produto(self, produto):
    if self.status != "aberto":
        print("Não é possível adicionar produto em pedido fechado ou cancelado.")
        return

    self.produtos.append(produto)
```

Essa regra fica dentro de `Pedido`, porque é o pedido que sabe se ainda aceita novos produtos.

## Passo 6 - Calcular o total

```python
def calcular_total(self):
    total = 0

    for produto in self.produtos:
        total += produto.consultar_preco()

    return total
```

O pedido não precisa saber como o preço é guardado por dentro. Ele usa o método público `consultar_preco`.

## Passo 7 - Criar formas de pagamento

Cada forma de pagamento terá o mesmo método:

```python
processar(valor)
```

Isso permite usar polimorfismo:

```python
pagamento.processar(pedido.calcular_total())
```

O sistema não precisa saber se é Pix, cartão ou boleto. Ele só chama `processar`.

## Código completo

O código completo está em [`sistema_pedidos.py`](sistema_pedidos.py).

## Como executar

Na raiz do curso, execute:

```bash
python3 conteudo/08-POO/projeto/sistema_pedidos.py
```

## Decisões tomadas

### Por que separar Cliente, Produto e Pedido?

Porque cada classe representa uma parte diferente do ecommerce.

O cliente guarda dados do comprador. O produto guarda dados do item vendido. O pedido organiza a compra.

### Por que usar `_email` e `_preco`?

Para indicar que esses atributos devem ser alterados por métodos, não diretamente.

Isso permite validar e evitar dados inválidos.

### Por que usar `__str__`?

Para melhorar a exibição dos objetos.

Assim, `print(cliente)` e `print(produto)` mostram informações úteis.

### Por que o pedido controla o status?

Porque o status pertence ao pedido.

Um produto não sabe se o pedido está aberto. Um cliente também não. Quem sabe isso é o próprio pedido.

### Por que criar classes de pagamento?

Porque cada pagamento pode ter uma regra diferente.

Cartão, Pix e boleto são diferentes, mas todos podem responder ao método `processar`.

## Desafios extras

1. Impedir que um pedido vazio seja pago.
2. Criar desconto no pedido.
3. Criar quantidade para cada produto.
4. Criar uma classe `ItemPedido` com produto e quantidade.
5. Salvar o resumo do pedido em um arquivo `.txt`.
