

# Desafio de Ciência de Dados — IMDB 🎬

Este projeto realiza análise exploratória de dados (EDA) e modelagem preditiva da nota **IMDB_Rating** a partir de um dataset de filmes.  

---

## 📂 Estrutura do Projeto

```
desafio/
├─ data/
│  ├─ raw/ (imdb.csv original)
│  └─ processed/ (CSVs gerados pelo app)
├─ models/ (model.pkl salvo)
├─ reports/ (prints de gráficos)
├─ src/ (app.py)
├─ resposta.txt (respostas formais)
├─ requirements.txt
└─ README.md
```

---

## ▶️ Como Rodar

```bash
# criar ambiente virtual
python -m venv .venv
source .venv/bin/activate   # (Windows: .venv\Scripts\activate)

# instalar dependências
pip install -r requirements.txt

# rodar a análise
python src/app.py
```

### Entrada esperada
- Arquivo `data/raw/imdb.csv` (dataset fornecido).  

---

## 📊 Saídas Geradas

- `data/processed/desafio_formatado.csv`
- `data/processed/top10_por_genero.csv`
- `data/processed/top20_gross_com_avaliacao.csv`
- `data/processed/recs_<genero>_top5.csv`
- `data/processed/recs_<genero>_score_top5.csv`
- `models/model.pkl` (pipeline Ridge salvo)

---

## ❓ Respostas ao Desafio

**(a) Recomendação de filme**  
Recomenda-se coletar o gênero de interesse da pessoa e indicar os filmes com melhores notas dentro desse gênero, considerando também o número de votos.  
Se não houver gênero definido, a recomendação é **The Dark Knight**, que combina alta nota com grande arrecadação.

**(b) Fatores ligados ao faturamento**  
- **No_of_Votes**: mais votos → maior bilheteria.  
- **IMDB_Rating**: filmes bem avaliados tendem a arrecadar mais.  
- **Meta_score**: influência adicional, mas menor que votos.  

O cruzamento `Gross × IMDB_Rating` permitiu identificar quatro grupos:
- Alta arrecadação + Alta nota → sucesso.
- Alta arrecadação + Baixa nota → hype/marketing.
- Baixa arrecadação + Alta nota → nicho.
- Baixa arrecadação + Baixa nota → flop.

**(c) Insight das Overview**  
As sinopses (`Overview`) foram processadas via **TF-IDF** e usadas como feature no modelo, enriquecendo a previsão de nota.  
Embora não tenha sido feita análise linguística detalhada, fica claro o potencial do texto como fonte complementar de informação.

---

## 📈 Métricas do Modelo (Ridge baseline)

- **MAE**: ~0.167  
- **RMSE**: ~0.208  
- **R²**: ~0.338  

Modelo salvo em: `models/model.pkl`

---

## 🖼️ Evidências (gráficos em reports/)

- Histograma das notas IMDB  
- Boxplot (outliers)  
- Quadrantes Gross × Nota  
- Heatmap de correlação  

---