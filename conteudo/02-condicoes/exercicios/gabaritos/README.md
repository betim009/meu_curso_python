# Gabaritos - Condições

Compare sua solução com calma.

O objetivo é entender como cada regra de negócio vira uma condição em Python.

---

## 1. Verificar idade mínima

```python
idade_cliente = 20

if idade_cliente >= 18:
    print("Cadastro permitido.")
```

Explicação:

- `>=` verifica se a idade é maior ou igual a 18.
- Como a condição é verdadeira, a mensagem aparece.

---

## 2. Cliente ativo

```python
cliente_ativo = True

if cliente_ativo:
    print("Cliente pode comprar.")
else:
    print("Cliente bloqueado.")
```

Explicação:

- Como `cliente_ativo` já é booleano, não precisamos escrever `cliente_ativo == True`.

---

## 3. Validar valor de pagamento

```python
valor_pagamento = 150.00

if valor_pagamento > 0:
    print("Pagamento válido.")
else:
    print("Pagamento inválido.")
```

Explicação:

- Pagamentos com valor zero ou negativo não fazem sentido em uma venda.

---

## 4. Comparar senha

```python
senha_digitada = "python123"
senha_cadastrada = "python123"

if senha_digitada == senha_cadastrada:
    print("Senha correta.")
else:
    print("Senha incorreta.")
```

Explicação:

- `==` compara dois valores.
- Se os textos forem iguais, a senha está correta.

---

## 5. Estoque mínimo

```python
quantidade_estoque = 8
estoque_minimo = 10

if quantidade_estoque < estoque_minimo:
    print("Reposição necessária.")
else:
    print("Estoque suficiente.")
```

Explicação:

- A reposição é necessária quando a quantidade atual está abaixo do mínimo.

---

## 6. Login com email e senha

```python
email_digitado = "usuario@empresa.com"
senha_digitada = "python123"

email_cadastrado = "usuario@empresa.com"
senha_cadastrada = "python123"

if email_digitado == email_cadastrado and senha_digitada == senha_cadastrada:
    print("Login aprovado.")
else:
    print("Login recusado.")
```

Explicação:

- Usamos `and` porque as duas condições precisam ser verdadeiras.

---

## 7. Aprovação de cadastro

```python
idade = 25
email_confirmado = True
aceitou_termos = True

if idade >= 18 and email_confirmado and aceitou_termos:
    print("Cadastro aprovado.")
else:
    print("Cadastro recusado.")
```

Explicação:

- O cadastro depende de três regras.
- Se uma delas falhar, o cadastro é recusado.

---

## 8. Classificação de compra

```python
valor_compra = 850.00

if valor_compra >= 1000:
    print("Premium")
elif valor_compra >= 500:
    print("Padrão")
else:
    print("Inicial")
```

Explicação:

- A maior faixa precisa vir primeiro.
- Se `>= 500` viesse antes, compras acima de 1000 seriam classificadas errado.

---

## 9. Desconto em pedido

```python
valor_pedido = 250.00
cliente_premium = True

if valor_pedido >= 300 or cliente_premium:
    print("Desconto aplicado.")
else:
    print("Sem desconto.")
```

Explicação:

- Usamos `or` porque basta uma das regras ser verdadeira.

---

## 10. Validação de salário

```python
salario = 1800.00

if salario <= 0:
    print("Salário inválido.")
elif salario < 1412:
    print("Salário abaixo do mínimo.")
else:
    print("Salário válido.")
```

Explicação:

- Primeiro validamos o caso mais grave: salário zero ou negativo.
- Depois verificamos se está abaixo do mínimo.

---

## 11. Aprovação de crédito simples

```python
idade = 32
renda_mensal = 4200.00
negativado = False

if idade >= 18 and renda_mensal >= 3000 and not negativado:
    print("Crédito aprovado.")
else:
    print("Crédito recusado.")
```

Explicação:

- `not negativado` significa que o cliente não está negativado.
- Todas as regras precisam ser verdadeiras.

---

## 12. Sistema de status de pedido

```python
pagamento_aprovado = True
produto_em_estoque = True
endereco_confirmado = False

if pagamento_aprovado and produto_em_estoque and endereco_confirmado:
    print("Pedido liberado para envio.")
elif not pagamento_aprovado:
    print("Aguardando pagamento.")
elif not produto_em_estoque:
    print("Produto indisponível.")
elif not endereco_confirmado:
    print("Endereço precisa ser confirmado.")
```

Explicação:

- Primeiro testamos o cenário ideal.
- Depois verificamos qual regra está impedindo o envio.

---

## 13. Validação completa de login interno

```python
email_digitado = "usuario@empresa.com"
senha_digitada = "python123"
email_cadastrado = "usuario@empresa.com"
senha_cadastrada = "python123"
usuario_ativo = True
tentativas = 1

if tentativas >= 3:
    print("Usuário bloqueado por tentativas.")
elif not usuario_ativo:
    print("Usuário inativo.")
elif email_digitado == email_cadastrado and senha_digitada == senha_cadastrada:
    print("Acesso liberado.")
else:
    print("Credenciais inválidas.")
```

Explicação:

- A ordem das regras importa.
- Bloqueio por tentativas deve vir antes da validação de senha.
- Usuário inativo também deve ser recusado antes do acesso.
