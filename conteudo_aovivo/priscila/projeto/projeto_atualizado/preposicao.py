import requests
import fitz  # PyMuPDF
import pandas as pd
import time

key = ""
url = (
    "https://generativelanguage.googleapis.com/"
    f"v1beta/models/gemini-2.0-flash:generateContent?key={key}"
)

lista_preposicoes = []
for i in range(1, 60):
    caminho_pdf = f"preposicoes/Proposicao{i}.pdf"
    try:
        doc = fitz.open(caminho_pdf)
        texto_pdf = ""
        for pagina in doc:
            texto_pdf += pagina.get_text()

        prompt = "Vou te enviar um texto abaixo, preciso extrair desse texto o numero de preposicao e o tema do texto(tema precisa ser bem objetivo). O numero da preposicao tem o seguinte padrao 'PROPOSIÇÃO  N° 501.00004.2024'. Sua resposta deve ter o seguinte padrao: Numero: valor - Tema: valor. Se nao conseguir encontrar o numero da preposicao, seguinte padrao: Numero: Não identificado - Tema: valor. Exemplo de resposta: Número: 501.00004.2024 - Tema: Prestação de Contas do Município de Curitiba (Exercício Financeiro de 2022). Outro exemplo: Número: Não identificado - Tema: Prestação de Contas do Município de Curitiba (Exercício Financeiro de 2022)" + f"\n${texto_pdf}"

        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        }
        resp = requests.post(url, json=payload)
        txt = str(resp.json()["candidates"][0]['content']['parts'][0]['text']).strip().replace('\n', ' ').replace('\r', '')
        split_txt = txt.split(" ", 4)
        print(split_txt)
        lista_preposicoes.append({
            "Arquivo": f"preposicao_{i}.pdf",
            "Numero": split_txt[1],
            "Tema": split_txt[4]
        })
        time.sleep(5)

    except Exception as e:
        print(f"Erro ao ler {caminho_pdf}: {e}")


# resp = requests.post(url, json=payload)
# print(resp.text)
pd.DataFrame(lista_preposicoes).to_csv("gemini_preposicao_3.csv", index=False)
# print(lista_preposicoes)
