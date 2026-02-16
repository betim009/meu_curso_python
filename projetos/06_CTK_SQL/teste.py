import customtkinter as ctk
import mysql.connector
from mysql.connector import Error


def button_callback():
    print("button clicked")


def connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="ctk_sql",
    )


def insertVenda(venda):
    conn = None
    cursor = None
    try:
        conn = connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO vendas (titulo, valor, metodo_pagamento, dia, mes, ano)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(
            query,
            (
                venda["titulo"],
                venda["valor"],
                venda["metodo_pagamento"],
                venda["dia"],
                venda["mes"],
                venda["ano"],
            ),
        )
        conn.commit()
        return True, "Venda salva com sucesso."
    except Error as error:
        return False, f"Erro ao salvar venda: {error}"
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()


def create_sale_form(parent):
    parent.grid_columnconfigure(0, weight=1)

    title = ctk.CTkLabel(parent, text="Cadastro de Venda", font=ctk.CTkFont(size=18, weight="bold"))
    title.grid(row=0, column=0, padx=16, pady=(16, 8), sticky="w")

    ctk.CTkLabel(parent, text="titulo").grid(row=1, column=0, padx=16, pady=(0, 4), sticky="w")
    titulo_entry = ctk.CTkEntry(parent, placeholder_text="Ex.: Venda de caderno")
    titulo_entry.grid(row=2, column=0, padx=16, pady=(0, 10), sticky="ew")

    ctk.CTkLabel(parent, text="valor").grid(row=3, column=0, padx=16, pady=(0, 4), sticky="w")
    valor_entry = ctk.CTkEntry(parent, placeholder_text="Ex.: 59.90")
    valor_entry.grid(row=4, column=0, padx=16, pady=(0, 10), sticky="ew")

    ctk.CTkLabel(parent, text="metodo_pagamento").grid(row=5, column=0, padx=16, pady=(0, 4), sticky="w")
    metodo_entry = ctk.CTkEntry(parent, placeholder_text="Ex.: pix")
    metodo_entry.grid(row=6, column=0, padx=16, pady=(0, 10), sticky="ew")

    ctk.CTkLabel(parent, text="dia").grid(row=7, column=0, padx=16, pady=(0, 4), sticky="w")
    dia_entry = ctk.CTkEntry(parent, placeholder_text="Ex.: 13")
    dia_entry.grid(row=8, column=0, padx=16, pady=(0, 10), sticky="ew")

    ctk.CTkLabel(parent, text="mes").grid(row=9, column=0, padx=16, pady=(0, 4), sticky="w")
    month_values = [
        "janeiro",
        "fevereiro",
        "marco",
        "abril",
        "maio",
        "junho",
        "julho",
        "agosto",
        "setembro",
        "outubro",
        "novembro",
        "dezembro",
    ]
    mes_select = ctk.CTkOptionMenu(parent, values=month_values)
    mes_select.grid(row=10, column=0, padx=16, pady=(0, 10), sticky="ew")

    ctk.CTkLabel(parent, text="ano").grid(row=11, column=0, padx=16, pady=(0, 4), sticky="w")
    ano_entry = ctk.CTkEntry(parent, placeholder_text="Ex.: 2026")
    ano_entry.grid(row=12, column=0, padx=16, pady=(0, 12), sticky="ew")
    status_label = ctk.CTkLabel(parent, text="")
    status_label.grid(row=13, column=0, padx=16, pady=(0, 8), sticky="w")

    def submit_sale():
        try:
            sale_data = {
                "titulo": titulo_entry.get().strip(),
                "valor": float(valor_entry.get()),
                "metodo_pagamento": metodo_entry.get().strip(),
                "dia": int(dia_entry.get()),
                "mes": mes_select.get(),
                "ano": int(ano_entry.get()),
            }
        except ValueError:
            status_label.configure(text="Valor, dia e ano precisam ser numericos.")
            return

        ok, message = insertVenda(sale_data)
        status_label.configure(text=message)

    submit_button = ctk.CTkButton(parent, text="Salvar venda", command=submit_sale)
    submit_button.grid(row=14, column=0, padx=16, pady=(0, 16), sticky="ew")


def create_month_buttons(parent):
    months = [
        "Janeiro",
        "Fevereiro",
        "Marco",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro",
    ]

    parent.grid_rowconfigure(0, weight=1)

    for col, month in enumerate(months):
        parent.grid_columnconfigure(col, weight=1)
        month_button = ctk.CTkButton(parent, text=month, command=button_callback)
        month_button.grid(row=0, column=col, padx=4, pady=0, sticky="")


def main():
    app = ctk.CTk()
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    app.geometry(f"{screen_width}x{screen_height}+0+0")

    # Container central para manter tudo no meio da janela
    layout = ctk.CTkFrame(app, corner_radius=0, fg_color="transparent")
    layout.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor="center")
    row_gap = 0.03  # 3% de margem vertical entre as linhas
    column_gap = 0.04  # 4% de margem horizontal entre as colunas
    left_col_width = 0.3
    right_col_width = 0.6
    left_margin = (1 - (left_col_width + right_col_width + column_gap)) / 2

    # Linha 1: 20% da altura da janela
    top_row = ctk.CTkFrame(layout, corner_radius=0, fg_color="#1c1c1c")
    top_row.place(relx=0, rely=0, relwidth=1, relheight=0.2)
    create_month_buttons(top_row)

    # Linha 2: 70% da altura da janela
    second_row = ctk.CTkFrame(layout, corner_radius=0, fg_color="#1c1c1c")
    second_row.place(relx=0, rely=0.2 + row_gap, relwidth=1, relheight=0.7)

    # Coluna 1 da linha 2: 30% da largura
    left_col = ctk.CTkFrame(second_row, corner_radius=0, fg_color="#6c6e6e")
    left_col.place(relx=left_margin, rely=0, relwidth=left_col_width, relheight=1)
    left_col_content = ctk.CTkScrollableFrame(left_col, fg_color="transparent")
    left_col_content.pack(fill="both", expand=True, padx=8, pady=8)
    create_sale_form(left_col_content)

    # Coluna 2 da linha 2: 60% da largura
    right_col = ctk.CTkFrame(second_row, corner_radius=0, fg_color="#6c6e6e")
    right_col.place(
        relx=left_margin + left_col_width + column_gap,
        rely=0,
        relwidth=right_col_width,
        relheight=1,
    )

    button = ctk.CTkButton(right_col, text="my button", command=button_callback)
    button.pack(padx=20, pady=20)

    app.mainloop()


if __name__ == "__main__":
    main()
