import xml.etree.ElementTree as ET

tree = ET.parse("base_1.L5X")
root = tree.getroot()

program = root.find(".//Program")
print(program.get("Name"))

descripthions = root.findall(".//Tag")
for tag in descripthions:
    print(tag.get("Name"))