# Introdução ao Flask

Flask é uma biblioteca Python usada para criar aplicações web.

Uma aplicação web é um programa que roda no computador ou servidor e pode ser acessado pelo navegador. Com Flask, conseguimos criar páginas, rotas, formulários e APIs simples usando Python.

---

## O que você vai aprender

- O que é uma rota.
- Como criar uma primeira aplicação Flask.
- Como retornar texto no navegador.
- Como renderizar uma página HTML.
- Como passar dados do Python para o HTML.
- Erros comuns ao começar com Flask.

---

## Explicação simples

Quando você acessa um site, o navegador faz uma requisição para um endereço.

No Flask, criamos funções que respondem a esses endereços.

Exemplo:

```python
@app.route("/")
def home():
    return "Ola, Flask!"
```

Isso significa:

- Quando o usuário acessar `/`
- Execute a função `home`
- Mostre o texto `"Ola, Flask!"`

---

## Instalando

Crie e ative um ambiente virtual fora do repositório ou dentro da sua máquina local:

```bash
python -m venv venv
source venv/bin/activate
```

No Windows:

```bash
venv\Scripts\activate
```

Instale o Flask:

```bash
pip install flask
```

---

## Exemplo comentado linha por linha

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Ola, Flask!"


if __name__ == "__main__":
    app.run(debug=True)
```

Explicando:

- `from flask import Flask` importa a classe principal do Flask.
- `app = Flask(__name__)` cria a aplicação.
- `@app.route("/")` define a rota principal do site.
- `def home():` cria a função que será executada nessa rota.
- `return "Ola, Flask!"` envia uma resposta para o navegador.
- `app.run(debug=True)` inicia o servidor local.

Para executar:

```bash
python app.py
```

Depois, acesse no navegador:

```text
http://127.0.0.1:5000
```

---

## Usando HTML

Em projetos reais, não queremos retornar apenas texto. Queremos mostrar páginas HTML.

Exemplo:

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
```

O arquivo `index.html` deve ficar dentro da pasta `templates`.

---

## Passando dados para o HTML

Também podemos enviar dados do Python para o HTML:

```python
resultados = [
    {"id": 1, "usuario": "Alberto"},
    {"id": 2, "usuario": "Maria"},
]


@app.route("/")
def home():
    return render_template("resultados.html", resultados=resultados)
```

Isso é útil para mostrar listas, tabelas, resultados de banco de dados e relatórios.

---

## Quando usar Flask?

Use Flask quando quiser:

- Criar uma API simples.
- Criar um site pequeno.
- Criar um formulário web.
- Mostrar dados em uma página.
- Entender como aplicações web funcionam por trás.

---

## Erros comuns

### 1. Esquecer de instalar o Flask

Se aparecer erro como:

```text
ModuleNotFoundError: No module named 'flask'
```

Instale com:

```bash
pip install flask
```

### 2. Criar `templates` com nome errado

O Flask procura HTML na pasta chamada exatamente:

```text
templates
```

### 3. Esquecer de iniciar o servidor

O arquivo não abre como HTML comum. Você precisa rodar:

```bash
python app.py
```

### 4. Confundir rota com arquivo

A rota `/` não é uma pasta. É um endereço da aplicação.

---

## Exercícios sugeridos

1. Crie uma rota `/` que mostre uma mensagem de boas-vindas.
2. Crie uma rota `/sobre` que fale sobre você.
3. Crie uma página HTML usando `render_template`.
4. Crie uma lista de alunos em Python e mostre no HTML.
5. Crie uma rota `/api/alunos` que retorne uma lista em JSON.

---

## Mini projeto

Crie um sistema web simples de cadastro de alunos.

Requisitos:

- Página inicial.
- Página com lista de alunos.
- Formulário para cadastrar nome e curso.
- Exibição dos alunos cadastrados.

Comece usando lista em memória. Depois, como desafio, salve os dados em CSV ou banco de dados.

---

## Resumo final

- Flask cria aplicações web com Python.
- Rotas são endereços da aplicação.
- Funções respondem às rotas.
- `render_template` mostra arquivos HTML.
- A pasta de HTML deve se chamar `templates`.
- Flask é um bom primeiro passo para entender desenvolvimento web.
