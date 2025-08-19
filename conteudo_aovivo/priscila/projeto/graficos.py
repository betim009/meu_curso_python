import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# 1) Carregar CSV (ajuste o nome/caminho se necessário)
# ============================================================
caminhos = [Path('atas_proposicoes.csv'), Path('atas_preposicoes.csv')]
df = None
for p in caminhos:
    if p.exists():
        df = pd.read_csv(p)
        break

if df is None:
    raise FileNotFoundError(
        "Não encontrei 'atas_proposicoes.csv' nem 'atas_preposicoes.csv' na pasta atual."
    )

# ============================================================
# 2) Limpeza e normalizações
# ============================================================
# Preencher decisões vazias
if 'decisao_inferida' in df.columns:
    df['decisao_inferida'] = df['decisao_inferida'].fillna('indefinida')
else:
    raise KeyError("Coluna 'decisao_inferida' não encontrada no CSV.")

# Extrair ano do final de numero_preposicao (ex.: 013.00003.2024 -> 2024)
if 'numero_preposicao' in df.columns:
    df['ano'] = df['numero_preposicao'].astype(str).str.extract(r'(\d{4})$')[0]
    df['ano'] = pd.to_numeric(df['ano'], errors='coerce').astype('Int64')
else:
    raise KeyError("Coluna 'numero_preposicao' não encontrada no CSV.")

# ============================================================
# 3) GRÁFICO 1: Barras - Decisão Inferida (contagem)
# ============================================================
contagem_decisoes = df['decisao_inferida'].value_counts().sort_index()

plt.figure()
contagem_decisoes.plot(kind='bar')
plt.title('Decisão Inferida - Contagem')
plt.xlabel('Decisão')
plt.ylabel('Quantidade')
plt.tight_layout()
plt.savefig('decisao_inferida_contagem.png', dpi=120)
plt.close()

print('Gerado: decisao_inferida_contagem.png')

# ============================================================
# 4) GRÁFICO 2: Pizza - Atas com proposições (2022, 2023, 2024)
#                (sem incluir atas sem ano)
# ============================================================
anos_interesse = [2022, 2023, 2024]
contagem_atas_por_ano = {}
for ano in anos_interesse:
    atas_no_ano = df.loc[df['ano'] == ano, 'arquivo'].dropna().unique()
    contagem_atas_por_ano[str(ano)] = len(atas_no_ano)

serie_pizza = pd.Series(contagem_atas_por_ano)

plt.figure()
# Um gráfico por figura (sem especificar cores). Mostrar percentuais para leitura rápida.
serie_pizza.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Atas com proposições por ano (2022–2024)')
plt.ylabel('')  # oculta rótulo do eixo y no pie
plt.axis('equal')  # deixa a pizza circular
plt.tight_layout()
plt.savefig('atas_por_ano_pizza.png', dpi=120)
plt.close()

print('Gerado: atas_por_ano_pizza.png')