# Exercícios - Tipos de Dados

Resolva os exercícios em ordem.

As atividades usam situações comuns em sistemas de empresas, planilhas, cadastros e relatórios.

Faça primeiro sem olhar o gabarito. Depois compare com as soluções em [`gabaritos/README.md`](gabaritos/README.md).

---

## Exercícios fáceis

### 1. Cadastro básico de cliente

Crie variáveis para guardar:

- nome do cliente;
- email;
- idade;
- cidade.

Depois, mostre cada informação no terminal.

---

### 2. Tipos de um funcionário

Crie variáveis para:

- nome do funcionário;
- idade;
- salário;
- funcionário ativo.

Mostre o tipo de cada variável usando `type()`.

---

### 3. Total de venda

Uma empresa vendeu 4 licenças de software.

Cada licença custa `350.00`.

Crie variáveis para preço, quantidade e total. Depois mostre:

```text
Total da venda: R$ 1400.00
```

---

### 4. Nome completo

Crie duas variáveis:

- `nome`
- `sobrenome`

Monte uma terceira variável chamada `nome_completo`.

Mostre o nome completo no terminal.

---

### 5. Cliente ativo

Crie uma variável chamada `cliente_ativo` com valor `True`.

Mostre no terminal uma frase usando f-string:

```text
Cliente ativo: True
```

---

## Exercícios médios

### 6. Conversão de idade do formulário

Um formulário enviou a idade do cliente como texto:

```python
idade_texto = "28"
```

Converta esse valor para inteiro e mostre a idade que o cliente terá no próximo ano.

---

### 7. Conversão de preço vindo de planilha

Uma planilha enviou o preço como texto:

```python
preco_texto = "129.90"
```

Converta para `float`, calcule o valor de 5 unidades e mostre o total formatado em reais.

---

### 8. Salário com bônus

Um funcionário tem salário base de `3200.00` e recebeu bônus de `850.00`.

Calcule e mostre o salário final.

---

### 9. Validação de idade

Crie uma variável `idade_cliente`.

Verifique se o cliente é maior de idade usando uma comparação.

Mostre o resultado no terminal.

---

### 10. Ajuste de preço com vírgula

Um sistema recebeu o valor:

```python
valor_texto = "249,90"
```

Troque a vírgula por ponto, converta para `float` e mostre o valor formatado.

---

## Exercícios desafiadores

### 11. Pedido vindo de API

Você recebeu os dados abaixo de uma API:

```python
pedido = {
    "id": "501",
    "cliente": "Tech Soluções",
    "quantidade": "3",
    "preco_unitario": "199.90",
    "pago": "True"
}
```

Converta os campos necessários e calcule o total do pedido.

Mostre:

- id como número inteiro;
- cliente;
- total formatado;
- pago como booleano.

---

### 12. Registro de funcionário

Você recebeu os dados abaixo como se viessem de uma planilha:

```python
nome = "Juliana Martins"
idade = "31"
salario = "5800.50"
ativo = "False"
```

Converta idade, salário e ativo para os tipos corretos.

Depois mostre uma ficha formatada do funcionário.

---

### 13. Relatório simples de venda

Crie variáveis para:

- nome do produto;
- preço unitário;
- quantidade vendida;
- percentual de desconto.

Calcule:

- total bruto;
- valor do desconto;
- total final.

Mostre um relatório formatado no terminal.
