# Repetições em Python

No módulo anterior, você aprendeu a tomar decisões com `if`, `elif` e `else`.

Agora você vai aprender a repetir ações automaticamente.

Em sistemas reais, repetição aparece o tempo todo:

- processar vários clientes;
- calcular o total de várias vendas;
- validar uma lista de cadastros;
- gerar relatórios;
- automatizar tarefas repetitivas;
- percorrer dados vindos de planilhas, APIs ou bancos de dados.

Sem repetição, você teria que copiar e colar o mesmo código várias vezes. Com loops, o programa faz isso automaticamente.

---

## O que você vai aprender

Neste módulo, você vai aprender:

- O que é repetição no contexto de sistemas.
- Como usar `while`.
- Como usar `for`.
- Como percorrer listas de dados.
- Como usar `range()`.
- Como parar um loop com `break`.
- Como pular uma repetição com `continue`.
- Como combinar loops com condições.
- Como criar um relatório simples de vendas.

---

## 1. O que é repetição?

Repetição é quando o programa executa uma ação várias vezes.

Exemplo real:

```text
Para cada venda da lista:
    somar o valor no total do dia
```

Em Python, usamos principalmente:

- `for`: quando queremos percorrer uma sequência de dados;
- `while`: quando queremos repetir enquanto uma condição for verdadeira.

---

## 2. Loop `while`

`while` significa "enquanto".

Use `while` quando você não sabe exatamente quantas vezes a repetição vai acontecer, mas sabe qual condição mantém o processo rodando.

Exemplo real: sistema de tentativas de login.

```python
tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    print(f"Tentativa {tentativas + 1}")
    tentativas += 1
```

Explicando:

- `tentativas = 0` começa o contador.
- `limite_tentativas = 3` define o máximo.
- `while tentativas < limite_tentativas:` repete enquanto o contador for menor que 3.
- `tentativas += 1` aumenta o contador a cada repetição.

Saída:

```text
Tentativa 1
Tentativa 2
Tentativa 3
```

Sem o aumento do contador, o loop nunca terminaria.

---

## 3. Loop `for`

`for` é usado para percorrer uma sequência de dados.

Em sistemas reais, usamos `for` para percorrer listas de:

- clientes;
- vendas;
- produtos;
- funcionários;
- pedidos;
- registros de planilha.

Exemplo:

```python
clientes = ["Ana Souza", "Carlos Lima", "Juliana Martins"]

for cliente in clientes:
    print(f"Enviando email para {cliente}")
```

Explicando:

- `clientes` é uma lista.
- `for cliente in clientes:` pega um cliente por vez.
- A variável `cliente` muda a cada repetição.

Saída:

```text
Enviando email para Ana Souza
Enviando email para Carlos Lima
Enviando email para Juliana Martins
```

---

## 4. Processando valores com `for`

Um uso muito comum de repetição é somar valores.

Exemplo real: total de vendas do dia.

```python
vendas = [1200.00, 850.50, 399.90, 1500.00]
total = 0

for venda in vendas:
    total += venda

print(f"Total vendido: R$ {total:.2f}")
```

Explicando:

- `vendas` guarda os valores.
- `total = 0` começa o acumulador.
- `for venda in vendas:` percorre cada venda.
- `total += venda` soma cada valor ao total.

Saída:

```text
Total vendido: R$ 3950.40
```

Esse padrão é chamado de acumulador. Ele aparece muito em relatórios.

---

## 5. Usando `range()`

`range()` cria uma sequência de números.

Use `range()` quando precisar repetir algo uma quantidade conhecida de vezes.

Exemplo: gerar números de pedidos.

```python
for numero in range(1, 6):
    print(f"Processando pedido {numero}")
```

Saída:

```text
Processando pedido 1
Processando pedido 2
Processando pedido 3
Processando pedido 4
Processando pedido 5
```

Importante:

```python
range(1, 6)
```

começa em 1 e vai até 5. O último número não entra.

---

## 6. Controle de loops

Às vezes precisamos controlar melhor a repetição.

Para isso, usamos:

