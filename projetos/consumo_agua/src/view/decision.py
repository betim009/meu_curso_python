import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


def train_linear():
    try:
        df = pd.read_csv("./data/file_0.csv")

        X = pd.get_dummies(df[["Classe", "Regiao"]], drop_first=True)
        y = df["Consumo"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        print("Regressão Linear")
        print("MSE:", mean_squared_error(y_test, y_pred))
        print("R²:", r2_score(y_test, y_pred))
    except Exception as e:
        print(f"Erro ao treinar Regressão Linear: {e}")


def train_decision_tree():
    try:
        df = pd.read_csv("./data/file_0.csv")

        X = pd.get_dummies(df[["Classe", "Regiao"]], drop_first=True)
        y = df["Consumo"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = DecisionTreeRegressor(max_depth=5, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        print("Árvore de Decisão")
        print("MSE:", mean_squared_error(y_test, y_pred))
        print("R²:", r2_score(y_test, y_pred))
    except Exception as e:
        print(f"Erro ao treinar Árvore de Decisão: {e}")


def train_random_forest():
    try:
        df = pd.read_csv("./data/file_0.csv")

        X = pd.get_dummies(df[["Classe", "Regiao"]], drop_first=True)
        y = df["Consumo"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        print("Random Forest")
        print("MSE:", mean_squared_error(y_test, y_pred))
        print("R²:", r2_score(y_test, y_pred))
    except Exception as e:
        print(f"Erro ao treinar Random Forest: {e}")


def compare_models():
    try:
        df = pd.read_csv("./data/file_0.csv")

        X = pd.get_dummies(df[["Classe", "Regiao"]], drop_first=True)
        y = df["Consumo"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        models = {
            "Regressão Linear": LinearRegression(),
            "Árvore de Decisão": DecisionTreeRegressor(max_depth=5, random_state=42),
            "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
        }

        for name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            print(f"\n{name}")
            print("MSE:", mean_squared_error(y_test, y_pred))
            print("R²:", r2_score(y_test, y_pred))
    except Exception as e:
        print(f"Erro ao comparar modelos: {e}")



train_linear()
train_decision_tree()
train_random_forest()

compare_models()