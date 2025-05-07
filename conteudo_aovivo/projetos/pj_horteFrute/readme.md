# 🍍 Projeto de Cadastro e Controle de Vendas de Frutas

## 🧠 Visão Geral

Este projeto simula um sistema de controle de **estoque** e **vendas** de frutas, legumes e verduras diretamente no terminal.

---

## 📋 Etapas do Projeto

### 1. Base de Dados dos Produtos

Você precisará de uma lista com informações sobre cada item vendido:

- Nome do produto  
- Preço de venda  
- Unidade de medida (kg, unidade, dúzia...)  
- Categoria (fruta, legume, verdura)

Exemplo:

```python
produto = {
    "nome": "Banana",
    "preco": 2.50,
    "unidade": "kg",
    "categoria": "fruta"
}
```

---

### 2. Base de Dados das Vendas

Aqui vamos registrar cada venda realizada:

- Cliente que comprou  
- Data da venda  
- Produtos vendidos  
- Quantidade  
- Valor total

---

### 3. Base de Dados das Entradas

Este banco serve para registrar o que foi comprado para abastecer o estoque:

- Produto comprado  
- Quantidade  
- Data de entrada  
- Preço de custo  

---

## ⚠️ Dica Importante

> **"Planeje antes de programar!"**

Assim como um pedreiro não constrói sem saber o tamanho do cômodo, o programador deve pensar antes de começar para evitar retrabalho.

---

## 🧑‍💻 Interface no Terminal

Vamos criar um **menu interativo no terminal**, com as seguintes opções:

- [x] Cadastrar entrada no estoque  
- [x] Cadastrar venda  
- [x] Consultar venda  
- [x] Consultar saldo de produtos  
- [x] Encerrar o programa  

---

## 💡 Exemplo de Interface (simulação inicial)

A ideia é simples: perguntar ao usuário o que ele deseja e responder com base na opção escolhida.

```python
# Loop principal do sistema
while True:
    print("###### Bem vindo ao programa #######\n")
    
    print("Digite 0 para encerrar.")
    print("Digite 1 para consultar uma venda.")
    resposta = input("- : ")

    if resposta == "1":
        print("Qual produto você deseja consultar?")
        # Aqui você vai implementar a lógica de busca no histórico de vendas
    
    if resposta == "0":
        print("Programa encerrado.")
        break
```

---

## 🔍 O que será implementado depois?

1. Lógica para consultar vendas específicas.  
2. Cadastro de novas vendas com data e valor.  
3. Registro de entrada de produtos no estoque.  
4. Exibir o saldo atual de cada produto (quantidade disponível).

---

## 📦 Exemplo de Cadastro Futuro (entrada de produtos)

```python
entrada = {
    "produto": "Maçã",
    "quantidade": 10,
    "preco_custo": 1.90,
    "data": "2025-05-01"
}
```

---

# 🛠️ Continuação do Projeto: Interface de Estoque e Vendas

## 🧰 Estrutura Inicial de Dados

Antes da lógica funcionar, precisamos de onde **guardar os dados**.

