# Exercício 12 - Sistema de pedidos

Crie um sistema de pedidos com três classes: `Cliente`, `Produto` e `Pedido`.

## Requisitos

### Cliente

- Atributos: `nome` e `email`.

### Produto

- Atributos: `nome` e `preco`.

### Pedido

- Atributos: `cliente`, `produtos` e `status`.
- O status inicial deve ser `"aberto"`.
- Método `adicionar_produto(produto)`.
- Método `calcular_total`.
- Método `fechar_pedido`.
- Método `exibir_resumo`.

## Regra

Depois que o pedido for fechado, não deve ser possível adicionar novos produtos.
