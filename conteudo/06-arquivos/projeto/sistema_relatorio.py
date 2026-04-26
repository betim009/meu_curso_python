import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CAMINHO_VENDAS = BASE_DIR / "vendas.csv"
CAMINHO_RELATORIO = BASE_DIR / "relatorio_vendas.txt"


def gerar_relatorio():
    total_vendido = 0
    total_pedidos = 0
    total_itens = 0
    maior_venda = 0
    cliente_maior_venda = ""
    produto_maior_venda = ""
    vendas_por_cliente = {}

    with open(CAMINHO_VENDAS, "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)

        for venda in leitor:
            cliente = venda["cliente"]
            produto = venda["produto"]
            quantidade = int(venda["quantidade"])
            preco_unitario = float(venda["preco_unitario"])
            subtotal = quantidade * preco_unitario

            total_vendido += subtotal
            total_pedidos += 1
            total_itens += quantidade

            vendas_por_cliente[cliente] = vendas_por_cliente.get(cliente, 0) + subtotal

            if subtotal > maior_venda:
                maior_venda = subtotal
                cliente_maior_venda = cliente
                produto_maior_venda = produto

    media_por_pedido = total_vendido / total_pedidos

    with open(CAMINHO_RELATORIO, "w", encoding="utf-8") as arquivo:
        arquivo.write("Relatorio de vendas\n")
        arquivo.write("===================\n")
        arquivo.write(f"Total de pedidos: {total_pedidos}\n")
        arquivo.write(f"Total de itens vendidos: {total_itens}\n")
        arquivo.write(f"Total vendido: R$ {total_vendido:.2f}\n")
        arquivo.write(f"Media por pedido: R$ {media_por_pedido:.2f}\n")
        arquivo.write(f"Maior venda: R$ {maior_venda:.2f}\n")
        arquivo.write(f"Cliente da maior venda: {cliente_maior_venda}\n")
        arquivo.write(f"Produto da maior venda: {produto_maior_venda}\n")
        arquivo.write("\nVendas por cliente:\n")

        for cliente, total in vendas_por_cliente.items():
            arquivo.write(f"- {cliente}: R$ {total:.2f}\n")

    print(f"Relatorio gerado em: {CAMINHO_RELATORIO}")


if __name__ == "__main__":
    gerar_relatorio()
