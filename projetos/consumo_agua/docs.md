# 📘 Documentação Detalhada das Funções

Este documento descreve em detalhes todas as funções implementadas no projeto **Consumo de Água**, explicando a lógica, os parâmetros utilizados, os métodos do Pandas e do Matplotlib, e o motivo de cada escolha.

---

## 🔹 `init_csv()`
### Função
```python
def init_csv():
    try:
        df = pd.read_excel("./data/consumo.xlsx", sheet_name=0)
        for i in range(2):
            df.to_csv(f"./data/file_{i}.csv", index=False)
        return True
    except Exception as e:
        print(f"Erro ao gerar CSV: {e}")
        return False
```
### Explicação
- **Objetivo:** ler a planilha `consumo.xlsx` (primeira aba) e gerar arquivos CSV que serão usados nas análises.
- **`pd.read_excel()`**: carrega a planilha do Excel para um DataFrame do Pandas. O parâmetro `sheet_name=0` indica que será lida a primeira aba.  
- **Loop `for i in range(2):`**: cria duas cópias do mesmo DataFrame em formato CSV (`file_0.csv` e `file_1.csv`). Isso é útil para testes iniciais.  
- **`index=False`**: evita que a coluna de índice do Pandas seja salva no CSV.  
- **Tratamento de erro (`try/except`)**: garante que, em caso de falha na leitura ou escrita, uma mensagem seja exibida e a função retorne `False`.

---

## 🔹 `overall_average()`
### Função
```python
def overall_average():
    try:
        df = pd.read_csv("./reports/file_0.csv")
        col_consumo = df["Consumo"]

        media = col_consumo.mean()
        mediana = col_consumo.median()
        moda = col_consumo.mode()[0]
        maior = col_consumo.max()
        menor = col_consumo.min()

        show = {
            "Média": [media],
            "Mediana": [mediana],
            "Moda": [moda],
            "Maior Consumo": [maior],
            "Menor Consumo": [menor]
        }

        print(pd.DataFrame(show))
    except Exception as e:
        print(f"Erro ao calcular estatísticas: {e}")
        return False
```
### Explicação
- **Objetivo:** calcular estatísticas descritivas da coluna `Consumo`.  
- **`df["Consumo"]`**: seleciona apenas a coluna de interesse.  
- **`.mean()`**: retorna a média aritmética. Boa para visão geral, mas sensível a valores muito altos (outliers).  
- **`.median()`**: retorna a mediana (valor central), menos sensível a outliers.  
- **`.mode()[0]`**: retorna a moda (valor mais frequente). O `[0]` pega o primeiro valor caso haja múltiplas modas.  
- **`.max()` e `.min()`**: mostram os extremos (maior e menor valor de consumo). Úteis para detectar variações grandes.  
- **`pd.DataFrame(show)`**: organiza os resultados em formato tabular para melhor leitura.  

### Interpretação
- **Média:** fornece uma visão geral do consumo médio, mas pode ser influenciada por valores muito altos ou baixos (outliers), o que pode distorcer a percepção do consumo típico.  
- **Mediana:** representa o consumo típico, especialmente útil quando a distribuição dos dados é assimétrica ou possui outliers, pois não é afetada por valores extremos.  
- **Moda:** indica o valor mais comum no conjunto de dados, ajudando a identificar padrões frequentes, como muitos consumidores com consumo zero ou baixo.  
- **Máximo e mínimo:** revelam os extremos do consumo, permitindo identificar casos atípicos ou variações significativas dentro da base de dados.

---

## 🔹 `overall_hist()`
### Função
```python
def overall_hist():
    try:
        df = pd.read_csv("./reports/file_0.csv")
        plt.hist(df["Consumo"], bins=20, color="skyblue", edgecolor="red")
        plt.title("Distribuição do Consumo")
        plt.xlabel("Consumo")
        plt.ylabel("Frequência")
        min_val = df["Consumo"].min()
        max_val = df["Consumo"].max()
        import numpy as np
        ticks = np.linspace(min_val, max_val, 5, dtype=int)
        plt.xticks(ticks, [f"{t/1_000_000:.1f}M" for t in ticks])
        plt.savefig("./reports/hist_consumo.png")
        plt.show()
    except Exception as e:
        print(f"Erro ao gerar histograma: {e}")
        return False
```
### Explicação
- **Objetivo:** visualizar a distribuição dos valores de consumo.  
- **`plt.hist()`**: gera o histograma.  
  - `bins=20`: divide os valores em 20 intervalos.  
  - `color="skyblue"` e `edgecolor="red"`: definem estilo visual.  
