# Exercicios - Requests e APIs

Estes exercicios simulam tarefas comuns de integracao: buscar dados externos, validar respostas, acessar JSON, filtrar informacoes e preparar relatorios simples.

APIs usadas:

- JSONPlaceholder: `https://jsonplaceholder.typicode.com`
- DummyJSON: `https://dummyjson.com`
- BrasilAPI: `https://brasilapi.com.br`
- Open-Meteo: `https://open-meteo.com`

## Exercicios faceis

### 1. Primeira requisicao

Faca uma requisicao GET para:

```text
https://jsonplaceholder.typicode.com/users
```

Mostre:

- codigo de status;
- tipo do dado convertido com `.json()`;
- quantidade de usuarios retornados.

### 2. Nome e email dos usuarios

Usando a mesma API de usuarios, mostre o nome e o email de cada usuario.

### 3. Acessando dados internos

Mostre o nome do usuario e a cidade onde ele mora.

Dica: a cidade esta dentro de `address`.

### 4. Consulta de CEP

Consulte o CEP `01001000` na BrasilAPI:

```text
https://brasilapi.com.br/api/cep/v1/01001000
```

Mostre:

- rua;
- bairro;
- cidade;
- estado.

### 5. Produtos simples

Consuma:

```text
https://dummyjson.com/products?limit=10
```

Mostre o nome e o preco de cada produto.

## Exercicios medios

### 6. Funcao reutilizavel

Crie uma funcao `buscar_json(url)` que:

- recebe uma URL;
- faz `GET`;
- usa `timeout`;
- valida erros com `raise_for_status()`;
- retorna o JSON;
- retorna `None` se algo der errado.

Teste com a API de usuarios.

### 7. Filtrar usuarios por email

Busque os usuarios da JSONPlaceholder e mostre apenas os usuarios cujo email termina com `.biz`.

### 8. Calcular preco medio

Busque 20 produtos na DummyJSON:

```text
https://dummyjson.com/products?limit=20
```

Calcule o preco medio dos produtos retornados.

### 9. Produtos com estoque baixo

Usando a DummyJSON, mostre produtos com estoque menor que 30.

Para cada produto, mostre:

- nome;
- categoria;
- preco;
- estoque.

### 10. API com pandas

Transforme os produtos da DummyJSON em um DataFrame pandas.

Mostre apenas as colunas:

- `title`;
- `category`;
- `price`;
- `stock`.

Depois, calcule:

- preco medio;
- estoque total.

## Exercicios desafiadores

### 11. Relatorio por categoria

Busque 100 produtos na DummyJSON:

```text
https://dummyjson.com/products?limit=100
```

Crie um relatorio por categoria com:

- quantidade de produtos;
- preco medio;
- estoque total.

Ordene pelo estoque total, do maior para o menor.

### 12. Consulta de clima

Use a Open-Meteo para buscar a temperatura atual de Sao Paulo.

URL:

```text
https://api.open-meteo.com/v1/forecast?latitude=-23.55&longitude=-46.63&current_weather=true
```

Mostre:

- temperatura;
- velocidade do vento;
- codigo do clima;
- horario da medicao.

### 13. Relatorio completo de produtos

Busque 100 produtos na DummyJSON e gere um relatorio com:

- total de produtos;
- preco medio;
- estoque total;
- produto mais caro;
- produto com maior desconto;
- categorias existentes;
- produtos com estoque menor que 20.

Organize o codigo em funcoes.
