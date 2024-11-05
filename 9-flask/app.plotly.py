from flask import Flask, render_template
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)


@app.route("/")
def home():
    # Cria o gráfico com Plotly
    x = ["A", "B", "C", "D"]
    y = [10, 20, 30, 40]
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(
        title="Gráfico Simples com Plotly", xaxis_title="Eixo X", yaxis_title="Eixo Y"
    )

    # Converte o gráfico para HTML
    graph_html = pio.to_html(fig, full_html=False)

    # Passa o HTML do gráfico para o template
    return render_template("plot3.html", graph_html=graph_html)


if __name__ == "__main__":
    app.run(debug=True)
