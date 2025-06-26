# 📄 Template de App Streamlit

Este diretório traz uma função **`init_app`** que serve como ponto de partida para novos projetos. Ela define configurações básicas e devolve a sidebar para inclusão de elementos.

```python
from template.base_app import init_app

sidebar = init_app("Minha Página", "Menu")
sidebar.write("Coloque suas opções aqui!")
```

A função cuida do `set_page_config`, define o título principal e, caso desejado, um título para a barra lateral.
