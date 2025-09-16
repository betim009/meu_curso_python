# Projeto de Ciência de Dados: Consumo de Água

## Descrição
Este projeto tem como objetivo analisar dados de consumo de água, aplicando técnicas de ciência de dados com Python e Pandas.  
O fluxo inclui leitura de dados, exportação para CSV, análise estatística e visualizações de gráficos.

## Tecnologias Utilizadas
- Python 3
- Pandas
- Matplotlib

## Estrutura do Projeto
```
src/app.py         # Código principal com funções de análise
reports/           # Saída dos arquivos CSV e gráficos
data/consumo.xlsx  # Planilha de entrada
```

## Funcionalidades
- **init_csv()** → Lê a planilha `consumo.xlsx` e exporta para CSV.  
- **overall_average()** → Calcula média, mediana, moda, maior e menor consumo.  
- **overall_hist()** → Gera histograma da distribuição de consumo.  
- **consumo_por_regiao()** → Gera gráfico de barras com consumo médio por região.  
- **consumo_por_classe()** → Gera gráfico de barras com consumo médio por classe.  

## Exemplos de Saída
- Histograma de distribuição do consumo (`reports/hist_consumo.png`)  
- Gráfico de barras do consumo por região (`reports/consumo_regiao.png`)  
- Gráfico de barras do consumo por classe (`reports/consumo_classe.png`)  

## Executando dependências

### Criando ambiente virtual (venv)
É recomendado criar um ambiente virtual para isolar as dependências do projeto.

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Instalando dependências
Você pode instalar manualmente ou usar o arquivo `requirements.txt`.

**Instalação manual**
```bash
pip install pandas matplotlib
```

**Instalação via requirements.txt**
```bash
pip install -r requirements.txt
```

### Executando o projeto
Certifique-se de que o arquivo `data/consumo.xlsx` esteja no diretório correto.  
Depois, rode:
```bash
python src/app.py
```