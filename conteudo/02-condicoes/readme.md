# Condições em Python

No módulo anterior, você aprendeu a guardar dados em variáveis e a trabalhar com tipos como texto, número e booleano.

Agora você vai aprender a fazer o programa tomar decisões.

Em sistemas reais, quase tudo depende de decisões:

- um usuário pode entrar no sistema ou não;
- um cadastro pode ser aprovado ou recusado;
- um cliente pode comprar ou ser bloqueado;
- um pagamento pode estar aprovado ou pendente;
- um pedido pode receber desconto ou não.

Essas decisões são feitas com condições.

---

## O que você vai aprender

Neste módulo, você vai aprender:

- O que são decisões em sistemas.
- Como usar `if`.
- Como usar `if` e `else`.
- Como usar `if`, `elif` e `else`.
- Como usar operadores de comparação.
- Como combinar regras com `and`, `or` e `not`.
- Como evitar erros comuns de lógica.
- Como criar um sistema simples de validação de usuário.

---

## 1. O que são decisões em sistemas?

Uma decisão acontece quando o programa precisa escolher um caminho.

Exemplo real:

```text
Se o usuário está ativo, permitir acesso.
Caso contrário, bloquear acesso.
```

Em Python, escrevemos essa regra usando `if`.

---

## 2. Estrutura `if`

`if` significa "se".

Use `if` quando quiser executar um bloco de código apenas se uma condição for verdadeira.

Exemplo:

```python
idade_cliente = 22

if idade_cliente >= 18:
    print("Cliente maior de idade.")
```

Explicando linha por linha:

- `idade_cliente = 22` guarda a idade.
- `if idade_cliente >= 18:` verifica se a idade é maior ou igual a 18.
- Se a condição for verdadeira, o `print()` é executado.
- A linha dentro do `if` precisa estar indentada, ou seja, com espaços antes.

Saída:

```text
Cliente maior de idade.
```

Se a idade fosse `16`, nada seria exibido, porque a condição seria falsa.

---

## 3. `if` e `else`

`else` significa "caso contrário".

Use `else` quando quiser executar uma ação alternativa se a condição do `if` for falsa.

Exemplo real: verificar se um usuário pode acessar um sistema.

```python
usuario_ativo = False

if usuario_ativo:
    print("Acesso liberado.")
else:
    print("Acesso bloqueado. Usuário inativo.")
```

Explicando:

- `usuario_ativo` é um valor booleano.
- Se for `True`, o acesso é liberado.
- Se for `False`, cai no `else`.

Saída:

```text
Acesso bloqueado. Usuário inativo.
```

---

## 4. `if`, `elif` e `else`

`elif` significa "senão se".

Use `elif` quando existem várias possibilidades.

Exemplo real: classificar cliente pelo valor de compra.

```python
valor_compra = 850.00

if valor_compra >= 1000:
    print("Cliente categoria Premium.")
elif valor_compra >= 500:
    print("Cliente categoria Padrão.")
else:
    print("Cliente categoria Inicial.")
```

Explicando:

- Primeiro o Python testa se a compra é maior ou igual a 1000.
- Se não for, testa se é maior ou igual a 500.
- Se nenhuma condição for verdadeira, executa o `else`.

Saída:

```text
Cliente categoria Padrão.
```

Importante: o Python executa apenas o primeiro bloco verdadeiro.

---

## 5. Operadores de comparação

Operadores de comparação servem para comparar valores.

| Operador | Significado | Exemplo real |
|---|---|---|
| `==` | igual a | senha digitada é igual à senha cadastrada |
| `!=` | diferente de | status é diferente de bloqueado |
| `>` | maior que | valor da compra é maior que limite |
| `<` | menor que | estoque é menor que mínimo |
| `>=` | maior ou igual a | idade é maior ou igual a 18 |
| `<=` | menor ou igual a | parcelas são menores ou iguais a 12 |

Exemplo:

```python
senha_digitada = "python123"
senha_cadastrada = "python123"

if senha_digitada == senha_cadastrada:
    print("Senha correta.")
```

Use `==` para comparar.  
Use `=` para guardar valor em variável.

---

## 6. Operadores lógicos

Operadores lógicos permitem combinar condições.

