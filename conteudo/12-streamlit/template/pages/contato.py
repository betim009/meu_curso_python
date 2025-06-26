import streamlit as st

def contato():
    st.title("Contato")
    email = st.text_input("Seu e-mail")
    mensagem = st.text_area("Sua mensagem")
    if st.button("Enviar"):
        st.success("Mensagem enviada com sucesso!")

contato()