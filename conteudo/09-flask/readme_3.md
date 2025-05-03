# 🌐 Organizando Rotas Separadas no Flask com Blueprints

Quando o projeto Flask começa a crescer, é importante **organizar o código em arquivos separados**, especialmente para rotas. Isso ajuda a manter o projeto limpo, legível e escalável.

Neste material você vai aprender:

- Como usar `Blueprint` no Flask
- Como separar as rotas do `app.py`
- Como importar e registrar rotas externas

---

## 📁 Estrutura sugerida

```
meu_app/
├── app.py                # Arquivo principal que inicia a aplicação
├── routes/
│   ├── __init__.py       # Torna a pasta um pacote Python
│   └── contratos.py      # Rotas relacionadas a contratos
└── venv/
```

---

## 🧱 Etapa 1 – Criando a rota separada (contratos.py)

Dentro da pasta `routes/`, crie o arquivo `contratos.py`:

```python
from flask import Blueprint, jsonify

# Criando um Blueprint
contratos_bp = Blueprint("contratos", __name__)

# Rota GET simples
@contratos_bp.route("/contratos", methods=["GET"])
def listar_contratos():
    dados_exemplo = [
        {"id": 1, "cliente": "João"},
        {"id": 2, "cliente": "Maria"},
    ]
    return jsonify(dados_exemplo)
```

---

## 📦 Etapa 2 – Importando o blueprint no app.py

No arquivo `app.py`, faça a importação e registro da rota:

```python
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
```

---

## 📄 Etapa 3 – Adicionando __init__.py

Na pasta `routes/`, crie um arquivo vazio com o nome `__init__.py`.

Isso torna a pasta um "pacote" Python, permitindo que ela seja importada normalmente com:

```python
from routes.contratos import contratos_bp
```

---

## ✅ Vantagens dessa abordagem

- Cada módulo (ex: contratos, usuários, produtos) pode ter seu próprio arquivo
- Facilita manutenção e leitura
- Permite separar rotas por áreas do sistema

---

## ⚠️ Cuidados

- Sempre registre os blueprints no `app.py`
- Use nomes únicos nos blueprints para evitar conflitos
- Evite colocar lógicas de banco de dados diretamente nas rotas, prefira separar por responsabilidade

---

## 🧠 Conclusão

Agora você sabe como:

- Criar rotas em arquivos separados com `Blueprint`
- Organizar melhor sua aplicação Flask
- Registrar os módulos de rota de forma limpa

Na próxima etapa podemos aprender como lidar com rotas dinâmicas, parâmetros na URL e separação por módulos maiores. Deseja seguir?