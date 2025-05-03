
# 🧠 Projeto Python + MySQL – Guia Didático Completo

Este material didático vai **transformar um projeto real em um guia passo a passo**, explicando tudo como se fosse para alguém que **está aprendendo há apenas duas semanas**.

Vamos aprender a **conectar com banco de dados**, **buscar dados**, **filtrar registros**, e até **fazer atualizações** usando Python e MySQL.

---

## 🎯 Objetivo do Projeto

Você vai aprender a:

- Conectar o Python com um banco de dados MySQL
- Fazer buscas com `SELECT *`
- Buscar registros filtrando por `id`
- Atualizar valores usando `UPDATE`
- Encerrar a conexão corretamente
- Organizar o código em arquivos separados (modularização)

---

## 🧱 Estrutura do Projeto

```
meu_projeto_mysql/
│
├── app.py           # Arquivo principal com funções
├── connection.py    # Responsável pela conexão com o MySQL
└── venv/            # Ambiente virtual (não precisa subir para o GitHub)
```

---

## ⚙️ connection.py – Como conectar com o banco de dados

Esse arquivo serve para centralizar os dados de **conexão** com o banco. Toda vez que você quiser usar o banco, basta importar `connection` e `cursor`.

### 📦 Código:

```python
import mysql.connector

config = {
    "user": "root",
    "password": "1234",          # sua senha do MySQL
    "host": "localhost",         # onde está o MySQL
    "database": "my_db2",        # nome do banco de dados
    "raise_on_warnings": True    # ajuda a ver erros com mais clareza
}

connection = mysql.connector.connect(**config)
cursor = connection.cursor()
```

### 🧠 Por que separar isso?

- Evita repetição
- Ajuda na organização do código
- Permite trocar a base de dados sem alterar todo o projeto

---

## 🚀 app.py – Lógica do projeto

Esse arquivo é o **principal**. Aqui estão as funções para **ver contratos**, **buscar por id**, e **editar um contrato**.

---

### 1️⃣ Ver todos os contratos – `get_contratos()`

```python
def get_contratos():
    cursor.execute("SELECT * FROM contratos")
    result = cursor.fetchall()

    for row in result:
        print({
            "id": row[0],
            "cpf_cliente": row[1], 
            "valor_parcela": format(float(row[2]), ".2f")
        })

    cursor.close()
    connection.close()
    print("Conexão encerrada.")
```

#### 🧠 Explicando:

- `fetchall()` pega **todos os registros** da tabela.
- Cada `row` é uma linha da tabela (`tuple`)
- A função `format(..., ".2f")` deixa o valor da parcela com **2 casas decimais**

---

### 2️⃣ Buscar contrato por ID – `get_contrato_id(id)`

```python
def get_contrato_id(id):
    cursor.execute("SELECT * FROM contratos WHERE id_contrato = %s", (id,))
    result = cursor.fetchone()

    if result:
        print({
            "id": result[0],
            "cpf_cliente": result[1], 
            "valor_parcela": format(float(result[2]), ".2f")
        })
    else:
        print(f"Contrato com id {id} não encontrado.")

    cursor.close()
    connection.close()
    print("Conexão encerrada.")
```

#### 💡 O que muda aqui?

- A consulta tem `WHERE id_contrato = %s`
- Usamos `fetchone()` porque esperamos **só um resultado**
- `id` é passado como argumento da função

---

### 3️⃣ Atualizar um contrato – `alterar_contrato(id, novo_valor)`

```python
def alterar_contrato(id, novo_valor):
    cursor.execute("UPDATE contratos SET valor_parcela = %s WHERE id_contrato = %s", (novo_valor, id))
    connection.commit()

    if cursor.rowcount > 0:
        print(f"Contrato com id {id} alterado com sucesso. Novo valor da parcela: {novo_valor:.2f}")
    else:
        print(f"Contrato com id {id} não encontrado ou não foi alterado.")

    cursor.close()
    connection.close()
    print("Conexão encerrada.")
```

#### 🧠 Novidade aqui:

- `commit()` é obrigatório para salvar a alteração
- `cursor.rowcount` mostra se **alguma linha foi afetada**

---

## 🔁 Testando as funções

Você pode **ativar e desativar** as funções comentando ou descomentando no final do `app.py`:

```python
# get_contratos()
# get_contrato_id(1)
alterar_contrato(1, 250.44)
```

---

## ⚠️ Cuidados importantes

- Sempre **feche** o cursor e a conexão com `close()`
- Use `commit()` em comandos que modificam o banco
- Evite abrir múltiplas conexões ao mesmo tempo
- Separe a conexão do restante do código sempre que possível

---

## 🧠 Conclusão

Você aprendeu a:

- Conectar seu código Python ao MySQL
- Executar `SELECT`, `WHERE`, e `UPDATE`
- Organizar melhor seu projeto com `connection.py`
- Trabalhar com listas e dicionários para exibir os dados

Se quiser, posso continuar com `INSERT`, `DELETE`, filtros com `LIKE`, integração com Flask ou até transformando isso em uma API. Deseja continuar?
