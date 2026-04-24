# Tipos de Dados em Python

Este é o primeiro módulo do curso.

Antes de aprender estruturas como condições, repetições, funções e bancos de dados, você precisa entender uma ideia fundamental: todo sistema trabalha com dados.

Um sistema de cadastro guarda nome, email, idade e status do cliente. Uma planilha de vendas guarda produto, quantidade, preço e faturamento. Uma API pode devolver dados de clientes, pedidos ou pagamentos em formato de texto. Python precisa saber que tipo de dado está sendo usado para conseguir calcular, comparar, salvar e exibir informações corretamente.

---

## O que você vai aprender

Neste módulo, você vai aprender:

- O que são dados em sistemas reais.
- O que é uma variável.
- Como usar os tipos `str`, `int`, `float` e `bool`.
- Como descobrir o tipo de um valor com `type()`.
- Como converter dados vindos como texto.
- Como fazer operações simples com dados reais.
- Quais erros são comuns no começo.
- Como criar um mini cadastro de funcionário.

---

## 1. O que são dados?

Dados são informações que um programa recebe, guarda, processa ou exibe.

Exemplos reais:

| Situação | Dados envolvidos |
|---|---|
| Cadastro de cliente | nome, email, telefone, idade |
| Sistema de vendas | produto, quantidade, preço, total |
| RH de uma empresa | funcionário, cargo, salário, ativo |
| Planilha financeira | data, descrição, valor, categoria |
| API de pagamentos | id do pedido, status, valor, aprovado |

Em Python, cada dado tem um tipo. O tipo define o que podemos fazer com aquele valor.

---

## 2. Variáveis

Uma variável é um nome que guarda um valor.

Pense em uma variável como uma etiqueta em uma informação.

```python
nome_funcionario = "Mariana Costa"
idade_funcionario = 29
salario_funcionario = 4200.50
funcionario_ativo = True
```

Explicando linha por linha:

- `nome_funcionario` guarda um texto.
- `idade_funcionario` guarda um número inteiro.
- `salario_funcionario` guarda um número decimal.
- `funcionario_ativo` guarda uma resposta lógica: verdadeiro ou falso.

Usamos nomes claros porque sistemas reais precisam ser lidos por outras pessoas. Um nome como `x` não explica nada. Um nome como `salario_funcionario` explica a intenção do dado.

---

## 3. Principais tipos de dados

Neste primeiro módulo, vamos focar nos quatro tipos mais usados no começo:

| Tipo | Nome em Python | Exemplo real |
|---|---|---|
| Texto | `str` | nome, email, cargo |
| Inteiro | `int` | idade, quantidade, código |
| Decimal | `float` | salário, preço, faturamento |
| Lógico | `bool` | ativo, aprovado, pago |

---

## 4. Texto: `str`

`str` é o tipo usado para representar texto.

Use `str` para dados como:

- nome de cliente;
- email;
- cargo;
- cidade;
- código que não será usado em cálculo, como CPF ou CEP.

Exemplo:

```python
nome_cliente = "Ana Souza"
email_cliente = "ana.souza@email.com"
cargo = "Analista de Dados"

print(nome_cliente)
print(email_cliente)
print(cargo)
```

Explicando:

- `"Ana Souza"` é um texto, por isso fica entre aspas.
- `email_cliente` também é texto, mesmo tendo ponto e arroba.
- `print()` mostra o valor no terminal.

### Juntando textos

Em sistemas reais, muitas vezes precisamos montar mensagens.

```python
nome = "Ana"
sobrenome = "Souza"
nome_completo = nome + " " + sobrenome

print(nome_completo)
```

Saída:

```text
Ana Souza
```

Também podemos usar f-string, que é mais comum em código profissional:

```python
nome = "Ana Souza"
cargo = "Analista de Dados"

mensagem = f"{nome} trabalha como {cargo}."
print(mensagem)
```

Saída:

```text
Ana Souza trabalha como Analista de Dados.
```

---

## 5. Inteiro: `int`

`int` é o tipo usado para números inteiros, sem casas decimais.

Use `int` para:

- idade;
- quantidade de produtos;
- número de parcelas;
- código interno;
- total de acessos.

Exemplo:

```python
idade_cliente = 34
quantidade_produtos = 5
numero_parcelas = 3

print(idade_cliente)
print(quantidade_produtos)
print(numero_parcelas)
```

Explicando:

- `34`, `5` e `3` são números inteiros.
- Eles não usam aspas.
- Como são números, podem participar de cálculos.

Exemplo com cálculo:

```python
quantidade = 8
estoque_minimo = 10

precisa_repor = quantidade < estoque_minimo

print(precisa_repor)
```

Saída:

```text
True
```

O resultado é `True` porque 8 é menor que 10.

---

## 6. Decimal: `float`

`float` é o tipo usado para números com casas decimais.

Use `float` para:

- salário;
- preço;
- faturamento;
- comissão;
- nota;
- percentual.

Exemplo:

```python
preco_unitario = 129.90
quantidade_vendida = 4
total_venda = preco_unitario * quantidade_vendida

print(total_venda)
```

Explicando:

- `preco_unitario` é `float`.
- `quantidade_vendida` é `int`.
- `total_venda` recebe o resultado da multiplicação.

