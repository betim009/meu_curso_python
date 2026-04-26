import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DADOS_DIR = BASE_DIR / "dados"


def carregar_vendas():
    vendas = []

    with open(DADOS_DIR / "vendas.csv", "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)

        for venda in leitor:
            vendas.append(venda)

    return vendas


def exercicio_6():
    """Calcula o total vendido."""
    total = 0

    for venda in carregar_vendas():
        quantidade = int(venda["quantidade"])
        preco_unitario = float(venda["preco_unitario"])
        total += quantidade * preco_unitario

    print(f"Total vendido: R$ {total:.2f}")


def exercicio_7():
    """Calcula a media por pedido."""
    vendas = carregar_vendas()
    total = 0

    for venda in vendas:
        quantidade = int(venda["quantidade"])
        preco_unitario = float(venda["preco_unitario"])
        total += quantidade * preco_unitario

    media = total / len(vendas)
    print(f"Media por pedido: R$ {media:.2f}")


def exercicio_8():
    """Gera um CSV apenas com produtos de estoque baixo."""
    produtos_estoque_baixo = []

    with open(DADOS_DIR / "produtos.csv", "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)

        for produto in leitor:
            if int(produto["estoque"]) < 10:
                produtos_estoque_baixo.append(produto)

    colunas = ["sku", "nome", "categoria", "estoque", "preco"]

    with open(DADOS_DIR / "estoque_baixo.csv", "w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor.writeheader()
        escritor.writerows(produtos_estoque_baixo)

    print("Arquivo estoque_baixo.csv gerado.")


def exercicio_9():
    """Conta clientes por cidade."""
    clientes_por_cidade = {}

    with open(DADOS_DIR / "clientes.csv", "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)

        for cliente in leitor:
            cidade = cliente["cidade"]
            clientes_por_cidade[cidade] = clientes_por_cidade.get(cidade, 0) + 1

    for cidade, total in clientes_por_cidade.items():
        print(f"{cidade}: {total}")


def exercicio_10():
    """Gera um TXT com clientes ativos."""
    with open(DADOS_DIR / "clientes.csv", "r", encoding="utf-8", newline="") as entrada:
        leitor = csv.DictReader(entrada)

        with open(DADOS_DIR / "clientes_ativos.txt", "w", encoding="utf-8") as saida:
            for cliente in leitor:
                if cliente["ativo"] == "sim":
                    linha = f"{cliente['nome']} - {cliente['email']} - {cliente['cidade']}\n"
                    saida.write(linha)

    print("Arquivo clientes_ativos.txt gerado.")


if __name__ == "__main__":
    exercicio_6()
    exercicio_7()
    exercicio_8()
    exercicio_9()
    exercicio_10()
