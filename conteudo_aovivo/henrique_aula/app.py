import streamlit as st
import pandas as pd


if __name__ == "__main__":
    st.title("Bem vindo")
    st.markdown("<h5>Formulario de Cadastro</h5>", unsafe_allow_html=True)

    # Linha abaixo obrigatoria 
    if "formulario_cadastro" not in st.session_state:
        st.session_state.formulario_cadastro = []

    nome_produto = st.text_input("Nome do produto", key="nome")
    prico_produto = st.number_input("Preco do pruduto", key="preco")

    btn_cadastrar_produto = st.button("Cadastrar")
    if btn_cadastrar_produto:
        produto = {
            "nome": nome_produto, 
            "preco": prico_produto
        }

        st.session_state.formulario_cadastro.append(produto)
        formulario = st.session_state.formulario_cadastro
        df = pd.DataFrame(formulario)
        df.to_csv("demo_1.csv", mode="a", index=False)