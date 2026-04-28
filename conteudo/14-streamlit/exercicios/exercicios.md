# Exercicios - Streamlit

Use o arquivo:

```text
../dados/vendas_dashboard.csv
```

Os exercicios simulam tarefas reais de dashboards: mostrar dados, criar KPIs, aplicar filtros e exibir graficos.

## Exercicios faceis

### 1. Primeiro app

Crie um app Streamlit com:

- titulo;
- texto explicativo;
- campo `text_input`;
- botao.

Quando o botao for clicado, mostre uma mensagem de sucesso.

### 2. Mostrar tabela de vendas

Leia `vendas_dashboard.csv` com pandas e mostre os dados usando `st.dataframe()`.

### 3. Criar KPIs

Mostre tres metricas:

- faturamento total;
- quantidade de pedidos;
- ticket medio.

### 4. Mostrar primeiras linhas

Mostre apenas as 10 primeiras linhas da base.

### 5. Filtro por cidade

Crie um `selectbox` com as cidades da base e mostre apenas vendas da cidade selecionada.

## Exercicios medios

### 6. Filtro por categoria

Crie um filtro com a opcao `Todas` e as categorias da base.

Se o usuario escolher `Todas`, mostre todos os dados. Caso contrario, filtre pela categoria.

### 7. Filtro por produto com multiselect

Crie um `multiselect` para o usuario selecionar um ou mais produtos.

Mostre apenas as vendas dos produtos selecionados.

### 8. Grafico de faturamento por mes

Crie um grafico de linha com matplotlib mostrando faturamento por mes dentro do Streamlit.

### 9. Grafico de faturamento por produto

Crie um grafico de barras mostrando faturamento por produto.

Ordene do maior para o menor.

### 10. Filtro de periodo

Converta a coluna `data` para datetime e crie filtros de data inicial e data final usando `st.date_input`.

Mostre os dados filtrados.

## Exercicios desafiadores

### 11. Dashboard com KPIs e filtros

Crie um dashboard com:

- filtros na sidebar;
- KPIs no topo;
- tabela filtrada;
- aviso quando nao houver dados.

Filtros:

- categoria;
- produto;
- periodo.

### 12. Dashboard com dois graficos

Crie um dashboard que mostre:

- grafico de linha com faturamento por mes;
- grafico de barras com faturamento por vendedor.

Os graficos devem respeitar os filtros escolhidos pelo usuario.

### 13. Projeto organizado em funcoes

Crie um app Streamlit organizado com funcoes:

- `carregar_dados()`;
- `aplicar_filtros(df)`;
- `mostrar_kpis(df)`;
- `mostrar_graficos(df)`;
- `mostrar_tabela(df)`.

O app deve funcionar como um dashboard simples de vendas.
