import fitz  # PyMuPDF
import pandas as pd
import re
import os
import unicodedata
from typing import Optional


def normalize_text(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch)).lower()


ORDINAIS_DIAS = {
    "primeiro": 1,
    "segundo": 2,
    "terceiro": 3,
    "quarto": 4,
    "quinto": 5,
    "sexto": 6,
    "setimo": 7,
    "oitavo": 8,
    "nono": 9,
    "decimo": 10,
    "decimo primeiro": 11,
    "decimo segundo": 12,
    "decimo terceiro": 13,
    "decimo quarto": 14,
    "decimo quinto": 15,
    "decimo sexto": 16,
    "decimo setimo": 17,
    "decimo oitavo": 18,
    "decimo nono": 19,
    "vigesimo": 20,
    "vigesimo primeiro": 21,
    "vigesimo segundo": 22,
    "vigesimo terceiro": 23,
    "vigesimo quarto": 24,
    "vigesimo quinto": 25,
    "vigesimo sexto": 26,
    "vigesimo setimo": 27,
    "vigesimo oitavo": 28,
    "vigesimo nono": 29,
    "trigesimo": 30,
    "trigesimo primeiro": 31,
}

MESES = {
    "janeiro": 1,
    "fevereiro": 2,
    "marco": 3,
    "abril": 4,
    "maio": 5,
    "junho": 6,
    "julho": 7,
    "agosto": 8,
    "setembro": 9,
    "outubro": 10,
    "novembro": 11,
    "dezembro": 12,
}


def parse_portuguese_ordinal(frase: str) -> Optional[int]:
    chave = normalize_text(frase)
    return ORDINAIS_DIAS.get(chave)


def parse_portuguese_cardinal(frase: str) -> Optional[int]:
    tokens = [
        token
        for token in re.split(r"[\s\-]+", normalize_text(frase))
        if token and token not in {"e", "de", "do", "da", "dos", "das"}
    ]
    if not tokens:
        return None

    unidades = {
        "zero": 0,
        "um": 1,
        "uma": 1,
        "dois": 2,
        "duas": 2,
        "tres": 3,
        "quatro": 4,
        "cinco": 5,
        "seis": 6,
        "sete": 7,
        "oito": 8,
        "nove": 9,
        "dez": 10,
        "onze": 11,
        "doze": 12,
        "treze": 13,
        "catorze": 14,
        "quatorze": 14,
        "quinze": 15,
        "dezesseis": 16,
        "dezessete": 17,
        "dezoito": 18,
        "dezenove": 19,
    }
    dezenas = {
        "vinte": 20,
        "trinta": 30,
        "quarenta": 40,
        "cinquenta": 50,
        "sessenta": 60,
        "setenta": 70,
        "oitenta": 80,
        "noventa": 90,
    }
    centenas = {
        "cem": 100,
        "cento": 100,
        "duzentos": 200,
        "trezentos": 300,
        "quatrocentos": 400,
        "quinhentos": 500,
        "seiscentos": 600,
        "setecentos": 700,
        "oitocentos": 800,
        "novecentos": 900,
    }

    total = 0
    corrente = 0

    for token in tokens:
        if token in unidades:
            corrente += unidades[token]
        elif token in dezenas:
            corrente += dezenas[token]
        elif token in centenas:
            corrente += centenas[token]
        elif token == "mil":
            if corrente == 0:
                corrente = 1
            total += corrente * 1000
            corrente = 0
        elif token.isdigit():
            corrente += int(token)
        else:
            continue

    resultado = total + corrente
    return resultado if resultado > 0 else None


def extrair_data_ata(texto: str) -> str:
    texto_normalizado = normalize_text(texto)
    texto_linear = re.sub(r"\s+", " ", texto_normalizado)

    padroes = [
        re.compile(r"\bno\s+(?!dia\b)(.+?)\s+dia do mes de\s+([a-z]+)\s+de\s+([a-z\s]+?)(?:\.|,|$)", re.IGNORECASE),
        re.compile(r"\baos\s+(.+?)\s+dias do mes de\s+([a-z]+)\s+de\s+([a-z\s]+?)(?:\.|,|$)", re.IGNORECASE),
        re.compile(r"\bno\s+dia\s+(.+?)\s+de\s+([a-z]+)\s+de\s+([a-z\s]+?)(?:\.|,|$)", re.IGNORECASE),
    ]

    for padrao in padroes:
        match = padrao.search(texto_linear)
        if match:
            dia_texto, mes_texto, ano_texto = match.groups()

            dia_texto = dia_texto.strip()
            dia = parse_portuguese_ordinal(dia_texto) or parse_portuguese_cardinal(dia_texto)
            if dia is None:
                numero = re.search(r"\d{1,2}", dia_texto)
                dia = int(numero.group()) if numero else None

            mes = MESES.get(mes_texto.strip())

            ano = parse_portuguese_cardinal(ano_texto)
            if ano is None:
                numero_ano = re.search(r"\d{4}", ano_texto)
                ano = int(numero_ano.group()) if numero_ano else None

            if dia and mes and ano:
                return f"{dia:02d}/{mes:02d}/{ano}"

    return ""


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

def parse_proposicoes(text: str, filename: str, hora_inicio: str, hora_fim: str, data_ata: str) -> list:
    proposicoes = []
    padrao = r"\d{3}\.\d{5}\.\d{4}"
    for numero in re.findall(padrao, text):
        decisao = extract_decisao(text, numero)
        proposicoes.append({
            "arquivo": filename,
            "numero_preposicao": numero,
            "decisao_inferida": decisao,
            "hora_inicio": hora_inicio,
            "hora_fim": hora_fim,
            "data_ata": data_ata
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
        data_ata = extrair_data_ata(texto)

        props_rows.extend(parse_proposicoes(texto, arquivo, hora_inicio, hora_fim, data_ata))

    dfp = pd.DataFrame(props_rows, columns=[
        "arquivo", "numero_preposicao", "decisao_inferida", "hora_inicio", "hora_fim", "data_ata"
    ])
    dfp.to_csv("atas_proposicoes.csv", index=False)

if __name__ == "__main__":
    main()
