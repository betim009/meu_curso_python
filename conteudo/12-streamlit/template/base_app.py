import streamlit as st


def init_app(title: str, sidebar_title: str | None = None) -> st.delta_generator.DeltaGenerator:
    """Configura uma estrutura básica para iniciar um novo app Streamlit.

    Parameters
    ----------
    title : str
        Título exibido na página principal.
    sidebar_title : str, optional
        Caso fornecido, título exibido na barra lateral.

    Returns
    -------
    st.delta_generator.DeltaGenerator
        Referência da sidebar para que você possa adicionar itens nela.
    """
    st.set_page_config(page_title=title)
    st.title(title)
    sidebar = st.sidebar
    if sidebar_title:
        sidebar.title(sidebar_title)
    return sidebar
