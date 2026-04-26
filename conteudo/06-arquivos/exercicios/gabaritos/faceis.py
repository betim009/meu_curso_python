import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DADOS_DIR = BASE_DIR / "dados"


def exercicio_1():
    """Lista os nomes dos clientes."""
    with open(DADOS_DIR / "clientes.csv", "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)

        for cliente in leitor:
            print(cliente["nome"])


def exercicio_2():
    """Mostra nome e email dos clientes ativos."""
    with open(DADOS_DIR / "clientes.csv", "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)

        for cliente in leitor:
            if cliente["ativo"] == "sim":
                print(f"{cliente['nome']} - {cliente['email']}")


def exercicio_3():
    """Conta quantas linhas existem no arquivo de chamados."""
    total_linhas = 0

    with open(DADOS_DIR / "chamados.txt", "r", encoding="utf-8") as arquivo:
        for _linha in arquivo:
            total_linhas += 1

    print(f"Total de chamados: {total_linhas}")


def exercicio_4():
    """Cria um arquivo de boas-vindas."""
    linhas = [
        "Bem-vindo ao sistema.",
        "Seu cadastro foi recebido.",
        "Em breve entraremos em contato.",
    ]

    with open(DADOS_DIR / "boas_vindas.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            arquivo.write(linha + "\n")

    print("Arquivo boas_vindas.txt criado.")


def exercicio_5():
    """Lista produtos com suas quantidades em estoque."""
    with open(DADOS_DIR / "produtos.csv", "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)

        for produto in leitor:
            print(f"{produto['nome']} - estoque: {produto['estoque']}")


if __name__ == "__main__":
    exercicio_1()
    exercicio_2()
    exercicio_3()
    exercicio_4()
    exercicio_5()
