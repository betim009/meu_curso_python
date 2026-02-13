import customtkinter as ctk

app = ctk.CTk()
app.geometry("500x300")

# Configura 3 colunas (máximo que vamos usar)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)

app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)


# Linha 0 → 2 colunas
ctk.CTkLabel(app, text="Coluna 1 da Linha 1").grid(row=0, column=0)
ctk.CTkLabel(app, text="Coluna 2 da Linha 1").grid(row=0, column=1)


# Linha 1 → 3 colunas
ctk.CTkLabel(app, text="Coluna 1 da Linha 2").grid(row=1, column=0)
ctk.CTkLabel(app, text="Coluna 2 da Linha 2").grid(row=1, column=1)
ctk.CTkLabel(app, text="Coluna 3 da Linha 2").grid(row=1, column=2)

app.mainloop()