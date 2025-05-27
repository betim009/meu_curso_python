# 🧮 Comparando duas listas com FOR

## 📚 Contexto

Vamos trabalhar com duas **listas de dicionários**:

- `produtos`: lista com todos os produtos do estoque.
- `vendas`: lista com os produtos que já foram vendidos.

Nosso objetivo é:
> 🔎 Descobrir quais produtos **ainda não foram vendidos**.

---

## 🗃️ Estrutura dos dados

```python
produtos = [
    {"id": 1, "produto": "i9 Intel de 10"},
    {"id": 2, "produto": "i9 Intel de 10"},
    {"id": 3, "produto": "i9 Intel de 10"},
    {"id": 4, "produto": "i9 Intel de 10"},
    {"id": 5, "produto": "i7 Intel de 13"},
    {"id": 6, "produto": "i7 Intel de 13"},
    {"id": 7, "produto": "i7 Intel de 13"},
]

vendas = [
    {"id": 1, "id_produto": 4},
    {"id": 2, "id_produto": 5},
]
```

---

## ❓Por que usar `for`?

Queremos fazer algo como:

1. **Para cada produto** no estoque:
2. Verificar se **o ID do produto está na lista de vendas**.
3. Se **não estiver**, significa que o produto **não foi vendido**.

---

## 🔁 Fluxo da lógica

```text
PARA CADA -> FOR

Para cada PRODUTO
   ↓
Verificar cada VENDA
   ↓
As vendas que têm o id DIFERENTE
```

---

## 🧠 Quando usar listas?

- Você vai ter mais de 1 produto? → **Então use lista.**
- Você vai ter mais de 1 venda? → **Também use lista.**

Essas listas começam **vazias**, e vão sendo preenchidas de acordo com a lógica.

---

## 🧠 Quando usar 2 `for`?

Pergunta: Você tem 1 ou 2 listas?

- Se tem **1 lista só** → provavelmente **1 for** resolve.
- Se tem **2 listas** → pode precisar de **2 for**.

> 📌 **Dica importante:**
> Se você precisa que **uma lista interaja com a outra**, o ideal é:
> `for` **dentro de outro** `for`.

---

## ✅ Exemplo prático: Produtos não vendidos

```python
for produto in produtos:
    vendido = False
    for venda in vendas:
        if produto["id"] == venda["id_produto"]:
            vendido = True
            break
    if not vendido:
        print(f'Produto em estoque: {produto["produto"]} (id {produto["id"]})')
```

### 🔍 O que esse código faz?

1. Percorre todos os produtos.
2. Para cada produto, verifica **em todas as vendas** se ele foi vendido.
3. Se **não achar o ID**, então esse produto ainda está **em estoque**.
4. Usa `break` para sair do `for` interno mais rápido se encontrar uma venda.

---

## 📝 Resultado esperado

```text
Produto em estoque: i9 Intel de 10 (id 1)
Produto em estoque: i9 Intel de 10 (id 2)
Produto em estoque: i9 Intel de 10 (id 3)
Produto em estoque: i7 Intel de 13 (id 6)
Produto em estoque: i7 Intel de 13 (id 7)
```

---

## 🧠 Resumo final

| Situação                                | O que usar            |
|----------------------------------------|------------------------|
| Só uma lista a ser verificada          | 1 `for`                |
| Duas listas comparando elementos       | 2 `for` (aninhado)     |
| Precisa verificar se está em outra     | `for` dentro de `for`  |
| Lista começa vazia                     | Vai sendo preenchida   |
