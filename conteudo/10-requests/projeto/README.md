# Projeto - Sistema de Relatorio de Produtos via API

Neste projeto, voce vai criar um sistema que consome uma API publica, processa os dados e gera um relatorio.

Esse tipo de tarefa e comum no mercado:

- um sistema busca produtos em uma API;
- os dados sao tratados no Python;
- metricas sao calculadas;
- um relatorio e exibido ou salvo para analise.

## API usada

Vamos usar a DummyJSON:

```text
https://dummyjson.com/products?limit=100
```

Ela retorna produtos ficticios com dados como:

- nome;
- categoria;
- preco;
- estoque;
- percentual de desconto;
- avaliacao.

## Objetivo do sistema

O sistema deve:

1. buscar produtos na API;
2. validar se a requisicao deu certo;
3. transformar os dados em DataFrame pandas;
4. gerar metricas gerais;
5. criar relatorio por categoria;
6. identificar produtos importantes;
7. salvar um CSV com os principais campos.

## Decisoes do projeto

### Por que usar `requests`?

Porque precisamos buscar dados externos via HTTP.

### Por que usar `timeout`?

Para evitar que o programa fique travado se a API demorar ou falhar.

### Por que usar `raise_for_status()`?

Para detectar respostas com erro, como `404` ou `500`.

### Por que usar pandas?

Porque depois que os dados chegam, pandas facilita filtros, metricas, agrupamentos e exportacao.

## Como executar

Instale as dependencias:

```bash
pip install requests pandas
```

Execute:

```bash
python3 relatorio_produtos_api.py
```

## Saida esperada

O sistema mostra:

- total de produtos;
- preco medio;
- estoque total;
- valor potencial em estoque;
- produto mais caro;
- produto com maior desconto;
- relatorio por categoria;
- produtos com estoque baixo.

Tambem gera o arquivo:

```text
relatorio_produtos.csv
```

## Codigo completo

Veja `relatorio_produtos_api.py`.
