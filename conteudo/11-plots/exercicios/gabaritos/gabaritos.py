from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PASTA_DADOS = Path(__file__).resolve().parents[2] / "dados"
PASTA_SAIDA = Path(__file__).resolve().parent / "graficos"


def exercicio_1():
    df = pd.read_csv(PASTA_DADOS / "vendas_mensais.csv")
    plt.plot(df["mes"], df["faturamento"], marker="o")
    plt.title("Faturamento mensal")
    plt.xlabel("Mes")
    plt.ylabel("Faturamento (R$)")
    plt.tight_layout()
    plt.show()


def exercicio_2():
    df = pd.read_csv(PASTA_DADOS / "vendas_mensais.csv")
    plt.bar(df["mes"], df["pedidos"])
    plt.title("Pedidos por mes")
    plt.xlabel("Mes")
    plt.ylabel("Pedidos")
    plt.tight_layout()
    plt.show()


def exercicio_3():
    df = pd.read_csv(PASTA_DADOS / "vendas_detalhadas.csv")
    faturamento_vendedor = df.groupby("vendedor")["valor_total"].sum()
    plt.bar(faturamento_vendedor.index, faturamento_vendedor.values)
    plt.title("Faturamento por vendedor")
    plt.xlabel("Vendedor")
    plt.ylabel("Faturamento (R$)")
    plt.tight_layout()
    plt.show()


def exercicio_4():
    df = pd.read_csv(PASTA_DADOS / "vendas_detalhadas.csv")
    pagamentos = df.groupby("forma_pagamento")["valor_total"].sum()
    plt.pie(pagamentos.values, labels=pagamentos.index, autopct="%1.1f%%")
    plt.title("Participacao por forma de pagamento")
    plt.tight_layout()
    plt.show()


def exercicio_5():
    df = pd.read_csv(PASTA_DADOS / "vendas_mensais.csv")
    PASTA_SAIDA.mkdir(exist_ok=True)
    plt.plot(df["mes"], df["faturamento"], marker="o")
    plt.title("Faturamento mensal")
    plt.xlabel("Mes")
    plt.ylabel("Faturamento (R$)")
    plt.tight_layout()
    plt.savefig(PASTA_SAIDA / "faturamento_mensal.png", dpi=120)
    plt.show()


def exercicio_6():
    df = pd.read_csv(PASTA_DADOS / "vendas_detalhadas.csv")
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


def exercicio_7():
    df = pd.read_csv(PASTA_DADOS / "vendas_detalhadas.csv")
    quantidade_produto = df.groupby("produto")["quantidade"].sum().sort_values()
    plt.barh(quantidade_produto.index, quantidade_produto.values)
    plt.title("Quantidade vendida por produto")
    plt.xlabel("Quantidade")
    plt.ylabel("Produto")
    plt.tight_layout()
    plt.show()


def exercicio_8():
    df = pd.read_csv(PASTA_DADOS / "vendas_mensais.csv")
    plt.plot(df["mes"], df["ticket_medio"], marker="o", color="seagreen")
    plt.title("Evolucao do ticket medio")
    plt.xlabel("Mes")
    plt.ylabel("Ticket medio (R$)")
    plt.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()


def exercicio_9():
    df = pd.read_csv(PASTA_DADOS / "vendas_mensais.csv")
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


def exercicio_10():
    df = pd.read_csv(PASTA_DADOS / "vendas_detalhadas.csv")
    faturamento_categoria = df.groupby("categoria")["valor_total"].sum()
    faturamento_categoria.plot(kind="bar")
    plt.title("Faturamento por categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Faturamento (R$)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


def exercicio_11():
    mensal = pd.read_csv(PASTA_DADOS / "vendas_mensais.csv")
    vendas = pd.read_csv(PASTA_DADOS / "vendas_detalhadas.csv")
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


def exercicio_12():
    df = pd.read_csv(PASTA_DADOS / "vendas_detalhadas.csv")
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


def exercicio_13():
    PASTA_SAIDA.mkdir(exist_ok=True)
    mensal = pd.read_csv(PASTA_DADOS / "vendas_mensais.csv")
    vendas = pd.read_csv(PASTA_DADOS / "vendas_detalhadas.csv")

    plt.figure(figsize=(9, 5))
    plt.plot(mensal["mes"], mensal["faturamento"], marker="o")
    plt.title("Faturamento mensal")
    plt.tight_layout()
    plt.savefig(PASTA_SAIDA / "faturamento_mensal.png", dpi=120)
    plt.close()

    top = vendas.groupby("produto")["valor_total"].sum().sort_values(ascending=False).head(5)
    plt.figure(figsize=(10, 5))
    plt.bar(top.index, top.values)
    plt.title("Top produtos")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(PASTA_SAIDA / "top_produtos.png", dpi=120)
    plt.close()

    categorias = vendas.groupby("categoria")["valor_total"].sum()
    plt.figure(figsize=(8, 6))
    plt.pie(categorias.values, labels=categorias.index, autopct="%1.1f%%")
    plt.title("Categorias")
    plt.tight_layout()
    plt.savefig(PASTA_SAIDA / "categorias.png", dpi=120)
    plt.close()


if __name__ == "__main__":
    exercicio_13()
