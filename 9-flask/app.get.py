from flask import Flask, render_template

app = Flask(__name__)


resultados = [
    {"id": 1, "usuario": "Alberto"},
    {"id": 2, "usuario": "Alberto"},
    {"id": 3, "usuario": "Alberto"},
]


@app.route("/")
def home():
    return render_template("resultados.html", resultados=resultados)


if __name__ == "__main__":
    app.run(debug=True)
