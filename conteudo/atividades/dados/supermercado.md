# 🧪 Exercícios de Prática — Lista de Supermercado

Este material contém **15 exercícios práticos** usando duas bases de dados sobre produtos de supermercado.  
Eles estão divididos em três blocos com dificuldade crescente:

---

## 🧱 Bases de Dados

```python
produtos = [
    {"nome": "Arroz", "preco": 5.50, "unidade": "kg", "estoque": 20},
    {"nome": "Feijão", "preco": 6.00, "unidade": "kg", "estoque": 15},
    {"nome": "Leite", "preco": 4.00, "unidade": "litro", "estoque": 30},
    {"nome": "Ovos", "preco": 12.00, "unidade": "dúzia", "estoque": 10},
    {"nome": "Café", "preco": 8.50, "unidade": "pacote", "estoque": 25}
]

supermercado = {
    "produtos": ["Arroz", "Feijão", "Leite", "Ovos", "Café"],
    "precos": [5.50, 6.00, 4.00, 12.00, 8.50],
    "unidades": ["kg", "kg", "litro", "dúzia", "pacote"],
    "estoque": [20, 15, 30, 10, 25]
}
```

---

## 📘 Bloco 1 — Acesso direto e modificação

1. Acesse e imprima o nome do primeiro produto na lista `produtos`. Use a chave corretamente.
2. Imprima o preço do terceiro item da lista `supermercado`, formatando a saída como: `'Preço: R$ 4.00'`.
3. Altere o valor do estoque do produto `'Feijão'` na lista `produtos` para `10`.
4. Mude a unidade do produto `'Café'` na estrutura `supermercado` para `'g'`.
5. Acesse e imprima o nome e a unidade do produto na posição 2 da estrutura `supermercado`, no formato: `'Produto: Leite | Unidade: litro'`.

---

## 🔁 Bloco 2 — Uso de `for item in ...`

6. Percorra a lista `produtos` e imprima o nome de cada item.
7. Usando `for`, mostre todas as unidades dos produtos na estrutura `supermercado`.
8. Liste todos os preços dos produtos contidos na lista `produtos`, com `for`.
9. Para cada produto da lista `produtos`, imprima o nome e o estoque, separados por hífen.
10. Use `for` para imprimir todos os produtos da estrutura `supermercado`, com índice + nome.

---

## 🔍 Bloco 3 — Uso de `for` com `if`

11. Percorra a lista `produtos` e imprima somente os produtos com estoque menor que `15`.
12. Imprima os nomes dos produtos da estrutura `supermercado` que custam mais de `R$ 5.00`.
13. Exiba os produtos da lista `produtos` cuja unidade é `'kg'`.
14. Mostre todos os produtos da estrutura `supermercado` que têm estoque acima de `20` unidades.
15. Percorra a lista `produtos` e imprima os nomes dos produtos cujo nome começa com a letra `'C'`.

---

**Dica:** Teste cada exercício no terminal do Python ou em um script `.py` para praticar o uso de listas, dicionários, laços e condições.

