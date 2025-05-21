musicas_rap = [
    {
        "titulo": "Falcão Urbano",
        "artista": "MC Renan",
        "ano": 2020,
        "duracao_min": 3.5,
        "album": "Cidade Cinza",
        "genero": "Rap Nacional",
        "temas": ["superação", "favela", "política"],
    },
    {
        "titulo": "Códigos da Rua",
        "artista": "DJ Miro",
        "ano": 2018,
        "duracao_min": 4.0,
        "album": "Ritmo e Realidade",
        "genero": "Rap Nacional",
        "temas": ["resistência", "respeito", "vida"],
    },
    {
        "titulo": "Versos Vivos",
        "artista": "Negra Luma",
        "ano": 2021,
        "duracao_min": 3.8,
        "album": "Poder Feminino",
        "genero": "Rap Feminino",
        "temas": ["empoderamento", "vida", "luta"],
    },
    {
        "titulo": "Na Lata",
        "artista": "Funkin' Flow",
        "ano": 2019,
        "duracao_min": 2.9,
        "album": "Underground Vibes",
        "genero": "Boom Bap",
        "temas": ["batalha", "rimadores", "rap"],
    },
    {
        "titulo": "Olhos de Vidro",
        "artista": "L7Kappa",
        "ano": 2022,
        "duracao_min": 3.2,
        "album": "Fumaça e Verso",
        "genero": "Trap",
        "temas": ["solidão", "reflexão", "vida"],
    },
    {
        "titulo": "Raiz Forte",
        "artista": "Rapadura",
        "ano": 2017,
        "duracao_min": 4.3,
        "album": "Nordeste Rima",
        "genero": "Rap Regional",
        "temas": ["cultura", "origem", "tradição"],
    },
    {
        "titulo": "Caminhos Tortos",
        "artista": "Ras MC",
        "ano": 2016,
        "duracao_min": 3.6,
        "album": "Conflitos Internos",
        "genero": "Consciente",
        "temas": ["escolhas", "família", "vida"],
    },
    {
        "titulo": "No Topo",
        "artista": "Yuri Black",
        "ano": 2023,
        "duracao_min": 2.7,
        "album": "Autoestima",
        "genero": "Trap",
        "temas": ["sucesso", "dinheiro", "motivação"],
    },
    {
        "titulo": "Ponte Aérea",
        "artista": "Drake & Emicida",
        "ano": 2021,
        "duracao_min": 3.9,
        "album": "Conexões",
        "genero": "Rap Internacional",
        "temas": ["parceria", "globalização", "vivência"],
    },
    {
        "titulo": "A Última Palavra",
        "artista": "Flow Real",
        "ano": 2015,
        "duracao_min": 4.1,
        "album": "Sem Censura",
        "genero": "Rap Consciente",
        "temas": ["verdade", "liberdade", "voz"],
    },
]

# SE TEM LISTA -> FOR

# FOR -> vai do PRIMEIRO ao ULTIMO elemento da lista
for item in musicas_rap:
    # print(item["titulo"], item['artista'])
    # print()
    pass

# FOR ENNUMERATE
for index, item in enumerate(musicas_rap):
    # print(index, item['artista'])
    pass

# FOR RANGE
for index in range(0, len(musicas_rap)):
    item = musicas_rap[index]
    print(item['artista'])