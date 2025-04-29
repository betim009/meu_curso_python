# 📚 Introdução: Entendendo Listas e Dicionários no Python

## 🧠 Processo de Aprendizado:
1. **Ver / Aprender algo**
2. **Repetir**
3. **Aprender algo novo**
4. **Repetir**

---

## 🚀 Objetivos atuais:
- [x] Trabalhar com **Tipos de dados**: `list` (listas)
- [x] Entender **Repetições**: `for`

---

# 1⃣ Trabalhando com Listas

Uma **lista** é usada para guardar **múltiplos valores** em uma mesma variável.

```python
# Lista de números (preços, dinheiro, etc.)
lista = [420, 123, 312.10, 320.99]

print(lista)
# Saída: [420, 123, 312.1, 320.99]
```

✅ Cada elemento da lista pode ser acessado pelo seu **índice** (posição).

```python
print(lista[0])  # Primeiro item -> 420
print(lista[1])  # Segundo item -> 123
```

---

# 2⃣ Trabalhando com Dicionários

Um **dicionário** guarda informações em **pares de chave:valor**.

```python
# Exemplo de dicionário
{
    "chave": "valor",
    "nome": "Alberto",
    "idade": 30,
    "professor": True
}
```

✅ Para acessar um valor, basta usar a chave:

```python
pessoa = {
    "nome": "Alberto",
    "idade": 30
}

print(pessoa["nome"])  # Alberto
print(pessoa["idade"])  # 30
```

---

# 3⃣ Lista de Dicionários

Você também pode criar **listas que guardam vários dicionários**.

```python
lista_dicts = [
    {"id": 1, "valor": 420, "data": "29/04"},
    {"id": 2, "valor": 123, "data": "29/04"},
    {"id": 3, "valor": 450.99, "data": "29/04"},
]

print(lista_dicts)
```

✅ Acessando elementos:

```python
print(lista_dicts[0])  # Primeiro dicionário
print(lista_dicts[1])  # Segundo dicionário

# Acessando a "data" do primeiro dicionário
print(lista_dicts[0]["data"])  # Saída: 29/04
```

---

# 4⃣ Percorrendo Listas com `for`

Para **percorrer** todos os itens de uma lista, usamos o `for`.

```python
# Errado:
# print(lista_dicts["data"])

# Correto:
for item in lista_dicts:
    print(item)        # Exibe o dicionário completo
    print(item["data"])  # Exibe apenas a data de cada item
```

🔹 O nome `item` é só uma escolha — poderia ser qualquer nome, mas `item` é o mais comum para representar cada elemento.

---

# 5⃣ Percorrendo Listas Simples

Você também pode percorrer **listas simples** (sem dicionários):

```python
for item in lista:
    print(item)
```

Isso vai imprimir cada número da lista, um por linha.

---

# 🔥 Resumo Visual

| Conceito | Exemplo | Descrição |
|:---|:---|:---|
| Lista | `[1, 2, 3]` | Coleção ordenada de valores |
| Dicionário | `{"nome": "Alberto"}` | Coleção de pares chave:valor |
| Lista de Dicionários | `[{"id": 1}, {"id": 2}]` | Vários dicionários dentro de uma lista |
| For | `for item in lista:` | Estrutura de repetição |

---

# 📢 Observação importante
- Listas são organizadas por **índices** (posição: 0, 1, 2, ...)
- Dicionários são organizados por **chaves** (nomes personalizados)
- `for` percorre **todos os itens** de listas e pode acessar dicionários dentro delas.

---

# ✍️ Dica final

> "Repetição é a mãe da aprendizagem."
>
> 🚀 **Veja → Repita → Veja algo novo → Repita novamente!**

