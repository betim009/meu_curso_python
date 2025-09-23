"""
Template Base para Modelos de Regressão
---------------------------------------
Este arquivo serve como guia para criar rapidamente modelos de previsão
em qualquer contexto (ex.: consumo, vendas, produção).
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Modelos disponíveis
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


# ======================
# CONFIGURAÇÕES INICIAIS
# ======================

# 1. Carregar os dados (substituir pelo dataset desejado)
df = pd.read_csv("./data/seu_arquivo.csv")

# 2. Definir as colunas explicativas (features) e alvo (target)
# Exemplo: ["Classe", "Regiao"] são as categorias e "Consumo" é o valor a prever
X = pd.get_dummies(df[["Classe", "Regiao"]], drop_first=True)
y = df["Consumo"]

# 3. Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =====================
# ESCOLHA DO MODELO
# =====================
# Descomente o modelo que deseja usar:

# modelo = LinearRegression()
# modelo = DecisionTreeRegressor(max_depth=5, random_state=42)
# modelo = RandomForestRegressor(n_estimators=100, random_state=42)

# 4. Treinar o modelo
modelo.fit(X_train, y_train)

# 5. Fazer previsões
y_pred = modelo.predict(X_test)

# 6. Avaliar o modelo
print("MSE:", mean_squared_error(y_test, y_pred))
print("R²:", r2_score(y_test, y_pred))


""""
    - Sobre alguns metodos:

    # max_depth (Árvore de Decisão e Random Forest)
	•	O que significa:
    É a profundidade máxima da árvore (quantos níveis de divisão ela pode ter).
	•	Uma árvore com profundidade muito alta → aprende demais os dados (overfitting).
	•	Uma árvore com profundidade baixa → pode não aprender o suficiente (underfitting).
	•	Valores possíveis:
	•	None (padrão): cresce até todas as folhas ficarem puras ou não houver mais divisões possíveis.
	•	Um número inteiro (ex.: 5, 10): limita a quantidade de níveis.


    # random_state
	•	O que significa:
    É a semente aleatória usada pelo algoritmo.
	•	Se você não definir, cada vez que rodar o modelo, pode dar resultados diferentes.
	•	Se definir (random_state=42 é muito usado como padrão), garante reprodutibilidade → sempre o mesmo resultado.
	•	Valores possíveis:
	•	None (padrão): cada execução gera resultados diferentes.
	•	Um número inteiro (ex.: 0, 42, 123): fixa a aleatoriedade.


    # n_estimators (Random Forest)
	•	O que significa:
    Número de árvores que serão criadas no Random Forest.
	•	Poucas árvores → rápido, mas pode não aprender bem.
	•	Muitas árvores → mais preciso, mas mais lento.
	•	Valores possíveis:
	•	Inteiro positivo (ex.: 10, 100, 500, 1000).
	•	100 é padrão.
	•	Em datasets maiores, 500 ou 1000 costuma dar resultados melhores.


    Resumindo:
	•	max_depth → controla a complexidade da árvore (inteiro ou None).
	•	random_state → fixa a aleatoriedade para resultados consistentes (inteiro ou None).
	•	n_estimators → número de árvores no Random Forest (inteiro positivo, padrão = 100).
"""