import streamlit as st
import pandas as pd

file_pacientes = pd.read_csv('pacientes.csv')
file_consultas = pd.read_csv('consultas.csv')

def main():
    st.title("Projeto - **NOME**")

    st.sidebar.title("Navegação")
    opcao = st.sidebar.radio("Escolha uma página:", ["Início", "Pacientes", "Consultas"])

    if opcao == "Início":
        st.title("Bem-vindo!")
        st.write("Esta é a página inicial.")
        
    elif opcao == "Pacientes":
        st.title("Pacientes")
        st.write("Informações dos pacientes")
        st.dataframe(file_pacientes, hide_index=True)
        
    elif opcao == "Consultas":
        st.title("Consultas")
        st.write("Informações de consultas")
        st.dataframe(file_consultas, hide_index=True)


if __name__ == "__main__":
    main()
