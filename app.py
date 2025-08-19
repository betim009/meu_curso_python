mercado_financeiro = [
    {
        "id": 1,
        "ativo": "PETR4",
        "tipo": "Ação",
        "setor": "Petróleo e Gás",
        "preco": 37.50,
    },
    {
        "id": 2,
        "ativo": "VALE3",
        "tipo": "Ação",
        "setor": "Mineração",
        "preco": 68.20,
    },
    {
        "id": 3,
        "ativo": "ITUB4",
        "tipo": "Ação",
        "setor": "Bancos",
        "preco": 32.10,
    },
    {
        "id": 4,
        "ativo": "BBDC4",
        "tipo": "Ação",
        "setor": "Bancos",
        "preco": 27.80,
    },
    {
        "id": 5,
        "ativo": "MGLU3",
        "tipo": "Ação",
        "setor": "Varejo",
        "preco": 2.90,
    },
    {
        "id": 6,
        "ativo": "BBAS3",
        "tipo": "Ação",
        "setor": "Bancos",
        "preco": 49.00,
    },
    {
        "id": 7,
        "ativo": "WEGE3",
        "tipo": "Ação",
        "setor": "Indústria",
        "preco": 38.70,
    },
    {
        "id": 8,
        "ativo": "ABEV3",
        "tipo": "Ação",
        "setor": "Bebidas",
        "preco": 14.50,
    },
    {
        "id": 9,
        "ativo": "LFT2029",
        "tipo": "Título Público",
        "setor": "Renda Fixa",
        "preco": 1050.00,
    },
    {
        "id": 10,
        "ativo": "NTN-B2035",
        "tipo": "Título Público",
        "setor": "Renda Fixa",
        "preco": 980.00,
    },
    {
        "id": 11,
        "ativo": "Tesouro Selic 2027",
        "tipo": "Título Público",
        "setor": "Renda Fixa",
        "preco": 10450.00,
    },
    {
        "id": 12,
        "ativo": "BRZUSD",
        "tipo": "Câmbio",
        "setor": "Moedas",
        "preco": 5.20,
    },
    {
        "id": 13,
        "ativo": "EURUSD",
        "tipo": "Câmbio",
        "setor": "Moedas",
        "preco": 1.08,
    },
    {
        "id": 14,
        "ativo": "BTC",
        "tipo": "Criptomoeda",
        "setor": "Digital",
        "preco": 65000.00,
    },
    {
        "id": 15,
        "ativo": "ETH",
        "tipo": "Criptomoeda",
        "setor": "Digital",
        "preco": 3200.00,
    },
]

for i in range(0, 15):
    item = mercado_financeiro[i]

    if item["preco"] < 3000:
        print(f'Esse ativo {item["ativo"]} esta abaixo de 3000 mil reais')