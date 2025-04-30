import pandas as pd
import streamlit as st


def main():
    st.title("Cidades do RJ")
    file = pd.read_csv("data.csv")

    input_cidade = st.text_input("Digite o nome da cidade:")

    if st.button("Buscar"):
        file = file[
            file["cidade"].str.contains(input_cidade, case=False, na=False)
        ]  # Filtra pelo nome digitado

    st.dataframe(file, hide_index=True)


if __name__ == "__main__":
    main()
