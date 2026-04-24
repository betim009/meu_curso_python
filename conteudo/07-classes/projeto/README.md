# Mini Projeto - Sistema Simples de Estoque

## Objetivo

Criar um pequeno sistema de estoque usando classes.

Este projeto ajuda a entender por que classes são úteis: um produto tem dados, e o estoque tem ações.

---

## Requisitos

Crie duas classes:

### Classe `Produto`

Atributos:

- `nome`
- `preco`
- `quantidade`

Métodos:

- `valor_total()`: retorna `preco * quantidade`
- `mostrar_dados()`: retorna uma frase com os dados do produto

### Classe `Estoque`

Atributos:

- `produtos`: lista de produtos cadastrados

Métodos:

- `adicionar_produto(produto)`
- `listar_produtos()`
- `calcular_valor_total()`

---

## Exemplo de uso

```python
estoque = Estoque()

produto_1 = Produto("Arroz", 25.90, 10)
produto_2 = Produto("Feijao", 8.50, 20)

estoque.adicionar_produto(produto_1)
estoque.adicionar_produto(produto_2)

estoque.listar_produtos()
print(estoque.calcular_valor_total())
```

---

## Desafio extra

Depois de fazer a versão básica, tente adicionar:

- Busca de produto por nome.
- Remoção de produto.
- Validação para não aceitar preço negativo.
- Validação para não aceitar quantidade negativa.
