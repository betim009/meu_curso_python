# Apostila de Estudo
## Python + Análise de Dados + IA para Geologia

---

# 1. Introdução

Esta apostila foi criada para ajudar uma estudante da área de Geologia a aprender Python de uma forma prática, aplicada e útil para sua carreira.

O objetivo deste material não é transformar a estudante em uma programadora profissional de software. Em vez disso, a proposta é ensinar como utilizar Python como uma ferramenta poderosa para:

- analisar dados
- organizar informações
- gerar gráficos
- automatizar tarefas
- utilizar inteligência artificial

Hoje em dia, muitas áreas científicas utilizam programação como ferramenta de apoio. A Geologia é uma dessas áreas. Profissionais que sabem trabalhar com dados possuem uma grande vantagem no mercado de trabalho.

Por isso, aprender Python pode ajudar muito em situações como:

- análise de dados de campo
- interpretação de amostras
- organização de planilhas
- geração de relatórios
- análise estatística
- visualização de padrões

---

# 2. O que é Python

Python é uma linguagem de programação muito utilizada em ciência, engenharia, análise de dados e inteligência artificial.

Uma linguagem de programação é simplesmente uma forma de dar instruções ao computador.

Essas instruções dizem ao computador o que fazer.

Por exemplo:

- calcular valores
- organizar dados
- filtrar informações
- gerar gráficos
- analisar padrões

Python é considerada uma linguagem muito amigável para iniciantes porque sua sintaxe é simples e fácil de ler.

---

# 3. Variáveis

Uma variável é um espaço onde podemos guardar uma informação.

Podemos imaginar uma variável como uma caixa que possui um nome e guarda um valor dentro dela.

Exemplo:

```python
mineral = "quartzo"
```

Neste exemplo:

- `mineral` é o nome da variável
- `"quartzo"` é o valor guardado

Outro exemplo:

```python
profundidade = 120
```

Aqui estamos guardando um número.

---

# 4. Tipos de dados

Python trabalha com diferentes tipos de dados.

Os principais são:

## Texto (string)

```python
rocha = "granito"
```

## Número inteiro

```python
amostras = 25
```

## Número decimal

```python
concentracao = 32.5
```

Cada tipo de dado possui utilidades diferentes dependendo da situação.

---

# 5. Listas

Uma lista permite armazenar vários valores dentro de uma única variável.

Exemplo:

```python
minerais = ["quartzo", "calcita", "feldspato"]
```

Agora a variável `minerais` contém três elementos.

Podemos acessar elementos da lista usando índices.

```python
print(minerais[0])
```

Isso mostrará:

```
quartzo
```

Porque Python começa a contar a partir do zero.

---

# 6. Estrutura de repetição

Muitas vezes precisamos repetir uma ação várias vezes.

Para isso usamos o `for`.

Exemplo:

```python
valores = [10, 20, 30, 40]

for valor in valores:
    print(valor)
```

Neste exemplo o Python percorre toda a lista e imprime cada valor.

---

# 7. Condições

Às vezes precisamos que o programa tome decisões.

Para isso usamos `if`.

Exemplo:

```python
concentracao = 45

if concentracao > 30:
    print("Concentração alta")
```

Aqui estamos dizendo ao computador:

Se a concentração for maior que 30, exiba a mensagem.

---

# 8. Funções

Funções são blocos de código que executam uma tarefa específica.

Elas ajudam a organizar o código.

Exemplo:

```python
def classificar(valor):

    if valor > 50:
        return "alta"

    elif valor > 20:
        return "media"

    else:
        return "baixa"
```

Agora podemos usar a função:

```python
print(classificar(60))
```

---

# 9. Trabalhando com dados usando Pandas

Pandas é uma biblioteca muito importante para trabalhar com tabelas de dados.

Primeiro precisamos importar a biblioteca:

```python
import pandas as pd
```

---

# 10. Lendo arquivos CSV

Arquivos CSV são muito usados para armazenar dados em formato de tabela.

Exemplo:

```
local,rocha,concentracao
A,granito,30
B,basalto,45
C,calcario,20
```

Para ler esse arquivo usamos:

```python
dados = pd.read_csv("dados.csv")
```

Agora `dados` representa toda a tabela.

---

# 11. Visualizando os dados

Podemos ver as primeiras linhas da tabela:

```python
dados.head()
```

Isso ajuda a entender como os dados estão organizados.

---

# 12. Selecionando colunas

```python
dados["concentracao"]
```

Isso seleciona apenas uma coluna da tabela.

---

# 13. Estatísticas simples

Podemos calcular a média:

```python
dados["concentracao"].mean()
```

Isso ajuda a entender o comportamento dos dados.

---

# 14. Filtrando dados

Podemos filtrar valores maiores que 30.

```python
dados[dados["concentracao"] > 30]
```

Isso retorna apenas os registros que atendem à condição.

---

# 15. Gráficos

Visualizar dados é muito importante.

Para isso usamos a biblioteca `matplotlib`.

```python
import matplotlib.pyplot as plt

plt.hist(dados["concentracao"])
plt.show()
```

Isso cria um histograma mostrando a distribuição dos valores.

---

# 16. Automação

Python também pode automatizar tarefas repetitivas.

Exemplo:

```python
arquivos = ["dados1.csv", "dados2.csv", "dados3.csv"]

for arquivo in arquivos:

    dados = pd.read_csv(arquivo)

    print(dados.head())
```

Isso permite abrir vários arquivos automaticamente.

---

# 17. Introdução à Inteligência Artificial

Inteligência Artificial é uma área da computação que permite que sistemas aprendam padrões a partir de dados.

Na prática, IA pode ajudar em situações como:

- prever resultados
- identificar padrões
- classificar informações

Uma biblioteca muito usada é:

```
scikit-learn
```

---

# 18. Exemplo simples de Machine Learning

```python
from sklearn.linear_model import LinearRegression
```

Machine Learning funciona usando dados de treinamento.

O modelo aprende padrões e depois pode fazer previsões.

---

# 19. Usando IA como ferramenta de apoio

Hoje em dia também podemos usar ferramentas de IA para:

- gerar código
- revisar código
- sugerir análises
- resumir textos técnicos

Ferramentas como ChatGPT podem acelerar muito o processo de aprendizagem.

Mas é importante lembrar que a IA não substitui o conhecimento humano.

Sempre é necessário revisar os resultados.

---

# 20. Conclusão

Aprender Python não significa apenas aprender uma linguagem de programação.

Significa aprender uma nova forma de analisar informações e resolver problemas.

Profissionais que sabem trabalhar com dados têm uma vantagem cada vez maior no mercado.

Na Geologia, isso pode significar:

- análises mais rápidas
- melhores interpretações
- automação de tarefas
- capacidade de trabalhar com grandes volumes de dados

Este material é apenas o começo.

Com o tempo, será possível avançar para:

- análise geoespacial
- machine learning aplicado
- modelagem de dados
- visualização avançada

---

# Próximos passos

Depois de estudar esta apostila, o próximo passo ideal é:

1. resolver exercícios
2. trabalhar com dados reais
3. desenvolver pequenos projetos

A prática constante é a melhor forma de consolidar o aprendizado.
