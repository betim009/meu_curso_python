"""
Programa para dados!! 

a gente so manipula DADOS - foco é o tipo do dado e nao o valor!! 

FODASE o valor do dado - A PARADA é o tipo!! 

Tipos de dados:

- String -> Textos
- Number -> Numeros inteiros e flutuantes
- Logicos (booleans) -> true e false
- Lists -> Listas de dados
- Dicts -> Conjunto de dados

Variavel -> No ato de nomear um container para guardar qualquer tipo de dados!




Coletar do usuario a quantidade de pagamentos de contas.
- Ex.: 3

Por 3 vezes vou perguntar o valor de cada conta. 
E somar o valor de todas as contas.


"""

total_contas = 0

entrada_quantidade_contas = int(input("Digite um numero inteiro da quantidade de contas que voce pagou: "))
for n in range(entrada_quantidade_contas):
    entrada_valor_conta = int(input("Digite o valor da sua conta: "))
    total_contas += entrada_valor_conta

entrada_salario = int(input("Qual o seu salario: "))

print(entrada_salario - total_contas)