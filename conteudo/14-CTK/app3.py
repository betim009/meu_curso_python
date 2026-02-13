import customtkinter as ctk

app = ctk.CTk()
app.geometry("700x400")

# -----------------------
# CONFIGURA GRID PRINCIPAL
# -----------------------

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=0)

# -----------------------
# FRAME 1 - FORMULÁRIO
# -----------------------

frame_form = ctk.CTkFrame(app)
frame_form.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

label = ctk.CTkLabel(frame_form, text="Digite algo:")
label.pack(pady=10)

entry = ctk.CTkEntry(frame_form)
entry.pack(pady=10)

button = ctk.CTkButton(frame_form, text="Buscar")
button.pack(pady=10)

# -----------------------
# FRAME 2 - RESULTADO
# -----------------------

frame_resultado = ctk.CTkFrame(app)
frame_resultado.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

titulo = ctk.CTkLabel(
    frame_resultado,
    text="Resultado da sua busca",
    font=("Arial", 18)
)
titulo.pack(pady=10)

paragrafo = ctk.CTkLabel(
    frame_resultado,
    text="Aqui aparecerá o resultado da sua busca.\nExemplo de texto qualquer.",
    wraplength=250,
    justify="left"
)
paragrafo.pack(pady=10)

# -----------------------
# FRAME 3 - RODAPÉ
# -----------------------

frame_footer = ctk.CTkFrame(app)
frame_footer.grid(
    row=1,
    column=0,
    columnspan=2,  # ocupa as 2 colunas
    sticky="ew",
    padx=10,
    pady=10
)

rodape = ctk.CTkLabel(frame_footer, text="2026")
rodape.pack(pady=5)

app.mainloop()