import fitz  # PyMuPDF
import re
import pandas as pd

dados = []

for i in range(1, 33):
    try:
        arquivo = f"atas/ata{i}.pdf"
        doc = fitz.open(arquivo)
        texto = ""
        for pagina in doc:
            texto += pagina.get_text()

        # Extrair número da proposição
        proposicao = re.search(r'\d{3}\.\d{5}\.\d{4}', texto)
        numero = proposicao.group(0) if proposicao else "Não encontrado"

        # Exemplo de extração de data da ata no texto
        data_match = re.search(r'\d{2}/\d{2}/\d{4}', texto)
        data = data_match.group(0) if data_match else "Não encontrada"

        dados.append({
            "arquivo": f"ata{i}.pdf",
            "data": data,
            "numero_proposicao": numero
        })

    except Exception as e:
        print(f"Erro ao processar ata{i}.pdf: {e}")

# Salvar no CSV
df = pd.DataFrame(dados)
df.to_csv("resumo_atas.csv", index=False)