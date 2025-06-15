# 🎨 Introdução ao CustomTkinter

O **CustomTkinter** é uma biblioteca que permite criar interfaces gráficas modernas utilizando a base do Tkinter.
Este material mostra um exemplo simples de como instalar e usar a biblioteca.


## Preparando o Ambiente

Siga os passos abaixo para criar e ativar um **ambiente virtual** antes de instalar o CustomTkinter:

1. No terminal, navegue até esta pasta.
2. Crie o ambiente:

   ```bash
   python -m venv venv
   ```
3. Ative o ambiente:
   - **Windows**
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/macOS**
     ```bash
     source venv/bin/activate
     ```
4. Instale a biblioteca:

   ```bash
   pip install customtkinter
   ```
5. Para sair do ambiente, use `deactivate` (opcional).

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
