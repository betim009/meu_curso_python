from pathlib import Path

import pandas as pd
import requests


URL_PRODUTOS = "https://dummyjson.com/products?limit=100"
ARQUIVO_RELATORIO = Path(__file__).resolve().parent / "relatorio_produtos.csv"


def buscar_json(url):
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        return resposta.json()
    except requests.exceptions.RequestException as erro:
        print("Erro ao buscar dados da API:", erro)
        return None


def carregar_produtos():
    dados = buscar_json(URL_PRODUTOS)

    if dados is None:
        return pd.DataFrame()

    produtos = dados.get("products", [])
    return pd.DataFrame(produtos)


def preparar_dados(df):
    colunas = [
        "id",
        "title",
        "category",
        "price",
        "stock",
        "discountPercentage",
        "rating",
        "brand",
    ]

    df = df[colunas].copy()
    df["valor_potencial_estoque"] = df["price"] * df["stock"]

    return df


def mostrar_metricas_gerais(df):
    total_produtos = len(df)
    preco_medio = df["price"].mean()
    estoque_total = df["stock"].sum()
    valor_potencial = df["valor_potencial_estoque"].sum()

    produto_mais_caro = df.sort_values(by="price", ascending=False).iloc[0]
    produto_maior_desconto = df.sort_values(by="discountPercentage", ascending=False).iloc[0]

    print("=== METRICAS GERAIS ===")
    print("Total de produtos:", total_produtos)
    print(f"Preco medio: US$ {preco_medio:.2f}")
    print("Estoque total:", estoque_total)
    print(f"Valor potencial em estoque: US$ {valor_potencial:.2f}")
    print("Produto mais caro:", produto_mais_caro["title"])
    print("Produto com maior desconto:", produto_maior_desconto["title"])


def mostrar_relatorio_categoria(df):
    relatorio = df.groupby("category").agg(
        quantidade_produtos=("id", "count"),
        preco_medio=("price", "mean"),
        estoque_total=("stock", "sum"),
        valor_potencial=("valor_potencial_estoque", "sum"),
        avaliacao_media=("rating", "mean"),
    )

    relatorio = relatorio.sort_values(by="valor_potencial", ascending=False)

    print("\n=== RELATORIO POR CATEGORIA ===")
    print(relatorio)


def mostrar_produtos_estoque_baixo(df):
    estoque_baixo = df[df["stock"] < 20].sort_values(by="stock")

    print("\n=== PRODUTOS COM ESTOQUE BAIXO ===")

    if estoque_baixo.empty:
        print("Nenhum produto com estoque baixo.")
        return

    print(estoque_baixo[["title", "category", "price", "stock"]])


def salvar_relatorio_csv(df):
    df.to_csv(ARQUIVO_RELATORIO, index=False)
    print(f"\nRelatorio salvo em: {ARQUIVO_RELATORIO}")


def main():
    produtos = carregar_produtos()

    if produtos.empty:
        print("Nao foi possivel gerar o relatorio.")
        return

    produtos = preparar_dados(produtos)

    mostrar_metricas_gerais(produtos)
    mostrar_relatorio_categoria(produtos)
    mostrar_produtos_estoque_baixo(produtos)
    salvar_relatorio_csv(produtos)


if __name__ == "__main__":
    main()
