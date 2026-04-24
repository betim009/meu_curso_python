nome = input("Nome do funcionário: ")
idade_texto = input("Idade: ")
cargo = input("Cargo: ")
salario_texto = input("Salário: ")
ativo_texto = input("Funcionário ativo? (s/n): ")

idade = int(idade_texto)
salario = float(salario_texto)
ativo = ativo_texto.lower() == "s"

salario_anual = salario * 12

print()
print("Ficha do funcionário")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Cargo: {cargo}")
print(f"Salário mensal: R$ {salario:.2f}")
print(f"Salário anual: R$ {salario_anual:.2f}")
print(f"Ativo: {ativo}")
