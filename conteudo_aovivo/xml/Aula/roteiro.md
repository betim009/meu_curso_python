### Roteiro de extração de dados

1. Crie um arquivo chamado main.py e faça a importação, na primeira linha do arquivo, da biblioteca etree.
   O que isso significa: vamos usar a biblioteca do Python para ler arquivos XML.

```py
# main.py
import xml.etree.ElementTree as ET
```

2. Crie as duas variáveis tree e root. A variável tree usa o método parse para ler o arquivo, e a variável root usa getroot para acessar os dados dentro do XML.
   O que isso significa: agora temos o XML carregado e podemos navegar pelos elementos.

```py
tree = ET.parse("file.L5X")
root = tree.getroot()
```

2.1 Código até o momento:
```py
import xml.etree.ElementTree as ET

tree = ET.parse("file.L5X")
root = tree.getroot()
```

3. O objetivo agora é encontrar tags <Tag> que estão dentro da tag <Controller>.
   O que isso significa: vamos localizar a lista de tags do controlador e ver quantas existem.

    3.1 Crie uma variável chamada `controllers_tags`
        O que isso significa: essa variável vai guardar todas as tags encontradas.

    3.2 Use o método `findall()` - serve para encontrar todos os elementos por um path
        O que isso significa: o path indica onde procurar dentro do XML.

    3.3 Utilize o path "./Controller/Tags/Tag" para coletar todas as tags
        O que isso significa: vamos buscar os elementos <Tag> dentro de <Controller>/<Tags>.

    3.4 Exiba a variável com print
        O que isso significa: vamos conferir o conteúdo retornado.

    3.5 Exiba a quantidade pelo método len
        O que isso significa: vamos ver quantas tags foram encontradas.

```py
controllers_tags = root.findall("./Controller/Tags/Tag")
print(controllers_tags)
print(len(controllers_tags))
```

3.6 Código até o momento:
```py
import xml.etree.ElementTree as ET

tree = ET.parse("file.L5X")
root = tree.getroot()

controllers_tags = root.findall("./Controller/Tags/Tag")
print(controllers_tags)
print(len(controllers_tags))
```

4. **Loops e métodos**

   Agora vamos adicionar um for (estrutura de repetição) para percorrer cada tag encontrada pelo findall.
   O que isso significa: vamos ler os atributos `Name` e `DataType` e o texto da tag `Description`.

    4.1 Comece o loop com `for tag in controllers_tags`
        O que isso significa: cada `tag` será um elemento XML diferente.

    4.2 Use `tag.get("Name")` para ler o atributo Name
        O que isso significa: vamos pegar o valor do atributo Name de cada tag.

    4.3 Use `tag.get("DataType")` para ler o atributo DataType
        O que isso significa: vamos pegar o tipo de dado da tag.

    4.4 Use `tag.findtext("Description")` para ler a descrição
        O que isso significa: vamos buscar o texto dentro de <Description>.

    4.5 Use `print("\n")` para separar visualmente cada tag no terminal
        O que isso significa: facilita a leitura do resultado.

```py
for tag in controllers_tags:
    print("Name: ", tag.get("Name"))
    print("DataType: ", tag.get("DataType"))
    print(tag.findtext("Description"))
    print("\n")
```

4.6 Código até o momento:
```py
import xml.etree.ElementTree as ET

tree = ET.parse("file.L5X")
root = tree.getroot()

controllers_tags = root.findall("./Controller/Tags/Tag")
print(controllers_tags)
print(len(controllers_tags))

for tag in controllers_tags:
    print("Name: ", tag.get("Name"))
    print("DataType: ", tag.get("DataType"))
    print(tag.findtext("Description"))
    print("\n")
```

5. Base de dados em lista de dicionários
   O que isso significa: vamos guardar os dados em memória antes de salvar em arquivo.

    5.1 Crie uma lista chamada `rows`
        O que isso significa: a lista guarda várias linhas de dados.

    5.2 Dentro do loop, salve Name, DataType e Description em variáveis
        O que isso significa: organizamos os dados antes de guardar.

    5.3 Ainda no loop, use `rows.append({...})`
        O que isso significa: o append adiciona uma nova linha (um dicionário) na lista.

    5.4 Cada dicionário representa uma linha da tabela
        O que isso significa: as chaves viram colunas e os valores viram os dados.

