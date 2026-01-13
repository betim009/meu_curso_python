import streamlit as st
import pandas as pd


if __name__ == "__main__":
    st.title("Bem vindo ao Cadastro de produtos")
    st.markdown("<h5>Insira as informacoes corretamente</h5>", unsafe_allow_html=True)

    if "produtos" not in st.session_state:
        st.session_state.produtos = []
    nome_produto = st.text_input("Nome do produto", key="nome")
    preco_produto = st.number_input("preco do produto", key="preco")
    marca_produto = st.text_input("Marca do produto", key="marca")
    categoria_produto = st.text_input("Categoria do produto", key="categoria")

    btn_cadastrar_produto = st.button("Cadastrar")
    if btn_cadastrar_produto:
        produto = {
            "nome": nome_produto,
            "preco": preco_produto,
            "marca": marca_produto,
            "categoria": categoria_produto
        }
        st.session_state.produtos.append(produto)

        df = pd.DataFrame([produto])
        csv_path = "produtos.csv"
        df.to_csv(csv_path, mode="a", index=False)

        st.text("Adicionado e salvo no CSV!")
        st.caption(f"Arquivo salvo em: {csv_path}")

    
    
