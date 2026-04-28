# 10 - Consumindo APIs com Requests

Neste modulo voce vai aprender a buscar dados externos usando Python.

Ate aqui, voce trabalhou com dados criados no proprio codigo, arquivos locais e planilhas com pandas. Agora o proximo passo e consumir dados que estao fora do seu computador: em sites, sistemas, servicos e APIs.

O objetivo deste modulo e ensinar o caminho completo:

- entender o que e uma API;
- fazer uma requisicao HTTP;
- usar a biblioteca `requests`;
- trabalhar com dados em JSON;
- validar respostas;
- tratar erros;
- processar dados recebidos;
- integrar APIs com funcoes, loops e pandas;
- construir um pequeno sistema que gera relatorio a partir de uma API publica.

## Estrutura do modulo

```text
10-requests/
  README.md
  exemplos/
    01_get_basico.py
    02_json_e_dados.py
    03_funcoes_tratamento_erros.py
    04_api_com_pandas.py
  exercicios/
    exercicios.md
    gabaritos/
      gabaritos.md
      gabaritos.py
  projeto/
    README.md
    relatorio_produtos_api.py
```

## 1. Introducao

### O que e uma API?

API significa Interface de Programacao de Aplicacoes.

Em linguagem simples: uma API e uma forma padronizada de um sistema conversar com outro.

Exemplo real:

- um aplicativo de clima busca a previsao em um servico externo;
- uma loja online busca produtos em um sistema de estoque;
- um sistema financeiro busca a cotacao de moedas;
- um aplicativo de entrega consulta enderecos pelo CEP;
- um dashboard busca dados de vendas em um sistema da empresa.

Quando voce acessa uma API, normalmente voce envia uma requisicao e recebe uma resposta.

### Exemplo fora da programacao

Imagine um restaurante:

- voce e o cliente;
- o garcom e a API;
- a cozinha e o sistema que tem os dados;
- o cardapio define o que voce pode pedir;
- o prato entregue e a resposta.

Voce nao entra na cozinha. Voce faz um pedido seguindo uma regra, e recebe uma resposta.

Com APIs acontece algo parecido.

### Onde APIs sao usadas?

APIs aparecem em praticamente todo sistema moderno:

- aplicativos mobile;
- sites;
- sistemas internos de empresas;
- dashboards;
- automacoes;
- integracoes entre plataformas;
- robos de atendimento;
- sistemas de pagamento;
- consulta de CEP;
- consulta de clima;
- sistemas de estoque e pedidos.

Trabalhar com APIs e uma habilidade essencial para desenvolvimento real.

## 2. Requisicao HTTP

HTTP e o protocolo usado para comunicacao na web.

Quando voce abre um site no navegador, seu navegador faz uma requisicao HTTP para um servidor. O servidor responde com dados.

Em Python, tambem podemos fazer requisicoes HTTP.

### O que e GET?

`GET` e um tipo de requisicao usado para buscar dados.

Exemplos:

- buscar usuarios;
- buscar produtos;
- buscar clima;
- buscar informacoes de um CEP;
- buscar posts de um blog.

Neste modulo, vamos focar em `GET`, porque e o primeiro passo para consumir APIs.

### Exemplo de URL de API

```text
https://jsonplaceholder.typicode.com/users
```

Essa URL retorna uma lista ficticia de usuarios. E uma API publica muito usada para estudos.

## 3. Biblioteca requests

`requests` e uma biblioteca Python usada para fazer requisicoes HTTP de forma simples.

### Instalacao

```bash
pip install requests
```

### Primeiro exemplo

```python
import requests

url = "https://jsonplaceholder.typicode.com/users"

resposta = requests.get(url, timeout=10)

print(resposta.status_code)
print(resposta.text)
```

Explicacao:

- `requests.get()` faz uma requisicao GET;
- `url` e o endereco da API;
- `timeout=10` evita que o programa fique travado para sempre se a API nao responder;
- `status_code` mostra o codigo da resposta;
- `text` mostra o conteudo bruto retornado pela API.

### Codigo de status

