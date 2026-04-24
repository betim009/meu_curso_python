import streamlit as st

st.title("Olá, Streamlit!")

nome = st.text_input("Digite seu nome:")

if st.button("Saudar"):
    st.write(f"Bem-vindo, {nome}!")
