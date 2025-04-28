from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    user_input = None  # Inicializa a variável que vai conter o dado do formulário

    if request.method == "POST":
        # Captura o dado enviado pelo formulário
        user_input = request.form.get("query")

    # Renderiza o template e passa o valor do input (ou None se for GET)
    return render_template("index.html", user_input=user_input)


if __name__ == "__main__":
    app.run(debug=True)
