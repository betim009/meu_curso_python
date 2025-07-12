# ✅ Gabarito Comentado — Exercícios Lista de Supermercado

---

## 📘 Bloco 1 — Acesso direto e modificação

1. Acesse e imprima o nome do primeiro produto na lista `produtos`.

```python
print(produtos[0]["nome"])  # Arroz
```

2. Imprima o preço do terceiro item da lista `supermercado`, formatando a saída.

```python
print(f"Preço: R$ {supermercado['precos'][2]:.2f}")  # Preço: R$ 4.00
```

3. Altere o valor do estoque do produto `'Feijão'`.

```python
produtos[1]["estoque"] = 10
```

4. Mude a unidade do produto `'Café'` na estrutura `supermercado`.

```python
indice = supermercado["produtos"].index("Café")
supermercado["unidades"][indice] = "g"
```

5. Acesse nome e unidade do produto na posição 2.

```python
print(f"Produto: {supermercado['produtos'][2]} | Unidade: {supermercado['unidades'][2]}")
# Produto: Leite | Unidade: litro
```

---

## 🔁 Bloco 2 — Uso de `for item in ...`

6. Imprima o nome de cada item em `produtos`.

```python
for item in produtos:
    print(item["nome"])
```

7. Mostre todas as unidades da estrutura `supermercado`.

```python
for unidade in supermercado["unidades"]:
    print(unidade)
```

8. Liste todos os preços da lista `produtos`.

```python
for item in produtos:
    print(item["preco"])
```

9. Nome e estoque separados por hífen.

```python
for item in produtos:
    print(f"{item['nome']} - {item['estoque']}")
```

10. Produtos com índice na estrutura `supermercado`.

```python
for i in range(len(supermercado["produtos"])):
    print(f"{i} - {supermercado['produtos'][i]}")
```

---

## 🔍 Bloco 3 — Uso de `for` com `if`

11. Produtos com estoque menor que 15.

```python
for item in produtos:
    if item["estoque"] < 15:
        print(item["nome"])
```

12. Produtos com preço maior que R$ 5.00.

```python
for i in range(len(supermercado["precos"])):
    if supermercado["precos"][i] > 5:
        print(supermercado["produtos"][i])
```

13. Produtos cuja unidade é "kg".

```python
for item in produtos:
    if item["unidade"] == "kg":
        print(item["nome"])
```

14. Produtos com estoque acima de 20.

```python
for i in range(len(supermercado["estoque"])):
    if supermercado["estoque"][i] > 20:
        print(supermercado["produtos"][i])
```

15. Produtos que começam com "C".

```python
for item in produtos:
    if item["nome"].startswith("C"):
        print(item["nome"])
```

---

**Observação:** Pode haver mais de uma forma correta para resolver cada exercício. O importante é entender a lógica e treinar bastante!
