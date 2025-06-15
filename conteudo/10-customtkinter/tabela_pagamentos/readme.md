# Visualizador de Pagamentos com CustomTkinter

Este projeto demonstra como exibir e gerenciar um arquivo CSV em uma interface gráfica utilizando **CustomTkinter** e **pandas**. Agora é possível visualizar, adicionar, editar e remover pagamentos de forma simples.

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

Uma janela será aberta com duas abas: a primeira exibe a tabela de pagamentos e a segunda permite inserir novos registros. Selecione uma linha da tabela para editá-la ou excluí-la.

## Explicação rápida

- O arquivo CSV é carregado com `pandas.read_csv`, preservando os valores como texto para manter a formatação.
- `CTkTabview` organiza a interface em abas de "Tabela" e "Novo Pagamento".
- Em cada linha da tabela há opções para editar ou remover o registro selecionado.
- A janela principal utiliza um grid que mantém a área da tabela com no máximo **60%** da largura disponível.
