import pandas as pd

class ExcelLoader:
    def __init__(self, df=None):
        self.df = df

    def carregar_excel(self, file, sheet=0, header=None, clean=False, tipo=str):
        self.df = pd.read_excel(
            file,
            sheet_name=sheet,
            header=header,
            keep_default_na=clean,
            dtype=tipo,
        )
        return self

    def carregar_csv(self, file, separador=","):
        self.df = pd.read_csv(file, sep=separador)
        return self

    def salvar_excel(self, nome):
        self.df.to_excel(nome, index=False)
        return self

    def get_df(self):
        return self.df


class DataFrameCleaner:
    def __init__(self, df):
        self.df = df

    def limpar(self):
        self.df = self.df.apply(lambda col: col.astype(str).str.strip())

        self.df = self.df.replace({"": pd.NA, "-": pd.NA, "nan": pd.NA, "None": pd.NA})

        self.df = self.df.dropna(how="all")

        return self

    def criar_colunas(self, index_col):
        linha_das_colunas = self.df.iloc[index_col]
        self.df.columns = linha_das_colunas
        self.df = self.df[index_col + 1 :]
        return self

    def corrigir_coluna_vazia(self, coluna, valor="-"):
        if coluna not in self.df.columns:
            raise ValueError(f"Coluna '{coluna}' não encontrada.")

        for index, row in self.df.iterrows():
            valor_atual = row[coluna]

            if pd.isna(valor_atual) or str(valor_atual).strip() == "":
                self.df.at[index, coluna] = valor

        return self

    def get_df(self):
        return self.df


class DataFrameFilter:
    def __init__(self, df):
        self.df = df

    def filtrar_coluna(self, coluna, valor):
        new_df = []

        for i, row in self.df.iterrows():
            try:
                if valor in row[coluna]:
                    new_df.append(row)
            except TypeError as error:
                print(f"Erro na linha: {i}", error)
                continue

        self.df = pd.DataFrame(new_df)
        return self

    def filtrar_coluna_null(self, coluna, valor):
        new_df = []

        for i, row in self.df.iterrows():
            try:
                if valor in row[coluna] or "-" in row[coluna]:
                    new_df.append(row)
            except TypeError as error:
                print(f"Erro na linha: {i}", error)
                continue

        self.df = pd.DataFrame(new_df)
        return self

    def remover_matricula(self, coluna):
        def tratar(valor):
            if pd.isna(valor):
                return valor

            partes = str(valor).split(",", 1)

            if len(partes) == 2:
                return partes[1].strip()

            return str(valor).strip()

        self.df[coluna] = self.df[coluna].apply(tratar)
        return self

    def get_df(self):
        return self.df
