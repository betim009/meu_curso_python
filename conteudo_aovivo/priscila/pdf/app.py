import fitz  # PyMuPDF

caminho_pdf = "relatorio.pdf"

# Abrir o PDF
doc = fitz.open(caminho_pdf)

# Iterar por cada página e imprimir o texto
for i, pagina in enumerate(doc):
    texto = pagina.get_text()
    print(f"\n--- Página {i+1} ---\n")
    print(texto)
