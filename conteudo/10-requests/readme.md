
# 🌐 Trabalhando com Requisições de API usando Requests em Python

## 📚 Introdução

Muitas aplicações modernas precisam se comunicar com outras através da **internet**, trocando informações por **APIs**.  
Em Python, usamos a biblioteca **requests** para fazer essas requisições HTTP.

---

## ✅ Requisitos

Antes de começar, é importante saber:

- O que é uma API (Interface de Programação de Aplicações).
- Como importar bibliotecas em Python.
- Conceitos básicos de JSON (dados em formato de dicionário/lista).

---

## 🔹 Fazendo uma requisição simples com `requests`

O primeiro passo é importar a biblioteca `requests` e fazer uma chamada para uma API.

```python
import requests  # Importa a biblioteca requests

# URL da API que retorna categorias de refeições
url = "https://www.themealdb.com/api/json/v1/1/categories.php"

# Faz a requisição GET
response = requests.get(url)

# Verifica se a resposta foi bem-sucedida
if response.status_code == 200:
    data = response.json()  # Converte a resposta em JSON
    print(data)             # Exibe os dados recebidos
else:
    print(f"Falha na requisição: {response.status_code}")
```

---

## 🧠 Explicação

- `requests.get(url)` envia uma requisição do tipo GET para o endereço.
- `response.status_code` traz o **código de resposta** HTTP (200 = sucesso).
- `response.json()` converte a resposta para um **dicionário Python**.

---

## 🔹 Melhorando com tratamento de erros usando `try/except`

Para evitar que erros de conexão travem o programa, usamos `try/except`.

```python
import requests

def getApi():
    try:
        url = "https://www.themealdb.com/api/json/v1/1/categories.php"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return f"Falha na requisição: {response.status_code}"

    except requests.RequestException as e:
        return f"Erro na requisição: {e}"

# Testando a função
resultado = getApi()
print(resultado)
```

---

## 🧠 Explicação

- `try/except` protege o código em caso de falha de rede ou outros problemas.
- `requests.RequestException` captura **qualquer erro relacionado** a requisições.
- A função retorna o resultado ou uma mensagem de erro.

---

## 🔹 Importando funções de outro arquivo

Se quisermos organizar melhor nosso código, podemos salvar a função `getApi` em outro arquivo, por exemplo `request_api.py`.

Depois, em outro arquivo, fazemos a importação:

```python
from request_api import getApi  # Importa a função getApi

resultado = getApi()  # Chama a função
```

Assim, podemos **separar responsabilidades** e **reutilizar funções** em projetos maiores.

---

## 🔹 Acessando dados específicos do JSON recebido

Depois de obter o resultado da API, podemos acessar partes específicas do dicionário:

```python
# Acessa o primeiro item da lista associada à chave 'categories'
resultado_1 = resultado['categories'][0]

# Exibe o primeiro item
print(resultado_1)
```

➡️ Aqui, estamos pegando o **primeiro elemento** da lista de categorias.

---

## ✅ Conclusão

Você aprendeu:

- Como **fazer requisições** GET em Python usando `requests`.
- Como **tratar erros** de requisições.
- Como **importar funções** de outros arquivos.
- Como **navegar** em dados JSON.

Esses conhecimentos são **essenciais** para trabalhar com APIs, aplicações web e integrações em Python!

