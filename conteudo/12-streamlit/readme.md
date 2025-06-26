# 🚀 Introdução ao Streamlit

O **Streamlit** é uma biblioteca que permite criar **aplicações web interativas** de forma rápida e simples, utilizando apenas Python. Com ele, você pode transformar scripts em páginas acessíveis no navegador, ideal para criar dashboards e protótipos.

---

## 📦 Instalação

1. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # ou
   venv\Scripts\activate    # Windows
   ```
2. Instale a biblioteca:
   ```bash
   pip install streamlit
   pip install -r requirements.txt

   ```

---

## 🖥️ Exemplo básico

Crie um arquivo `app.py` com o seguinte conteúdo:

```python
import streamlit as st

st.title("Olá, Streamlit!")

nome = st.text_input("Digite seu nome:")

if st.button("Saudar"):
    st.write(f"Bem-vindo, {nome}!")
```

Execute o aplicativo com:

```bash
streamlit run app.py
```

A aplicação abrirá no navegador padrão exibindo o título, um campo para digitar o nome e um botão para exibir a saudação.

---

## ✅ Conclusão

Com poucas linhas de código é possível criar interfaces amigáveis usando o Streamlit. Explore componentes como _sliders_, _charts_ e _tables_ para enriquecer suas aplicações.

## 📚 Outras seções

- [Template base](./template/readme.md): função para iniciar projetos rapidamente.
- [Widgets](./widgets/readme.md): lista e exemplos dos principais componentes interativos.
