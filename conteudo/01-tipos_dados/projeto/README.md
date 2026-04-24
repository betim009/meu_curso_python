# Projeto - Cadastro de Funcionário

Neste projeto, você vai criar um cadastro simples de funcionário.

Esse tipo de lógica aparece em sistemas de RH, sistemas internos de empresas, planilhas automatizadas e formulários de cadastro.

---

## Objetivo

Criar um programa que:

1. Recebe dados de um funcionário.
2. Converte os dados para os tipos corretos.
3. Calcula uma informação derivada.
4. Exibe uma ficha formatada.

---

## Dados do funcionário

O sistema deve receber:

- nome;
- idade;
- cargo;
- salário;
- status ativo.

Como `input()` sempre retorna texto, alguns dados precisam ser convertidos.

| Campo | Tipo correto |
|---|---|
| nome | `str` |
| idade | `int` |
| cargo | `str` |
| salário | `float` |
| ativo | `bool` |

---

## Passo a passo

### 1. Receber os dados

```python
nome = input("Nome do funcionário: ")
idade_texto = input("Idade: ")
cargo = input("Cargo: ")
salario_texto = input("Salário: ")
ativo_texto = input("Funcionário ativo? (s/n): ")
```

Neste momento, todos os valores são texto.

### 2. Converter os tipos

```python
idade = int(idade_texto)
salario = float(salario_texto)
ativo = ativo_texto.lower() == "s"
```

Por que converter?

- Idade precisa ser número para comparações.
- Salário precisa ser decimal para cálculos.
- Ativo precisa virar `True` ou `False`.

### 3. Calcular salário anual

```python
salario_anual = salario * 12
```

Esse cálculo simula uma informação comum em relatórios de RH.

### 4. Exibir ficha

```python
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Cargo: {cargo}")
print(f"Salário mensal: R$ {salario:.2f}")
print(f"Salário anual: R$ {salario_anual:.2f}")
print(f"Ativo: {ativo}")
```

---

## Código completo

O código completo está no arquivo [`cadastro_funcionario.py`](cadastro_funcionario.py).

Execute com:

```bash
python cadastro_funcionario.py
```

---

## Exemplo de uso

Entrada:

```text
Nome do funcionário: Juliana Martins
Idade: 31
Cargo: Analista de Dados
Salário: 5800.50
Funcionário ativo? (s/n): s
```

Saída:

```text
Ficha do funcionário
Nome: Juliana Martins
Idade: 31
Cargo: Analista de Dados
Salário mensal: R$ 5800.50
Salário anual: R$ 69606.00
Ativo: True
```

---

## Decisões tomadas

- `nome` e `cargo` ficam como texto porque não serão usados em cálculo.
- `idade` vira `int` porque pode ser usada em validações.
- `salario` vira `float` porque possui casas decimais.
- `ativo` vira `bool` porque representa estado verdadeiro ou falso.
- O salário anual é calculado para simular um relatório simples.

---

## Melhorias futuras

Depois de estudar os próximos módulos, você poderá melhorar este projeto com:

- condições para validar idade;
- tratamento de erro se o salário for inválido;
- repetição para cadastrar vários funcionários;
- funções para organizar o código;
- arquivo CSV para salvar os cadastros.