```py
rows = []

for tag in controllers_tags:
    name = tag.get("Name")
    data_type = tag.get("DataType")
    description = tag.findtext("Description")

    print("Name: ", name)
    print("DataType: ", data_type)
    print(description)
    print("\n")

    rows.append(
        {
            "name": name,
            "data_type": data_type,
            "description": description,
        }
    )
```

6. Salvar com pandas
   O que isso significa: vamos transformar a lista de dicionários em uma tabela e salvar em CSV.

    6.1 Importe o pandas
        O que isso significa: pandas ajuda a trabalhar com dados em formato de tabela.

    6.2 Crie um DataFrame com `rows`
        O que isso significa: o DataFrame é a tabela criada a partir da lista.

    6.3 Use `to_csv` para salvar
        O que isso significa: o arquivo "tags.csv" será criado com cabeçalho.

```py
import pandas as pd

df = pd.DataFrame(rows)
df.to_csv("tags.csv", index=False)
```

6.4 Código até o momento:
```py
import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse("file.L5X")
root = tree.getroot()

controllers_tags = root.findall("./Controller/Tags/Tag")
print(controllers_tags)
print(len(controllers_tags))

rows = []

for tag in controllers_tags:
    name = tag.get("Name")
    data_type = tag.get("DataType")
    description = tag.findtext("Description")

    print("Name: ", name)
    print("DataType: ", data_type)
    print(description)
    print("\n")

    rows.append(
        {
            "name": name,
            "data_type": data_type,
            "description": description,
        }
    )

df = pd.DataFrame(rows)
df.to_csv("tags.csv", index=False)
```

7. Programas do Controller (Programs)
   O que isso significa: agora vamos encontrar os programas dentro de <Controller>.

   Recomendação: crie um novo arquivo, por exemplo `main_programs.py`, para não misturar com o roteiro de tags.

    7.1 Crie uma variável chamada `programs`
        O que isso significa: essa variável vai guardar todos os programas encontrados.

    7.2 Use o método `findall()` com o path "./Controller/Programs/Program"
        O que isso significa: vamos buscar todos os elementos <Program> dentro de <Programs>.

    7.3 Exiba a variável com print
        O que isso significa: vamos conferir o conteúdo retornado.

    7.4 Exiba a quantidade pelo método len
        O que isso significa: vamos ver quantos programas existem.

```py
import xml.etree.ElementTree as ET

tree = ET.parse("file.L5X")
root = tree.getroot()

programs = root.findall("./Controller/Programs/Program")
print(programs)
print(len(programs))
```

8. Percorrer os programas com for
   O que isso significa: vamos acessar os dados de cada <Program>.

    8.1 Comece o loop com `for program in programs`
        O que isso significa: cada `program` será um elemento XML diferente.

    8.2 Use `program.get("Name")` para ler o nome do programa
        O que isso significa: vamos pegar o atributo Name de cada programa.

    8.3 Use `program.findtext("Description")` para ler a descrição
        O que isso significa: vamos buscar o texto dentro de <Description>.

    8.4 Use `print("\n")` para separar visualmente cada programa
        O que isso significa: facilita a leitura no terminal.

```py
for program in programs:
    print("Name: ", program.get("Name"))
    print(program.findtext("Description"))
    print("\n")
```

9. For dentro do for (Program -> Routines)
   O que isso significa: cada Program pode ter várias Routines, então fazemos um segundo loop.

    9.1 Crie uma variável `program_name` para guardar o nome do programa
        O que isso significa: vamos usar esse nome para identificar a rotina.

    9.2 Busque as rotinas com `program.findall("./Routines/Routine")`
        O que isso significa: estamos pegando todas as rotinas dentro do Program atual.

    9.3 Faça um novo loop para cada rotina
        O que isso significa: o loop interno percorre as rotinas daquele programa.

```py
for program in programs:
    program_name = program.get("Name")
    print("Program: ", program_name)

    routines = program.findall("./Routines/Routine")
    for routine in routines:
        print("  Routine: ", routine.get("Name"))

    print("\n")
```

9.4 Código até o momento:
```py
import xml.etree.ElementTree as ET

tree = ET.parse("file.L5X")
root = tree.getroot()

programs = root.findall("./Controller/Programs/Program")
print(programs)
print(len(programs))

for program in programs:
    print("Name: ", program.get("Name"))
    print(program.findtext("Description"))
    print("\n")

for program in programs:
    program_name = program.get("Name")
    print("Program: ", program_name)

    routines = program.findall("./Routines/Routine")
    for routine in routines:
        print("  Routine: ", routine.get("Name"))

    print("\n")
```
