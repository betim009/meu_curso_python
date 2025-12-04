## Anotações sobre leitura e conversão com pandas

- `parse_dates=["data_pagamento"]` em `pd.read_csv`: pede para o pandas converter essa coluna de texto para datetime já na leitura, permitindo usar `.dt.year`, `.dt.month` e operações de data sem conversões adicionais.
- `pd.to_numeric(..., errors="coerce")`: controla como lidar com valores não numéricos. Com `errors="coerce"`, qualquer valor inválido vira `NaN` em vez de disparar erro ou ficar como string, evitando que a leitura quebre e permitindo tratar esses `NaN` depois.
- `date()` em um `datetime` retorna só a parte de data (ano-mês-dia), descartando hora. `isoformat()` transforma um `date`/`datetime` em string padrão ISO (para `date`, fica `YYYY-MM-DD`; para `datetime`, inclui horário).
- `df["data_pagamento"].min().date().isoformat()` pega a data mais antiga; para pegar a mais recente, use `max()` no lugar de `min()`.
- `agg` em um `groupby` permite aplicar múltiplas agregações nomeadas. Ex.: `df_ano.groupby("mes")["valor_parcela"].agg(valor_total="sum", qtd_pagamentos="size")` cria, para cada mês, a soma (`valor_total`) e a contagem de linhas (`qtd_pagamentos`), retornando um DataFrame com uma linha por grupo e colunas para cada agregação definida.
