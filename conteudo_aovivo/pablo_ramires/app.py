import pandas as pd

raw = pd.read_csv("raw.csv")

motos = [
    {"id": 1, "modelo": "XRE", "preco": 18000},
    {"id": 2, "modelo": "Titan 160", "preco": 20000},
]

motos_2 = {
    "ids": [1, 2],
    "modelos": ["XRE", "Titan 160"],
    "precos": [18000, 20000]
}

df_motos = pd.DataFrame(motos).to_csv("motos.csv")
df_motos = pd.DataFrame(motos_2).to_csv("motos_2.csv")