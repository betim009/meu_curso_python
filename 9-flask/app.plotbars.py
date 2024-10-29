from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def home():
    # Cria o gráfico
    plt.figure()
    x = ["A", "B", "C", "D"]
    y = [10, 20, 30, 40]  # Alterado para ter 4 elementos, como `x`
    plt.bar(x, y)
    plt.title("Gráfico Simples")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")

    # Salva o gráfico em um buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # Converte o gráfico para uma string base64
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()

    # Passa a imagem para o template HTML
    return render_template('plot2.html', image=image_base64)

if __name__ == '__main__':
    app.run(debug=True)
