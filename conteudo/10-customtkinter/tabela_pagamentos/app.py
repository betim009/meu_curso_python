import customtkinter as ctk
import pandas as pd
from tkinter import ttk


# Carrega o arquivo CSV em um DataFrame
DF_PATH = "pagamentos_empresas.csv"

def load_data(path: str) -> pd.DataFrame:
    """Carrega o CSV como texto para preservar a formatação."""
    return pd.read_csv(path, dtype=str, sep=',')


def create_table(master: ctk.CTk, dataframe: pd.DataFrame) -> None:
    """Cria um Treeview dentro de um frame com barras de rolagem."""
    frame = ctk.CTkFrame(master)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    columns = list(dataframe.columns)
    tree = ttk.Treeview(frame, columns=columns, show="headings")

    # Define cabeçalhos
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center")

    # Barras de rolagem
    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(yscroll=vsb.set, xscroll=hsb.set)

    vsb.pack(side="right", fill="y")
    hsb.pack(side="bottom", fill="x")
    tree.pack(side="left", expand=True, fill="both")

    # Insere as linhas
    for row in dataframe.itertuples(index=False):
        tree.insert("", "end", values=row)


def main() -> None:
    data = load_data(DF_PATH)

    app = ctk.CTk()
    app.title("Pagamentos de Empresas")
    app.geometry("1000x600")

    create_table(app, data)

    app.mainloop()


if __name__ == "__main__":
    main()
