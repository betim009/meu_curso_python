import pandas as pd

def init_csv():
    try:
        for i in range(0, 2):
            df = pd.read_excel("./data/consumo.xlsx", sheet_name=i)
            df.to_csv(f"./data/file_{i}.csv", index=False)
        return True
    except Exception as e:
        print(f"Erro ao gerar CSV: {e}")
        return False
