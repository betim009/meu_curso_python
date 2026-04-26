import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DADOS_DIR = BASE_DIR / "dados"


def exercicio_11():
    """Gera vendas_por_cliente.csv com o total comprado por cliente."""
    totais_por_cliente = {}

    with open(DADOS_DIR / "vendas.csv", "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)

        for venda in leitor:
            cliente = venda["cliente"]
            quantidade = int(venda["quantidade"])
            preco_unitario = float(venda["preco_unitario"])
            subtotal = quantidade * preco_unitario

            totais_por_cliente[cliente] = totais_por_cliente.get(cliente, 0) + subtotal

    with open(DADOS_DIR / "vendas_por_cliente.csv", "w", encoding="utf-8", newline="") as arquivo:
        colunas = ["cliente", "total"]
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader()

        for cliente, total in totais_por_cliente.items():
            escritor.writerow({"cliente": cliente, "total": f"{total:.2f}"})

    print("Arquivo vendas_por_cliente.csv gerado.")


def exercicio_12():
    """Encontra o produto mais vendido em quantidade."""
    quantidades_por_produto = {}

    with open(DADOS_DIR / "vendas.csv", "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)

        for venda in leitor:
            produto = venda["produto"]
            quantidade = int(venda["quantidade"])
            quantidades_por_produto[produto] = quantidades_por_produto.get(produto, 0) + quantidade

    produto_mais_vendido = ""
    maior_quantidade = 0

    for produto, quantidade in quantidades_por_produto.items():
        if quantidade > maior_quantidade:
            produto_mais_vendido = produto
            maior_quantidade = quantidade

    print(f"Produto mais vendido: {produto_mais_vendido}")
    print(f"Quantidade vendida: {maior_quantidade}")


def exercicio_13():
    """Gera um relatorio completo de estoque."""
    produtos = []

    with open(DADOS_DIR / "produtos.csv", "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)

        for produto in leitor:
            produtos.append(produto)

    total_produtos = len(produtos)
    total_unidades = 0
    produto_menor_estoque = produtos[0]
    produto_maior_preco = produtos[0]
    estoque_baixo = []

    for produto in produtos:
        estoque = int(produto["estoque"])
        preco = float(produto["preco"])

        total_unidades += estoque

        if estoque < int(produto_menor_estoque["estoque"]):
            produto_menor_estoque = produto

        if preco > float(produto_maior_preco["preco"]):
            produto_maior_preco = produto

        if estoque < 10:
            estoque_baixo.append(produto)

    with open(DADOS_DIR / "relatorio_estoque.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Relatorio de estoque\n")
        arquivo.write("====================\n")
        arquivo.write(f"Produtos cadastrados: {total_produtos}\n")
        arquivo.write(f"Unidades em estoque: {total_unidades}\n")
        arquivo.write(f"Menor estoque: {produto_menor_estoque['nome']} ({produto_menor_estoque['estoque']})\n")
        arquivo.write(f"Maior preco: {produto_maior_preco['nome']} (R$ {float(produto_maior_preco['preco']):.2f})\n")
        arquivo.write("\nProdutos com estoque abaixo de 10:\n")

        for produto in estoque_baixo:
            arquivo.write(f"- {produto['nome']}: {produto['estoque']} unidades\n")

    print("Arquivo relatorio_estoque.txt gerado.")


if __name__ == "__main__":
    exercicio_11()
    exercicio_12()
    exercicio_13()
