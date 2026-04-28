# Gabaritos Comentados - Visualizacao de Dados

## 1. Grafico de linha do faturamento mensal

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dados/vendas_mensais.csv")

plt.plot(df["mes"], df["faturamento"], marker="o")
plt.title("Faturamento mensal")
plt.xlabel("Mes")
plt.ylabel("Faturamento (R$)")
plt.tight_layout()
plt.show()
```

Explicacao: grafico de linha e adequado porque os meses formam uma sequencia no tempo.

## 2. Grafico de barras de pedidos por mes

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dados/vendas_mensais.csv")

plt.bar(df["mes"], df["pedidos"])
plt.title("Pedidos por mes")
plt.xlabel("Mes")
plt.ylabel("Pedidos")
plt.tight_layout()
plt.show()
```

Explicacao: barras funcionam bem para comparar valores por mes.

## 3. Grafico de barras por vendedor

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dados/vendas_detalhadas.csv")

faturamento_vendedor = df.groupby("vendedor")["valor_total"].sum()

plt.bar(faturamento_vendedor.index, faturamento_vendedor.values)
plt.title("Faturamento por vendedor")
plt.xlabel("Vendedor")
plt.ylabel("Faturamento (R$)")
plt.tight_layout()
plt.show()
```

Explicacao: primeiro agrupamos, depois criamos o grafico.

## 4. Grafico de pizza por forma de pagamento

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dados/vendas_detalhadas.csv")

pagamentos = df.groupby("forma_pagamento")["valor_total"].sum()

plt.pie(pagamentos.values, labels=pagamentos.index, autopct="%1.1f%%")
plt.title("Participacao por forma de pagamento")
plt.tight_layout()
plt.show()
```

Explicacao: pizza mostra proporcao dentro de um total.

## 5. Salvar um grafico

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dados/vendas_mensais.csv")

plt.plot(df["mes"], df["faturamento"], marker="o")
plt.title("Faturamento mensal")
plt.xlabel("Mes")
plt.ylabel("Faturamento (R$)")
plt.tight_layout()
plt.savefig("faturamento_mensal.png", dpi=120)
plt.show()
```

Explicacao: `savefig()` salva o grafico como imagem.

## 6. Top 5 produtos por faturamento

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dados/vendas_detalhadas.csv")

top_produtos = (
    df.groupby("produto")["valor_total"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

plt.bar(top_produtos.index, top_produtos.values)
plt.title("Top 5 produtos por faturamento")
plt.xlabel("Produto")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
```

Explicacao: usamos `head(5)` para evitar excesso de informacao.

## 7. Quantidade vendida por produto

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dados/vendas_detalhadas.csv")

quantidade_produto = (
    df.groupby("produto")["quantidade"]
    .sum()
    .sort_values()
)

plt.barh(quantidade_produto.index, quantidade_produto.values)
plt.title("Quantidade vendida por produto")
plt.xlabel("Quantidade")
plt.ylabel("Produto")
plt.tight_layout()
plt.show()
```

Explicacao: barras horizontais melhoram a leitura de nomes longos.

## 8. Evolucao do ticket medio

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dados/vendas_mensais.csv")

plt.plot(df["mes"], df["ticket_medio"], marker="o", color="seagreen")
plt.title("Evolucao do ticket medio")
plt.xlabel("Mes")
plt.ylabel("Ticket medio (R$)")
plt.grid(True, axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
```

Explicacao: linha mostra a evolucao do ticket medio ao longo dos meses.

## 9. Comparar faturamento e pedidos

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dados/vendas_mensais.csv")

plt.figure(figsize=(10, 7))

plt.subplot(2, 1, 1)
plt.plot(df["mes"], df["faturamento"], marker="o")
plt.title("Faturamento por mes")
plt.ylabel("Faturamento (R$)")

plt.subplot(2, 1, 2)
plt.bar(df["mes"], df["pedidos"])
plt.title("Pedidos por mes")
plt.xlabel("Mes")
plt.ylabel("Pedidos")

