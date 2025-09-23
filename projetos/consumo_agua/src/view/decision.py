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
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print("MSE:", mse)
        print("R²:", r2)
        resultados_df = pd.DataFrame([{
            "Modelo": "Regressão Linear",
            "MSE": mse,
            "R2": r2
        }])
        resultados_df.to_csv("./data/processed/decision_results.csv", index=False)
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
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print("MSE:", mse)
        print("R²:", r2)
        resultados_df = pd.DataFrame([{
            "Modelo": "Árvore de Decisão",
            "MSE": mse,
            "R2": r2
        }])
        resultados_df.to_csv("./data/processed/decision_results.csv", index=False)
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
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print("MSE:", mse)
        print("R²:", r2)
        resultados_df = pd.DataFrame([{
            "Modelo": "Random Forest",
            "MSE": mse,
            "R2": r2
        }])
        resultados_df.to_csv("./data/processed/decision_results.csv", index=False)
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

        resultados = []
        for name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            print(f"\n{name}")
            print("MSE:", mse)
            print("R²:", r2)
            resultados.append({"Modelo": name, "MSE": mse, "R2": r2})
        pd.DataFrame(resultados).to_csv("./data/processed/decision_results.csv", index=False)
    except Exception as e:
        print(f"Erro ao comparar modelos: {e}")


def predict_all(classe, regiao):
    try:
        df = pd.read_csv("./data/file_0.csv")

        # Features e target
        X = pd.get_dummies(df[["Classe", "Regiao"]], drop_first=True)
        y = df["Consumo"]

        # Treinar todos os modelos com o dataset completo
        models = {
            "Regressão Linear": LinearRegression(),
            "Árvore de Decisão": DecisionTreeRegressor(max_depth=5, random_state=42),
            "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
        }

        for model in models.values():
            model.fit(X, y)

        # Novo registro
        novo_dado = pd.DataFrame([{"Classe": classe, "Regiao": regiao}])
        novo_dado_encoded = pd.get_dummies(novo_dado)
        novo_dado_encoded = novo_dado_encoded.reindex(columns=X.columns, fill_value=0)

        # Previsões
        rows = []
        for name, model in models.items():
            previsao = float(model.predict(novo_dado_encoded)[0])
            rows.append({
                "Classe": classe,
                "Regiao": regiao,
                "Modelo": name,
                "Previsao": previsao
            })

        resultados_df = pd.DataFrame(rows, columns=["Classe", "Regiao", "Modelo", "Previsao"])
        resultados_df.to_csv("./data/processed/predictions.csv", index=False)

        resultados = {row["Modelo"]: row["Previsao"] for row in rows}
        return resultados
    except Exception as e:
        print(f"Erro ao prever com os 3 modelos: {e}")
        return None



