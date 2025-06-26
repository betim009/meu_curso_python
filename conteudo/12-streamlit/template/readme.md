# 🚀 Template para Projetos Streamlit

Este repositório é um **template base para novos projetos em Streamlit**.  
Aqui você encontra a estrutura recomendada, exemplos de uso dos principais métodos do Streamlit e instruções para rodar e expandir seu app.

---

## 📦 Estrutura do Projeto

```
template/
│
├── app.py                # Página inicial do app
├── requirements.txt      # Dependências do projeto
├── pages/                # Outras páginas do app (multipage)
│   ├── home.py
│   └── contato.py
└── readme.md             # Este guia
```

---

## ▶️ Como rodar o projeto

1. **Clone o repositório e acesse a pasta:**
   ```bash
   git clone <url-do-repo>
   cd template
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o app:**
   ```bash
   streamlit run app.py
   ```

---

## 🛠️ Métodos do Streamlit Utilizados

Abaixo estão os principais métodos usados neste template, com seus parâmetros mais comuns:

### `st.set_page_config`
Configurações globais da página.
```python
st.set_page_config(page_title="Título", layout="centered")
```
- **page_title**: str — Título da aba do navegador
- **page_icon**: str/emoji — Ícone da aba
- **layout**: "centered" (padrão) ou "wide"
- **initial_sidebar_state**: "auto", "expanded", "collapsed"

---

### `st.title`
Exibe um título grande na página.
```python
st.title("Título Principal")
```
- **body**: str — Texto do título

---

### `st.write`
Exibe texto, variáveis, listas, DataFrames, etc.
```python
st.write("Olá", 123, {"chave": "valor"})
```
- **args**: vários tipos — Conteúdo a ser exibido

---

### `st.text_input`
Campo para digitação de texto curto.
```python
nome = st.text_input("Seu nome")
```
- **label**: str — Texto acima do campo
- **value**: str — Valor inicial
- **max_chars**: int — Máximo de caracteres
- **type**: "default" ou "password"
- **placeholder**: str — Texto fantasma
- **key**: str — Identificador único

---

### `st.text_area`
Campo de texto multilinha.
```python
msg = st.text_area("Mensagem")
```
- **label**: str — Texto acima do campo
- **height**: int — Altura do campo (px)
- **max_chars**: int — Máximo de caracteres
- **placeholder**: str — Texto fantasma
- **key**: str — Identificador único

---

### `st.button`
Botão interativo.
```python
if st.button("Enviar"):
    st.success("Mensagem enviada!")
```
- **label**: str — Texto do botão
- **key**: str — Identificador único
- **help**: str — Texto de ajuda

---

### `st.success`
Mensagem de sucesso em destaque.
```python
st.success("Mensagem enviada com sucesso!")
```
- **body**: str — Texto exibido

---

## 🧩 Organização do Código

- Cada página do app deve ser criada como um arquivo Python dentro da pasta `pages/`.
- Para projetos maiores, recomenda-se organizar o código em funções para facilitar a manutenção e expansão.

---

## 📚 Documentação Oficial

Confira todos os widgets e recursos disponíveis em:  
[https://docs.streamlit.io/](https://docs.streamlit.io/)

---

Feito com ❤️ para acelerar o início dos seus projetos em Streamlit!
