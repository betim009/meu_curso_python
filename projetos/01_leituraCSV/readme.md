### Exercício 1: Filtro por Data
Descrição do exercício:
Crie um código que leia um arquivo CSV e filtre os dados de acordo com uma data específica fornecida. Os resultados devem ser salvos em um novo arquivo CSV, contendo apenas os nomes e a data de vencimento original.

Passo a passo:
- Importe a biblioteca pandas.
- Carregue o arquivo CSV utilizando o método pd.read_csv().
- Defina a data que deseja filtrar.
- Percorra as linhas do DataFrame usando iterrows().
- Verifique se a data na coluna "Data de vencimento original" corresponde à data definida.
- Se a condição for verdadeira, adicione as informações ao resultado.
- Crie um novo DataFrame com os resultados filtrados e salve-o como resultado_1.csv.


### Exercício 2: Filtro por Nome
Descrição do exercício:
Escreva um código para ler um arquivo CSV e filtrar os dados por um nome específico. Salve as informações filtradas em um novo arquivo CSV, contendo apenas o nome e a situação.

Passo a passo:
- Importe a biblioteca pandas.
- Carregue o arquivo CSV usando pd.read_csv().
- Defina o nome que deseja filtrar.
- Percorra as linhas do DataFrame com iterrows().
- Verifique se a coluna "Nome" é igual ao nome definido.
- Adicione ao resultado apenas o nome e a situação.
- Salve os resultados filtrados em um arquivo chamado resultado_2.csv.

### Exercício 3: Filtro com Múltiplas Condições
Descrição do exercício:
Implemente um código que leia um arquivo CSV e filtre os dados por nome e situação específicos. Salve os dados filtrados em um novo arquivo CSV, contendo nome, situação e data de vencimento.

Passo a passo:
- Importe a biblioteca pandas.
- Leia o arquivo CSV com pd.read_csv().
- Defina o nome e a situação que deseja filtrar (exemplo: nome = "Bitrix" e situação = "Encerrado").
- Use um loop for com iterrows() para percorrer cada linha.
- Adicione os dados ao resultado apenas se as duas condições forem verdadeiras.
- Salve os resultados filtrados em um arquivo chamado resultado_2.csv.


### Exercício 4: Filtro Simples com Pandas
Descrição do exercício:
Utilize pandas para criar um código que leia um arquivo CSV e filtre os dados pela coluna "Descrição - Portador" com um valor específico. Exporte o resultado para um arquivo CSV.

Passo a passo:
- Importe a biblioteca pandas.
- Leia o arquivo CSV com pd.read_csv().
- Defina o valor que deseja filtrar na coluna "Descrição - Portador".
- Utilize a indexação booleana para aplicar o filtro no DataFrame.
- Salve os dados filtrados em um novo arquivo chamado resultado_3.csv.