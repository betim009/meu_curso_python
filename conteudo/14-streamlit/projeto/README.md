# Projeto - Dashboard de Analise de Vendas

Neste projeto, voce vai construir um dashboard empresarial com Streamlit.

O dashboard simula uma empresa que quer acompanhar suas vendas de forma visual e interativa.

## Dataset

Arquivo usado:

```text
../dados/vendas_dashboard.csv
```

Colunas principais:

- `data`;
- `cliente`;
- `cidade`;
- `produto`;
- `categoria`;
- `vendedor`;
- `forma_pagamento`;
- `quantidade`;
- `valor_total`.

## Funcionalidades

O dashboard mostra:

- faturamento total;
- quantidade de pedidos;
- ticket medio;
- produto mais vendido;
- grafico de vendas por mes;
- grafico de vendas por produto;
- grafico de vendas por vendedor;
- tabela detalhada.

Filtros:

- periodo;
- categoria;
- produto;
- vendedor;
- cidade.

## Como executar

Instale as dependencias:

```bash
pip install streamlit pandas matplotlib
```

Execute dentro da pasta `projeto`:

```bash
streamlit run dashboard_vendas.py
```

## Decisoes tomadas

### Por que usar sidebar?

Filtros ficam melhor na lateral porque deixam a area principal livre para KPIs e graficos.

### Por que usar funcoes?

Funcoes deixam o app mais organizado:

- uma funcao carrega dados;
- outra aplica filtros;
- outra mostra KPIs;
- outra cria graficos.

### Por que usar cache?

`@st.cache_data` evita recarregar o CSV toda vez que o usuario muda um filtro.

### Por que tratar dados vazios?

Filtros podem remover todas as linhas. Nesse caso, o app precisa avisar o usuario em vez de quebrar.

## Interpretacao dos graficos

- Linha mensal: mostra evolucao do faturamento.
- Barras por produto: mostra quais produtos geram mais receita.
- Barras por vendedor: mostra desempenho comercial.
- Tabela: permite verificar os dados detalhados.
