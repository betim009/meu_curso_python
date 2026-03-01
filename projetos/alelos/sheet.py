import pandas as pd

if __name__ == "__main__":
    resultados = []

    for i in range(15):
        df_sheet = pd.read_excel("epitopes.xlsx", sheet_name=i)

        df_resultado = (
            df_sheet.sort_values("netmhciipan_el percentile")
            .drop_duplicates(subset="allele", keep="first")
            .reset_index(drop=True)
        )
        df_resultado["origem_sheet"] = i
        resultados.append(df_resultado)

    df_final = pd.concat(resultados, ignore_index=True)
    df_final.to_excel("alelos_filtrados.xlsx", sheet_name="resultado_unico", index=False)

    # Cria novo arquivo com cada allele como coluna e os percentiles como valores
    df_gerado = pd.read_excel("alelos_filtrados.xlsx", sheet_name="resultado_unico")
    df_pivot = df_gerado[["allele", "netmhciipan_el percentile"]].copy()
    df_pivot["ordem"] = df_pivot.groupby("allele").cumcount()
    df_saida = (
        df_pivot.pivot(
            index="ordem",
            columns="allele",
            values="netmhciipan_el percentile",
        )
        .reset_index(drop=True)
    )
    df_saida.to_excel("alelos_percentile_colunas.xlsx", index=False)
