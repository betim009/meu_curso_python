import pandas as pd

if __name__ == "__main__":
    with pd.ExcelWriter("alelos_filtrados.xlsx", engine="openpyxl") as writer:
        for i in range(15):
            df_sheet = pd.read_excel("epitopes.xlsx", sheet_name=i)

            df_resultado = (
                df_sheet.sort_values("netmhciipan_el percentile")
                .drop_duplicates(subset="allele", keep="first")
                .reset_index(drop=True)
            )

            df_resultado.to_excel(writer, sheet_name=f"sheet_{i}", index=False)