| Operador | Quando usar |
|---|---|
| `and` | quando todas as condições precisam ser verdadeiras |
| `or` | quando pelo menos uma condição precisa ser verdadeira |
| `not` | quando queremos inverter uma condição |

### Usando `and`

Exemplo: usuário só pode acessar se estiver ativo e a senha estiver correta.

```python
usuario_ativo = True
senha_correta = True

if usuario_ativo and senha_correta:
    print("Acesso liberado.")
else:
    print("Acesso negado.")
```

### Usando `or`

Exemplo: cliente recebe atendimento prioritário se for premium ou tiver chamado crítico.

```python
cliente_premium = False
chamado_critico = True

if cliente_premium or chamado_critico:
    print("Atendimento prioritário.")
else:
    print("Atendimento normal.")
```

### Usando `not`

Exemplo: bloquear se o usuário não estiver ativo.

```python
usuario_ativo = False

if not usuario_ativo:
    print("Usuário inativo. Acesso bloqueado.")
```

---

## 7. Comparações reais

### Validar senha

```python
senha_digitada = "admin123"
senha_cadastrada = "admin123"

if senha_digitada == senha_cadastrada:
    print("Login aprovado.")
else:
    print("Senha inválida.")
```

### Validar idade mínima

```python
idade = 17

if idade >= 18:
    print("Cadastro aprovado.")
else:
    print("Cadastro recusado. Idade mínima não atingida.")
```

### Validar valor financeiro

```python
valor_pagamento = 0

if valor_pagamento > 0:
    print("Pagamento válido.")
else:
    print("Pagamento inválido.")
```

### Aprovar crédito simples

```python
renda_mensal = 4200.00
nome_limpo = True

if renda_mensal >= 3000 and nome_limpo:
    print("Crédito pré-aprovado.")
else:
    print("Crédito não aprovado.")
```

---

## 8. Erros comuns

### Erro 1: confundir `=` com `==`

Errado:

```python
if senha = "admin123":
    print("Acesso liberado.")
```

Correto:

```python
if senha == "admin123":
    print("Acesso liberado.")
```

Use `=` para atribuir valor.  
Use `==` para comparar valor.

---

### Erro 2: esquecer os dois pontos

Errado:

```python
if idade >= 18
    print("Maior de idade")
```

Correto:

```python
if idade >= 18:
    print("Maior de idade")
```

---

### Erro 3: esquecer a indentação

Errado:

```python
if usuario_ativo:
print("Acesso liberado")
```

Correto:

```python
if usuario_ativo:
    print("Acesso liberado")
```

Indentação é parte da sintaxe do Python.

---

### Erro 4: criar condições redundantes

Evite:

```python
if cliente_ativo == True:
    print("Cliente ativo")
```

Prefira:

```python
if cliente_ativo:
    print("Cliente ativo")
```

---

### Erro 5: ordenar mal as condições

Errado:

```python
valor_compra = 1500

if valor_compra >= 500:
    print("Padrão")
elif valor_compra >= 1000:
    print("Premium")
```

O cliente nunca chegará na categoria Premium, porque `1500 >= 500` já é verdadeiro.

Correto:

```python
if valor_compra >= 1000:
    print("Premium")
elif valor_compra >= 500:
    print("Padrão")
```

---

## 9. Mini desafios

Tente resolver antes de ir para os exercícios completos.

1. Crie uma regra que aprove cadastro apenas se a idade for maior ou igual a 18.
2. Crie uma regra que bloqueie acesso se o usuário estiver inativo.
3. Crie uma regra que aprove pagamento apenas se o valor for maior que zero.
4. Crie uma regra que valide login comparando email e senha.
5. Crie uma regra que classifique uma compra como pequena, média ou grande.

---

## 10. Resumo

Neste módulo, você aprendeu que:

- Condições permitem que o programa tome decisões.
- `if` executa um bloco se a condição for verdadeira.
- `else` executa um caminho alternativo.
- `elif` permite testar várias possibilidades.
- `==`, `!=`, `>`, `<`, `>=` e `<=` comparam valores.
- `and`, `or` e `not` combinam regras.
- Regras de negócio reais usam condicionais o tempo todo.
- Indentação, dois pontos e ordem das condições são essenciais em Python.
