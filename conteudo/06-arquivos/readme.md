# 06 - Arquivos em Python

Neste modulo voce vai aprender a usar Python para ler, criar, atualizar e processar arquivos reais. Essa habilidade aparece em automacao, analise de dados, sistemas administrativos, importacao de planilhas, exportacao de relatorios e integracoes entre ferramentas.

Ao final, voce sera capaz de:

- Abrir arquivos com seguranca usando `open()`.
- Ler arquivos `.txt` e `.csv`.
- Salvar informacoes em novos arquivos.
- Adicionar novas linhas sem apagar dados anteriores.
- Processar registros linha por linha.
- Gerar relatorios simples a partir de dados reais.

## Estrutura do modulo

```text
06-arquivos/
  README.md
  dados/
    chamados.txt
    clientes.csv
    produtos.csv
    vendas.csv
  exemplos/
    01_ler_txt.py
    02_escrever_txt.py
    03_ler_csv.py
    04_processar_vendas.py
    05_gerar_relatorio.py
  exercicios/
    README.md
    gabaritos/
      faceis.py
      medios.py
      desafiadores.py
  projeto/
    README.md
    vendas.csv
    sistema_relatorio.py
```

## 1. Introducao

Um arquivo e uma forma de guardar informacoes fora da memoria do programa.

Quando voce cria uma variavel em Python, o valor existe enquanto o programa esta rodando:

```python
nome = "Ana"
```

Quando o programa termina, essa variavel desaparece. Se voce precisa guardar informacoes para usar depois, enviar para outra pessoa ou gerar um historico, precisa salvar esses dados em algum lugar.

Na pratica, sistemas usam arquivos para muitas tarefas:

- Uma loja exporta as vendas do dia em CSV.
- Um sistema salva logs de erros em TXT.
- Uma empresa recebe uma planilha de clientes para importar.
- Um setor financeiro gera relatorios mensais.
- Uma automacao le um arquivo, calcula resultados e salva outro arquivo pronto.

Neste modulo, vamos trabalhar principalmente com:

- `.txt`: arquivos de texto simples.
- `.csv`: arquivos parecidos com planilhas, muito usados em dados.

CSV significa "Comma-Separated Values", ou seja, valores separados por virgula. Na pratica, tambem e comum encontrar CSV separado por ponto e virgula.

Exemplo:

```csv
nome,email,cidade
Ana Souza,ana@email.com,Sao Paulo
Bruno Lima,bruno@email.com,Curitiba
```

A primeira linha normalmente contem os nomes das colunas. As linhas seguintes contem os dados.

## 2. Abrindo arquivos

Em Python, usamos a funcao `open()` para abrir um arquivo.

```python
arquivo = open("dados/chamados.txt", "r", encoding="utf-8")
```

O primeiro argumento e o caminho do arquivo. O segundo argumento e o modo de abertura.

| Modo | Nome | O que faz |
| --- | --- | --- |
| `r` | read | Abre para leitura. O arquivo precisa existir. |
| `w` | write | Abre para escrita. Se o arquivo existir, apaga o conteudo anterior. |
| `a` | append | Abre para adicionar conteudo ao final, sem apagar o que ja existe. |

Exemplo com fechamento manual:

```python
arquivo = open("dados/chamados.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
arquivo.close()

print(conteudo)
```

Na pratica profissional, preferimos usar `with`, porque ele fecha o arquivo automaticamente:

```python
with open("dados/chamados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
```

Use `encoding="utf-8"` para evitar problemas com acentos em portugues.

## 3. Leitura de arquivos

Existem varias formas de ler um arquivo. Cada uma serve melhor para uma situacao.

### `read()`

Le todo o arquivo de uma vez e devolve uma unica string.

```python
with open("dados/chamados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
```

Use quando o arquivo e pequeno e voce quer o texto inteiro.

### `readline()`

Le apenas uma linha por vez.

```python
with open("dados/chamados.txt", "r", encoding="utf-8") as arquivo:
    primeira_linha = arquivo.readline()
    segunda_linha = arquivo.readline()

print(primeira_linha)
print(segunda_linha)
```

Use quando voce quer controlar a leitura linha por linha.

