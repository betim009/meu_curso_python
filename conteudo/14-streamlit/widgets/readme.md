# 🧩 Widgets do Streamlit

Esta página apresenta os principais widgets disponíveis no Streamlit. Utilize-os para coletar entrada do usuário e exibir informações de forma interativa.

| Widget | Descrição | Exemplo |
|--------|-----------|---------|
| `st.button` | Botão simples que executa uma ação quando clicado | `if st.button('Enviar'):` |
| `st.text_input` | Campo de texto de uma linha | `nome = st.text_input('Digite seu nome')` |
| `st.text_area` | Campo de texto multilinha | `obs = st.text_area('Observações')` |
| `st.number_input` | Entrada numérica com incremento | `qtd = st.number_input('Quantidade', step=1)` |
| `st.slider` | Seleção em barra deslizante | `idade = st.slider('Idade', 0, 100)` |
| `st.selectbox` | Caixa de seleção única | `opcao = st.selectbox('Escolha', ['A', 'B', 'C'])` |
| `st.multiselect` | Seleção múltipla | `opts = st.multiselect('Opções', ['A', 'B', 'C'])` |
| `st.checkbox` | Caixa de seleção booleana | `aceito = st.checkbox('Aceito os termos')` |
| `st.radio` | Seleção única em lista de opções | `cor = st.radio('Cor', ['Azul', 'Verde'])` |
| `st.date_input` | Seleção de datas | `dt = st.date_input('Data')` |
| `st.time_input` | Seleção de horário | `horario = st.time_input('Horário')` |
| `st.file_uploader` | Envio de arquivos | `arquivo = st.file_uploader('CSV', type='csv')` |
| `st.color_picker` | Escolha de cor | `cor = st.color_picker('Cor')` |

Explore mais componentes na [documentação oficial](https://docs.streamlit.io/).
