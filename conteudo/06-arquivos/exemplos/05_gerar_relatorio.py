import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
CAMINHO_VENDAS = BASE_DIR / "dados" / "vendas.csv"
CAMINHO_RELATORIO = BASE_DIR / "dados" / "relatorio_vendas.txt"

total_vendido = 0
total_pedidos = 0
maior_venda = 0
cliente_maior_venda = ""

with open(CAMINHO_VENDAS, "r", encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)

    for venda in leitor:
        quantidade = int(venda["quantidade"])
        preco_unitario = float(venda["preco_unitario"])
        subtotal = quantidade * preco_unitario

        total_vendido += subtotal
        total_pedidos += 1

        if subtotal > maior_venda:
            maior_venda = subtotal
            cliente_maior_venda = venda["cliente"]

media_por_pedido = total_vendido / total_pedidos

with open(CAMINHO_RELATORIO, "w", encoding="utf-8") as arquivo:
    arquivo.write("Relatorio de vendas\n")
    arquivo.write("===================\n")
    arquivo.write(f"Total de pedidos: {total_pedidos}\n")
    arquivo.write(f"Total vendido: R$ {total_vendido:.2f}\n")
    arquivo.write(f"Media por pedido: R$ {media_por_pedido:.2f}\n")
    arquivo.write(f"Maior venda: R$ {maior_venda:.2f}\n")
    arquivo.write(f"Cliente da maior venda: {cliente_maior_venda}\n")

print(f"Relatorio gerado em: {CAMINHO_RELATORIO}")
