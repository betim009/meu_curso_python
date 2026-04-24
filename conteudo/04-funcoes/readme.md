# Funções em Python

Você já aprendeu tipos de dados, condições e repetições.

Agora chegou o momento de aprender a organizar melhor o código.

Em sistemas reais, não basta o código funcionar. Ele precisa ser claro, reutilizável e fácil de manter. Funções ajudam exatamente nisso.

---

## O que você vai aprender

Neste módulo, você vai aprender:

- Por que código repetido é um problema.
- O que é uma função.
- Como criar funções com `def`.
- Como usar parâmetros.
- Como retornar valores com `return`.
- Como organizar regras de negócio.
- Boas práticas para funções.
- Erros comuns de iniciantes.
- Como criar um sistema simples de folha de pagamento.

---

## 1. O problema do código repetido

Imagine que uma empresa precisa calcular o salário final de vários funcionários.

Sem função, o código pode ficar assim:

```python
salario_base = 3000
bonus = 500
desconto = 200
salario_final = salario_base + bonus - desconto
print(salario_final)

salario_base = 4500
bonus = 800
desconto = 350
salario_final = salario_base + bonus - desconto
print(salario_final)
```

Funciona, mas tem problemas:

- a regra fica repetida;
- se a regra mudar, será preciso alterar em vários lugares;
- o código cresce rápido;
- fica mais fácil cometer erros.

Com função, colocamos a regra em um lugar só.

```python
def calcular_salario_final(salario_base, bonus, desconto):
    return salario_base + bonus - desconto
```

Agora podemos reutilizar:

```python
print(calcular_salario_final(3000, 500, 200))
print(calcular_salario_final(4500, 800, 350))
```

---

## 2. O que é uma função?

Uma função é um bloco de código que executa uma tarefa.

Pense em uma função como uma caixa:

```text
entra dados -> função processa -> sai resultado
```

Exemplo:

```python
def calcular_total_venda(preco, quantidade):
    total = preco * quantidade
    return total
```

Essa função:

- recebe `preco`;
- recebe `quantidade`;
- calcula o total;
- devolve o resultado.

---

## 3. Criando uma função com `def`

Usamos `def` para criar uma função.

```python
def exibir_mensagem():
    print("Sistema iniciado.")
```

Para executar a função, precisamos chamá-la:

```python
exibir_mensagem()
```

Explicando:

- `def` indica que estamos criando uma função.
- `exibir_mensagem` é o nome da função.
- `()` indica que a função não recebe dados.
- O código indentado pertence à função.

---

## 4. Parâmetros

Parâmetros são dados que a função recebe para trabalhar.

Exemplo real: calcular total de venda.

```python
def calcular_total_venda(preco_unitario, quantidade):
    return preco_unitario * quantidade


total = calcular_total_venda(250.00, 3)
print(f"Total: R$ {total:.2f}")
```

Explicando:

- `preco_unitario` e `quantidade` são parâmetros.
- `250.00` e `3` são valores enviados para a função.
- A função calcula e retorna o total.

---

## 5. `return`

`return` devolve um valor para quem chamou a função.

Sem `return`, a função pode até executar algo, mas não entrega resultado para ser reutilizado.

Exemplo com `return`:

```python
def calcular_bonus(salario, percentual):
    return salario * (percentual / 100)


bonus = calcular_bonus(4000, 10)
print(f"Bônus: R$ {bonus:.2f}")
```

Por que isso é útil?

Porque podemos guardar o resultado em uma variável e usar depois em outro cálculo.

---

## 6. Funções com condições

Funções também podem conter regras de negócio.

Exemplo: validar se um cliente pode comprar.

```python
def cliente_pode_comprar(idade, ativo):
    if idade >= 18 and ativo:
        return True

    return False


resultado = cliente_pode_comprar(25, True)
print(resultado)
```

Explicando:

- A função recebe idade e status.
- Se o cliente for maior de idade e estiver ativo, retorna `True`.
- Caso contrário, retorna `False`.

---

## 7. Funções com loops

Funções podem processar listas.

Exemplo: calcular total de vendas.

```python
def calcular_total_vendas(vendas):
    total = 0

    for venda in vendas:
        total += venda

    return total


vendas = [1200.00, 850.50, 399.90]
total = calcular_total_vendas(vendas)

print(f"Total vendido: R$ {total:.2f}")
```

Essa função pode ser usada em qualquer lista de vendas.

---

## 8. Antes e depois

### Sem função

```python
preco = 100
quantidade = 3
desconto = 20
total = preco * quantidade - desconto
print(total)
```

### Com função

```python
def calcular_total_com_desconto(preco, quantidade, desconto):
    return preco * quantidade - desconto


total = calcular_total_com_desconto(100, 3, 20)
print(total)
```

A segunda versão é melhor porque a regra tem nome e pode ser reutilizada.

---

## 9. Boas práticas

### Use nomes claros

Prefira:

```python
def calcular_salario_final():
```

Evite:

```python
def calc():
```

### Faça funções pequenas

Uma função deve ter uma responsabilidade principal.

Exemplos bons:

- `calcular_bonus`
- `validar_idade`
- `calcular_total_vendas`
- `aplicar_desconto`

### Retorne valores quando precisar reutilizar

Se o resultado será usado depois, use `return`.

### Evite misturar muitas responsabilidades

Uma função que calcula salário não deveria também imprimir relatório, salvar arquivo e validar login ao mesmo tempo.

---

## 10. Erros comuns

### Erro 1: esquecer de chamar a função

Errado:

```python
def exibir_mensagem():
    print("Olá")
```

Correto:

```python
def exibir_mensagem():
    print("Olá")


exibir_mensagem()
```

---

### Erro 2: esquecer o `return`

Errado:

```python
def calcular_total(preco, quantidade):
    total = preco * quantidade


resultado = calcular_total(100, 2)
print(resultado)
```

Isso imprime `None`.

Correto:

```python
def calcular_total(preco, quantidade):
    return preco * quantidade
```

---

### Erro 3: criar função grande demais

Se uma função faz muitas coisas, fica difícil de entender e testar.

Prefira dividir:

- uma função para calcular;
- outra para validar;
- outra para exibir.

---

### Erro 4: usar nomes genéricos

Evite nomes como:

- `funcao1`
- `calculo`
- `teste`
- `x`

Use nomes que expliquem a intenção.

---

## 11. Mini desafios

Tente resolver antes dos exercícios:

1. Crie uma função que calcule o total de uma venda.
2. Crie uma função que valide se uma idade é maior ou igual a 18.
3. Crie uma função que calcule salário com bônus.
4. Crie uma função que aplique desconto em um pedido.
5. Crie uma função que receba uma lista de vendas e retorne o total.

---

## 12. Resumo

Neste módulo, você aprendeu que:

- Funções organizam código.
- `def` cria uma função.
- Parâmetros são dados de entrada.
- `return` devolve resultado.
- Funções evitam repetição.
- Funções ajudam a representar regras de negócio.
- Nomes claros tornam o código mais profissional.
- Funções pequenas são mais fáceis de entender, testar e reutilizar.
