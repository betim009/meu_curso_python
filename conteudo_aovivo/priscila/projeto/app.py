import fitz  # PyMuPDF

todos_os_textos = []

for i in range(1, 60):
    caminho_pdf = f"preposicoes/Proposicao{i}.pdf"
    try:
        doc = fitz.open(caminho_pdf)
        texto_pdf = ""
        for pagina in doc:
            texto_pdf += pagina.get_text()
        todos_os_textos.append(texto_pdf)
    except Exception as e:
        print(f"Erro ao ler {caminho_pdf}: {e}")

# Salvar cada texto em um arquivo separado
for i, texto in enumerate(todos_os_textos, start=1):
    with open(f"Proposicao{i}.txt", "w", encoding="utf-8") as f:
        f.write(texto)