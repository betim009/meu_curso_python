# Exercício 13 - Agenda de consultas

Crie um sistema simples de agenda para uma clínica.

## Requisitos

### Paciente

- Atributos: `nome`, `telefone` e `idade`.

### Consulta

- Atributos: `paciente`, `data`, `horario` e `especialidade`.
- Método `exibir_resumo`.

### Agenda

- Atributo `consultas`, começando como lista vazia.
- Método `marcar_consulta(consulta)`.
- Método `listar_consultas`.
- Método `buscar_por_paciente(nome)`.

## Situação real

Uma clínica precisa registrar consultas e localizar agendamentos pelo nome do paciente.
