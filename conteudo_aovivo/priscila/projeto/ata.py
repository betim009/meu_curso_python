import fitz  # PyMuPDF
import pandas as pd
import re
import os

def extract_horas(text: str) -> tuple:
    # Regex para horas no formato HH:MM ou escritas por extenso (exemplos simples)
    # Exemplos de horas escritas por extenso: "dez horas", "quinze horas e trinta minutos"
    # Para simplicidade, vamos capturar apenas HH:MM e "X horas" (onde X é número)
    padrao_horas = re.compile(
        r'(\b(?:[01]?\d|2[0-3]):[0-5]\d\b)|(\b(?:zero|um|dois|três|quatro|cinco|seis|sete|oito|nove|dez|onze|doze|treze|quatorze|catorze|quinze|dezesseis|dezessete|dezoito|dezenove|vinte|vinte e um|vinte e dois|vinte e três|vinte e quatro)\s+horas(?:\s+e\s+\d{1,2}\s+minutos)?)',
        re.IGNORECASE
    )
    # Encontrar todas as ocorrências
    horas_encontradas = [m.group() for m in padrao_horas.finditer(text)]
    if not horas_encontradas:
        return "", ""
    return horas_encontradas[0], horas_encontradas[-1]

def extract_decisao(text: str, numero: str) -> str:
    # Palavras-chave para decisão
    palavras_chave = [
        "aprovada",
        "devolução ao autor",
        "pedido de vista",
        "inclusão na pauta",
        "tramitação",
        "admissibilidade"
    ]
    # Buscar o número no texto e pegar contexto próximo (ex: 100 caracteres antes e depois)
    pos = text.find(numero)
    if pos == -1:
        return ""
    inicio = max(0, pos - 100)
    fim = pos + 100
    contexto = text[inicio:fim].lower()

    for palavra in palavras_chave:
        if palavra in contexto:
            return palavra
    return ""

def parse_proposicoes(text: str, filename: str, hora_inicio: str, hora_fim: str) -> list:
    proposicoes = []
    padrao = r"\d{3}\.\d{5}\.\d{4}"
    for numero in re.findall(padrao, text):
        decisao = extract_decisao(text, numero)
        proposicoes.append({
            "arquivo": filename,
            "numero_preposicao": numero,
            "decisao_inferida": decisao,
            "hora_inicio": hora_inicio,
            "hora_fim": hora_fim
        })
    return proposicoes

def main():
    pasta = "atas"
    props_rows = []

    arquivos_pdf = sorted(
        [f for f in os.listdir(pasta) if f.lower().endswith(".pdf")],
        key=lambda x: (int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else float('inf'), x)
    )

    for arquivo in arquivos_pdf:
        caminho = os.path.join(pasta, arquivo)
        with fitz.open(caminho) as pdf:
            texto = ""
            for pagina in pdf:
                texto += pagina.get_text()

        hora_inicio, hora_fim = extract_horas(texto)

        props_rows.extend(parse_proposicoes(texto, arquivo, hora_inicio, hora_fim))

    dfp = pd.DataFrame(props_rows, columns=[
        "arquivo", "numero_preposicao", "decisao_inferida", "hora_inicio", "hora_fim"
    ])
    dfp.to_csv("atas_proposicoes.csv", index=False)

if __name__ == "__main__":
    main()