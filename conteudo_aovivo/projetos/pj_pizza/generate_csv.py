import pandas as pd
from cardapio import cardapio

cardaipo_df = pd.DataFrame(cardapio)
cardaipo_df.to_csv("cardapio.csv", index=False)