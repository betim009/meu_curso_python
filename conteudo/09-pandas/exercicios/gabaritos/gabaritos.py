import pandas as pd
from pathlib import Path


PASTA_DADOS = Path(__file__).resolve().parents[2] / "dados"


def exercicio_1():
    df = pd.read_csv(PASTA_DADOS / "vendas.csv")
    print(df.head())
    print(df.shape)
    print(df.columns)


def exercicio_2():
    df = pd.read_csv(PASTA_DADOS / "vendas.csv")
    faturamento_total = df["valor_total"].sum()
    print(f"Faturamento total: R$ {faturamento_total:.2f}")


def exercicio_3():
    df = pd.read_csv(PASTA_DADOS / "vendas.csv")
    relatorio = df[["data", "cliente", "produto", "valor_total"]]
    print(relatorio.head(10))


def exercicio_4():
    df = pd.read_csv(PASTA_DADOS / "vendas.csv")
    vendas_sp = df[df["cidade"] == "Sao Paulo"]
    print(vendas_sp[["cliente", "produto", "valor_total"]])


def exercicio_5():
    df = pd.read_csv(PASTA_DADOS / "vendas.csv")
    ticket_medio = df["valor_total"].mean()
    print(f"Ticket medio: R$ {ticket_medio:.2f}")


def exercicio_6():
    df = pd.read_csv(PASTA_DADOS / "vendas.csv")
    maiores_vendas = df.sort_values(by="valor_total", ascending=False)
    print(maiores_vendas.head(5))


def exercicio_7():
    df = pd.read_csv(PASTA_DADOS / "vendas.csv")
    quantidade_por_produto = (
        df.groupby("produto")["quantidade"]
        .sum()
        .sort_values(ascending=False)
    )
    print(quantidade_por_produto)
    print("Produto mais vendido:", quantidade_por_produto.index[0])


def exercicio_8():
    df = pd.read_csv(PASTA_DADOS / "vendas.csv")
    faturamento_por_produto = (
        df.groupby("produto")["valor_total"]
        .sum()
        .sort_values(ascending=False)
    )
    print(faturamento_por_produto)


def exercicio_9():
    df = pd.read_csv(PASTA_DADOS / "vendas.csv")
    relatorio_vendedor = df.groupby("vendedor").agg(
        faturamento_total=("valor_total", "sum"),
        quantidade_vendas=("id_venda", "count"),
        ticket_medio=("valor_total", "mean"),
    )
    print(relatorio_vendedor.sort_values(by="faturamento_total", ascending=False))


def exercicio_10():
    df = pd.read_csv(PASTA_DADOS / "vendas.csv")
    vendas_altas = df[df["valor_total"] > 1000]
    print(vendas_altas)
    print("Quantidade:", vendas_altas["id_venda"].count())
    print(f"Faturamento: R$ {vendas_altas['valor_total'].sum():.2f}")


def exercicio_11():
    df = pd.read_csv(PASTA_DADOS / "vendas.csv")
    relatorio_cidade = df.groupby("cidade").agg(
        faturamento_total=("valor_total", "sum"),
        quantidade_vendas=("id_venda", "count"),
        media_por_venda=("valor_total", "mean"),
        maior_venda=("valor_total", "max"),
    )
    print(relatorio_cidade.sort_values(by="faturamento_total", ascending=False))


def exercicio_12():
    df = pd.read_csv(PASTA_DADOS / "vendas_com_problemas.csv")
    df = df.drop_duplicates()
    df = df.dropna(subset=["cliente", "produto", "preco_unitario"])
    df["desconto"] = df["desconto"].fillna(0)
    df["vendedor"] = df["vendedor"].fillna("Nao informado")
    df["data"] = pd.to_datetime(df["data"], errors="coerce")
    df = df[df["quantidade"] > 0]
    df["valor_total_recalculado"] = (df["preco_unitario"] * df["quantidade"]) - df["desconto"]
    print(df)


def exercicio_13():
    vendas = pd.read_csv(PASTA_DADOS / "vendas.csv")
    produtos = pd.read_csv(PASTA_DADOS / "produtos.csv")
    base = vendas.merge(produtos[["produto", "custo_unitario"]], on="produto", how="left")
    base["lucro_estimado"] = base["valor_total"] - (base["custo_unitario"] * base["quantidade"])
    relatorio_margem = base.groupby("produto").agg(
        faturamento=("valor_total", "sum"),
        lucro_estimado=("lucro_estimado", "sum"),
        unidades_vendidas=("quantidade", "sum"),
    )
    print(relatorio_margem.sort_values(by="lucro_estimado", ascending=False))


if __name__ == "__main__":
    exercicio_1()
