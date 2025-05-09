from pizzas import pizzas

# Funções
def get_pizza_id(id):
    for pizza in pizzas:
        if pizza['id'] == id:
            return pizza
    
    return "Não existe essa pizza!" 

# Resgatar todas as pizzas
def get_all():
    pass

# Resgatar pizza por nome
def get_pizza_nome(nome):
    pass

# Resgar pizzas por tamanho
def get_pizzas_tamanho(tamanho):
    pass

# Criar uma nova pizza
def create_pizza(pizza):
    pass