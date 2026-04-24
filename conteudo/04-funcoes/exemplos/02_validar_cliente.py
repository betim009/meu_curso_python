def cliente_pode_comprar(idade, ativo):
    if idade >= 18 and ativo:
        return True

    return False


resultado = cliente_pode_comprar(25, True)

print(f"Cliente pode comprar: {resultado}")
