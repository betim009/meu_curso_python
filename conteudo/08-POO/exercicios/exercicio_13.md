# Exercício 13 - Sistema de RH com polimorfismo

Crie um sistema de pagamento para funcionários.

## Requisitos

- Classe base `Funcionario`.
- Classes filhas `FuncionarioCLT`, `FuncionarioPJ` e `Estagiario`.
- Todas devem ter o método `calcular_pagamento`.
- Crie uma lista com funcionários de tipos diferentes.
- Percorra a lista exibindo o pagamento de cada um.

## Regras sugeridas

- CLT recebe salário fixo.
- PJ recebe `valor_hora * horas_trabalhadas`.
- Estagiário recebe bolsa fixa mais auxílio transporte.

## Situação real

Um sistema de RH pode tratar diferentes contratos por meio do mesmo método.
