
# 🍉 Funções e Estruturas de Menu em Python

## 📚 Introdução

Funções são blocos de código que executam uma tarefa específica e podem ser chamadas várias vezes.  
Elas ajudam a organizar melhor o programa, evitando repetições.

Também vamos aprender a criar **menus interativos** usando `while` e `input()`.

---

## 🔹 Criando uma função simples para calcular média

Uma função pode receber **parâmetros** e retornar um **resultado**.

```python
# Define a função chamada 'media' que recebe dois valores
def media(nota1, nota2):
    return (nota1 + nota2) / 2

# Exemplo de uso
print(media(9.4, 5))
```

➡️ A função `media()` calcula a média entre duas notas fornecidas.

---

## 🔹 Melhorando a leitura com variáveis

Para deixar o código mais **organizado e compreensível**, podemos **armazenar o resultado** da função em uma variável:

```python
# Calcula a média e armazena em uma variável
media_alberto = media(9.4, 5)

# Exibe o resultado com uma mensagem
print(f"A média de notas do Alberto é: {media_alberto}")
```

---

## 🔹 Trabalhando com listas de dicionários

Uma lista pode armazenar **vários dicionários**, cada um contendo informações sobre frutas e seus preços.

```python
frutas_precos = [
    {"fruta": "Morango", "preco": 2.19},
    {"fruta": "Laranja", "preco": 3.0},
    {"fruta": "Melancia", "preco": 1.77},
    {"fruta": "Manga", "preco": 3.5},
    {"fruta": "Goiaba", "preco": 2.09},
]
```

---

## 🔹 Funções para manipular a lista de frutas

### Adicionar uma nova fruta:

```python
def adicionar(fruta, preco):
    frutas_precos.append({"fruta": fruta, "preco": preco})
```

➡️ Essa função adiciona um novo dicionário contendo a fruta e seu preço à lista.

---

### Listar todas as frutas:

```python
def listar():
    for item in frutas_precos:
        print(item["fruta"], item["preco"])
```

➡️ Esta função percorre toda a lista e exibe as frutas e seus preços.

---

## 🔹 Criando um menu interativo

Podemos criar um menu para o usuário escolher o que deseja fazer:

```python
def main():
    while True:
        print("[1] - Para adicionar uma nova fruta")
        print("[2] - Para listar todas as frutas")
        print("[0] - Para encerrar \n")
        
        entrada = input("Sua opção: ")

        if entrada == "0":
            break  # Encerra o programa

        if entrada == "1":
            entrada_fruta = input("Nome da fruta: ")
            entrada_preco = input("Preço da fruta: ")
            adicionar(entrada_fruta, entrada_preco)

        if entrada == "2":
            listar()
```

---

## 🧠 Funcionamento do menu

- O programa fica rodando (`while True`) até o usuário digitar `0`.
- `1` permite adicionar uma nova fruta.
- `2` permite listar as frutas.
- Sempre que uma ação termina, o menu é exibido novamente.

---

## ✅ Conclusão

Você aprendeu:

- Como **criar funções** simples e funções que manipulam listas.
- Como **chamar funções** dentro de outras funções.
- Como criar um **menu de opções** interativo.
- Como trabalhar com **listas de dicionários** para organizar dados de forma eficiente.

Esses conceitos são essenciais para criar programas mais organizados e dinâmicos em Python!
