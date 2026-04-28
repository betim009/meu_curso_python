import streamlit as st


st.set_page_config(page_title="Primeiro App", layout="centered")

st.title("Meu primeiro app com Streamlit")
st.write("Este app mostra como criar uma tela simples usando apenas Python.")

nome = st.text_input("Digite seu nome")

if st.button("Enviar"):
    if nome:
        st.success(f"Ola, {nome}!")
    else:
        st.warning("Digite um nome antes de enviar.")
