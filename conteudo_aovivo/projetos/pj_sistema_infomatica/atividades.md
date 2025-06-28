# 📝 Atividades com Listas de Dicionários

Abaixo temos **3 diferentes bases de dados** representadas por listas de dicionários. 
Elas servirão como base para você praticar **acesso, filtragem e exibição** de informações.

---

## 🛒 Base 1: Produtos de Informática

```python
produtos = [
    {"id": 1, "nome": "Notebook Dell", "preco": 3500.00},
    {"id": 2, "nome": "Impressora HP", "preco": 850.00},
    {"id": 3, "nome": "Pen Drive 64GB", "preco": 60.00},
    {"id": 4, "nome": "Mouse sem fio", "preco": 120.00},
    {"id": 5, "nome": "Câmera Logitech", "preco": 460.00},
]
```

---

## 🎥 Base 2: Filmes em Cartaz

```python
filmes = [
    {"titulo": "Missão Impossível", "ano": 2023, "genero": "Ação"},
    {"titulo": "Elementos", "ano": 2023, "genero": "Animação"},
    {"titulo": "Oppenheimer", "ano": 2023, "genero": "Drama"},
    {"titulo": "Homem-Aranha", "ano": 2021, "genero": "Aventura"},
    {"titulo": "Super Mario Bros", "ano": 2023, "genero": "Animação"},
]
```

---

## 🏫 Base 3: Alunos da Turma

```python
alunos = [
    {"nome": "Carlos", "nota": 8.0, "aprovado": True},
    {"nome": "Beatriz", "nota": 5.5, "aprovado": False},
    {"nome": "João", "nota": 9.2, "aprovado": True},
    {"nome": "Larissa", "nota": 6.9, "aprovado": True},
    {"nome": "Pedro", "nota": 4.8, "aprovado": False},
]
```

---

## 📌 Sugestões de Atividades

### Base 1: Produtos
1. Exiba apenas os nomes dos produtos.
2. Mostre nome e preço de todos.
3. Filtre os produtos com preço acima de R$ 500.
4. Encontre o produto que contém a palavra "Mouse".

### Base 2: Filmes
1. Mostre todos os filmes lançados em 2023.
2. Exiba apenas os filmes do gênero "Animação".
3. Conte quantos filmes são do tipo "Drama".

### Base 3: Alunos
1. Mostre todos os nomes dos alunos aprovados.
2. Liste os alunos com nota menor que 6.
3. Exiba nome, nota e se foi aprovado.

---

## ✅ Dica

Você pode fazer tudo com `for` e `if`, como aprendeu no material anterior!

```python
for aluno in alunos:
    if aluno["aprovado"]:
        print(aluno["nome"])
```