plt.tight_layout()
plt.show()
```

Explicacao: `subplot()` permite colocar mais de um grafico na mesma figura.

## 10. Grafico com pandas `.plot()`

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dados/vendas_detalhadas.csv")

faturamento_categoria = df.groupby("categoria")["valor_total"].sum()

faturamento_categoria.plot(kind="bar")
plt.title("Faturamento por categoria")
plt.xlabel("Categoria")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
```

Explicacao: pandas usa matplotlib por baixo e facilita a criacao do grafico.

## 11. Dashboard simples em uma figura

```python
import pandas as pd
import matplotlib.pyplot as plt

mensal = pd.read_csv("../dados/vendas_mensais.csv")
vendas = pd.read_csv("../dados/vendas_detalhadas.csv")

top_produtos = vendas.groupby("produto")["valor_total"].sum().sort_values(ascending=False).head(5)
vendedores = vendas.groupby("vendedor")["valor_total"].sum().sort_values(ascending=False)
categorias = vendas.groupby("categoria")["valor_total"].sum().sort_values(ascending=False)

plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
plt.plot(mensal["mes"], mensal["faturamento"], marker="o")
plt.title("Faturamento mensal")

plt.subplot(2, 2, 2)
plt.bar(top_produtos.index, top_produtos.values)
plt.title("Top 5 produtos")
plt.xticks(rotation=45, ha="right")

plt.subplot(2, 2, 3)
plt.bar(vendedores.index, vendedores.values)
plt.title("Faturamento por vendedor")

plt.subplot(2, 2, 4)
plt.pie(categorias.values, labels=categorias.index, autopct="%1.1f%%")
plt.title("Participacao por categoria")

plt.tight_layout()
plt.show()
```

Explicacao: esse formato simula um dashboard simples de empresa.

## 12. Comparacao de categorias por mes

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dados/vendas_detalhadas.csv")

tabela = df.pivot_table(
    index="mes",
    columns="categoria",
    values="valor_total",
    aggfunc="sum",
    fill_value=0,
)

tabela.plot(kind="bar", figsize=(12, 6))
plt.title("Faturamento por categoria e mes")
plt.xlabel("Mes")
plt.ylabel("Faturamento (R$)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
```

Explicacao: `pivot_table()` organiza os dados para comparar categorias ao longo dos meses.

## 13. Relatorio visual salvo em arquivos

```python
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


PASTA_SAIDA = Path("graficos")
PASTA_SAIDA.mkdir(exist_ok=True)


def salvar_faturamento_mensal():
    df = pd.read_csv("../dados/vendas_mensais.csv")
    plt.figure(figsize=(9, 5))
    plt.plot(df["mes"], df["faturamento"], marker="o")
    plt.title("Faturamento mensal")
    plt.tight_layout()
    plt.savefig(PASTA_SAIDA / "faturamento_mensal.png", dpi=120)
    plt.close()


def salvar_top_produtos():
    df = pd.read_csv("../dados/vendas_detalhadas.csv")
    top = df.groupby("produto")["valor_total"].sum().sort_values(ascending=False).head(5)
    plt.figure(figsize=(10, 5))
    plt.bar(top.index, top.values)
    plt.title("Top produtos")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(PASTA_SAIDA / "top_produtos.png", dpi=120)
    plt.close()


def salvar_categorias():
    df = pd.read_csv("../dados/vendas_detalhadas.csv")
    categorias = df.groupby("categoria")["valor_total"].sum()
    plt.figure(figsize=(8, 6))
    plt.pie(categorias.values, labels=categorias.index, autopct="%1.1f%%")
    plt.title("Categorias")
    plt.tight_layout()
    plt.savefig(PASTA_SAIDA / "categorias.png", dpi=120)
    plt.close()


salvar_faturamento_mensal()
salvar_top_produtos()
salvar_categorias()
```

Explicacao: separar em funcoes deixa o projeto mais organizado e facil de manter.