APIs retornam codigos de status HTTP.

Os mais comuns:

| Codigo | Significado |
|---:|---|
| 200 | Sucesso |
| 201 | Criado com sucesso |
| 400 | Requisicao invalida |
| 401 | Nao autorizado |
| 403 | Acesso proibido |
| 404 | Nao encontrado |
| 500 | Erro interno no servidor |

Para iniciantes, pense assim:

- `200`: deu certo;
- `400` a `499`: problema na requisicao;
- `500` a `599`: problema no servidor da API.

## 4. Trabalhando com JSON

### O que e JSON?

JSON e um formato de dados muito usado em APIs.

Ele parece bastante com dicionarios e listas do Python.

Exemplo de JSON:

```json
{
  "id": 1,
  "name": "Leanne Graham",
  "email": "Sincere@april.biz",
  "address": {
    "city": "Gwenborough"
  }
}
```

No Python, depois de converter a resposta com `.json()`, acessamos os dados como dicionarios e listas.

### Convertendo resposta para JSON

```python
import requests

url = "https://jsonplaceholder.typicode.com/users"
resposta = requests.get(url, timeout=10)

if resposta.status_code == 200:
    usuarios = resposta.json()
    print(usuarios[0]["name"])
    print(usuarios[0]["email"])
else:
    print("Erro ao buscar dados:", resposta.status_code)
```

`resposta.json()` transforma o corpo da resposta em estruturas Python.

Se a API retornar uma lista, voce acessa por indice:

```python
primeiro_usuario = usuarios[0]
```

Se a API retornar um dicionario, voce acessa por chave:

```python
nome = primeiro_usuario["name"]
```

### Acessando dados dentro de dados

Alguns dados ficam dentro de outros.

```python
cidade = usuarios[0]["address"]["city"]
print(cidade)
```

Leia assim:

- pegue o primeiro usuario;
- dentro dele, pegue `address`;
- dentro de `address`, pegue `city`.

## 5. Processamento de dados

Buscar dados e apenas o comeco. Em sistemas reais, voce precisa usar esses dados.

Exemplo: listar usuarios com nome, email e cidade.

```python
import requests

url = "https://jsonplaceholder.typicode.com/users"
resposta = requests.get(url, timeout=10)

if resposta.status_code == 200:
    usuarios = resposta.json()

    for usuario in usuarios:
        nome = usuario["name"]
        email = usuario["email"]
        cidade = usuario["address"]["city"]

        print(f"{nome} - {email} - {cidade}")
else:
    print("Erro ao buscar usuarios.")
```

Exemplo: filtrar dados.

```python
usuarios = resposta.json()

usuarios_com_biz = []

for usuario in usuarios:
    if usuario["email"].endswith(".biz"):
        usuarios_com_biz.append(usuario)

print(usuarios_com_biz)
```

Processar dados significa transformar a resposta da API em algo util para o sistema.

## 6. Integracao com outros modulos

### Usando com funcoes

```python
import requests


def buscar_usuarios():
    url = "https://jsonplaceholder.typicode.com/users"
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()
    return resposta.json()


usuarios = buscar_usuarios()
print(usuarios[0]["name"])
```

Funcoes ajudam a organizar o codigo e reutilizar chamadas de API.

### Usando com loops

```python
usuarios = buscar_usuarios()

for usuario in usuarios:
    print(usuario["name"])
```

Loops permitem processar varios registros retornados pela API.

### Usando com pandas

Como voce ja aprendeu pandas, pode transformar uma resposta de API em DataFrame.

```python
import pandas as pd
import requests

url = "https://dummyjson.com/products?limit=10"
resposta = requests.get(url, timeout=10)
resposta.raise_for_status()

dados = resposta.json()
produtos = dados["products"]

df = pd.DataFrame(produtos)

print(df[["title", "category", "price", "stock"]])
```

Isso e muito usado em analise de dados: buscar dados externos e depois analisar com pandas.

## 7. Boas praticas

### Use timeout

Sempre use `timeout`.

```python
requests.get(url, timeout=10)
```

