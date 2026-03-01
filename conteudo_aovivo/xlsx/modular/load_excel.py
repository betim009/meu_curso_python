import pandas as pd

def load_excel(file, sheet=0, header=None, clean=False, type=str):
    data_frame = pd.read_excel(
        file,
        sheet_name=sheet,
        header=header,
        keep_default_na=clean,
        dtype=type,
    )

    return data_frame