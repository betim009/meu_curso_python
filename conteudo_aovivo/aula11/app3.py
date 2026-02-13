import customtkinter


def main():
    app = customtkinter.CTk()
    app.geometry("600x400")
    app.title("Grid Exemplo")

    app.grid_columnconfigure((0, 1), weight=1)
    app.grid_rowconfigure(1, weight=1)

    # Primeira linha sem divisão em colunas (ocupa as 2 colunas)
    linha1 = customtkinter.CTkLabel(app, text="Primeira linha sem coluna")
    linha1.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="ew")

    # Segunda linha com 2 colunas
    coluna_esquerda = customtkinter.CTkFrame(app)
    coluna_esquerda.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="nsew")

    coluna_direita = customtkinter.CTkFrame(app)
    coluna_direita.grid(row=1, column=1, padx=(10, 20), pady=10, sticky="nsew")

    customtkinter.CTkLabel(coluna_esquerda, text="valor1").pack(pady=(120, 6))
    customtkinter.CTkLabel(coluna_esquerda, text="valor2").pack(pady=6)
    customtkinter.CTkButton(coluna_esquerda).pack()

    customtkinter.CTkLabel(coluna_direita, text="valor3").pack(pady=(12, 6))
    customtkinter.CTkLabel(coluna_direita, text="valor4").pack(pady=6)

    return app


if __name__ == "__main__":
    app = main()
    app.mainloop()
