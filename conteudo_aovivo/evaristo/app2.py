import xml.etree.ElementTree as ET

tree = ET.parse("base_1.L5X")
file = tree.getroot()


program = file.find(".//Program")
print(program.get("Name"))

tags = file.findall(".//Tag")
for tag in tags:
    print(tag.get("Name"))