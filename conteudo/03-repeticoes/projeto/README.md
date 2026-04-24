# Projeto - Processamento de Dados de Vendas

Neste projeto, você vai criar um relatório simples de vendas.

Esse tipo de lógica aparece em análise de dados, sistemas comerciais, dashboards e rotinas de fechamento diário.

---

## Objetivo

Criar um programa que processe uma lista de vendas e calcule:

- total vendido;
- quantidade de vendas;
- média por venda;
- maior venda;
- vendas acima de um valor definido.

---

## Dados do projeto

Vamos usar uma lista simples de valores:

```python
vendas = [1200.00, 850.50, 399.90, 1500.00, 220.00, 990.00]
```

Cada número representa o valor de uma venda.

---

## Passo a passo

### 1. Criar as variáveis iniciais

```python
total = 0
quantidade = 0
maior_venda = 0
vendas_acima_meta = 0
meta = 1000
```

Por que começar com zero?

Porque ainda não processamos nenhuma venda.

### 2. Percorrer a lista

```python
for venda in vendas:
    total += venda
    quantidade += 1
```

Aqui o programa passa venda por venda e atualiza os totais.

### 3. Encontrar a maior venda

```python
if venda > maior_venda:
    maior_venda = venda
```

Se a venda atual for maior que a maior já encontrada, atualizamos o valor.

### 4. Contar vendas acima da meta

```python
if venda >= meta:
    vendas_acima_meta += 1
```

Isso simula uma métrica de desempenho comercial.

---

## Código completo

O código está no arquivo [`relatorio_vendas.py`](relatorio_vendas.py).

Execute com:

```bash
python relatorio_vendas.py
```

---

## Saída esperada

```text
Relatório de vendas
Total vendido: R$ 5160.40
Quantidade de vendas: 6
Média por venda: R$ 860.07
Maior venda: R$ 1500.00
Vendas acima da meta: 2
```

---

## Decisões tomadas

- Usamos `for` porque já temos uma lista de vendas.
- Usamos acumulador para calcular o total.
- Usamos contador para calcular quantidade.
- Usamos condição para descobrir a maior venda.
- Usamos outra condição para contar vendas acima da meta.

---

## Melhorias futuras

Depois de estudar os próximos módulos, você poderá melhorar este projeto com:

- funções para separar responsabilidades;
- leitura de vendas a partir de um arquivo CSV;
- tratamento de erros;
- gráficos;
- dashboard com Streamlit.