- `break`: para parar o loop;
- `continue`: para pular para a próxima repetição.

---

## 7. Usando `break`

`break` interrompe o loop imediatamente.

Exemplo real: parar busca ao encontrar um cliente.

```python
clientes = ["Ana Souza", "Carlos Lima", "Juliana Martins"]
cliente_procurado = "Carlos Lima"

for cliente in clientes:
    if cliente == cliente_procurado:
        print("Cliente encontrado.")
        break
```

Quando o cliente é encontrado, não faz sentido continuar procurando.

---

## 8. Usando `continue`

`continue` pula o restante da repetição atual e vai para a próxima.

Exemplo real: ignorar clientes inativos.

```python
clientes = [
    {"nome": "Ana Souza", "ativo": True},
    {"nome": "Carlos Lima", "ativo": False},
    {"nome": "Juliana Martins", "ativo": True},
]

for cliente in clientes:
    if not cliente["ativo"]:
        continue

    print(f"Enviando cobrança para {cliente['nome']}")
```

Explicando:

- Se o cliente estiver inativo, `continue` pula para o próximo.
- Apenas clientes ativos recebem a cobrança.

---

## 9. Loops com condições

Loops ficam muito mais úteis quando combinados com `if`.

Exemplo real: contar vendas acima de R$ 1000.

```python
vendas = [1200.00, 850.50, 399.90, 1500.00]
vendas_altas = 0

for venda in vendas:
    if venda >= 1000:
        vendas_altas += 1

print(f"Vendas acima de R$ 1000: {vendas_altas}")
```

Explicando:

- O `for` percorre cada venda.
- O `if` verifica se a venda é maior ou igual a 1000.
- O contador aumenta apenas quando a condição é verdadeira.

---

## 10. Percorrendo lista de dicionários

Dados reais muitas vezes vêm como listas de dicionários.

Exemplo:

```python
produtos = [
    {"nome": "Notebook", "preco": 4200.00, "estoque": 5},
    {"nome": "Monitor", "preco": 950.00, "estoque": 0},
    {"nome": "Teclado", "preco": 180.00, "estoque": 12},
]

for produto in produtos:
    if produto["estoque"] == 0:
        print(f"{produto['nome']} está sem estoque.")
```

Esse formato é parecido com dados vindos de APIs e planilhas convertidas para Python.

---

## 11. Erros comuns

### Erro 1: loop infinito

Errado:

```python
contador = 0

while contador < 3:
    print(contador)
```

O contador nunca muda. O loop não termina.

Correto:

```python
contador = 0

while contador < 3:
    print(contador)
    contador += 1
```

---

### Erro 2: usar `range()` achando que inclui o último número

```python
for numero in range(1, 5):
    print(numero)
```

Saída:

```text
1
2
3
4
```

O número 5 não entra.

---

### Erro 3: esquecer o acumulador

Errado:

```python
vendas = [100, 200, 300]

for venda in vendas:
    total += venda
```

Correto:

```python
vendas = [100, 200, 300]
total = 0

for venda in vendas:
    total += venda
```

Antes de somar, o total precisa existir.

---

### Erro 4: alterar a lógica do contador no lugar errado

Em um `while`, o contador precisa mudar dentro do loop.

```python
tentativas = 0

while tentativas < 3:
    print("Tentando login")
    tentativas += 1
```

---

## 12. Mini desafios

Tente resolver antes dos exercícios:

1. Percorra uma lista de clientes e mostre o nome de cada um.
2. Some uma lista de valores de vendas.
3. Conte quantas vendas foram maiores que R$ 500.
4. Percorra uma lista de produtos e mostre os que estão sem estoque.
5. Use `while` para simular três tentativas de login.

---

## 13. Resumo

Neste módulo, você aprendeu que:

- Loops automatizam tarefas repetitivas.
- `while` repete enquanto uma condição for verdadeira.
- `for` percorre listas e sequências.
- `range()` ajuda a repetir por quantidade.
- `break` interrompe o loop.
- `continue` pula uma repetição.
- Loops com `if` permitem criar regras reais.
- Acumuladores e contadores são essenciais para relatórios.
