from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def home():
    # Cria o gráfico
    plt.figure()
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.plot(x, y)
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
    return render_template('plot.html', image=image_base64)

if __name__ == '__main__':
    app.run(debug=True)
