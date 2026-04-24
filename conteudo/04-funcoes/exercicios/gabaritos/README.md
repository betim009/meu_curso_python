# Gabaritos - Funções

Compare sua solução com calma.

O objetivo é entender como funções ajudam a organizar regras de negócio.

---

## 1. Calcular total de venda

```python
def calcular_total_venda(preco_unitario, quantidade):
    return preco_unitario * quantidade


total = calcular_total_venda(250.00, 3)
print(f"Total: R$ {total:.2f}")
```

Explicação:

- A função recebe os dados necessários.
- O `return` devolve o total calculado.

---

## 2. Validar maioridade

```python
def eh_maior_de_idade(idade):
    return idade >= 18


print(eh_maior_de_idade(20))
```

Explicação:

- A comparação `idade >= 18` já retorna `True` ou `False`.

---

## 3. Calcular bônus

```python
def calcular_bonus(salario, percentual_bonus):
    return salario * (percentual_bonus / 100)


bonus = calcular_bonus(4000.00, 10)
print(f"Bônus: R$ {bonus:.2f}")
```

Explicação:

- Percentual precisa ser dividido por 100 antes do cálculo.

---

## 4. Aplicar desconto

```python
def aplicar_desconto(valor_pedido, percentual_desconto):
    desconto = valor_pedido * (percentual_desconto / 100)
    return valor_pedido - desconto


valor_final = aplicar_desconto(1000.00, 15)
print(f"Valor final: R$ {valor_final:.2f}")
```

Explicação:

- Primeiro calculamos o desconto.
- Depois subtraímos do valor original.

---

## 5. Exibir nome formatado

```python
def formatar_nome_cliente(nome, sobrenome):
    return f"{nome} {sobrenome}"


print(formatar_nome_cliente("Ana", "Souza"))
```

Explicação:

- A função junta nome e sobrenome e retorna uma string.

---

## 6. Validar cliente ativo

```python
def cliente_pode_comprar(idade, ativo):
    return idade >= 18 and ativo


print(cliente_pode_comprar(25, True))
```

Explicação:

- Usamos `and` porque as duas regras precisam ser verdadeiras.

---

## 7. Calcular salário final

```python
def calcular_salario_final(salario_base, bonus, desconto):
    return salario_base + bonus - desconto


salario = calcular_salario_final(3000.00, 500.00, 200.00)
print(f"Salário final: R$ {salario:.2f}")
```

Explicação:

- A regra fica centralizada em uma única função.

---

## 8. Calcular total de vendas

```python
def calcular_total_vendas(vendas):
    total = 0

    for venda in vendas:
        total += venda

    return total


vendas = [1200.00, 850.50, 399.90]
print(f"Total: R$ {calcular_total_vendas(vendas):.2f}")
```

Explicação:

- A função usa um acumulador para somar a lista.

---

## 9. Contar vendas acima da meta

```python
def contar_vendas_acima_meta(vendas, meta):
    quantidade = 0

    for venda in vendas:
        if venda >= meta:
            quantidade += 1

    return quantidade


vendas = [1200.00, 850.50, 399.90, 1500.00]
print(contar_vendas_acima_meta(vendas, 1000))
```

Explicação:

- A função percorre a lista e conta apenas vendas que atingiram a meta.

---

## 10. Classificar cliente por compra

```python
def classificar_cliente(valor_compra):
    if valor_compra >= 1000:
        return "Premium"
    elif valor_compra >= 500:
        return "Padrão"

    return "Inicial"


print(classificar_cliente(850.00))
```

Explicação:

- A ordem das condições importa.
- A maior faixa precisa vir primeiro.

---

## 11. Processar pedido

```python
def processar_pedido(preco_unitario, quantidade, percentual_desconto):
    total_bruto = preco_unitario * quantidade
    desconto = total_bruto * (percentual_desconto / 100)
    return total_bruto - desconto


total = processar_pedido(200.00, 4, 10)
print(f"Total do pedido: R$ {total:.2f}")
```

Explicação:

- A função concentra a regra completa do pedido.

---

## 12. Gerar resumo de vendas

```python
def gerar_resumo_vendas(vendas):
    total = 0
    quantidade = 0
    maior_venda = 0

    for venda in vendas:
        total += venda
        quantidade += 1

        if venda > maior_venda:
            maior_venda = venda

    media = total / quantidade

    return {
        "total": total,
        "quantidade": quantidade,
        "media": media,
        "maior_venda": maior_venda,
    }


vendas = [1200.00, 850.50, 399.90, 1500.00]
resumo = gerar_resumo_vendas(vendas)

print(resumo)
```

Explicação:

- A função retorna um dicionário porque existem vários resultados relacionados.

---

## 13. Validar cadastro completo

```python
def validar_cadastro(idade, email_confirmado, aceitou_termos, usuario_ativo):
    return idade >= 18 and email_confirmado and aceitou_termos and usuario_ativo


print(validar_cadastro(28, True, True, True))
```

Explicação:

- Todas as regras precisam ser verdadeiras para aprovar o cadastro.
