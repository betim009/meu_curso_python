import streamlit as st
import requests


def main():
    st.set_page_config(page_title="App Base", layout="centered")
    st.title("API DE FUTEBOL")

    url = (
        "https://free-api-live-football-data.p.rapidapi.com/football-get-list-all-team"
    )
    querystring = {"leagueid": "42"}
    headers = {
        "x-rapidapi-key": "3be01a29a9msh1147fa36f6934f8p13aa60jsn802d2dd1cc9f",
        "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com",
    }

    response = requests.get(url, headers=headers, params=querystring).json()
    data = response["response"]["list"]

    cl1, cl2, cl3, cl4 = st.columns([0.9, 0.9, 0.9, 0.9])
    with cl2:
        st.markdown("**Time**")

    with cl3:
        st.markdown("**Vitória**")

    with cl4:
        st.markdown("**Derrota**")

    for item in data:
        col1, col2, col3, col4 = st.columns([0.9, 0.9, 0.9, 0.9])

        with col1:
            st.image(item["logo"], width=26)

        with col2:
            st.markdown(f"**{item['name']}**")

        with col3:
            st.markdown(f"*{item['wins']} vitórias*")

        with col4:
            st.markdown(f"*{item['losses']} derrotas*")
        
        st.markdown(f"---")


if __name__ == "__main__":
    main()
