### Comando para iniciar um projeto novo
    py -m venv venv

    .\venv\Scripts\Activate

    pip install -r requirements.txt

    streamlit run app.py


# Elementos Visuais do Streamlit

## Textos
- `st.title("Título")` → Exibe um título grande.
- `st.header("Cabeçalho")` → Exibe um cabeçalho.
- `st.subheader("Subcabeçalho")` → Exibe um subcabeçalho.
- `st.text("Texto simples")` → Exibe um texto básico.
- `st.markdown("**Texto em negrito**")` → Exibe texto formatado em Markdown.

## Entrada de Dados
- `st.text_input("Nome:")` → Campo de entrada de texto.
- `st.number_input("Idade:", min_value=0, max_value=100)` → Campo numérico.
- `st.text_area("Comentário:")` → Área de texto maior.
- `st.selectbox("Escolha uma opção:", ["Opção 1", "Opção 2"])` → Menu suspenso.
- `st.radio("Escolha uma opção:", ["A", "B", "C"])` → Botões de rádio.
- `st.checkbox("Aceito os termos")` → Caixa de seleção.
- `st.slider("Escolha um número:", 0, 100)` → Controle deslizante.
- `st.file_uploader("Envie um arquivo")` → Upload de arquivo.

## Botões
- `st.button("Clique Aqui")` → Botão simples.
- `st.download_button("Baixar Arquivo", data, file_name="dados.txt")` → Botão de download.

## Exibição de Dados
- `st.write("Texto ou variável")` → Exibe diversos tipos de dados.
- `st.json({"chave": "valor"})` → Exibe um JSON formatado.
- `st.dataframe(df)` → Exibe um dataframe interativo.
- `st.table(df)` → Exibe uma tabela estática.
- `st.metric("Vendas", "R$ 1000", "+10%")` → Exibe métrica com variação.

## Gráficos
- `st.line_chart(df)` → Gráfico de linha.
- `st.bar_chart(df)` → Gráfico de barras.
- `st.pyplot(fig)` → Exibe um gráfico do Matplotlib.

## Layout
- `st.sidebar.button("Menu Lateral")` → Adiciona elemento na barra lateral.
- `col1, col2 = st.columns(2)` → Cria colunas para organizar elementos.
- `st.expander("Mais informações")` → Seção expansível.

## Template para Novo Projeto
```python
import streamlit as st

def main():
    st.title("Meu Novo Projeto Streamlit")
    st.write("Bem-vindo ao meu app!")
    
    if st.button("Clique aqui"):
        st.write("Botão pressionado!")

if __name__ == "__main__":
    main()
```


