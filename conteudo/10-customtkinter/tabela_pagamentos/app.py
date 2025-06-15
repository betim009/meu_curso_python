import customtkinter as ctk
import pandas as pd
from tkinter import ttk

DF_PATH = "pagamentos_empresas.csv"


def load_data(path: str) -> pd.DataFrame:
    """Carrega o CSV preservando o texto"""
    return pd.read_csv(path, dtype=str, sep=",")


def save_data(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path, index=False)


def filter_data(df: pd.DataFrame, text: str) -> pd.DataFrame:
    if not text:
        return df
    mask = df.apply(lambda col: col.str.contains(text, case=False, na=False))
    return df[mask.any(axis=1)]


def create_table(master: ctk.CTk, columns: list[str]) -> ttk.Treeview:
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
    tree.delete(*tree.get_children())
    for idx, row in dataframe.iterrows():
        tree.insert("", "end", iid=str(idx), values=list(row))


def create_add_form(tab: ctk.CTkFrame, columns: list[str], callback):
    entries = {}
    for i, col in enumerate(columns):
        label = ctk.CTkLabel(tab, text=col)
        entry = ctk.CTkEntry(tab)
        label.grid(row=i, column=0, sticky="e", padx=5, pady=2)
        entry.grid(row=i, column=1, sticky="ew", padx=5, pady=2)
        entries[col] = entry
    tab.columnconfigure(1, weight=1)
    btn = ctk.CTkButton(tab, text="Adicionar", command=lambda: callback(entries))
    btn.grid(row=len(columns), column=0, columnspan=2, pady=10)
    return entries


def main() -> None:
    data = load_data(DF_PATH)
    columns = list(data.columns)

    ctk.set_appearance_mode("system")
    app = ctk.CTk()
    app.title("Pagamentos de Empresas")
    app.geometry("1024x600")
    app.minsize(700, 400)

    # Grid para manter 60% do tamanho
    app.columnconfigure(0, weight=2)
    app.columnconfigure(1, weight=6)
    app.columnconfigure(2, weight=2)
    app.rowconfigure(0, weight=1)

    tabview = ctk.CTkTabview(app)
    tabview.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    table_tab = tabview.add("Tabela")
    add_tab = tabview.add("Novo Pagamento")

    # ---- tabela ----
    table_tab.rowconfigure(2, weight=1)
    table_tab.columnconfigure(0, weight=1)

    search_frame = ctk.CTkFrame(table_tab)
    search_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10))
    search_frame.columnconfigure(0, weight=1)
    search_var = ctk.StringVar()
    entry = ctk.CTkEntry(search_frame, textvariable=search_var, placeholder_text="Buscar...")
    entry.grid(row=0, column=0, sticky="ew", padx=(0, 5))

    tree = create_table(table_tab, columns)
    populate_table(tree, data)

    def perform_search(*_):
        filtered = filter_data(data, search_var.get())
        populate_table(tree, filtered)

    entry.bind("<Return>", perform_search)
    ctk.CTkButton(search_frame, text="Buscar", command=perform_search).grid(row=0, column=1)

    action_frame = ctk.CTkFrame(table_tab)
    action_frame.grid(row=3, column=0, pady=(5, 0))

    def delete_selected():
        selected = tree.selection()
        if not selected:
            return
        idx = int(selected[0])
        tree.delete(selected[0])
        nonlocal data
        data = data.drop(idx)
        save_data(data, DF_PATH)
        populate_table(tree, data)

    def open_edit():
        selected = tree.selection()
        if not selected:
            return
        idx = int(selected[0])
        values = data.loc[idx].tolist()
        win = ctk.CTkToplevel(app)
        win.title("Editar")
        ent = {}
        for i, col in enumerate(columns):
            ctk.CTkLabel(win, text=col).grid(row=i, column=0, sticky="e", padx=5, pady=2)
            e = ctk.CTkEntry(win)
            e.insert(0, values[i])
            e.grid(row=i, column=1, sticky="ew", padx=5, pady=2)
            ent[col] = e
        win.columnconfigure(1, weight=1)
        def save_edit():
            for col in columns:
                data.at[idx, col] = ent[col].get()
            save_data(data, DF_PATH)
            populate_table(tree, data)
            win.destroy()
        ctk.CTkButton(win, text="Salvar", command=save_edit).grid(row=len(columns), column=0, columnspan=2, pady=10)

    ctk.CTkButton(action_frame, text="Excluir Selecionado", command=delete_selected).pack(side="left", padx=5)
    ctk.CTkButton(action_frame, text="Editar Selecionado", command=open_edit).pack(side="left", padx=5)

    # ---- adicionar ----
    add_tab.columnconfigure(1, weight=1)

    def add_payment(entries):
        nonlocal data
        row = {col: entries[col].get() for col in columns}
        new_row = pd.DataFrame([row])
        data = pd.concat([data, new_row], ignore_index=True)
        save_data(data, DF_PATH)
        populate_table(tree, data)
        for e in entries.values():
            e.delete(0, "end")

    create_add_form(add_tab, columns, add_payment)

    app.mainloop()


if __name__ == "__main__":
    main()
