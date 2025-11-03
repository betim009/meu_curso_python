import requests
import fitz  # PyMuPDF
import pandas as pd
import time

key = ""
url = (
    "https://generativelanguage.googleapis.com/"
    f"v1beta/models/gemini-2.0-flash:generateContent?key={key}"
)

lista_atas = []
for i in range(1, 33):
    caminho_pdf = f"atas/ata{i}.pdf"
    try:
        doc = fitz.open(caminho_pdf)
        texto_pdf = ""
        for pagina in doc:
            texto_pdf += pagina.get_text()
        print(texto_pdf)
        prompt = "Vou te enviar um texto abaixo sobre uma ata de reuniao de uma camara de vereadores, preciso extrair desse texto algumas informacoes: 'Titulo da ata', 'Data da Ata', 'Assunto da ata', 'Numero de todas preposicoes que encontrar'. Preciso de um padrao na sua resposta. Ele deve ser: Ata: Ata da vigésima primeira reunião ordinária da Comissão de Economia, Finanças e Fiscalização; Data: 11/dezembro/2024; Assunto: Apresentação da fase atual de trabalho e resultados pelos estagiários de pós-graduação do PPGEcon da UFPR, discussão e votação das proposições 013.00003.2024 e 013.00004.2024; Preposicoes: 013.00003.2024 e 013.00004.2024; Nao insira nada na sua resposta alem do exemplo informado."+f"\n${texto_pdf}"

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
        req = requests.post(url, json=payload)
        res = req.json()
        result = res["candidates"][0]["content"]["parts"][0]["text"].strip().replace('\n', ' ').replace('\r', '')
        
        partes = result.replace("**", "").split(";")
        resultado = {
            "arquivo": f"ata_{i}.pdf"
        }
        for parte in partes:
            if ":" in parte:
                chave, valor = parte.split(":", 1)
                resultado[chave.strip()] = valor.strip()
        lista_atas.append(resultado)
        time.sleep(5)

    except Exception as e:
        print(f"Erro ao ler {caminho_pdf}: {e}")

pd.DataFrame(lista_atas).to_csv("gemini_ata_3.csv", index=False)

print(lista_atas)