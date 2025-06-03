
# 🛒 Construir um ERP de Mercado

Este projeto tem como objetivo construir a lógica de um sistema de **ERP (Enterprise Resource Planning)** para um pequeno mercado, começando apenas com a estrutura de dados, sem interface gráfica.

---

## 📦 Etapa 1: Definição dos Produtos

Você deve começar definindo os **produtos iniciais** do sistema.  
Exemplos:

- Arroz  
- Feijão  
- Cebola  
- Macarrão

Esses produtos devem ser organizados em uma **lista de dicionários**.  
Cada produto será um dicionário com **chaves** (propriedades) como:

```python
{
  "id": 123,
  "nome": "Arroz",
  "preco": 6.50,
  "estoque": 20
}
```

### 🔍 Pontos para refletir:

- O produto pode acabar (estoque 0).
- Podem existir diferentes tipos de arroz.
- Não é possível vender um produto que não está no estoque.
- É necessário ter uma função para alterar os dados de um produto.
- Você poderá cadastrar novos produtos futuramente.

---

## 🧾 Etapa 2: Registro das Vendas

As vendas também serão armazenadas em uma **lista de dicionários**.  
Cada venda será representada por um dicionário contendo, no mínimo:

```python
{
  "id_produto": 231,
  "data": "23/03/2025 08:42:04"
}
```

### Exemplo:

#### Venda 1:
```python
[
  { "id_produto": 231, "data": "23/03/25 08:42:04" },
  { "id_produto": 123, "data": "23/03/25 08:42:04" }
]
```

#### Venda 2:
```python
[
  { "id_produto": 131, "data": "23/03/25 08:45:04" }
]
```

### 🤔 O que considerar:

- Cada venda precisa estar ligada a um produto existente.
- Pode ser necessário corrigir vendas feitas com erro.
- Você poderá cadastrar novas vendas.
- Também será possível excluir uma venda já registrada.

---

## 🚀 Expansão futura do projeto

Depois que toda a lógica estiver implementada corretamente, você poderá:

- Criar uma **interface gráfica** com bibliotecas como Tkinter ou PyQt.
- Conectar com um **banco de dados** para persistência de dados.
- Adicionar controle de **usuários e permissões**.
- Implementar **relatórios de vendas** com gráficos.
- Adicionar filtros por data ou produto.

---

## 💡 Observações Finais

Inicialmente, este será um projeto **sem interface gráfica**.  
O foco será na construção da **lógica e organização dos dados**.

Após essa etapa, com a lógica funcionando corretamente, poderemos planejar juntos como será a **interface visual** do sistema.

---

📌 *Esse projeto é excelente para praticar dicionários, listas, controle de fluxo e organização de dados em Python!*
