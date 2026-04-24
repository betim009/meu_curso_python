# Exercícios - Condições

Resolva os exercícios em ordem.

Eles simulam regras comuns em sistemas reais: cadastro, login, pagamento, crédito, pedidos e validação de dados.

Faça primeiro sem olhar o gabarito. Depois compare com [`gabaritos/README.md`](gabaritos/README.md).

---

## Exercícios fáceis

### 1. Verificar idade mínima

Crie uma variável `idade_cliente`.

Se a idade for maior ou igual a 18, mostre:

```text
Cadastro permitido.
```

---

### 2. Cliente ativo

Crie uma variável `cliente_ativo` com valor booleano.

Se o cliente estiver ativo, mostre:

```text
Cliente pode comprar.
```

Caso contrário, mostre:

```text
Cliente bloqueado.
```

---

### 3. Validar valor de pagamento

Crie uma variável `valor_pagamento`.

Se o valor for maior que zero, mostre:

```text
Pagamento válido.
```

Caso contrário, mostre:

```text
Pagamento inválido.
```

---

### 4. Comparar senha

Crie duas variáveis:

- `senha_digitada`
- `senha_cadastrada`

Se forem iguais, mostre:

```text
Senha correta.
```

Caso contrário:

```text
Senha incorreta.
```

---

### 5. Estoque mínimo

Crie duas variáveis:

- `quantidade_estoque`
- `estoque_minimo`

Se a quantidade em estoque for menor que o estoque mínimo, mostre:

```text
Reposição necessária.
```

Caso contrário:

```text
Estoque suficiente.
```

---

## Exercícios médios

### 6. Login com email e senha

Crie variáveis para:

- email digitado;
- senha digitada;
- email cadastrado;
- senha cadastrada.

O login só deve ser aprovado se email e senha estiverem corretos.

---

### 7. Aprovação de cadastro

Um cadastro só pode ser aprovado se:

- idade for maior ou igual a 18;
- email foi confirmado;
- usuário aceitou os termos.

Crie as variáveis e mostre se o cadastro foi aprovado ou recusado.

---

### 8. Classificação de compra

Crie uma variável `valor_compra`.

Classifique:

- `Premium` para compras a partir de `1000`;
- `Padrão` para compras a partir de `500`;
- `Inicial` para compras abaixo de `500`.

---

### 9. Desconto em pedido

Um pedido recebe desconto se:

- valor for maior ou igual a `300`; ou
- cliente for premium.

Crie as variáveis e mostre se o desconto foi aplicado.

---

### 10. Validação de salário

Crie uma variável `salario`.

Se o salário for menor ou igual a zero, mostre:

```text
Salário inválido.
```

Se for menor que `1412`, mostre:

```text
Salário abaixo do mínimo.
```

Caso contrário:

```text
Salário válido.
```

---

## Exercícios desafiadores

### 11. Aprovação de crédito simples

Um cliente só tem crédito aprovado se:

- for maior de idade;
- tiver renda mensal maior ou igual a `3000`;
- não estiver negativado.

Crie as variáveis e mostre uma mensagem de aprovação ou recusa.

---

### 12. Sistema de status de pedido

Crie variáveis:

- `pagamento_aprovado`;
- `produto_em_estoque`;
- `endereco_confirmado`.

Regras:

- Se tudo estiver verdadeiro, mostre `Pedido liberado para envio`.
- Se pagamento não estiver aprovado, mostre `Aguardando pagamento`.
- Se produto não estiver em estoque, mostre `Produto indisponível`.
- Se endereço não estiver confirmado, mostre `Endereço precisa ser confirmado`.

---

### 13. Validação completa de login interno

Crie variáveis:

- `email_digitado`;
- `senha_digitada`;
- `email_cadastrado`;
- `senha_cadastrada`;
- `usuario_ativo`;
- `tentativas`.

Regras:

- Se tentativas for maior ou igual a 3, mostre `Usuário bloqueado por tentativas`.
- Se o usuário estiver inativo, mostre `Usuário inativo`.
- Se email e senha estiverem corretos, mostre `Acesso liberado`.
- Caso contrário, mostre `Credenciais inválidas`.
