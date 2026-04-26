import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
CAMINHO_CLIENTES = BASE_DIR / "dados" / "clientes.csv"

with open(CAMINHO_CLIENTES, "r", encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)

    for cliente in leitor:
        print(f"{cliente['nome']} - {cliente['cidade']} - ativo: {cliente['ativo']}")
