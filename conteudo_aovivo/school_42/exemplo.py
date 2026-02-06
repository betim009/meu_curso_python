class Plant:
    # Metodo construtor que vai criar os atributos do objeto.
    def __init__(self, name, height, age): # name, height, age continua sendo argumentos
        self.namePlant = name
        self.heightPlant = height
        self.agePlant = age
        self.price = 10

    def print_plant(self):
        print(f"{self.namePlant} {self.heightPlant} {self.agePlant}")


name = input("Digite o nome: ")
height = input("Digite a altura: ")
age = input("Digite a idade: ")

tomato = Plant(name, height, age)
tomato.print_plant()