# 🎨 Introdução ao CustomTkinter

O **CustomTkinter** é uma biblioteca que permite criar interfaces gráficas modernas utilizando a base do Tkinter.
Este material mostra um exemplo simples de como instalar e usar a biblioteca.

## Instalação

```bash
pip install customtkinter
```

## Exemplo básico

```python
import customtkinter as ctk

app = ctk.CTk()
app.title("Exemplo CustomTkinter")
app.geometry("300x200")

label = ctk.CTkLabel(app, text="Olá, CustomTkinter!")
label.pack(padx=10, pady=10)

app.mainloop()
```

Salve o código acima em um arquivo `app.py` e execute com:

```bash
python app.py
```

Assim, uma janela será aberta exibindo a mensagem do label.
