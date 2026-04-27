class Paciente:
    def __init__(self, nome, telefone, idade):
        self.nome = nome
        self.telefone = telefone
        self.idade = idade


class Consulta:
    def __init__(self, paciente, data, horario, especialidade):
        self.paciente = paciente
        self.data = data
        self.horario = horario
        self.especialidade = especialidade

    def exibir_resumo(self):
        return (
            f"{self.data} às {self.horario} | {self.especialidade} | "
            f"{self.paciente.nome} ({self.paciente.telefone})"
        )


class Agenda:
    def __init__(self):
        self.consultas = []

    def marcar_consulta(self, consulta):
        self.consultas.append(consulta)

    def listar_consultas(self):
        for consulta in self.consultas:
            print(consulta.exibir_resumo())

    def buscar_por_paciente(self, nome):
        encontradas = []

        for consulta in self.consultas:
            if consulta.paciente.nome.lower() == nome.lower():
                encontradas.append(consulta)

        return encontradas


# A consulta recebe um objeto Paciente, não apenas um texto com o nome.
agenda = Agenda()

paciente_1 = Paciente("Mariana Silva", "11999990000", 32)
paciente_2 = Paciente("João Pereira", "11988887777", 45)

agenda.marcar_consulta(Consulta(paciente_1, "10/05/2026", "09:00", "Cardiologia"))
agenda.marcar_consulta(Consulta(paciente_2, "11/05/2026", "14:30", "Dermatologia"))
agenda.marcar_consulta(Consulta(paciente_1, "20/05/2026", "10:00", "Retorno"))

agenda.listar_consultas()

print("Consultas da Mariana:")
for consulta in agenda.buscar_por_paciente("Mariana Silva"):
    print(consulta.exibir_resumo())
