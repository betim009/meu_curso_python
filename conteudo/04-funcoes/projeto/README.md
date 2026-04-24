# Projeto - Sistema Simples de Folha de Pagamento

Neste projeto, você vai organizar uma regra de folha de pagamento usando funções.

Esse tipo de lógica aparece em sistemas de RH, sistemas financeiros, planilhas automatizadas e rotinas internas de empresas.

---

## Objetivo

Criar um programa que calcule:

- bônus;
- desconto;
- salário final;
- resumo do pagamento.

Cada responsabilidade ficará em uma função separada.

---

## Regras do sistema

O sistema deve:

1. Calcular o bônus a partir do salário base.
2. Calcular o desconto a partir do salário base.
3. Calcular o salário final.
4. Exibir um resumo formatado.

---

## Funções do projeto

| Função | Responsabilidade |
|---|---|
| `calcular_bonus` | calcular valor do bônus |
| `calcular_desconto` | calcular valor do desconto |
| `calcular_salario_final` | somar salário e bônus, depois subtrair desconto |
| `gerar_resumo_pagamento` | montar os dados finais em um dicionário |

---

## Código completo

O código está no arquivo [`folha_pagamento.py`](folha_pagamento.py).

Execute com:

```bash
python folha_pagamento.py
```

---

## Saída esperada

```text
Resumo da folha de pagamento
Funcionário: Juliana Martins
Salário base: R$ 5800.00
Bônus: R$ 580.00
Desconto: R$ 464.00
Salário final: R$ 5916.00
```

---

## Decisões tomadas

- Cada função tem uma responsabilidade clara.
- Funções de cálculo retornam valores.
- A função de resumo centraliza os dados finais.
- O código principal fica mais fácil de ler.

---

## Melhorias futuras

Depois de estudar os próximos módulos, você poderá melhorar este projeto com:

- tratamento de erros;
- cadastro de vários funcionários;
- leitura de funcionários por CSV;
- relatório final com pandas;
- interface com Streamlit.
