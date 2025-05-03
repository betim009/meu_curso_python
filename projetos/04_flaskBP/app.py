from flask import Flask
from routes.contratos import contratos_bp  # importa o blueprint

app = Flask(__name__)

# Registrando o blueprint
app.register_blueprint(contratos_bp)


@app.route("/")
def home():
    return "API com rotas separadas funcionando!"


if __name__ == "__main__":
    app.run(debug=True)