Saída:

```text
519.6
```

Para exibir valores financeiros de forma mais adequada, use f-string com duas casas decimais:

```python
print(f"Total da venda: R$ {total_venda:.2f}")
```

Saída:

```text
Total da venda: R$ 519.60
```

---

## 7. Lógico: `bool`

`bool` representa verdadeiro ou falso.

Os únicos valores booleanos são:

```python
True
False
```

Use `bool` para dados como:

- cliente ativo;
- pagamento aprovado;
- produto disponível;
- funcionário em contrato ativo;
- pedido entregue.

Exemplo:

```python
cliente_ativo = True
pagamento_aprovado = False

print(cliente_ativo)
print(pagamento_aprovado)
```

Comparações também geram valores booleanos:

```python
idade_cliente = 22
maior_de_idade = idade_cliente >= 18

print(maior_de_idade)
```

Saída:

```text
True
```

---

## 8. Descobrindo o tipo com `type()`

Quando você não sabe o tipo de um valor, use `type()`.

```python
nome = "Carlos Lima"
idade = 41
salario = 6300.75
ativo = True

print(type(nome))
print(type(idade))
print(type(salario))
print(type(ativo))
```

Saída:

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

Isso é útil quando dados vêm de formulários, planilhas ou APIs.

---

## 9. Dados vindos como texto

No mundo real, muitos dados chegam como texto.

Exemplos:

- Dados digitados pelo usuário com `input()`.
- Dados lidos de CSV.
- Dados recebidos de APIs.
- Campos importados de planilhas.

Veja este exemplo:

```python
idade = input("Digite a idade do cliente: ")
print(type(idade))
```

Mesmo que o usuário digite `30`, o Python recebe `"30"` como texto.

Por isso, se quisermos calcular, precisamos converter.

---

## 10. Conversão de tipos

Converter tipo significa transformar um valor de um tipo para outro.

Funções comuns:

| Função | O que faz |
|---|---|
| `str()` | converte para texto |
| `int()` | converte para inteiro |
| `float()` | converte para decimal |
| `bool()` | converte para booleano |

Exemplo real com formulário:

```python
idade_texto = "32"
salario_texto = "4500.75"

idade = int(idade_texto)
salario = float(salario_texto)

print(idade + 1)
print(f"Salário: R$ {salario:.2f}")
```

Explicando:

- `"32"` é texto.
- `int("32")` transforma em número inteiro.
- `"4500.75"` é texto.
- `float("4500.75")` transforma em número decimal.

---

## 11. Operações reais com dados

### Cálculo de faturamento

```python
preco_produto = 89.90
quantidade_vendida = 12
faturamento = preco_produto * quantidade_vendida

print(f"Faturamento: R$ {faturamento:.2f}")
```

### Cálculo de salário com bônus

```python
salario_base = 3000.00
bonus = 750.00
salario_final = salario_base + bonus

print(f"Salário final: R$ {salario_final:.2f}")
```

### Validação de idade

```python
idade_cliente = 17
pode_comprar = idade_cliente >= 18

print(pode_comprar)
```

### Verificação de status

```python
cliente_ativo = True

print(cliente_ativo == True)
```

Em código profissional, é comum simplificar:

```python
print(cliente_ativo)
```

---

## 12. Erros comuns

### Erro 1: somar texto com número

Errado:

```python
idade = "30"
proxima_idade = idade + 1
```

Isso gera erro porque `"30"` é texto e `1` é número.

Correto:

```python
idade = "30"
proxima_idade = int(idade) + 1

print(proxima_idade)
```

### Erro 2: usar vírgula em número decimal

Errado:

```python
preco = float("129,90")
```

Python espera ponto decimal, não vírgula.

Correto:

```python
preco_texto = "129,90"
preco = float(preco_texto.replace(",", "."))

print(preco)
```

### Erro 3: transformar texto inválido em número

Errado:

```python
salario = float("quatro mil")
```

Esse texto não representa um número.

Correto:

```python
salario = float("4000")
print(salario)
```

### Erro 4: escrever `true` em vez de `True`

Errado:

```python
ativo = true
```

Correto:

```python
ativo = True
```

Python diferencia letras maiúsculas e minúsculas.

---

## 13. Mini desafios

Antes dos exercícios completos, tente resolver estes desafios:

1. Crie variáveis para nome, cargo, salário e status ativo de um funcionário.
2. Calcule o total de uma venda usando preço e quantidade.
3. Receba uma idade como texto e converta para `int`.
4. Receba um preço como texto e converta para `float`.
5. Monte uma mensagem usando f-string com nome do cliente e valor de compra.

---

## 14. Resumo

Neste módulo, você aprendeu que:

- Dados são a base de qualquer sistema.
- Variáveis guardam valores.
- `str` representa texto.
- `int` representa números inteiros.
- `float` representa números decimais.
- `bool` representa verdadeiro ou falso.
- `type()` mostra o tipo de um valor.
- Dados de formulário, CSV e API muitas vezes chegam como texto.
- Conversão de tipos é essencial para cálculos.
- Entender tipos evita muitos erros no começo da programação.

Agora você já tem base para criar programas simples que recebem, tratam e exibem dados reais.
