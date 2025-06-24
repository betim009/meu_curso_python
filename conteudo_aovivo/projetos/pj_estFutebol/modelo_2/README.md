# Projeto: Tabela de Partidas e Jogadores com Streamlit

Este projeto exibe uma tabela interativa de partidas e jogadores utilizando o Streamlit, tornando a visualização de dados simples e acessível via navegador web.

## Instalação

1. **Clone o repositório** (se ainda não fez):
   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>
   cd modelo_2
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate    # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install streamlit pandas
   ```

## Como rodar o app

Execute o comando abaixo no terminal dentro da pasta do projeto:

```bash
streamlit run app_streamlit.py
```

O navegador abrirá automaticamente mostrando a tabela.

## Customizações possíveis na tabela

Você pode personalizar a tabela alterando o código no arquivo `app_streamlit.py`. Algumas sugestões:

- **Ajustar a altura da tabela:**
  Modifique o parâmetro `height` em `st.dataframe(df, use_container_width=True, height=450)` para o valor desejado.

- **Ajustar a largura:**
  O parâmetro `use_container_width=True` faz a tabela ocupar toda a largura disponível. Para largura fixa, remova esse parâmetro.

- **Adicionar filtros interativos:**
  Utilize widgets do Streamlit, como `st.selectbox`, `st.multiselect` ou `st.slider` para filtrar os dados antes de exibir a tabela.

- **Permitir download da tabela:**
  Adicione:
  ```python
  st.download_button("Baixar CSV", df.to_csv(index=False), file_name="tabela.csv")
  ```

- **Destacar linhas ou colunas:**
  Use `st.dataframe` com pandas Styler para destacar valores:
  ```python
  st.dataframe(df.style.highlight_max(axis=0))
  ```

- **Exibir gráficos:**
  Utilize funções como `st.bar_chart(df)`, `st.line_chart(df)` para visualizar os dados de outras formas.

Consulte a [documentação oficial do Streamlit](https://docs.streamlit.io/) para mais ideias de customização! 