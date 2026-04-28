# 11 - Visualizacao de Dados com Matplotlib

Neste modulo voce vai aprender a transformar dados em graficos.

Ate aqui, voce ja aprendeu a trabalhar com Python, arquivos, pandas e APIs. Agora voce vai dar um passo essencial para analise de dados: comunicar informacoes de forma visual.

Um grafico bom ajuda uma pessoa a entender rapidamente algo que seria dificil enxergar olhando apenas para uma tabela.

## Estrutura do modulo

```text
11-plots/
  README.md
  dados/
    vendas_mensais.csv
    vendas_detalhadas.csv
  exemplos/
    01_grafico_linha.py
    02_grafico_barras.py
    03_grafico_pizza.py
    04_pandas_plot.py
  exercicios/
    exercicios.md
    gabaritos/
      gabaritos.md
      gabaritos.py
  projeto/
    README.md
    relatorio_visual_vendas.py
```

## 1. Introducao

### O que e visualizacao de dados?

Visualizacao de dados e o uso de graficos para entender, comparar e comunicar informacoes.

Em vez de olhar apenas para uma tabela assim:

| mes | faturamento |
|---|---:|
| Jan | 18500 |
| Fev | 21300 |
| Mar | 19800 |
| Abr | 24600 |

Podemos criar um grafico de linha e perceber rapidamente se as vendas estao subindo ou caindo.

### Por que graficos sao importantes?

Graficos ajudam a responder perguntas como:

- o faturamento cresceu ao longo dos meses?
- qual produto vende mais?
- qual categoria representa a maior parte da receita?
- qual vendedor tem melhor desempenho?
- existe algum mes com queda preocupante?

No mundo real, gestores, analistas e equipes de negocio usam graficos para tomar decisoes.

### Exemplo real

Imagine uma empresa analisando vendas.

Ela tem uma planilha com centenas de linhas. Olhar linha por linha seria lento. Com graficos, a empresa consegue ver:

- evolucao mensal do faturamento;
- produtos mais vendidos;
- categorias com maior participacao;
- comparacao entre vendedores.

Esse e o papel da visualizacao: transformar dados em entendimento.

## 2. Biblioteca de graficos

Neste modulo vamos usar principalmente `matplotlib`.

`matplotlib` e uma das bibliotecas mais tradicionais de graficos em Python. Ela e muito usada em analise de dados, relatorios, estudos e projetos com pandas.

### Instalacao

```bash
pip install matplotlib pandas
```

### Importacao

```python
import matplotlib.pyplot as plt
```

`plt` e o apelido mais comum para `matplotlib.pyplot`.

### Estrutura basica

```python
import matplotlib.pyplot as plt

meses = ["Jan", "Fev", "Mar"]
vendas = [18500, 21300, 19800]

plt.plot(meses, vendas)
plt.title("Vendas por mes")
plt.xlabel("Mes")
plt.ylabel("Faturamento")
plt.show()
```

Leia o codigo assim:

- `plt.plot()` cria o grafico;
- `plt.title()` adiciona titulo;
- `plt.xlabel()` nomeia o eixo horizontal;
- `plt.ylabel()` nomeia o eixo vertical;
- `plt.show()` exibe o grafico.

## 3. Grafico de linha

Grafico de linha e usado para mostrar evolucao no tempo.

Use quando voce tiver:

- vendas por mes;
- acessos por dia;
- faturamento por semana;
- temperatura ao longo do tempo;
- quantidade de pedidos por periodo.

Exemplo:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/vendas_mensais.csv")

plt.plot(df["mes"], df["faturamento"], marker="o")
plt.title("Evolucao do faturamento mensal")
plt.xlabel("Mes")
plt.ylabel("Faturamento (R$)")
plt.grid(True)
plt.show()
```

### Por que linha?

Porque existe uma ordem natural: Janeiro vem antes de Fevereiro, Fevereiro antes de Marco, e assim por diante.

O grafico de linha ajuda a enxergar tendencia.

## 4. Grafico de barras

Grafico de barras e usado para comparar categorias.

Use quando voce quiser comparar:

- vendas por produto;
- faturamento por vendedor;
- quantidade por categoria;
- clientes por cidade.

Exemplo:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/vendas_detalhadas.csv")

vendas_por_produto = (
    df.groupby("produto")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

plt.bar(vendas_por_produto.index, vendas_por_produto.values)
plt.title("Faturamento por produto")
plt.xlabel("Produto")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
```

### Por que barras?

Porque produtos sao categorias. Nao existe uma linha do tempo entre `Notebook`, `Mouse` e `Monitor`. Queremos comparar tamanhos.

## 5. Grafico de pizza

Grafico de pizza mostra proporcao, ou seja, partes de um todo.

Use com cuidado. Ele funciona melhor quando existem poucas categorias.

Bom uso:

- participacao de 3 ou 4 categorias no faturamento;
- divisao simples entre formas de pagamento;
- percentual de vendas por canal.

Exemplo:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/vendas_detalhadas.csv")

faturamento_categoria = df.groupby("categoria")["valor_total"].sum()

