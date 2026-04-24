clientes = [
    {"nome": "Ana Souza", "ativo": True},
    {"nome": "Carlos Lima", "ativo": False},
    {"nome": "Juliana Martins", "ativo": True},
]

for cliente in clientes:
    if not cliente["ativo"]:
        continue

    print(f"Cliente ativo: {cliente['nome']}")
