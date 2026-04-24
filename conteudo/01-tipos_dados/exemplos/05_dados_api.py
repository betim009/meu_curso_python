pedido_api = {
    "id": "1045",
    "cliente": "Empresa Alfa",
    "valor": "1290.50",
    "pago": "True",
}

id_pedido = int(pedido_api["id"])
cliente = pedido_api["cliente"]
valor = float(pedido_api["valor"])
pago = pedido_api["pago"] == "True"

print(f"Pedido: {id_pedido}")
print(f"Cliente: {cliente}")
print(f"Valor: R$ {valor:.2f}")
print(f"Pago: {pago}")
