# 🧰 Trabalhando com Listas de Produtos e Condições em Python

Este material ensina como acessar e filtrar dados em **listas de dicionários**, 
utilizando estruturas de repetição e condições em Python. O foco é mostrar 
formas **estáticas e dinâmicas** de exibir os dados, e aplicar filtros com `if`.

---

## 🛍️ Lista de Produtos

Vamos usar a seguinte lista com dicionários representando produtos:

```python
produtos = [
    {"id_produto": 1, "produto": "Intel i9, 10ª geração", "preco": 1200.00},
    {"id_produto": 2, "produto": "AMD Ryzen 7 5800X", "preco": 950.00},
    {"id_produto": 3, "produto": "Placa-mãe ASUS B550", "preco": 750.00},
    {"id_produto": 4, "produto": "Memória RAM 16GB DDR4", "preco": 320.00},
    {"id_produto": 5, "produto": "SSD NVMe 1TB", "preco": 600.00},
    {"id_produto": 6, "produto": "Fonte Corsair 650W", "preco": 420.00},
    {"id_produto": 7, "produto": "Gabinete Gamer RGB", "preco": 350.00},
    {"id_produto": 8, "produto": "Monitor LG 24'' Full HD", "preco": 900.00},
    {"id_produto": 9, "produto": "Teclado Mecânico Redragon", "preco": 250.00},
    {"id_produto": 10, "produto": "Mouse Gamer Logitech G203", "preco": 180.00},
    {"id_produto": 11, "produto": "Headset HyperX Cloud Stinger", "preco": 320.00},
    {"id_produto": 12, "produto": "HD Seagate 2TB", "preco": 400.00},
]
```

---

## 📌 Acesso Estático

A forma **estática** acessa item por item, manualmente:

```python
print(produtos[0]["produto"])  # Intel i9, 10ª geração
print(produtos[1]["produto"])  # AMD Ryzen 7 5800X
print(produtos[2]["produto"])  # Placa-mãe ASUS B550
```

---

## 🔁 Acesso Dinâmico com `for`

Usamos `for` para **percorrer** a lista automaticamente:

```python
for item in produtos:
    print(item["produto"], item["preco"])
```

### Melhorando a visualização:

```python
for item in produtos:
    print(f"Nome: {item['produto']}")
    print(f"Preço: {item['preco']}")
    print()
```

---

## 🧠 Condições com `if`

Podemos combinar `for` com `if` para criar **filtros**.

### Verificar se o nome do produto é exatamente igual:

```python
for item in produtos:
    if item["produto"] == "Intel i9, 10ª geração":
        print(item)
```

### Verificar se o nome **contém** a palavra `"HD"`:

```python
for item in produtos:
    if "HD" in item["produto"]:
        print(item)
```

### Verificar todos os produtos que **não contêm** `"HD"`:

```python
for item in produtos:
    if "HD" not in item["produto"]:
        print(item)
```

### Verificar produtos com preço acima de 500 reais:

```python
for item in produtos:
    if item["preco"] > 500:
        print(item)
```

---

## ✅ Tabela de Operadores Comuns

| Símbolo | Significado              |
|---------|--------------------------|
| `=`     | Atribuição de valor      |
| `==`    | Igualdade                |
| `!=`    | Diferente                |
| `>`     | Maior                    |
| `<`     | Menor                    |
| `>=`    | Maior ou igual           |
| `<=`    | Menor ou igual           |
| `+=`    | Incrementar              |
| `-=`    | Decrementar              |
| `%`     | Resto da divisão         |
| `in`    | Verifica se contém       |
| `not in`| Verifica se não contém   |

---

## 📝 Dica Final

Sempre que quiser exibir, procurar ou filtrar dados em listas de dicionários, 
use `for` com `if`. Esse padrão aparece muito em sistemas, listas de produtos, 
dados de usuários, etc.