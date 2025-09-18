import pandas as pd

from view.overall import *
from hist.hist_overall import *
from view.spread import *
from scatter.scatter_overall import *


def init_csv():
    try:
        df = pd.read_excel("./data/consumo.xlsx", sheet_name=0)
        for i in range(2):
            df.to_csv(f"./data/file_{i}.csv", index=False)
        return True
    except Exception as e:
        print(f"Erro ao gerar CSV: {e}")
        return False


if __name__ == "__main__":
    # overall_average()
    # overall_class_average()
    # overall_region_average()
    # overall_region_class_average()

    # spread_overral()
    # spread_class_consumo()
    # spread_region_consumo()
    # spread_region_class_consumo()

    # hist_overall()
    # hist_class()
    # hist_regiao()

    # overall_scatter()
    scatter_class()
    scatter_region()
    scatter_region_class()
    # pass
