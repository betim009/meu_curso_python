# Projeto - Sistema de geracao de relatorio de vendas

Neste projeto voce vai criar um programa que le um arquivo CSV de vendas, calcula indicadores importantes e gera um relatorio em TXT.

Essa atividade simula uma tarefa comum em empresas: receber uma exportacao de vendas e transformar os dados em um resumo facil de entender.

## Objetivo

Criar um sistema que:

1. Leia o arquivo `vendas.csv`.
2. Calcule o total vendido.
3. Calcule a quantidade de pedidos.
4. Calcule a quantidade total de itens vendidos.
5. Calcule a media de valor por pedido.
6. Identifique a maior venda.
7. Calcule o total vendido por cliente.
8. Salve tudo em `relatorio_vendas.txt`.

## Dados de entrada

Arquivo `vendas.csv`:

```csv
id,data,cliente,produto,quantidade,preco_unitario
1,2026-04-01,Ana Souza,Teclado,2,120.00
2,2026-04-01,Bruno Lima,Mouse,1,80.00
```

Cada linha representa uma venda.

O subtotal de uma venda e:

```text
quantidade * preco_unitario
```

## Passo a passo

### 1. Importar bibliotecas

Usamos `csv` para ler o arquivo CSV de forma segura e `Path` para montar caminhos de arquivo.

```python
import csv
from pathlib import Path
```

### 2. Definir caminhos

```python
BASE_DIR = Path(__file__).resolve().parent
CAMINHO_VENDAS = BASE_DIR / "vendas.csv"
CAMINHO_RELATORIO = BASE_DIR / "relatorio_vendas.txt"
```

Assim o programa funciona mesmo se voce executar de outra pasta.

### 3. Criar variaveis acumuladoras

```python
total_vendido = 0
total_pedidos = 0
total_itens = 0
maior_venda = 0
cliente_maior_venda = ""
produto_maior_venda = ""
vendas_por_cliente = {}
```

Essas variaveis guardam os resultados enquanto o arquivo e processado.

### 4. Ler e processar cada linha

```python
with open(CAMINHO_VENDAS, "r", encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)

    for venda in leitor:
        quantidade = int(venda["quantidade"])
        preco_unitario = float(venda["preco_unitario"])
        subtotal = quantidade * preco_unitario
```

CSV guarda tudo como texto. Por isso precisamos converter:

- `quantidade` para `int`
- `preco_unitario` para `float`

### 5. Gerar o arquivo final

O relatorio final sera salvo em texto para poder ser enviado, lido ou arquivado.

## Codigo completo

Veja o arquivo `sistema_relatorio.py`.

Para executar:

```bash
python3 conteudo/06-arquivos/projeto/sistema_relatorio.py
```

## Resultado esperado

O programa gera `relatorio_vendas.txt` com conteudo parecido com:

```text
Relatorio de vendas
===================
Total de pedidos: 10
Total de itens vendidos: 15
Total vendido: R$ 8180.00
Media por pedido: R$ 818.00
Maior venda: R$ 4200.00
Cliente da maior venda: Gabriela Martins
Produto da maior venda: Notebook

Vendas por cliente:
- Ana Souza: R$ 1190.00
- Bruno Lima: R$ 310.00
```

## Decisoes tomadas

- O arquivo de entrada ficou em CSV porque esse formato e comum em exportacoes de sistemas.
- O relatorio final ficou em TXT porque e simples de abrir, enviar e validar.
- O codigo usa `DictReader` para acessar os campos pelo nome da coluna.
- Os calculos sao feitos dentro do loop para evitar repetir leituras do arquivo.
- O total por cliente usa dicionario porque o nome do cliente vira a chave e o total comprado vira o valor.

## Expansoes possiveis

Depois de concluir, tente melhorar o projeto:

1. Gerar tambem um CSV com vendas por cliente.
2. Filtrar vendas por data.
3. Mostrar o produto mais vendido.
4. Separar o codigo em funcoes.
5. Tratar erro de arquivo nao encontrado.
