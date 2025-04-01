"""
1.  Você deve usar o for para exibir todos os nomes
    =>  Creusa
        Adriana
        Alexander
        Fernando


2.  Você deve usar o for e combinar com o if e econtrar apenas 'Adriana' em nomes.
    => Adriana

3. Você deve usar o for com if, econtrar todos que não são Creusa e exibir.
    =>  Adriana
        Alexander
        Fernando


4. Você deve usar o for com if, tentar encontar João e caso não econtrar deve exibir.

    => Não foi possível econtrar o João

    Se econtrar
    => João

5. Você deve usar o for para percorrer idades, e exibir todos numeros maiores que 25.
    =>  65
        32
        41

6. Você deve criar uma variavel maior e atribuir o valor 0.
   Depois deve passar para a variavel maior, o maior numero dentro da lista idades.
   Você vai usar for com if.

   => 65

7. Você deve exibir todas as informacoes de menos o id da lista de dicionarios pessoas.
   Usando for com if.

   =>   Creusa 20 aposentado
        Adriana 17 não-aposentado
        Alexander 65 aposentado
        Fernando 41 não-aposentado


8.  Preciso que você corrija a pessoa do id 1 para False a chave aposentado.

    =>
    [
        {"id": "1", "nome": "Creusa", "idade": 20, "aposentado": False},
        {"id": "2", "nome": "Adriana", "idade": 17, "aposentado": False},
        {"id": "3", "nome": "Alexander", "idade": 65, "aposentado": True},
        {"id": "4", "nome": "Fernando", "idade": 41, "aposentado": False},
    ]
"""

nomes = ["Creusa", "Adriana", "Alexander", "Fernando"]
idades = [20, 17, 65, 32, 41]
pessoas = [
    {"id": "1", "nome": "Creusa", "idade": 20, "aposentado": True},
    {"id": "2", "nome": "Adriana", "idade": 17, "aposentado": False},
    {"id": "3", "nome": "Alexander", "idade": 65, "aposentado": True},
    {"id": "4", "nome": "Fernando", "idade": 41, "aposentado": False},
]
