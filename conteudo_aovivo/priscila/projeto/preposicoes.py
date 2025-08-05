import re
import pandas as pd

dados = []

for i in range(1, 60):
    try:
        with open(f"Proposicao{i}.txt", "r", encoding="utf-8") as f:
            texto = f.read()

            # Buscar o número da proposição (ex: 501.00004.2024)
            num_match = re.search(r'PROPOSIÇÃO\s+N[º°]?\s+([0-9.]+)', texto, re.IGNORECASE)

            # Buscar a ementa (linha após "EMENTA")
            tema_match = re.search(r'EMENTA\s*\n(.+?)(?:\n\s*\n|$)', texto, re.DOTALL | re.IGNORECASE)
            if tema_match:
                ementa_completa = tema_match.group(1).replace('\n', ' ').strip()
                tema = ementa_completa.split('.')[0]
            else:
                tema = "Não encontrado"

            numero = num_match.group(1) if num_match else "Não encontrado"

            dados.append({
                "arquivo": f"Proposicao{i}.txt",
                "numero": numero,
                "tema": tema
            })

    except Exception as e:
        print(f"Erro ao processar Proposicao{i}.txt: {e}")

# Salvar em CSV
df = pd.DataFrame(dados)
df.to_csv("resumo_proposicoes.csv", index=False)