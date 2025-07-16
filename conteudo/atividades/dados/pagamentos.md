# 💸 Exercícios de Prática — Pagamentos de Salários

Este material contém **20 exercícios práticos** usando duas bases de dados sobre funcionários e salários.  
Eles estão divididos em três blocos com dificuldade crescente:

---

## 🗃️ Bases de Dados

```python
funcionarios = [
    {"nome": "Ana", "salario": 3200.00, "departamento": "RH", "tempo_empresa": 2},
    {"nome": "Bruno", "salario": 4500.00, "departamento": "TI", "tempo_empresa": 5},
    {"nome": "Carla", "salario": 3900.00, "departamento": "Financeiro", "tempo_empresa": 3},
    {"nome": "Diego", "salario": 2500.00, "departamento": "Operacional", "tempo_empresa": 1},
    {"nome": "Elisa", "salario": 5200.00, "departamento": "TI", "tempo_empresa": 7}
]

pagamentos = {
    "nomes": ["Ana", "Bruno", "Carla", "Diego", "Elisa"],
    "salarios": [3200.00, 4500.00, 3900.00, 2500.00, 5200.00],
    "departamentos": ["RH", "TI", "Financeiro", "Operacional", "TI"],
    "tempo_empresa": [2, 5, 3, 1, 7]
}
```

---

## 📗 Bloco 1 — Acesso direto e modificação

1. Acesse e imprima o nome do primeiro funcionário na lista `funcionarios`.
2. Imprima o salário do terceiro item da lista `pagamentos`, formatando a saída como: `'Salário: R$ 3900.00'`.
3. Altere o tempo de empresa do funcionário 'Bruno' na lista `funcionarios` para `6`.
4. Mude o departamento do funcionário 'Elisa' na estrutura `pagamentos` para 'Diretoria'.
5. Acesse e imprima o nome e o departamento do funcionário na posição 2 da estrutura `pagamentos`, no formato: `'Funcionário: Carla | Departamento: Financeiro'`.

---

## 🔄 Bloco 2 — Uso de `for item in ...`

6. Percorra a lista `funcionarios` e imprima o nome de cada funcionário.
7. Usando `for`, mostre todos os departamentos dos funcionários na estrutura `pagamentos`.
8. Liste todos os salários dos funcionários contidos na lista `funcionarios`, com `for`.
9. Para cada funcionário da lista `funcionarios`, imprima o nome e o tempo de empresa, separados por hífen.
10. Use `for` para imprimir todos os funcionários da estrutura `pagamentos`, com índice + nome.
11. Imprima todos os salários da estrutura `pagamentos` multiplicados por 1.1 (simulando um aumento de 10%).
12. Liste todos os nomes dos funcionários da lista `funcionarios` em letras maiúsculas.
13. Para cada funcionário da estrutura `pagamentos`, imprima o nome e o salário, separados por dois pontos.

---

## 🔍 Bloco 3 — Uso de `for` com `if`

14. Percorra a lista `funcionarios` e imprima somente os funcionários com salário maior que `4000`.
15. Imprima os nomes dos funcionários da estrutura `pagamentos` que trabalham há mais de `3` anos na empresa.
16. Exiba os funcionários da lista `funcionarios` cujo departamento é 'TI'.
17. Mostre todos os funcionários da estrutura `pagamentos` que têm salário abaixo de `3000`.
18. Percorra a lista `funcionarios` e imprima os nomes dos funcionários cujo nome começa com a letra 'C'.
19. Imprima os nomes dos funcionários da estrutura `pagamentos` que pertencem ao departamento 'Financeiro' ou 'RH'.
20. Liste os funcionários da lista `funcionarios` que têm tempo de empresa igual ou superior a 5 anos.

---

**Dica:** Teste cada exercício no terminal do Python ou em um script `.py` para praticar o uso de listas, dicionários, laços e condições. 