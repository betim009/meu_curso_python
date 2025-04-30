import streamlit as st
import pandas as pd

def main():
    medicos = pd.read_csv("medicos.csv")
    st.dataframe(medicos)

if __name__ == "__main__":
    main()