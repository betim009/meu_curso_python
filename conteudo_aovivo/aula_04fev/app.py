import pandas as pd
import tkinter as tk

usuarios = [
    {"nome": "Alberto"},
    {"nome": "Alexandre"}
]


tabela = pd.DataFrame(usuarios)


def on_cadastrar():
    tabela.to_csv("arquivo3.csv", index=False)
    print("Registro salvo em arquivo3.csv")


root = tk.Tk()
root.title("App de Cadastro")

button = tk.Button(root, text="Cadastrar", command=on_cadastrar)
button.pack(padx=20, pady=20)

root.mainloop()