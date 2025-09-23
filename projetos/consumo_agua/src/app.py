# from view.overall import *
# from view.spread import *
from view.overall import overall_sam, overall_sam_uf
from hist.hist_overall import *
from scatter.scatter_overall import *
from view.decision import *
from utils.init_csv import init_csv


if __name__ == "__main__":
    init_csv()
    overall_sam.overall_average()
    overall_sam_uf.overall_average()

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
    # scatter_class()
    # scatter_region()
    # scatter_region_class()

    # compare_models()
    # print(predict_all("Residencial", "Sul"))
