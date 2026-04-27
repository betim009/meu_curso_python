# Exercício 12 - Catálogo com produtos físicos e digitais

Crie uma classe base `Produto` e duas classes filhas: `ProdutoFisico` e `ProdutoDigital`.

## Requisitos

### Produto

- Atributos: `nome` e `preco`.
- Método `calcular_preco_final`.

### ProdutoFisico

- Atributo extra: `frete`.
- O preço final deve ser `preco + frete`.

### ProdutoDigital

- Atributo extra: `taxa_plataforma`.
- O preço final deve ser `preco + taxa_plataforma`.

## Situação real

Produtos diferentes podem compartilhar uma base e ter regras específicas.
