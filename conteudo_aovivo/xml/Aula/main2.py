import xml.etree.ElementTree as ET

tree = ET.parse("./Aula/file.L5X")
root = tree.getroot()

programs = root.findall("./Controller/Programs/Program")
print(programs)
print(len(programs))

for program in programs:
    print("Name: ", program.get("Name"))
    print(program.findtext("Description"))
    print("\n")

for program in programs:
    program_name = program.get("Name")
    print("Program: ", program_name)

    routines = program.findall("./Routines/Routine")
    for routine in routines:
        print("  Routine: ", routine.get("Name"))

    print("\n")