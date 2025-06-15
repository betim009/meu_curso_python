# Elementos e Estilização no CustomTkinter

Este guia apresenta os widgets mais comuns do **CustomTkinter** e mostra rapidamente como personalizá-los. Ele complementa o `readme.md` e os exemplos encontrados na pasta `10-customtkinter`.

## Configurando o Tema

Logo no início da aplicação, defina o modo de aparência (claro ou escuro) e o tema de cores padrão:

```python
import customtkinter as ctk

ctk.set_appearance_mode("dark")      # ou "light"
ctk.set_default_color_theme("dark-blue")
```

## Janela Principal

A classe `CTk` cria a janela principal. Nela é possível definir título e tamanho inicial:

```python
app = ctk.CTk()
app.title("Minha Aplicação")
app.geometry("400x300")
```

## Labels (`CTkLabel`)

Exibem textos ou informações na interface. Cores e fonte podem ser ajustadas com argumentos como `text_color` e `font`:

```python
label = ctk.CTkLabel(
    master=app,
    text="Olá, CustomTkinter!",
    text_color="cyan",
    font=("Arial", 16, "bold")
)
label.pack(pady=10)
```

## Campos de Entrada (`CTkEntry`)

Recebem texto digitado pelo usuário. É possível definir um `placeholder_text` e larguras personalizadas.

```python
nome_entry = ctk.CTkEntry(app, width=200, placeholder_text="Digite seu nome")
nome_entry.pack(padx=10, pady=5)
```

## Botões (`CTkButton`)

Além do texto e da função `command`, botões aceitam cores de fundo e de hover. No projeto `tabela_pagamentos/app.py` utiliza-se constantes para manter o padrão:

```python
BTN_COLOR = "#008B8B"
BTN_HOVER = "#00CED1"

enviar_btn = ctk.CTkButton(
    master=app,
    text="Enviar",
    command=enviar,
    fg_color=BTN_COLOR,
    hover_color=BTN_HOVER
)
enviar_btn.pack(pady=15)
```

## Frames (`CTkFrame`)

Servem para agrupar outros widgets. Você pode configurar `corner_radius` e cores para criar seções personalizadas:

```python
form_frame = ctk.CTkFrame(app, corner_radius=8, fg_color="#333333")
form_frame.pack(fill="both", expand=True, padx=10, pady=10)
```

## Abas (`CTkTabview`)

Permitem organizar a interface em páginas. No exemplo de pagamentos a janela possui duas abas:

```python
tabview = ctk.CTkTabview(app)
tabela_tab = tabview.add("Tabela")
novo_tab = tabview.add("Novo Pagamento")
```

Widgets podem ser colocados dentro de cada aba normalmente.

## Outras opções úteis

- **`CTkCheckBox` e `CTkRadioButton`** – Para seleções simples e múltiplas.
- **`CTkSlider` e `CTkProgressBar`** – Indicadores de valores. Suportam cores personalizadas.
- **`CTkToplevel`** – Cria janelas auxiliares, ideal para formulários de edição (veja a função `open_edit` em `tabela_pagamentos/app.py`).
- **`CTkScrollableFrame`** – Uma área rolável para muitos widgets.

## Dicas finais

- Use `pack` ou `grid` para posicionar os widgets. Combine `padx`, `pady` e `sticky` para ajustar o layout.
- Cores aceitam nomes padrão ou códigos HEX (`#rrggbb`).
- Mantenha as fontes e cores em variáveis para reutilizá-las em vários lugares.

Com esses elementos você consegue criar interfaces modernas e consistentes em Python utilizando o CustomTkinter. Consulte os arquivos `app.py`, `form_example.py` e o projeto `tabela_pagamentos` para exemplos completos.

