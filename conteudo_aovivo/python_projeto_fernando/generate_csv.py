import pandas as pd

def generate_csv(lista, path_csv):
    data_frame = pd.DataFrame(lista)
    data_frame.to_csv(path_csv)

    return "Feito!"