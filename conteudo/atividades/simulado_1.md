# 🏋️‍♂️ Simulado — Processamento de Dados de Clientes de Academia

Este simulado tem como objetivo desenvolver lógica de programação, manipulação de vetores e criação de funções.  
Todos os exercícios devem ser feitos utilizando **vetores paralelos** e **funções**.

---

## 1. Entrada de dados

O programa deve ler, repetidamente, os dados de cada cliente e armazená-los em vetores paralelos, até que o campo **Preço do plano** receba o valor **-1**.

Os dados necessários para cada cliente são:

- **Tipo de plano**  
  Valores permitidos:
  - `"CARDIO"`
  - `"MAQUINAS"`
  - `"PREMIUM"`

- **Quantidade de dias de treino por semana**  
  - Valor permitido: **1 a 7**

- **Preço do plano**  
  - Valor permitido: **≥ 0**  
  - **Encerrar a leitura quando for digitado -1**

- **Código do cliente**  
  - Valor permitido: **1 a 5**

### ✔️ Regras de validação

O programa deve rejeitar valores inválidos e pedir nova entrada quando:

- O tipo de plano não estiver entre os três permitidos.
- A quantidade de dias não estiver entre 1 e 7.
- O preço for negativo.
- O código não estiver entre 1 e 5.

---

## 2. Função para exibir dados de um cliente

Criar uma função que receba:

- A **posição** do cliente no vetor  
- Todos os vetores carregados

E exiba **todos os dados** desse cliente.

---

## 3. Função para buscar cliente por código

Após finalizar a entrada de dados (item 1):

1. O programa deve solicitar um código de cliente via console.  
2. Criar uma função que:  
   - Receba o código procurado e todos os vetores  
   - Retorne a **posição** do cliente correspondente  
3. Com a posição retornada, **chamar a função do item 2** para exibir os dados do cliente.

---

## 4. Função para encontrar quem treina mais dias

Criar uma função que:

- Analise o vetor de quantidade de dias  
- Identifique o cliente que treina **mais dias por semana**  
- Retorne a posição desse cliente  

Depois disso, utilizar a função do item 2 para exibir seus dados.

---

## 5. Função para mostrar um vetor

Criar uma função genérica que receba **qualquer vetor** e exiba todos os seus valores.

---

## 6. Função para calcular o treino médio

Criar uma função que:

- Calcule a **média da quantidade de dias de treino** entre todos os clientes  
- Retorne esta média

---

## 7. Função para filtrar quem treina acima da média

Criar uma função que:

1. Receba o vetor de dias e a média calculada (item 6)  
2. Gere um **novo vetor** contendo **apenas os códigos dos clientes** que treinam acima da média  
3. Retorne esse novo vetor

---

## 8. Função para ordenar por preço

Criar uma função que ordene **todos os vetores paralelos** de forma **decrescente pelo preço**.

- O maior preço deve ficar na primeira posição  
- Todos os outros vetores devem ser rearranjados juntos, mantendo a correspondência entre eles

Após a ordenação, utilizar a função do item 5 para exibir todos os vetores.

---