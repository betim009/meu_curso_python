# Documentação Técnica - Modelos de Previsão (Decision)

Este documento explica detalhadamente as funções implementadas no arquivo `decision.py`, assim como os conceitos estatísticos e de aprendizado de máquina utilizados para prever o consumo de água a partir das variáveis `Classe` e `Região`.

---

## 1. Objetivo
A análise descritiva (média, mediana, moda, dispersão) mostra como os dados se comportam **no presente**.  
Já os modelos de previsão têm como objetivo **estimar o consumo futuro** ou prever valores desconhecidos, ajudando no planejamento e tomada de decisão.

---

## 2. Funções implementadas

### `train_linear()`
- Modelo: **Regressão Linear**.
- Lógica: assume que há uma relação **linear** entre as variáveis `Classe`, `Região` e o `Consumo`.
- Uso: rápido e interpretável, mas limitado se os dados não seguem uma tendência linear.

---

### `train_decision_tree()`
- Modelo: **Árvore de Decisão**.
- Lógica: divide os dados em **regras hierárquicas**, criando ramos baseados em condições (ex.: "Se Região = Sul, vá para a esquerda; se Classe = Comercial, vá para a direita").
- Uso: capta relações **não lineares**. Melhor que a regressão linear em muitos casos, mas pode sofrer de *overfitting* (memorizar os dados).

---

### `train_random_forest()`
- Modelo: **Random Forest**.
- Lógica: constrói **várias árvores de decisão** e combina os resultados (média das previsões).
- Uso: mais robusto que uma árvore simples, reduz risco de *overfitting*, normalmente atinge melhor performance.

---

### `compare_models()`
- Executa os três modelos (Linear, Decision Tree e Random Forest).
- Imprime os resultados de **MSE** e **R²** para facilitar a comparação.
- Útil para escolher qual modelo se adapta melhor aos dados.

---

## 3. Métricas de avaliação

### 🔹 MSE (Mean Squared Error – Erro Quadrático Médio)
- Mede o erro médio entre valores previstos e reais.
- Fórmula:

\[
MSE = \frac{1}{n} \sum (y_i - \hat{y}_i)^2
\]

- Quanto **menor**, melhor.  
- Como os erros são elevados ao quadrado, valores muito distantes pesam mais.

---

### 🔹 R² (Coeficiente de Determinação)
- Mede **quanto da variação nos dados o modelo consegue explicar**.
- Fórmula:

\[
R^2 = 1 - \frac{\text{Soma dos erros do modelo}}{\text{Soma dos erros da média}}
\]

- Intervalo: de -∞ até 1.
  - 0 → modelo não explica nada.
  - 1 → previsão perfeita.
- Exemplo: `R² = 0.63` significa que **63% da variação do consumo** é explicada pelo modelo.

---

## 4. Interpretação dos resultados

- **Regressão Linear**  
  MSE alto, R² baixo (~0.45). Captura pouco da variação, porque os dados não seguem um padrão linear simples.

- **Árvore de Decisão**  
  MSE menor, R² melhor (~0.62). Captura padrões mais complexos, mas pode sobreajustar.

- **Random Forest**  
  Melhor desempenho até agora (R² ~0.63). Mais estável, combina várias árvores, reduzindo erros.

---

## 5. Por que usar modelos de previsão?

- Entender **tendências futuras de consumo**.
- **Planejar recursos** (infraestrutura, abastecimento).
- **Comparar cenários** (ex.: impacto de mudanças na Classe ou Região).
- **Descobrir variáveis mais relevantes** para o consumo.

---

## 6. Explicação detalhada do código

Nesta seção, explicamos linha por linha do arquivo `decision.py`, detalhando cada método, função e parâmetro utilizado.

---

### Importações de bibliotecas

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
```

- `pandas` → manipulação de dados em DataFrames.
- `train_test_split` → divide os dados em conjunto de treino e teste.
- `LinearRegression` → modelo de regressão linear.
- `DecisionTreeRegressor` → modelo baseado em árvore de decisão para regressão.
- `RandomForestRegressor` → modelo de floresta aleatória para regressão.
- `mean_squared_error` → calcula o MSE (erro quadrático médio).
- `r2_score` → calcula o R² (coeficiente de determinação).

---

### Estrutura geral das funções

Cada função segue a mesma lógica:
1. Carregar os dados (`pd.read_csv`).
2. Transformar variáveis categóricas (`pd.get_dummies`).
3. Definir variáveis explicativas (X) e variável alvo (y).
4. Dividir os dados em treino e teste (`train_test_split`).
5. Criar e treinar o modelo (`fit`).
6. Fazer previsões (`predict`).
7. Avaliar desempenho com métricas (MSE e R²).

---

### `train_linear()`

```python
df = pd.read_csv("./data/file_0.csv")
```
- Lê os dados do arquivo CSV.

```python
X = pd.get_dummies(df[["Classe", "Regiao"]], drop_first=True)
y = df["Consumo"]
```
- `X`: variáveis independentes (Classe e Região), transformadas em numéricas com `get_dummies` (One-Hot Encoding).  
- `drop_first=True`: evita multicolinearidade removendo uma categoria de referência.  
- `y`: variável dependente (Consumo).

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
- Divide os dados em treino (80%) e teste (20%).  
- `test_size=0.2`: define a proporção.  
- `random_state=42`: garante reprodutibilidade (sempre a mesma divisão).

```python
model = LinearRegression()
model.fit(X_train, y_train)
```
- Cria o modelo de regressão linear e treina com os dados de treino.  
- `fit`: ajusta os coeficientes do modelo.

```python
y_pred = model.predict(X_test)
```
- Faz previsões no conjunto de teste.

```python
print("MSE:", mean_squared_error(y_test, y_pred))
print("R²:", r2_score(y_test, y_pred))
```
- Calcula e exibe as métricas de avaliação.

---

### `train_decision_tree()`

```python
model = DecisionTreeRegressor(max_depth=5, random_state=42)
```
- Cria uma árvore de decisão com profundidade máxima = 5.  
- `max_depth`: limita a complexidade da árvore (evita overfitting).  
- `random_state=42`: garante consistência nos resultados.

---

### `train_random_forest()`

```python
model = RandomForestRegressor(n_estimators=100, random_state=42)
```
- Cria uma floresta com 100 árvores.  
- `n_estimators=100`: número de árvores usadas na média das previsões.  
- `random_state=42`: garante reprodutibilidade.

---

### `compare_models()`

```python
models = {
    "Regressão Linear": LinearRegression(),
    "Árvore de Decisão": DecisionTreeRegressor(max_depth=5, random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
}
```
- Define um dicionário com três modelos para comparação.  
- Itera sobre eles, treinando e testando cada um.  
- Exibe MSE e R² para facilitar a análise.

---

## Conclusão

O arquivo `decision.py` mostra três abordagens diferentes de previsão: linear, árvore de decisão e random forest. Cada modelo tem vantagens e limitações, e a escolha depende do equilíbrio entre **interpretação**, **performance** e **complexidade**.
