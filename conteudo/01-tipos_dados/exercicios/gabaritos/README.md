# Gabaritos - Tipos de Dados

Compare sua solução com calma.

O mais importante não é decorar o código, mas entender por que cada tipo foi usado.

---

## 1. Cadastro básico de cliente

```python
nome_cliente = "Ana Souza"
email_cliente = "ana.souza@email.com"
idade_cliente = 34
cidade_cliente = "São Paulo"

print(nome_cliente)
print(email_cliente)
print(idade_cliente)
print(cidade_cliente)
```

Explicação:

- Nome, email e cidade são textos, então usamos `str`.
- Idade é número inteiro, então usamos `int`.

---

## 2. Tipos de um funcionário

```python
nome_funcionario = "Carlos Lima"
idade_funcionario = 41
salario_funcionario = 6300.75
funcionario_ativo = True

print(type(nome_funcionario))
print(type(idade_funcionario))
print(type(salario_funcionario))
print(type(funcionario_ativo))
```

Explicação:

- `type()` mostra o tipo real de cada valor.
- Isso ajuda a validar dados antes de cálculos e comparações.

---

## 3. Total de venda

```python
preco_licenca = 350.00
quantidade = 4
total = preco_licenca * quantidade

print(f"Total da venda: R$ {total:.2f}")
```

Explicação:

- Preço usa `float`.
- Quantidade usa `int`.
- O total vem de uma multiplicação.

---

## 4. Nome completo

```python
nome = "Ana"
sobrenome = "Souza"
nome_completo = nome + " " + sobrenome

print(nome_completo)
```

Explicação:

- O espaço `" "` é necessário para separar nome e sobrenome.

---

## 5. Cliente ativo

```python
cliente_ativo = True

print(f"Cliente ativo: {cliente_ativo}")
```

Explicação:

- `True` indica um estado lógico verdadeiro.
- Em sistemas reais, isso pode representar um cliente habilitado no cadastro.

---

## 6. Conversão de idade do formulário

```python
idade_texto = "28"
idade = int(idade_texto)

print(idade + 1)
```

Explicação:

- Dados vindos de formulário costumam chegar como texto.
- Para somar, precisamos converter com `int()`.

---

## 7. Conversão de preço vindo de planilha

```python
preco_texto = "129.90"
preco = float(preco_texto)
quantidade = 5
total = preco * quantidade

print(f"Total: R$ {total:.2f}")
```

Explicação:

- Preço tem casas decimais, então usamos `float`.
- A formatação `:.2f` mostra duas casas decimais.

---

## 8. Salário com bônus

```python
salario_base = 3200.00
bonus = 850.00
salario_final = salario_base + bonus

print(f"Salário final: R$ {salario_final:.2f}")
```

Explicação:

- Valores financeiros geralmente usam `float` no início do aprendizado.
- Mais adiante, em sistemas financeiros reais, existem técnicas mais específicas para dinheiro.

---

## 9. Validação de idade

```python
idade_cliente = 19
maior_de_idade = idade_cliente >= 18

print(maior_de_idade)
```

Explicação:

- A comparação `>=` retorna `True` ou `False`.
- Esse resultado é do tipo `bool`.

---

## 10. Ajuste de preço com vírgula

```python
valor_texto = "249,90"
valor_ajustado = valor_texto.replace(",", ".")
valor = float(valor_ajustado)

print(f"Valor: R$ {valor:.2f}")
```

Explicação:

- Python usa ponto como separador decimal.
- `replace(",", ".")` ajusta o texto antes da conversão.

---

## 11. Pedido vindo de API

```python
pedido = {
    "id": "501",
    "cliente": "Tech Soluções",
    "quantidade": "3",
    "preco_unitario": "199.90",
    "pago": "True",
}

id_pedido = int(pedido["id"])
cliente = pedido["cliente"]
quantidade = int(pedido["quantidade"])
preco_unitario = float(pedido["preco_unitario"])
pago = pedido["pago"] == "True"
total = quantidade * preco_unitario

print(f"ID: {id_pedido}")
print(f"Cliente: {cliente}")
print(f"Total: R$ {total:.2f}")
print(f"Pago: {pago}")
```

Explicação:

- APIs frequentemente enviam números como texto.
- O campo `pago` foi convertido por comparação.

---

## 12. Registro de funcionário

```python
nome = "Juliana Martins"
idade = "31"
salario = "5800.50"
ativo = "False"

idade_convertida = int(idade)
salario_convertido = float(salario)
ativo_convertido = ativo == "True"

print("Ficha do funcionário")
print(f"Nome: {nome}")
print(f"Idade: {idade_convertida}")
print(f"Salário: R$ {salario_convertido:.2f}")
print(f"Ativo: {ativo_convertido}")
```

Explicação:

- `"False"` é texto.
- Para virar booleano corretamente, comparamos com `"True"`.
- Como o valor é `"False"`, o resultado da comparação é `False`.

---

## 13. Relatório simples de venda

```python
produto = "Notebook corporativo"
preco_unitario = 4200.00
quantidade = 2
percentual_desconto = 10

total_bruto = preco_unitario * quantidade
valor_desconto = total_bruto * (percentual_desconto / 100)
total_final = total_bruto - valor_desconto

print("Relatório de venda")
print(f"Produto: {produto}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Total final: R$ {total_final:.2f}")
```

Explicação:

- O total bruto é preço vezes quantidade.
- O desconto é calculado usando percentual dividido por 100.
- O total final é o total bruto menos o desconto.
