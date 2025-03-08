### 1. **Leitura e Escrita de Dados**

* **`pd.read_csv()`**: Lê um arquivo CSV e retorna um DataFrame.
* **`pd.read_excel()`**: Lê um arquivo Excel.
* **`pd.read_sql()`**: Lê dados de uma consulta SQL.
* **`df.to_csv()`**: Salva um DataFrame em um arquivo CSV.
* **`df.to_excel()`**: Salva um DataFrame em um arquivo Excel.

### 2. **Inspeção de Dados**

* **`df.head()`**: Retorna as primeiras `n` linhas do DataFrame.
* **`df.tail()`**: Retorna as últimas `n` linhas do DataFrame.
* **`df.info()`**: Exibe um resumo do DataFrame, incluindo tipos de dados e valores não nulos.
* **`df.describe()`**: Retorna estatísticas descritivas (média, desvio padrão, etc.) para colunas numéricas.
* **`df.shape`**: Retorna uma tupla com o número de linhas e colunas.
* **`df.columns`**: Retorna uma lista com os nomes das colunas.
* **`df.dtypes`**: Retorna os tipos de dados de cada coluna.

### 3. **Seleção e Filtragem de Dados**

* **`df[coluna]`**: Seleciona uma coluna específica.
* **`df.loc[]`**: Seleciona linhas e colunas por rótulo.
* **`df.iloc[]`**: Seleciona linhas e colunas por índice inteiro.
* **`df.filter()`**: Filtra colunas ou linhas com base em padrões.
* **`df.query()`**: Filtra linhas com base em uma expressão booleana.

### 4. **Manipulação de Dados**

* **`df.drop()`**: Remove linhas ou colunas.
* **`df.rename()`**: Renomeia colunas ou índices.
* **`df.sort_values()`**: Ordena o DataFrame por valores de uma ou mais colunas.
* **`df.drop_duplicates()`**: Remove linhas duplicadas.
* **`df.fillna()`**: Preenche valores ausentes (NaN) com um valor específico.
* **`df.replace()`**: Substitui valores no DataFrame.

### 5. **Agregação e Agrupamento**

* **`df.groupby()`**: Agrupa dados com base em uma ou mais colunas.
* **`df.agg()`**: Aplica funções de agregação (como soma, média, etc.) a colunas.
* **`df.pivot_table()`**: Cria uma tabela dinâmica.
* **`df.crosstab()`**: Cria uma tabela de contingência.

### 6. **Combinação de DataFrames**

* **`pd.concat()`**: Concatena DataFrames ao longo de um eixo.
* **`pd.merge()`**: Combina DataFrames com base em uma chave comum (semelhante a um JOIN em SQL).
* **`df.join()`**: Junta DataFrames com base em índices.

### 7. **Transformação de Dados**

* **`df.apply()`**: Aplica uma função a uma coluna ou linha.
* **`df.map()`**: Mapeia valores de uma coluna para outros valores.
* **`df.pivot()`**: Transforma o DataFrame de long para wide format.
* **`df.melt()`**: Transforma o DataFrame de wide para long format.

### 8. **Manipulação de Índices**

* **`df.set_index()`**: Define uma coluna como índice.
* **`df.reset_index()`**: Reseta o índice para o padrão (0, 1, 2, ...).
* **`df.sort_index()`**: Ordena o DataFrame pelo índice.

### 9. **Estatísticas e Análise**

* **`df.corr()`**: Calcula a correlação entre colunas.
* **`df.cov()`**: Calcula a covariância entre colunas.
* **`df.value_counts()`**: Conta a frequência de valores únicos em uma coluna.
* **`df.isnull()`**: Retorna um DataFrame booleano indicando valores ausentes.
* **`df.notnull()`**: Retorna um DataFrame booleano indicando valores não ausentes.

### 10. **Visualização de Dados**

* **`df.plot()`**: Cria gráficos a partir dos dados do DataFrame.
* **`df.hist()`**: Cria histogramas para colunas numéricas.
* **`df.boxplot()`**: Cria boxplots para colunas numéricas.
