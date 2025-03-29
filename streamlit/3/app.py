import pandas as pd
import streamlit as st
from plot_pizza import create_plot_pizza

def main():
    st.title("Cidades do RJ")
    file = pd.read_csv("pacientes.csv")

    input_paciente = st.text_input("Pesquise o paciente:")

    if st.button("Buscar"):
        file = file[
            file["nome"].str.contains(input_paciente, case=False, na=False)
        ]  # Filtra pelo nome digitado

    st.dataframe(file, hide_index=True)

    fig_pizza = create_plot_pizza()
    
    st.pyplot(fig_pizza)

if __name__ == "__main__":
    main()
