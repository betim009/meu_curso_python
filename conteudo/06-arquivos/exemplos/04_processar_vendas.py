import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
CAMINHO_VENDAS = BASE_DIR / "dados" / "vendas.csv"

total_vendido = 0
quantidade_itens = 0

with open(CAMINHO_VENDAS, "r", encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)

    for venda in leitor:
        quantidade = int(venda["quantidade"])
        preco_unitario = float(venda["preco_unitario"])
        subtotal = quantidade * preco_unitario

        total_vendido += subtotal
        quantidade_itens += quantidade

print(f"Total vendido: R$ {total_vendido:.2f}")
print(f"Quantidade de itens vendidos: {quantidade_itens}")
