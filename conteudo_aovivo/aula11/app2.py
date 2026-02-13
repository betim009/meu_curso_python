import customtkinter


def main():
    app = customtkinter.CTk()
    app.geometry("600x520")
    app.title("Exemplo CheckBox")

    titulo = customtkinter.CTkLabel(app, text="Selecione interesses (CheckBox):")
    titulo.pack(pady=(20, 12))

    python_var = customtkinter.StringVar(value="off")
    dados_var = customtkinter.StringVar(value="off")
    web_var = customtkinter.StringVar(value="off")

    checkbox_python = customtkinter.CTkCheckBox(
        app, text="Python", variable=python_var, onvalue="on", offvalue="off"
    )
    checkbox_dados = customtkinter.CTkCheckBox(
        app, text="Dados", variable=dados_var, onvalue="on", offvalue="off"
    )
    checkbox_web = customtkinter.CTkCheckBox(
        app, text="Web", variable=web_var, onvalue="on", offvalue="off"
    )

    checkbox_python.pack(anchor="w", padx=20, pady=6)
    checkbox_dados.pack(anchor="w", padx=20, pady=6)
    checkbox_web.pack(anchor="w", padx=20, pady=6)

    return app


if __name__ == "__main__":
    app = main()
    app.mainloop()