### `readlines()`

Le todas as linhas e devolve uma lista.

```python
with open("dados/chamados.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

print(linhas)
```

Cada item da lista representa uma linha do arquivo.

### Percorrendo o arquivo com `for`

Esta e uma das formas mais usadas no mundo real:

```python
with open("dados/chamados.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())
```

O `strip()` remove espacos extras e a quebra de linha no final. Essa abordagem e boa porque o Python processa uma linha por vez, sem precisar carregar o arquivo inteiro na memoria.

## 4. Escrita em arquivos

Escrever em arquivo significa salvar informacoes.

### Criando ou sobrescrevendo com `w`

```python
with open("dados/relatorio.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Relatorio de vendas\n")
    arquivo.write("Total: R$ 1500.00\n")
```

Atencao: o modo `w` apaga o conteudo anterior se o arquivo ja existir.

### Adicionando conteudo com `a`

```python
with open("dados/log.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Nova venda registrada\n")
```

O modo `a` adiciona o texto no final do arquivo.

### Quebra de linha

Python nao adiciona uma nova linha automaticamente. Voce precisa usar `\n`:

```python
with open("dados/clientes_exportados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Ana Souza\n")
    arquivo.write("Bruno Lima\n")
```

Sem `\n`, os textos ficariam colados.

## 5. Trabalhando com CSV

Arquivos CSV sao muito usados porque podem ser abertos em Excel, Google Sheets, sistemas internos e ferramentas de dados.

Exemplo de `dados/clientes.csv`:

```csv
id,nome,email,cidade,ativo
1,Ana Souza,ana.souza@email.com,Sao Paulo,sim
2,Bruno Lima,bruno.lima@email.com,Curitiba,sim
```

### Leitura simples com `split()`

```python
with open("dados/clientes.csv", "r", encoding="utf-8") as arquivo:
    cabecalho = arquivo.readline()

    for linha in arquivo:
        id_cliente, nome, email, cidade, ativo = linha.strip().split(",")
        print(nome, "-", cidade)
```

Essa forma e didatica, mas limitada. Se um campo tiver virgula dentro do texto, o `split(",")` pode quebrar o dado errado.

### Leitura profissional com `csv`

Python ja vem com um modulo chamado `csv`, feito para trabalhar com arquivos CSV.

```python
import csv

with open("dados/clientes.csv", "r", encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)

    for cliente in leitor:
        print(cliente["nome"], "-", cliente["email"])
```

O `DictReader` transforma cada linha em um dicionario:

```python
{
    "id": "1",
    "nome": "Ana Souza",
    "email": "ana.souza@email.com",
    "cidade": "Sao Paulo",
    "ativo": "sim"
}
```

Isso deixa o codigo mais claro, porque voce acessa os dados pelo nome da coluna.

### Escrevendo CSV

```python
import csv

clientes = [
    {"nome": "Carla Mendes", "email": "carla@email.com", "cidade": "Recife"},
    {"nome": "Daniel Rocha", "email": "daniel@email.com", "cidade": "Salvador"},
]

with open("dados/clientes_novos.csv", "w", encoding="utf-8", newline="") as arquivo:
    colunas = ["nome", "email", "cidade"]
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)

    escritor.writeheader()
    escritor.writerows(clientes)
```

## 6. Processamento de dados

Processar dados significa ler informacoes, aplicar alguma regra e produzir um resultado.

Exemplo: calcular o total de vendas.

Arquivo `dados/vendas.csv`:

```csv
id,data,cliente,produto,quantidade,preco_unitario
1,2026-04-01,Ana Souza,Teclado,2,120.00
2,2026-04-01,Bruno Lima,Mouse,1,80.00
```

Codigo:

```python
import csv

total = 0

with open("dados/vendas.csv", "r", encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)

    for venda in leitor:
        quantidade = int(venda["quantidade"])
        preco = float(venda["preco_unitario"])
        total += quantidade * preco

print(f"Total vendido: R$ {total:.2f}")
```

O que acontece:

1. O arquivo e aberto.
2. Cada linha vira um dicionario.
3. `quantidade` e convertida para inteiro.
4. `preco_unitario` e convertido para decimal.
5. O subtotal da linha e calculado.
6. O resultado entra no total geral.

