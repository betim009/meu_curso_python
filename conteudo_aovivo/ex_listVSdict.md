
# 📦 Quando Usar Listas e Dicionários em Python

Este material vai te mostrar **quando usar listas** e **quando usar dicionários**, com exemplos bem práticos. Ideal para quem está começando.

---

## 🧠 Conceito Básico

### 🔹 Lista (`list`)

- Usamos **listas** quando temos **múltiplos dados do mesmo tipo**.
- Ideal para armazenar **vários elementos** como se fossem uma "caixa com posições".

```python
frutas = ["Manga", "Uva", "Goiaba"]  # Lista com frutas
```

---

### 🔹 Dicionário (`dict`)

- Usamos **dicionário** quando queremos **organizar informações com significado**.
- Cada informação tem uma **chave (nome)** e um **valor**.

```python
usuario = {
    "nome": "João",
    "idade": 30,
    "assinante": True
}
```

---

## ❌ Exemplo Ruim

Quando temos vários dados soltos, fica bagunçado:

```python
venda1 = 250
data_venda1 = "30/01/2024"
nome_venda = "João"
```

---

## ✅ Forma Ideal: Dicionário

```python
venda = {
    "valor": 250,
    "data_venda": "30/01/24",
    "usuario": "João"
}
```

Assim temos **todas as informações organizadas** com nomes claros.

---

## 📚 Diferença Visual

| Lista               | Dicionário                     |
|---------------------|--------------------------------|
| Usa colchetes `[ ]` | Usa chaves `{ }`              |
| Usa posição `0, 1`  | Usa nomes: `"valor"`, `"data"` |

---

## 🧾 Exemplo com Múltiplas Vendas

Se temos várias vendas, usamos uma **lista de dicionários**:

```python
lista_vendas = [
    {
        "valor": 250,
        "data_venda": "30/01/24",
        "usuario": "João",
        "assinante": True
    },
    {
        "valor": 350,
        "data_venda": "30/01/24",
        "usuario": "Guilherme",
        "assinante": False
    }
]
```

Cada elemento da lista é um **dicionário representando uma venda**.

---

## 🔁 Percorrendo a Lista com `for`

### Exibir toda a lista:

```python
print(lista_vendas)
```

### Exibir cada venda separadamente:

```python
for x in lista_vendas:
    print(x)
```

**Saída esperada:**

```
{'valor': 250, 'data_venda': '30/01/24', 'usuario': 'João', 'assinante': True}
{'valor': 350, 'data_venda': '30/01/24', 'usuario': 'Guilherme', 'assinante': False}
```

---

## ✅ Conclusão

- Use **listas** para guardar **múltiplos itens em ordem**.
- Use **dicionários** para representar **uma entidade completa** com várias informações nomeadas.
- Para **múltiplas entidades organizadas**, use uma **lista de dicionários**.

---
