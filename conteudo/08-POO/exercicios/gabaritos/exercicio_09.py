class PagamentoCartao:
    def processar(self, valor):
        return f"Cartão aprovado: R$ {valor:.2f}"


class PagamentoPix:
    def processar(self, valor):
        return f"Pix recebido: R$ {valor:.2f}"


class PagamentoBoleto:
    def processar(self, valor):
        return f"Boleto gerado: R$ {valor:.2f}"


# Objetos diferentes respondem ao mesmo método processar.
pagamentos = [
    PagamentoCartao(),
    PagamentoPix(),
    PagamentoBoleto(),
]

for pagamento in pagamentos:
    print(pagamento.processar(100.00))
