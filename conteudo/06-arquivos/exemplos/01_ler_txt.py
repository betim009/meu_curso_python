from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
CAMINHO_ARQUIVO = BASE_DIR / "dados" / "chamados.txt"

with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
