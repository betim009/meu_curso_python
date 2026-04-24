# Exercícios - Funções

Resolva os exercícios em ordem.

Eles simulam regras comuns em sistemas reais: vendas, cadastro, salário, desconto, validação e relatórios.

Faça primeiro sem olhar o gabarito. Depois compare com [`gabaritos/README.md`](gabaritos/README.md).

---

## Exercícios fáceis

### 1. Calcular total de venda

Crie uma função chamada `calcular_total_venda`.

Ela deve receber:

- preço unitário;
- quantidade.

Ela deve retornar o total da venda.

---

### 2. Validar maioridade

Crie uma função chamada `eh_maior_de_idade`.

Ela deve receber uma idade e retornar `True` se a idade for maior ou igual a 18.

Caso contrário, deve retornar `False`.

---

### 3. Calcular bônus

Crie uma função chamada `calcular_bonus`.

Ela deve receber:

- salário;
- percentual de bônus.

Ela deve retornar o valor do bônus.

---

### 4. Aplicar desconto

Crie uma função chamada `aplicar_desconto`.

Ela deve receber:

- valor do pedido;
- percentual de desconto.

Ela deve retornar o valor final com desconto.

---

### 5. Exibir nome formatado

Crie uma função chamada `formatar_nome_cliente`.

Ela deve receber nome e sobrenome e retornar o nome completo.

---

## Exercícios médios

### 6. Validar cliente ativo

Crie uma função chamada `cliente_pode_comprar`.

Ela deve receber:

- idade;
- status ativo.

Retorne `True` apenas se o cliente for maior de idade e estiver ativo.

---

### 7. Calcular salário final

Crie uma função chamada `calcular_salario_final`.

Ela deve receber:

- salário base;
- bônus;
- desconto.

Ela deve retornar o salário final.

---

### 8. Calcular total de vendas

Crie uma função chamada `calcular_total_vendas`.

Ela deve receber uma lista de vendas e retornar o total.

---

### 9. Contar vendas acima da meta

Crie uma função chamada `contar_vendas_acima_meta`.

Ela deve receber:

- lista de vendas;
- valor da meta.

Retorne quantas vendas foram maiores ou iguais à meta.

---

### 10. Classificar cliente por compra

Crie uma função chamada `classificar_cliente`.

Ela deve receber o valor total de compra e retornar:

- `"Premium"` para valor maior ou igual a `1000`;
- `"Padrão"` para valor maior ou igual a `500`;
- `"Inicial"` para valores menores.

---

## Exercícios desafiadores

### 11. Processar pedido

Crie uma função chamada `processar_pedido`.

Ela deve receber:

- preço unitário;
- quantidade;
- percentual de desconto.

Ela deve retornar o total final do pedido.

---

### 12. Gerar resumo de vendas

Crie uma função chamada `gerar_resumo_vendas`.

Ela deve receber uma lista de vendas e retornar um dicionário com:

- total;
- quantidade;
- média;
- maior venda.

---

### 13. Validar cadastro completo

Crie uma função chamada `validar_cadastro`.

Ela deve receber:

- idade;
- email confirmado;
- aceitou termos;
- usuário ativo.

Retorne `True` apenas se todas as regras forem atendidas.