plt.pie(
    faturamento_categoria.values,
    labels=faturamento_categoria.index,
    autopct="%1.1f%%",
    startangle=90,
)
plt.title("Participacao por categoria")
plt.show()
```

### Quando evitar pizza?

Evite quando:

- houver muitas categorias;
- as fatias forem muito parecidas;
- voce precisar comparar valores com precisao.

Nesses casos, grafico de barras costuma ser melhor.

## 6. Customizacao

Customizar nao e enfeitar por enfeitar. O objetivo e tornar o grafico mais claro.

### Titulo

```python
plt.title("Faturamento mensal")
```

O titulo deve explicar o que o grafico mostra.

### Rotulos dos eixos

```python
plt.xlabel("Mes")
plt.ylabel("Faturamento (R$)")
```

Rotulos ajudam a pessoa a entender o significado dos valores.

### Cores

```python
plt.bar(produtos, valores, color="steelblue")
```

Use cores para facilitar leitura, nao para poluir.

### Grade

```python
plt.grid(True, axis="y", alpha=0.3)
```

Grade leve ajuda a comparar valores.

### Rotacao dos textos

```python
plt.xticks(rotation=45, ha="right")
```

Isso evita que nomes longos fiquem sobrepostos.

### Layout

```python
plt.tight_layout()
```

Ajuda a ajustar espacos para que titulos e rotulos nao sejam cortados.

### Salvando grafico

```python
plt.savefig("grafico.png", dpi=120)
```

Salvar graficos e util para relatorios, apresentações e dashboards simples.

## 7. Integracao com pandas

Pandas tambem consegue gerar graficos diretamente a partir de DataFrames e Series.

Exemplo:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/vendas_detalhadas.csv")

vendas_por_vendedor = df.groupby("vendedor")["valor_total"].sum()

vendas_por_vendedor.plot(kind="bar", color="seagreen")

plt.title("Faturamento por vendedor")
plt.xlabel("Vendedor")
plt.ylabel("Faturamento (R$)")
plt.tight_layout()
plt.show()
```

Esse recurso e pratico porque voce usa o resultado do pandas direto no grafico.

Tipos comuns:

| Tipo | Codigo | Uso |
|---|---|---|
| Linha | `kind="line"` | Evolucao no tempo |
| Barras | `kind="bar"` | Comparar categorias |
| Barras horizontais | `kind="barh"` | Categorias com nomes longos |
| Pizza | `kind="pie"` | Proporcao |
| Histograma | `kind="hist"` | Distribuicao de valores |

## 8. Boas praticas

### Escolha o grafico correto

- Linha: evolucao no tempo.
- Barras: comparacao entre categorias.
- Pizza: proporcao simples.
- Histograma: distribuicao de valores.

### Use titulos claros

Ruim:

```text
Grafico 1
```

Melhor:

```text
Faturamento mensal em 2026
```

### Evite excesso de informacao

Um grafico com 40 barras pode ficar dificil de ler.

Prefira:

- top 5 produtos;
- top 10 cidades;
- agrupar categorias menores como "Outros";
- dividir em mais de um grafico.

### Ordene os dados

Em rankings, ordene do maior para o menor.

```python
ranking = vendas_por_produto.sort_values(ascending=False)
```

### Nao use pizza para tudo

Grafico de pizza parece simples, mas nem sempre e o melhor. Para comparar categorias, barras geralmente sao mais claras.

### Comece simples

Um grafico claro e simples vale mais do que um grafico bonito e confuso.

## 9. Erros comuns

### Usar grafico errado para o dado

Exemplo ruim: usar linha para comparar produtos.

Produtos nao sao sequencia temporal. Use barras.

### Excesso de categorias

Se o grafico tem muitos nomes no eixo X, ele fica ilegivel.

Solucoes:

- ordenar;
- mostrar top 10;
- usar barras horizontais;
- aumentar tamanho da figura.

### Esquecer `plt.show()`

Sem `plt.show()`, o grafico pode nao aparecer em alguns ambientes.

### Esquecer `plt.tight_layout()`

Sem `tight_layout()`, textos podem ficar cortados.

### Nao agrupar os dados antes

Se cada linha da tabela for uma venda, voce precisa agrupar antes de comparar produtos.

```python
df.groupby("produto")["valor_total"].sum()
```

## 10. Mini desafios

Use os arquivos em `dados/`.

### Mini desafio 1

Crie um grafico de linha com o faturamento mensal.

### Mini desafio 2

Crie um grafico de barras com faturamento por produto.

### Mini desafio 3

Crie um grafico de pizza com participacao por categoria.

### Mini desafio 4

Crie um grafico de barras com faturamento por vendedor.

### Mini desafio 5

Mostre apenas os 5 produtos com maior faturamento.

### Mini desafio 6

Salve um grafico em arquivo PNG.

### Mini desafio 7

Use pandas `.plot()` para criar um grafico de barras por forma de pagamento.

## 11. Resumo

Neste modulo voce aprendeu que:

- visualizacao de dados transforma tabelas em entendimento;
- graficos ajudam na tomada de decisao;
- `matplotlib` e uma biblioteca muito usada para graficos em Python;
- grafico de linha mostra evolucao no tempo;
- grafico de barras compara categorias;
- grafico de pizza mostra proporcao, mas deve ser usado com cuidado;
- titulos, rotulos, cores e layout melhoram a leitura;
- pandas se integra bem com matplotlib;
- bons graficos sao simples, claros e escolhidos de acordo com a pergunta.

Ao final deste modulo, voce ja consegue criar graficos uteis para relatorios de vendas, dashboards simples e analises de desempenho.
