# 🌐 Flask com Jinja, CSS e Gráficos: Visual Dinâmico com Python

Este material ensina como:

- Criar páginas HTML com Flask
- Usar **Jinja** para exibir dados dinâmicos
- Aplicar **CSS** para estilizar
- Exibir gráficos gerados com `matplotlib`

---

## ❓ O que é o Jinja?

Jinja é a **linguagem de template do Flask**.  
Ela permite escrever código dinâmico dentro do HTML. É como se fosse um "tradutor" que mistura Python com HTML.  

### ✨ Por que usar Jinja?

- Porque HTML puro **não entende Python**
- Permite exibir listas, dicionários, valores e até condições e laços de repetição dentro da página
- Torna sua aplicação web **flexível e interativa**

### 🔥 Exemplo Jinja:
```html
<p>Olá {{ nome }}</p>  <!-- Mostra uma variável -->
<ul>
  {% for fruta in frutas %}
    <li>{{ fruta }}</li>
  {% endfor %}
</ul>
```

---

## 📁 Estrutura de Pastas

```
meu_projeto/
├── app.py                 # Código Python principal
├── static/
│   └── style.css          # Arquivo CSS
├── templates/
│   └── index.html         # Template HTML com Jinja
└── venv/                  # Ambiente virtual
```

---

## 🧱 1. Criando a aplicação Flask (`app.py`)

```python
from flask import Flask, render_template
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route("/")
def home():
    nome = "Alberto"
    frutas = ["Morango", "Maçã", "Banana"]
    precos = {"Morango": 2.5, "Maçã": 3.0, "Banana": 1.8}

    # Criando um gráfico com matplotlib
    plt.figure()
    plt.bar(precos.keys(), precos.values())
    plt.title("Preço das Frutas")
    plt.ylabel("Preço em R$")
    caminho = os.path.join("static", "grafico.png")
    plt.savefig(caminho)
    plt.close()

    # Enviando tudo para o HTML com render_template
    return render_template(
        "index.html",
        nome=nome,
        frutas=frutas,
        precos=precos,
        grafico=caminho
    )

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 🖼 2. HTML com Jinja (`templates/index.html`)

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8" />
    <title>Página com Jinja</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Olá, {{ nome }}!</h1>

    <h2>Lista de frutas:</h2>
    <ul>
        {% for fruta in frutas %}
            <li>{{ fruta }}</li>
        {% endfor %}
    </ul>

    <h2>Preços:</h2>
    <ul>
        {% for fruta, preco in precos.items() %}
            <li>{{ fruta }}: R$ {{ preco }}</li>
        {% endfor %}
    </ul>

    <h2>Gráfico:</h2>
    <img src="{{ url_for('static', filename='grafico.png') }}" alt="Gráfico de preços">
</body>
</html>
```

✅ Explicações:
- `{{ nome }}` → insere a variável `nome` enviada pelo Python
- `{% for fruta in frutas %}` → faz um laço de repetição
- `url_for()` → indica o caminho para arquivos da pasta `static/`

---

## 🎨 3. CSS básico (`static/style.css`)

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f5f5f5;
    padding: 30px;
}

h1 {
    color: #2c3e50;
}

ul {
    list-style-type: square;
}
```

---

## ✅ O que aprendemos

- Como **passar dados do Python para HTML**
- Como usar `Jinja` para criar templates com lógica (laços, variáveis, dicionários)
- Como aplicar **CSS** para estilizar
- Como gerar **gráficos com `matplotlib`** e exibir como imagem

---

## ⚠️ Cuidados

- Coloque todos os arquivos HTML em `templates/`
- Coloque CSS e imagens em `static/`
- Sempre use `url_for()` ao referenciar arquivos estáticos
- Sempre feche o gráfico com `plt.close()` após `savefig()`

---

## 💡 Dica para praticar

Tente adicionar:

- Um botão que atualiza os dados
- Um gráfico de pizza
- Títulos personalizados com base em uma rota dinâmica

Se quiser, posso continuar com exemplos avançados de formulários ou banco de dados com Flask. Deseja?