- **Eixos:**  
  - X = valores de consumo.  
  - Y = frequência (quantas linhas caem em cada intervalo).  
- **`np.linspace()`**: gera 5 pontos igualmente espaçados entre o valor mínimo e máximo para personalizar o eixo X.  
- **`plt.xticks()`**: substitui os valores do eixo X por versões formatadas em milhões (`M`).  
- **`plt.savefig()`**: salva a figura em `reports/` para uso posterior.  
- **`plt.show()`**: exibe o gráfico interativamente.  

### Interpretação
- O histograma mostra como os consumos estão distribuídos, permitindo observar se os valores se concentram em faixas baixas, se estão espalhados, ou se a distribuição é simétrica ou assimétrica.  
- É útil para identificar padrões gerais no consumo, como a presença de muitos zeros, outliers, ou outras características importantes da distribuição dos dados.

---

## 🔹 `consumo_por_regiao()`
### Função
```python
def consumo_por_regiao():
    try:
        df = pd.read_csv("./reports/file_0.csv")
        consumo_regiao = df.groupby("Regiao")["Consumo"].mean().sort_values()

        consumo_regiao.plot(kind="bar", color="skyblue", edgecolor="black")
        plt.title("Consumo Médio por Região")
        plt.ylabel("Consumo Médio")
        plt.xlabel("Região")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("./reports/consumo_regiao.png")
        plt.show()
    except Exception as e:
        print(f"Erro ao gerar gráfico por região: {e}")
        return False
```
### Explicação
- **Objetivo:** comparar o consumo médio entre diferentes regiões.  
- **`df.groupby("Regiao")["Consumo"].mean()`**: agrupa os dados por região e calcula a média do consumo.  
- **`.sort_values()`**: organiza as barras do menor para o maior consumo, facilitando a comparação visual.  
- **`.plot(kind="bar")`**: gera gráfico de barras.  
- **`plt.xticks(rotation=45)`**: gira os rótulos para evitar sobreposição.  
- **`plt.tight_layout()`**: ajusta margens automaticamente.  
- **Resultado:** gráfico salvo em `consumo_regiao.png`.  

### Interpretação
- O gráfico de barras evidencia as diferenças no consumo médio entre as regiões, permitindo identificar claramente quais regiões apresentam maior ou menor consumo.  
- Essa visualização facilita comparações rápidas e ajuda a direcionar análises ou ações específicas para regiões com padrões de consumo distintos.

---

## 🔹 `consumo_por_classe()`
### Função
```python
def consumo_por_classe():
    try:
        df = pd.read_csv("./reports/file_0.csv")
        consumo_classe = df.groupby("Classe")["Consumo"].mean().sort_values()

        consumo_classe.plot(kind="bar", color="lightgreen", edgecolor="black")
        plt.title("Consumo Médio por Classe")
        plt.ylabel("Consumo Médio")
        plt.xlabel("Classe")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("./reports/consumo_classe.png")
        plt.show()
    except Exception as e:
        print(f"Erro ao gerar gráfico por classe: {e}")
        return False
```
### Explicação
- **Objetivo:** comparar o consumo médio entre diferentes classes (Residencial, Comercial, Industrial, etc.).  
- **`df.groupby("Classe")["Consumo"].mean()`**: agrupa dados por classe e calcula a média.  
- **`.sort_values()`**: facilita identificar quais classes mais consomem.  
- **`.plot(kind="bar")`**: gera gráfico de barras.  
- **Cores:** usa `lightgreen` para diferenciar do gráfico por região.  
- **Resultado:** gráfico salvo em `consumo_classe.png`.  

### Interpretação
- O gráfico de barras mostra as diferenças no consumo médio entre as classes, ajudando a entender quais setores (residencial, comercial, industrial, etc.) são os maiores consumidores.  
- Essa análise é importante para identificar quais setores têm maior impacto no consumo total e onde podem ser focadas estratégias de eficiência ou redução.

---