```python
# Lista de vendas realizadas
vendas = [
    {
        "produto": "Maçã",
        "quantidade": 5,
        "preco_custo": 2.90,
        "data": "2025-05-03"
    },
    {
        "produto": "Melancia",
        "quantidade": 1,
        "preco_custo": 3.90,
        "data": "2025-05-04"
    },
    {
        "produto": "Banana",
        "quantidade": 10,
        "preco_custo": 1.50,
        "data": "2025-05-05"
    },
    {
        "produto": "Alface",
        "quantidade": 5,
        "preco_custo": 1.10,
        "data": "2025-05-06"
    },
    {
        "produto": "Tomate",
        "quantidade": 6,
        "preco_custo": 2.80,
        "data": "2025-05-06"
    },
    {
        "produto": "Cenoura",
        "quantidade": 4,
        "preco_custo": 1.40,
        "data": "2025-05-07"
    },
    {
        "produto": "Laranja",
        "quantidade": 12,
        "preco_custo": 2.00,
        "data": "2025-05-07"
    },
    {
        "produto": "Batata",
        "quantidade": 8,
        "preco_custo": 1.80,
        "data": "2025-05-08"
    },
    {
        "produto": "Cebola",
        "quantidade": 6,
        "preco_custo": 1.50,
        "data": "2025-05-08"
    },
    {
        "produto": "Uva",
        "quantidade": 4,
        "preco_custo": 4.00,
        "data": "2025-05-09"
    }
]


# Lista de entradas no estoque
entradas = [
    {
        "produto": "Maçã",
        "quantidade": 10,
        "preco_custo": 1.90,
        "data": "2025-05-01"
    },
    {
        "produto": "Melancia",
        "quantidade": 10,
        "preco_custo": 2.90,
        "data": "2025-05-01"
    },
    {
        "produto": "Banana",
        "quantidade": 25,
        "preco_custo": 1.20,
        "data": "2025-05-02"
    },
    {
        "produto": "Alface",
        "quantidade": 15,
        "preco_custo": 0.80,
        "data": "2025-05-03"
    },
    {
        "produto": "Cenoura",
        "quantidade": 20,
        "preco_custo": 1.00,
        "data": "2025-05-03"
    },
    {
        "produto": "Laranja",
        "quantidade": 30,
        "preco_custo": 1.50,
        "data": "2025-05-04"
    },
    {
        "produto": "Tomate",
        "quantidade": 18,
        "preco_custo": 2.30,
        "data": "2025-05-04"
    },
    {
        "produto": "Batata",
        "quantidade": 22,
        "preco_custo": 1.40,
        "data": "2025-05-05"
    },
    {
        "produto": "Cebola",
        "quantidade": 16,
        "preco_custo": 1.10,
        "data": "2025-05-05"
    },
    {
        "produto": "Uva",
        "quantidade": 12,
        "preco_custo": 3.20,
        "data": "2025-05-06"
    }
]

# Dicionário para controlar o saldo atual do produto
estoque = {}
```

---

## 🧑‍💻 Interface com todas as opções

Aqui está o menu completo com as funcionalidades:

```python
while True:
    print("\n###### Bem vindo ao sistema #######")
    print("Digite 0 para ENCERRAR o sistema")
    print("Digite 1 para CONSULTAR uma venda")
    print("Digite 2 para CADASTRAR uma venda")
    print("Digite 3 para CONSULTAR saldo de um produto")
    print("Digite 4 para CADASTRAR entrada no estoque")

    opcao = input("Opção escolhida: ")

    if opcao == "0":
        print("Programa encerrado.")
        break

    elif opcao == "1":
        nome = input("Nome do produto vendido: ")
        for venda in vendas:
            if venda["produto"] == nome:
                print(venda)

    elif opcao == "2":
        produto = input("Qual produto foi vendido? ")
        qtd = int(input("Quantas unidades foram vendidas? "))
        preco = float(input("Qual o preço da unidade? "))
        total = qtd * preco
        data = input("Qual a data da venda? ")

        venda = {
            "produto": produto,
            "quantidade": qtd,
            "preco_unitario": preco,
            "total": total,
            "data": data
        }

        vendas.append(venda)

        # Atualizar o estoque
        if produto in estoque:
            estoque[produto] -= qtd
        else:
            estoque[produto] = -qtd

        print("Venda cadastrada com sucesso!")

    elif opcao == "3":
        nome = input("Digite o nome do produto: ")
        saldo = estoque.get(nome, 0)
        print(f"Saldo disponível de {nome}: {saldo}")

    elif opcao == "4":
        produto = input("Qual produto está entrando no estoque? ")
        qtd = int(input("Quantas unidades entraram? "))
        custo = float(input("Qual o preço de custo por unidade? "))
        data = input("Qual a data da entrada? ")

        entrada = {
            "produto": produto,
            "quantidade": qtd,
            "preco_custo": custo,
            "data": data
        }

        entradas.append(entrada)

        # Atualizar o saldo do estoque
        if produto in estoque:
            estoque[produto] += qtd
        else:
            estoque[produto] = qtd

        print("Entrada registrada com sucesso!")
```

---

## 📝 Conclusão

Com esse sistema, conseguimos simular um controle básico de vendas e estoque com:

- Registro de vendas realizadas
- Atualização automática de saldo
- Consulta de dados salvos
- Entrada de produtos para reabastecimento

Esse é o **primeiro passo** para evoluir para algo mais robusto no futuro (como um app com interface gráfica ou web).

---