### Transformando dados

Voce tambem pode gerar uma nova lista com dados calculados:

```python
import csv

vendas_processadas = []

with open("dados/vendas.csv", "r", encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)

    for venda in leitor:
        quantidade = int(venda["quantidade"])
        preco = float(venda["preco_unitario"])
        subtotal = quantidade * preco

        vendas_processadas.append({
            "cliente": venda["cliente"],
            "produto": venda["produto"],
            "subtotal": subtotal,
        })

print(vendas_processadas)
```

Esse padrao e muito usado em automacoes e analise de dados.

## 7. Boas praticas

Use `with` para abrir arquivos:

```python
with open("dados/clientes.csv", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
```

Sempre informe o `encoding`:

```python
encoding="utf-8"
```

Use o modulo `csv` para arquivos CSV:

```python
import csv
```

Converta valores antes de calcular:

```python
quantidade = int(venda["quantidade"])
preco = float(venda["preco_unitario"])
```

Use nomes claros:

```python
total_vendas = 0
clientes_ativos = []
```

Evite sobrescrever arquivos importantes sem querer. Antes de usar `w`, pergunte:

- Eu quero criar um arquivo novo?
- Posso apagar o conteudo anterior?
- Seria melhor salvar com outro nome?

## 8. Erros comuns

### Arquivo nao encontrado

```python
with open("clientes.csv", "r", encoding="utf-8") as arquivo:
    print(arquivo.read())
```

Se o arquivo nao estiver na pasta esperada, o Python gera `FileNotFoundError`.

Tratamento:

```python
try:
    with open("dados/clientes.csv", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("Arquivo nao encontrado. Confira o caminho informado.")
```

### Erro ao converter numero

```python
preco = float("R$ 120,00")
```

Esse texto nao esta no formato esperado por `float()`. Em arquivos de dados, mantenha numeros em formato simples quando possivel:

```csv
120.00
80.50
```

### Sobrescrever dados sem querer

```python
with open("dados/vendas.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("teste")
```

Esse codigo apaga o conteudo anterior de `vendas.csv`. Se a intencao e adicionar uma nova linha, use `a`:

```python
with open("dados/log.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Processamento concluido\n")
```

### Esquecer a quebra de linha

```python
arquivo.write("Ana")
arquivo.write("Bruno")
```

Resultado:

```text
AnaBruno
```

Correto:

```python
arquivo.write("Ana\n")
arquivo.write("Bruno\n")
```

## 9. Mini desafios

1. Leia `dados/clientes.csv` e mostre apenas os nomes dos clientes.
2. Leia `dados/clientes.csv` e mostre apenas os clientes ativos.
3. Leia `dados/vendas.csv` e calcule o total vendido.
4. Gere um arquivo `relatorio_clientes.txt` com a quantidade de clientes por cidade.
5. Leia `dados/produtos.csv` e mostre os produtos com estoque abaixo de 10 unidades.
6. Leia `dados/chamados.txt` e conte quantas linhas existem no arquivo.
7. Crie um arquivo `log_execucao.txt` e adicione uma linha com o texto `Programa executado com sucesso`.

## 10. Resumo

Neste modulo voce aprendeu que arquivos permitem que programas leiam e salvem dados reais. Voce viu como abrir arquivos com `open()`, como usar os modos `r`, `w` e `a`, como ler conteudo com `read()`, `readline()` e `readlines()`, e como percorrer arquivos linha por linha.

Tambem aprendeu a trabalhar com CSV, um formato muito usado em empresas para planilhas, exportacoes e relatorios. O fluxo principal e:

```text
abrir arquivo -> ler dados -> processar informacoes -> gerar resultado -> salvar arquivo
```

Esse fluxo aparece em automacao, analise de dados, sistemas internos, rotinas financeiras, relatorios comerciais e muitas outras situacoes do mercado.

Para praticar, siga esta ordem:

1. Rode os exemplos da pasta `exemplos/`.
2. Resolva os exercicios faceis.
3. Resolva os exercicios medios.
4. Tente os desafios.
5. Faca o projeto da pasta `projeto/`.
