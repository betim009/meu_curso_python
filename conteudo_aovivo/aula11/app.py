import customtkinter
import pandas as pd
from pathlib import Path


CSV_FILE = Path("clientes.csv")
COLUNAS = ["nome", "idade", "email", "cidade", "estado"]


def salvar_clientes(clientes):
    df = pd.DataFrame(clientes, columns=COLUNAS)
    df.to_csv(CSV_FILE, index=False, encoding="utf-8")

def main():
    app = customtkinter.CTk()
    app.geometry("600x520")
    app.title("Cadastro de Clientes")

    clientes = []
    entries = {}
    estado_var = customtkinter.StringVar(value="ES")

    titulo = customtkinter.CTkLabel(app, text="Cadastro de clientes", font=("Arial", 20))
    titulo.pack(pady=(20, 15))

    formulario = customtkinter.CTkFrame(app)
    formulario.pack(fill="x", padx=20, pady=10)

    for coluna in COLUNAS:
        label = customtkinter.CTkLabel(formulario, text=coluna.capitalize())
        label.pack(anchor="w", padx=10, pady=(8, 2))

        if coluna == "estado":
            option_estado = customtkinter.CTkOptionMenu(
                formulario,
                values=["ES", "RJ", "SP", "RS"],
                variable=estado_var,
            )
            option_estado.pack(fill="x", padx=10, pady=(0, 8))
        else:
            entry = customtkinter.CTkEntry(formulario, placeholder_text=f"Digite {coluna}")
            entry.pack(fill="x", padx=10, pady=(0, 8))
            entries[coluna] = entry

    acoes = customtkinter.CTkFrame(app, fg_color="transparent")
    acoes.pack(fill="x", padx=20, pady=(8, 0))

    status_label = customtkinter.CTkLabel(app, text="", text_color="green")
    status_label.pack(pady=(8, 6))

    def cadastrar_cliente():
        cliente = {coluna: entries[coluna].get().strip() for coluna in entries}
        cliente["estado"] = estado_var.get().strip()

        if not all(cliente.values()):
            status_label.configure(text="Preencha todos os campos.", text_color="red")
            return

        clientes.append(cliente)
        salvar_clientes(clientes)

        for entry in entries.values():
            entry.delete(0, "end")
        estado_var.set("ES")

        status_label.configure(text="Cliente cadastrado e salvo no CSV.", text_color="green")

    btn = customtkinter.CTkButton(acoes, text="Cadastrar", command=cadastrar_cliente)
    btn.pack(fill="x")

    return app


if __name__ == "__main__":
    app = main()
    app.mainloop()
