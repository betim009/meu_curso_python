import customtkinter as ctk


def main():
    ctk.set_appearance_mode("dark")

    app = ctk.CTk()
    app.title("Widgets CTk")
    app.geometry("800x800")

    # LABEL
    label = ctk.CTkLabel(app, text="Digite seu nome:")
    label.pack(pady=10)

    # ENTRY / INPUT
    entry = ctk.CTkEntry(app, placeholder_text="Seu nome")
    entry.pack(pady=10)

    # TEXTBOX / Text Label
    textbox = ctk.CTkTextbox(app, height=100)
    textbox.pack(pady=10)

    # OPTION MENU
    def opcao_escolhida(valor):
        print(f"Opção: {valor}\n")

    option_menu = ctk.CTkOptionMenu(
        app,
        values=["Aluno", "Professor", "Administrador"],
        command=opcao_escolhida
    )
    option_menu.pack(pady=10)

    # SWITCH
    def switch_event():
        estado = switch.get()
        print(f"Switch: {estado}\n")

    switch = ctk.CTkSwitch(
        app,
        text="Modo Ativo",
        command=switch_event
    )
    switch.pack(pady=10)

    # SLIDER
    def slider_event(valor):
        label_slider.configure(text=f"Volume: {int(valor)}")

    slider = ctk.CTkSlider(
        app,
        from_=0,
        to=100,
        command=slider_event
    )
    slider.pack(pady=10)

    label_slider = ctk.CTkLabel(app, text="Volume: 0")
    label_slider.pack()

    # ==========================
    # BUTTON
    # ==========================

    def enviar():
        nome = entry.get()
        textbox.insert("end", f"Nome digitado: {nome}\n")
        entry.delete(0, "end")

    button = ctk.CTkButton(app, text="Enviar", command=enviar)
    button.pack(pady=20)

    app.mainloop()


if __name__ == "__main__":
    main()