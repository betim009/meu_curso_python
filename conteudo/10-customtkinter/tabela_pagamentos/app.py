import customtkinter as ctk
import pandas as pd
from tkinter import ttk


# Caminho do arquivo CSV de dados
DF_PATH = "pagamentos_empresas.csv"

def load_data(path: str) -> pd.DataFrame:
    """Carrega o CSV como texto para preservar a formatação."""
    return pd.read_csv(path, dtype=str, sep=",")


def filter_data(df: pd.DataFrame, text: str) -> pd.DataFrame:
    """Filtra o DataFrame verificando se o texto aparece em alguma coluna."""
    if not text:
        return df
    mask = df.apply(lambda col: col.str.contains(text, case=False, na=False))
    return df[mask.any(axis=1)]


def create_table(master: ctk.CTk, columns: list[str]) -> ttk.Treeview:
    """Cria um Treeview responsivo dentro de um frame com barras de rolagem."""
    frame = ctk.CTkFrame(master)
    frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)

    tree = ttk.Treeview(frame, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=120)

    vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")

    return tree


def populate_table(tree: ttk.Treeview, dataframe: pd.DataFrame) -> None:
    """Insere os dados no Treeview, limpando entradas antigas."""
    tree.delete(*tree.get_children())
    for row in dataframe.itertuples(index=False):
        tree.insert("", "end", values=row)


def main() -> None:
    data = load_data(DF_PATH)

    ctk.set_appearance_mode("system")
    app = ctk.CTk()
    app.title("Pagamentos de Empresas")
    app.geometry("1024x600")
    app.minsize(700, 400)
    app.rowconfigure(1, weight=1)
    app.columnconfigure(0, weight=1)

    search_frame = ctk.CTkFrame(app)
    search_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 0))
    search_frame.columnconfigure(0, weight=1)
    search_var = ctk.StringVar()

    entry = ctk.CTkEntry(search_frame, textvariable=search_var, placeholder_text="Buscar...")
    entry.grid(row=0, column=0, sticky="ew", padx=(0, 5))

    def perform_search(*_):
        filtered = filter_data(data, search_var.get())
        populate_table(tree, filtered)

    button = ctk.CTkButton(search_frame, text="Buscar", command=perform_search)
    button.grid(row=0, column=1)
    entry.bind("<Return>", perform_search)

    tree = create_table(app, list(data.columns))
    populate_table(tree, data)

    app.mainloop()


if __name__ == "__main__":
    main()