Sem timeout, seu programa pode ficar parado por muito tempo se a API nao responder.

### Valide o status da resposta

```python
if resposta.status_code == 200:
    dados = resposta.json()
else:
    print("Erro:", resposta.status_code)
```

Ou use:

```python
resposta.raise_for_status()
```

`raise_for_status()` gera erro automaticamente se a resposta for `400`, `404`, `500` etc.

### Trate erros de rede

```python
import requests

try:
    resposta = requests.get("https://jsonplaceholder.typicode.com/users", timeout=10)
    resposta.raise_for_status()
    dados = resposta.json()
    print(dados)
except requests.exceptions.RequestException as erro:
    print("Erro na requisicao:", erro)
```

### Use `.get()` quando a chave puder nao existir

```python
telefone = usuario.get("phone", "Telefone nao informado")
```

Isso evita erro se a chave nao existir.

### Separe responsabilidades

Uma boa organizacao:

1. funcao para buscar dados;
2. funcao para tratar/processar dados;
3. funcao para exibir ou salvar relatorio.

## 8. Erros comuns

### API fora do ar

A internet pode cair, a API pode estar lenta ou o servidor pode estar fora do ar.

Use `try/except` e `timeout`.

### Dados inesperados

Voce esperava uma lista, mas a API retornou um dicionario com mensagem de erro.

Sempre confira:

```python
print(type(dados))
print(dados)
```

### Erro de chave

```python
print(usuario["cidade"])
```

Se a chave `cidade` nao existir, voce tera `KeyError`.

Use as chaves reais da API:

```python
print(usuario["address"]["city"])
```

Ou use `.get()` quando fizer sentido:

```python
print(usuario.get("cidade", "Cidade nao informada"))
```

### Esquecer que JSON pode ter lista dentro de dicionario

Na API DummyJSON, produtos ficam dentro da chave `products`.

```python
dados = resposta.json()
produtos = dados["products"]
```

Se voce tentar percorrer `dados` diretamente, talvez percorra as chaves do dicionario, nao os produtos.

### Esquecer de instalar requests

Erro comum:

```text
ModuleNotFoundError: No module named 'requests'
```

Resolva com:

```bash
pip install requests
```

## 9. Mini desafios

### Mini desafio 1

Use a API:

```text
https://jsonplaceholder.typicode.com/users
```

Mostre o nome e email de todos os usuarios.

### Mini desafio 2

Mostre apenas os usuarios cuja cidade termina com a letra `h`.

### Mini desafio 3

Use a API:

```text
https://dummyjson.com/products?limit=10
```

Mostre o nome, preco e estoque de cada produto.

### Mini desafio 4

Calcule o valor medio dos produtos retornados pela DummyJSON.

### Mini desafio 5

Use a BrasilAPI para consultar um CEP:

```text
https://brasilapi.com.br/api/cep/v1/01001000
```

Mostre cidade, estado, bairro e rua.

### Mini desafio 6

Crie uma funcao chamada `buscar_json(url)` que:

- recebe uma URL;
- faz uma requisicao GET;
- valida erro;
- retorna o JSON.

### Mini desafio 7

Transforme os produtos da DummyJSON em um DataFrame pandas e mostre as colunas `title`, `category`, `price` e `stock`.

## 10. Resumo

Neste modulo voce aprendeu que:

- API e uma forma de sistemas conversarem;
- HTTP e o protocolo usado na web;
- `GET` e usado para buscar dados;
- `requests.get()` faz requisicoes HTTP em Python;
- APIs geralmente retornam JSON;
- JSON vira dicionario/lista no Python com `.json()`;
- dados de API precisam ser validados antes de usar;
- `timeout`, `raise_for_status()` e `try/except` tornam o codigo mais confiavel;
- APIs podem ser integradas com funcoes, loops e pandas;
- sistemas reais usam APIs para buscar usuarios, produtos, clima, enderecos e outros dados externos.

Ao final deste modulo, voce ja consegue consumir APIs publicas, processar respostas e construir pequenas integracoes em Python.
