# 14 - Streamlit para Dashboards de Dados

Neste modulo voce vai aprender a transformar analises de dados em aplicacoes visuais interativas.

Ate aqui, voce ja aprendeu Python, pandas, APIs, graficos, banco de dados e Flask. Agora voce vai usar esses conhecimentos para criar uma interface simples no navegador, com tabelas, indicadores, filtros e graficos.

O foco sera um dashboard de vendas, parecido com ferramentas usadas em empresas para acompanhar desempenho comercial.

## Estrutura do modulo

```text
14-streamlit/
  README.md
  dados/
    vendas_dashboard.csv
  exemplos/
    01_primeiro_app.py
    02_exibindo_dados.py
    03_graficos.py
    04_filtros_interativos.py
  exercicios/
    exercicios.md
    gabaritos/
      gabaritos.md
      gabaritos.py
  projeto/
    README.md
    dashboard_vendas.py
```

## 1. Introducao

### O que e Streamlit?

Streamlit e uma biblioteca Python usada para criar aplicacoes web de dados de forma simples.

Com Streamlit, voce escreve Python e consegue mostrar:

- textos;
- tabelas;
- metricas;
- filtros;
- graficos;
- formularios;
- arquivos enviados pelo usuario.

O Streamlit e muito usado para dashboards, prototipos, ferramentas internas e relatorios interativos.

### Onde e usado?

Streamlit aparece em projetos como:

- dashboard de vendas;
- acompanhamento de indicadores;
- analise de clientes;
- relatorios financeiros;
- ferramentas internas para equipes;
- prototipos de ciencia de dados;
- paineis que consomem CSV, APIs ou banco de dados.

### Exemplo real

Imagine uma empresa que vende produtos de tecnologia.

Ela quer acompanhar:

- faturamento total;
- quantidade de pedidos;
- ticket medio;
- produto mais vendido;
- faturamento por mes;
- vendas por produto;
- desempenho por vendedor;
- filtros por periodo, categoria e produto.

Com pandas, voce calcula os dados.  
Com matplotlib, voce cria graficos.  
Com Streamlit, voce transforma tudo em uma aplicacao visual para o usuario interagir.

## 2. Instalando Streamlit

Instale as dependencias:

```bash
pip install streamlit pandas matplotlib
```

Para testar se funcionou:

```bash
streamlit hello
```

Para rodar um app:

```bash
streamlit run app.py
```

O Streamlit abre uma pagina no navegador. Normalmente o endereco sera:

```text
http://localhost:8501
```

## 3. Criando primeiro app

Crie um arquivo chamado `app.py`.

```python
import streamlit as st

st.title("Meu primeiro app")
st.write("Este texto aparece no navegador.")

nome = st.text_input("Digite seu nome")

if st.button("Enviar"):
    st.success(f"Ola, {nome}!")
```

Execute:

```bash
streamlit run app.py
```

### Estrutura basica

```python
import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("Dashboard de Vendas")
st.write("Analise simples de vendas da empresa.")
```

`st.set_page_config()` configura a pagina.  
`layout="wide"` usa melhor a largura da tela, o que ajuda em dashboards.

## 4. Exibindo dados

Streamlit consegue exibir dados de varias formas.

### Texto

```python
st.title("Titulo principal")
st.header("Secao")
st.subheader("Subsecao")
st.write("Texto simples ou variaveis.")
```

### Tabelas com pandas

```python
import pandas as pd
import streamlit as st

df = pd.read_csv("dados/vendas_dashboard.csv")

st.dataframe(df)
```

`st.dataframe()` mostra uma tabela interativa.

Para mostrar uma tabela estatica:

```python
st.table(df.head())
```

### Metricas

Metricas sao indicadores importantes, tambem chamados de KPIs.

```python
faturamento_total = df["valor_total"].sum()
quantidade_pedidos = df["id_pedido"].nunique()
ticket_medio = faturamento_total / quantidade_pedidos

st.metric("Faturamento", f"R$ {faturamento_total:,.2f}")
st.metric("Pedidos", quantidade_pedidos)
st.metric("Ticket medio", f"R$ {ticket_medio:,.2f}")
```

KPI significa indicador-chave de desempenho. Em empresas, KPIs ajudam a acompanhar se o negocio esta indo bem.

## 5. Graficos

Streamlit pode exibir graficos criados com matplotlib.

```python
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

df = pd.read_csv("dados/vendas_dashboard.csv")

vendas_mes = df.groupby("mes")["valor_total"].sum()

fig, ax = plt.subplots()
ax.plot(vendas_mes.index, vendas_mes.values, marker="o")
ax.set_title("Faturamento por mes")
ax.set_xlabel("Mes")
ax.set_ylabel("Faturamento")

st.pyplot(fig)
```

`fig` representa a figura.  
`ax` representa a area do grafico.  
`st.pyplot(fig)` mostra o grafico no app.

### Grafico de barras

```python
vendas_produto = df.groupby("produto")["valor_total"].sum().sort_values(ascending=False)

fig, ax = plt.subplots()
ax.bar(vendas_produto.index, vendas_produto.values)
ax.set_title("Faturamento por produto")
ax.tick_params(axis="x", rotation=45)

st.pyplot(fig)
```

