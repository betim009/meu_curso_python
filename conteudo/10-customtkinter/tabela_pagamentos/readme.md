# Visualizador de Pagamentos com CustomTkinter

Este projeto demonstra como exibir um arquivo CSV em uma interface gráfica utilizando **CustomTkinter** e **pandas**. O exemplo lê o arquivo `pagamentos_empresas.csv` e apresenta os dados em uma tabela com rolagem.

## Estrutura

```
conteudo/10-customtkinter/
└─ tabela_pagamentos/
   ├─ app.py
   ├─ pagamentos_empresas.csv
   └─ readme.md
```

- **app.py** &ndash; código responsável por criar a janela e preencher a tabela.
- **pagamentos_empresas.csv** &ndash; arquivo de dados utilizado no exemplo.

## Como executar

1. Navegue até a pasta do projeto:

   ```bash
   cd conteudo/10-customtkinter/tabela_pagamentos
   ```

2. (Opcional) Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Instale as dependências necessárias:

   ```bash
   pip install customtkinter pandas
   ```

4. Execute o aplicativo:

   ```bash
   python app.py
   ```

Uma janela será aberta exibindo os dados do arquivo CSV em formato de tabela. Utilize as barras de rolagem para navegar pelas informações.

## Explicação rápida

- O arquivo CSV é carregado com `pandas.read_csv`, preservando os valores como texto para manter a formatação.
- `ttk.Treeview` é usado para criar a tabela, e o `customtkinter` fornece o estilo moderno da janela.
- O aplicativo é simples, servindo como base para projetos que precisem listar dados tabulares de maneira amigável.
