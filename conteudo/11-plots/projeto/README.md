# Projeto - Relatorio Visual de Vendas

Neste projeto, voce vai criar um relatorio visual de vendas simulando uma demanda real de empresa.

A empresa quer entender:

- como o faturamento evoluiu ao longo do ano;
- quais produtos geram mais receita;
- quais categorias representam maior participacao;
- qual vendedor teve melhor desempenho;
- como as categorias se comportam mes a mes.

## Dados usados

```text
../dados/vendas_mensais.csv
../dados/vendas_detalhadas.csv
```

## Graficos gerados

O projeto gera:

- `01_faturamento_mensal.png`: grafico de linha;
- `02_top_produtos.png`: grafico de barras;
- `03_participacao_categorias.png`: grafico de pizza;
- `04_faturamento_vendedores.png`: grafico de barras;
- `05_dashboard_vendas.png`: figura com varios graficos.

## Passo a passo

### 1. Ler os dados

```python
mensal = pd.read_csv("../dados/vendas_mensais.csv")
vendas = pd.read_csv("../dados/vendas_detalhadas.csv")
```

### 2. Gerar metricas agrupadas

```python
top_produtos = vendas.groupby("produto")["valor_total"].sum().sort_values(ascending=False).head(5)
```

### 3. Criar graficos

Usamos `matplotlib` para criar cada visualizacao.

### 4. Salvar em PNG

```python
plt.savefig("graficos/faturamento_mensal.png", dpi=120)
```

Salvar imagens permite usar os graficos em relatorios, apresentacoes e dashboards simples.

## Como executar

Instale as dependencias:

```bash
pip install pandas matplotlib
```

Execute:

```bash
python3 relatorio_visual_vendas.py
```

Os graficos serao salvos na pasta:

```text
projeto/graficos/
```

## Interpretacao dos graficos

- O grafico de linha mostra tendencia de crescimento ou queda.
- O grafico de barras mostra comparacao entre produtos ou vendedores.
- O grafico de pizza mostra a participacao das categorias no total.
- O dashboard junta visoes importantes em uma unica figura.

Esse projeto simula um relatorio visual basico usado em empresas para apoiar decisoes comerciais.
