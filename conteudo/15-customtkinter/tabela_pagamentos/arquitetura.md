# Arquitetura do Projeto

Este aplicativo demonstra como gerenciar um arquivo CSV em uma interface gráfica moderna com **CustomTkinter**. Ele permite visualizar, adicionar, editar e remover pagamentos registrados em `pagamentos_empresas.csv`.

## Visão geral
- **Linguagem:** Python 3
- **Bibliotecas:** `customtkinter` para interface e `pandas` para manipulação de dados.
- **Entrada de dados:** um arquivo CSV com diversas colunas de pagamentos.
- **Saída:** atualização do próprio CSV e exibição em formato de tabela.

## Algoritmo principal
1. **Leitura do CSV**: `load_data` carrega os registros para um `DataFrame` preservando o texto original.
2. **Criação da interface**: a função `main` configura o tema escuro e cria uma janela com duas abas.
3. **Exibição da tabela**: `create_table` monta um `Treeview` com rolagem e `populate_table` insere as linhas carregadas do arquivo.
4. **Filtragem**: ao digitar no campo de busca e pressionar Enter, `filter_data` filtra o `DataFrame` e a tabela é atualizada.
5. **Edição e remoção**: botões permitem editar ou excluir a linha selecionada, salvando as alterações no CSV.
6. **Adição de novos pagamentos**: a aba "Novo Pagamento" possui um formulário criado por `create_add_form` que insere novas linhas no final do arquivo.

## Detalhes do código
- `BTN_COLOR` e `BTN_HOVER` definem as cores padrão (cyan e darkcyan) dos botões.
- `create_table` organiza a tabela em um `CTkFrame` que ocupa cerca de 80% da altura da janela.
- `main` ajusta o grid da aplicação, configura o tema escuro e cria os widgets principais.
- Cada ação (buscar, adicionar, editar, excluir) é tratada por funções específicas que atualizam o `DataFrame` e persistem as mudanças no CSV.

Esta estrutura simples demonstra como unir `pandas` e `customtkinter` para criar uma interface de gerenciamento de dados enxuta e personalizável.
