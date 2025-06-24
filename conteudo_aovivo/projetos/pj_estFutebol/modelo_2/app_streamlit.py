import streamlit as st
import pandas as pd
from scripts import cria_tabela

CSV_PATH = "partidas_jogadores.csv"

st.set_page_config(page_title="Tabela de Partidas e Jogadores", layout="wide")

# Sidebar para navegação
st.sidebar.title("Navegação")
page = st.sidebar.radio("Ir para:", ["Tabela", "Cadastrar nova partida", "Artilheiros", "Assistentes"])

def striped_custom(row):
    if row.name % 2 == 0:
        return ['background-color: #e0e0e0; color: #000000'] * len(row)
    else:
        return ['background-color: #23272f; color: #ffffff'] * len(row)

def striped_custom_reset(row):
    if row.name % 2 == 0:
        return ['background-color: #e0e0e0; color: #000000'] * len(row)
    else:
        return ['background-color: #23272f; color: #ffffff'] * len(row)

if page == "Tabela":
    st.title("Tabela de Partidas e Jogadores")
    df = cria_tabela()
    st.dataframe(df.style.apply(striped_custom, axis=1), use_container_width=True, height=450)

elif page == "Cadastrar nova partida":
    st.title("Cadastro de Nova Partida")
    with st.form("cadastro_partida"):
        id_jogador = st.number_input("ID do Jogador", min_value=0, step=1)
        nome_jogador = st.text_input("Nome do Jogador")
        id_partida = st.number_input("ID da Partida", min_value=0, step=1)
        time_atual = st.text_input("Time Atual")
        time_contra = st.text_input("Time Contra")
        minuto = st.number_input("Minutos jogado", min_value=0, step=1)
        data = st.text_input("Data (ex: 01/01/2025)")
        campeonato = st.text_input("Campeonato")
        gols = st.number_input("Gols", min_value=0, step=1)
        assistencia = st.number_input("Assistências", min_value=0, step=1)
        submit = st.form_submit_button("Cadastrar")

    if submit:
        if all([
            nome_jogador, time_atual, time_contra, data, campeonato
        ]):
            try:
                df = pd.read_csv(CSV_PATH)
            except FileNotFoundError:
                df = pd.DataFrame(columns=[
                    "id_jogador", "nome_jogador", "id_partida", "time_atual", "time_contra", "minuto", "data", "campeonato", "gols", "assistencia"
                ])
            nova_linha = {
                "id_jogador": int(id_jogador),
                "nome_jogador": nome_jogador,
                "id_partida": int(id_partida),
                "time_atual": time_atual,
                "time_contra": time_contra,
                "minuto": int(minuto),
                "data": data,
                "campeonato": campeonato,
                "gols": int(gols),
                "assistencia": int(assistencia)
            }
            df = pd.concat([df, pd.DataFrame([nova_linha])], ignore_index=True)
            df.to_csv(CSV_PATH, index=False)
            st.success("Nova partida cadastrada com sucesso!")
        else:
            st.error("Preencha todos os campos obrigatórios.")

elif page == "Artilheiros":
    st.title("Artilheiros - Quem fez mais gols")
    df = cria_tabela()
    artilheiros = df.groupby(["id_jogador", "nome_jogador", "time_atual"])["gols"].sum().reset_index()
    artilheiros = artilheiros.sort_values(by="gols", ascending=False).reset_index(drop=True)
    st.dataframe(artilheiros.style.apply(striped_custom_reset, axis=1), use_container_width=True, height=450)

elif page == "Assistentes":
    st.title("Assistentes - Quem fez mais assistências")
    df = cria_tabela()
    assistentes = df.groupby(["id_jogador", "nome_jogador", "time_atual"])["assistencia"].sum().reset_index()
    assistentes = assistentes.sort_values(by="assistencia", ascending=False).reset_index(drop=True)
    st.dataframe(assistentes.style.apply(striped_custom_reset, axis=1), use_container_width=True, height=450) 