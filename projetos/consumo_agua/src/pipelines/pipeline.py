import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os


def train_model():
    df = pd.read_csv("./data/file_0.csv")

    X = pd.get_dummies(df[["Classe", "Regiao"]], drop_first=True)
    y = df["Consumo"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    pipeline = Pipeline(
        [("scaler", StandardScaler()), ("rf", RandomForestRegressor(random_state=42))]
    )

    param_grid = {"rf__n_estimators": [100, 200], "rf__max_depth": [5, 10, None]}
    grid = GridSearchCV(
        estimator=pipeline, param_grid=param_grid, cv=5, scoring="r2", n_jobs=-1
    )

    grid.fit(X_train, y_train)
    best_model = grid.best_estimator_
    return best_model, grid.best_params_, X_test, y_test


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2


def save_model(model, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    joblib.dump(model, path)
    print(f"Modelo salvo em {path}")


def load_model(path):
    return joblib.load(path)


def predict_consumo(classe, regiao, model_path):
    model = load_model(model_path)
    cols = pd.DataFrame([{"Classe": classe, "Regiao": regiao}])

    X = pd.get_dummies(pd.read_csv("./data/file_0.csv")[["Classe", "Regiao"]], drop_first=True)
    new_cols = pd.get_dummies(cols).reindex(columns=X.columns, fill_value=0)

    previsao = model.predict(new_cols)
    return previsao[0]


def run_pipeline():
    model, params, X_test, y_test = train_model()
    mse, r2 = evaluate_model(model, X_test, y_test)
    save_model(model)
    print("Melhores parâmetros:", params)
    print("MSE:", mse)
    print("R²:", r2)
    return model



# train_model() → treina e retorna modelo + parâmetros.
# evaluate_model() → calcula métricas.
# save_model() e load_model() → salvar/carregar modelo.
# predict_consumo() → só prevê usando modelo salvo.
# run_pipeline() → orquestra tudo: treina, avalia, salva e imprime métricas.

# Exemplos de uso:
# run_pipeline()
print(predict_consumo("Residencial", "Sul", "./models/residencial_sul.pkl"))
