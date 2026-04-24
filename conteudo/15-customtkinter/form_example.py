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
