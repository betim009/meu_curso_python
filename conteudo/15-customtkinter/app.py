import customtkinter as ctk

app = ctk.CTk()
app.title("Exemplo CustomTkinter")
app.geometry("300x200")

label = ctk.CTkLabel(app, text="Olá, CustomTkinter!")
label.pack(padx=10, pady=10)

app.mainloop()
