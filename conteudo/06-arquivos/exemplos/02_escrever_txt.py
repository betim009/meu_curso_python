from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
CAMINHO_RELATORIO = BASE_DIR / "dados" / "relatorio_simples.txt"

linhas = [
    "Relatorio simples de atendimento",
    "Total de chamados analisados: 5",
    "Status: processamento concluido",
]

with open(CAMINHO_RELATORIO, "w", encoding="utf-8") as arquivo:
    for linha in linhas:
        arquivo.write(linha + "\n")

print(f"Arquivo gerado em: {CAMINHO_RELATORIO}")
