from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PASTA_MODULO = Path(__file__).resolve().parents[1]
PASTA_DADOS = PASTA_MODULO / "dados"
PASTA_GRAFICOS = Path(__file__).resolve().parent / "graficos"


def carregar_dados():
    mensal = pd.read_csv(PASTA_DADOS / "vendas_mensais.csv")
    vendas = pd.read_csv(PASTA_DADOS / "vendas_detalhadas.csv")
    return mensal, vendas


def salvar_faturamento_mensal(mensal):
    plt.figure(figsize=(10, 5))
    plt.plot(mensal["mes"], mensal["faturamento"], marker="o", color="steelblue")
    plt.title("Evolucao do faturamento mensal")
    plt.xlabel("Mes")
    plt.ylabel("Faturamento (R$)")
    plt.grid(True, axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(PASTA_GRAFICOS / "01_faturamento_mensal.png", dpi=120)
    plt.close()


def salvar_top_produtos(vendas):
    top_produtos = (
        vendas.groupby("produto")["valor_total"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    plt.figure(figsize=(10, 5))
    plt.bar(top_produtos.index, top_produtos.values, color="seagreen")
    plt.title("Top 5 produtos por faturamento")
    plt.xlabel("Produto")
    plt.ylabel("Faturamento (R$)")
    plt.xticks(rotation=45, ha="right")
    plt.grid(True, axis="y", alpha=0.25)
    plt.tight_layout()
    plt.savefig(PASTA_GRAFICOS / "02_top_produtos.png", dpi=120)
    plt.close()


def salvar_participacao_categorias(vendas):
    categorias = (
        vendas.groupby("categoria")["valor_total"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 6))
    plt.pie(categorias.values, labels=categorias.index, autopct="%1.1f%%", startangle=90)
    plt.title("Participacao do faturamento por categoria")
    plt.tight_layout()
    plt.savefig(PASTA_GRAFICOS / "03_participacao_categorias.png", dpi=120)
    plt.close()


def salvar_faturamento_vendedores(vendas):
    vendedores = (
        vendas.groupby("vendedor")["valor_total"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 5))
    plt.bar(vendedores.index, vendedores.values, color="slateblue")
    plt.title("Faturamento por vendedor")
    plt.xlabel("Vendedor")
    plt.ylabel("Faturamento (R$)")
    plt.grid(True, axis="y", alpha=0.25)
    plt.tight_layout()
    plt.savefig(PASTA_GRAFICOS / "04_faturamento_vendedores.png", dpi=120)
    plt.close()


def salvar_dashboard(mensal, vendas):
    top_produtos = (
        vendas.groupby("produto")["valor_total"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )
    vendedores = vendas.groupby("vendedor")["valor_total"].sum().sort_values(ascending=False)
    categorias = vendas.groupby("categoria")["valor_total"].sum().sort_values(ascending=False)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    axes[0, 0].plot(mensal["mes"], mensal["faturamento"], marker="o", color="steelblue")
    axes[0, 0].set_title("Faturamento mensal")
    axes[0, 0].set_xlabel("Mes")
    axes[0, 0].set_ylabel("Faturamento (R$)")
    axes[0, 0].grid(True, axis="y", alpha=0.3)

    axes[0, 1].bar(top_produtos.index, top_produtos.values, color="seagreen")
    axes[0, 1].set_title("Top 5 produtos")
    axes[0, 1].set_ylabel("Faturamento (R$)")
    axes[0, 1].tick_params(axis="x", rotation=45)

    axes[1, 0].bar(vendedores.index, vendedores.values, color="slateblue")
    axes[1, 0].set_title("Faturamento por vendedor")
    axes[1, 0].set_ylabel("Faturamento (R$)")
    axes[1, 0].grid(True, axis="y", alpha=0.25)

    axes[1, 1].pie(categorias.values, labels=categorias.index, autopct="%1.1f%%", startangle=90)
    axes[1, 1].set_title("Participacao por categoria")

    fig.suptitle("Relatorio Visual de Vendas", fontsize=16)
    fig.tight_layout()
    fig.savefig(PASTA_GRAFICOS / "05_dashboard_vendas.png", dpi=120)
    plt.close(fig)


def mostrar_resumo(vendas):
    faturamento_total = vendas["valor_total"].sum()
    produto_lider = vendas.groupby("produto")["valor_total"].sum().idxmax()
    vendedor_lider = vendas.groupby("vendedor")["valor_total"].sum().idxmax()
    categoria_lider = vendas.groupby("categoria")["valor_total"].sum().idxmax()

    print("=== RESUMO DO RELATORIO ===")
    print(f"Faturamento total: R$ {faturamento_total:.2f}")
    print(f"Produto com maior faturamento: {produto_lider}")
    print(f"Vendedor com maior faturamento: {vendedor_lider}")
    print(f"Categoria com maior faturamento: {categoria_lider}")
    print(f"Graficos salvos em: {PASTA_GRAFICOS}")


def main():
    PASTA_GRAFICOS.mkdir(exist_ok=True)
    mensal, vendas = carregar_dados()

    salvar_faturamento_mensal(mensal)
    salvar_top_produtos(vendas)
    salvar_participacao_categorias(vendas)
    salvar_faturamento_vendedores(vendas)
    salvar_dashboard(mensal, vendas)
    mostrar_resumo(vendas)


if __name__ == "__main__":
    main()
