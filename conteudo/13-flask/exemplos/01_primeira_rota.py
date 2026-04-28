from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"mensagem": "API Flask funcionando"})


@app.route("/status")
def status():
    return jsonify({"status": "online"})


if __name__ == "__main__":
    app.run(debug=True)