## 6. Interatividade

A grande vantagem do Streamlit e permitir que o usuario filtre e explore dados.

### Selectbox

```python
categoria = st.selectbox("Categoria", df["categoria"].unique())
df_filtrado = df[df["categoria"] == categoria]
```

### Multiselect

```python
produtos = st.multiselect(
    "Produtos",
    options=sorted(df["produto"].unique()),
    default=sorted(df["produto"].unique()),
)

df_filtrado = df[df["produto"].isin(produtos)]
```

### Slider

```python
valor_minimo = st.slider(
    "Valor minimo da venda",
    min_value=0,
    max_value=5000,
    value=0,
)

df_filtrado = df[df["valor_total"] >= valor_minimo]
```

### Date input

```python
df["data"] = pd.to_datetime(df["data"])

data_inicio = st.date_input("Data inicial", df["data"].min())
data_fim = st.date_input("Data final", df["data"].max())

df_filtrado = df[
    (df["data"].dt.date >= data_inicio)
    & (df["data"].dt.date <= data_fim)
]
```

### Sidebar

Filtros geralmente ficam na lateral.

```python
st.sidebar.header("Filtros")
categoria = st.sidebar.selectbox("Categoria", options=["Todas", "Computadores"])
```

## 7. Organizacao do app

Um dashboard pequeno pode ficar em um arquivo. Mesmo assim, organize em funcoes.

Boa estrutura:

```python
def carregar_dados():
    return pd.read_csv("dados/vendas_dashboard.csv")


def aplicar_filtros(df):
    # filtros do usuario
    return df_filtrado


def mostrar_kpis(df):
    # metricas
    pass


def mostrar_graficos(df):
    # graficos
    pass
```

Essa organizacao ajuda a:

- evitar codigo baguncado;
- testar partes do app;
- reaproveitar funcoes;
- facilitar manutencao.

## 8. Boas praticas

### Clareza visual

O usuario deve entender rapidamente o que esta vendo.

Use:

- titulos claros;
- metricas principais no topo;
- filtros na lateral;
- graficos com nomes de eixos;
- tabelas abaixo dos graficos.

### Simplicidade

Evite colocar tudo na tela.

Um bom dashboard responde perguntas importantes, nao mostra todos os dados ao mesmo tempo.

### Cuidado com excesso de filtros

Filtros demais confundem. Comece com:

- periodo;
- categoria;
- produto;
- vendedor.

### Use cache para carregar dados

```python
@st.cache_data
def carregar_dados():
    return pd.read_csv("dados/vendas_dashboard.csv")
```

`st.cache_data` evita recarregar o arquivo toda vez que o usuario muda um filtro.

### Trate dados vazios

Depois de aplicar filtros, pode nao sobrar nenhuma linha.

```python
if df_filtrado.empty:
    st.warning("Nenhum dado encontrado para os filtros selecionados.")
    st.stop()
```

## 9. Erros comuns

### Codigo baguncado

Erro comum: colocar leitura, filtro, calculo e grafico tudo misturado.

Solucao: separar em funcoes.

### Excesso de informacao

Um dashboard com 20 graficos na mesma tela fica dificil de usar.

Solucao: mostrar primeiro KPIs e graficos principais.

### Esquecer de converter datas

Se a coluna de data for texto, filtros de periodo podem dar erro.

```python
df["data"] = pd.to_datetime(df["data"])
```

### Erro de caminho do arquivo

Se o app nao encontra o CSV, use `Path`.

```python
from pathlib import Path

CAMINHO_DADOS = Path(__file__).resolve().parents[1] / "dados" / "vendas_dashboard.csv"
```

### Grafico nao aparece

Com matplotlib no Streamlit, lembre de usar:

```python
st.pyplot(fig)
```

## 10. Mini desafios

Use `dados/vendas_dashboard.csv`.

### Mini desafio 1

Crie um app que mostre titulo e uma tabela com as vendas.

### Mini desafio 2

Mostre tres KPIs:

- faturamento total;
- quantidade de pedidos;
- ticket medio.

### Mini desafio 3

Crie um filtro por categoria usando `selectbox`.

### Mini desafio 4

Crie um filtro por produto usando `multiselect`.

### Mini desafio 5

Crie um grafico de linha com faturamento por mes.

### Mini desafio 6

Crie um grafico de barras com faturamento por produto.

### Mini desafio 7

Mostre uma mensagem de aviso quando nenhum dado for encontrado apos os filtros.

## 11. Resumo

Neste modulo voce aprendeu que:

- Streamlit transforma scripts Python em apps web;
- dashboards mostram dados de forma visual e interativa;
- `st.title`, `st.write`, `st.dataframe` e `st.metric` ajudam a montar a interface;
- `selectbox`, `multiselect`, `slider` e `date_input` criam interatividade;
- matplotlib pode ser exibido com `st.pyplot`;
- pandas e Streamlit funcionam muito bem juntos;
- filtros devem ficar claros e simples;
- dashboards profissionais precisam de organizacao, boas metricas e visual limpo.

Ao final deste modulo, voce ja consegue transformar uma analise de dados em um dashboard interativo para uso real.
