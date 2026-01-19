import xml.etree.ElementTree as ET

tree = ET.parse("base.L5X")
root = tree.getroot()

program = root.get("Name")
program_1 = root.find(".//Program")

print(program_1)

for tag in root.findall("./Tags/Tag"):
    print(tag.get("Name"), tag.get("DataType"))