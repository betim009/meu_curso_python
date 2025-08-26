# CRIAR UM Objeto

# Objeto é um elemento que tem atributo e metodos.

class User:
    def __init__(self, nome, email, password):
        self.nome = nome
        self.email = email
        self.password = password
        self.status = True

    def updatePassword(self, newPassword):
        self.password = newPassword
        return "Sua senha foi alterada com sucesso."

    def __str__ (self):
        return f"Objeto do usuario: {self.nome}"



clare = User("clare", "clare@email.com", "123456")
clare.updatePassword("abc123")

alberto = User("Alberto", "alberto@email.com", "123456")

class Anivesarios:
    def __init__(self):
        self.data = []
        self.id = 1

    def criar_Aniversario(self, date, name):
        self.data.append({
            "id": self.id,
            "name": name,
            "date": date
        })
        self.id += 1
        return "Aniversariante criado com sucesso."
    
    def exibir_aniversariantes(self):
        return self.data
    
    def exibir_aniversariantes_id(self, id):
        for item in self.data:
            if item["id"] == id:
                return item
    

clare_niver = Anivesarios()
clare_niver.criar_Aniversario("2025-12-01", "Daniel")
clare_niver.criar_Aniversario("2025-12-01", "Carlos")
clare_niver.criar_Aniversario("2025-12-01", "Maria")
clare_niver.criar_Aniversario("2025-12-01", "Daniela")

alberto_niver = Anivesarios()
alberto_niver.criar_Aniversario("2025-12-01", "Messi")
alberto_niver.criar_Aniversario("2025-12-01", "Cristiano")
alberto_niver.criar_Aniversario("2025-12-01", "Pedro")
alberto_niver.criar_Aniversario("2025-12-01", "Gabigol")
alberto_niver.criar_Aniversario("2025-12-01", "Halland")
alberto_niver.criar_Aniversario("2025-12-01", "Lewandovisk")

print(clare_niver.exibir_aniversariantes())
print()
print(alberto_niver.exibir_aniversariantes())