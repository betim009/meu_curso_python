import pandas as pd

df_sheet1 = pd.read_excel("epitopes.xlsx")

# Para cada allele repetido, mantém apenas a linha com o menor percentile.
df_resultado = (
    df_sheet1.sort_values("netmhciipan_el percentile")
    .drop_duplicates(subset="allele", keep="first")
    .reset_index(drop=True)
)

df_resultado.to_excel("allele.xlsx")
