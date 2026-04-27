class PagamentoCartao:
    def processar(self, valor):
        return f"Pagamento de R$ {valor:.2f} aprovado no cartão."


class PagamentoPix:
    def processar(self, valor):
        return f"Pagamento de R$ {valor:.2f} aprovado via Pix."


class PagamentoBoleto:
    def processar(self, valor):
        return f"Boleto de R$ {valor:.2f} gerado para pagamento."


formas_pagamento = [
    PagamentoCartao(),
    PagamentoPix(),
    PagamentoBoleto(),
]

for forma_pagamento in formas_pagamento:
    print(forma_pagamento.processar(250.00))
