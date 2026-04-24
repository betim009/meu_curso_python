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

---

## Criando um formul\u00e1rio simples

Vamos adicionar **campos de texto** e um **bot\u00e3o** para capturar dados digitados pelo usu\u00e1rio.
O exemplo abaixo cria um peque\u00f1o formul\u00e1rio com os campos *Nome* e *E-mail*.

```python
import customtkinter as ctk


def enviar():
    nome = nome_entry.get()
    email = email_entry.get()
    print(f"Nome: {nome} | Email: {email}")


app = ctk.CTk()
app.title("Formul\u00e1rio simples")
app.geometry("300x240")

ctk.CTkLabel(app, text="Nome").pack(padx=10, pady=(10, 0), fill="x")
nome_entry = ctk.CTkEntry(app)
nome_entry.pack(padx=10, pady=5, fill="x")

ctk.CTkLabel(app, text="E-mail").pack(padx=10, pady=(10, 0), fill="x")
email_entry = ctk.CTkEntry(app)
email_entry.pack(padx=10, pady=5, fill="x")

ctk.CTkButton(app, text="Enviar", command=enviar).pack(pady=15)

app.mainloop()
```

Salve o exemplo em `form_example.py` e execute com:

```bash
python form_example.py
```

Ao clicar em **Enviar**, os valores digitados s\u00e3o exibidos no terminal.
