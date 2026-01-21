import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse("./Aula/file.L5X")
root = tree.getroot()

controllers_tags = root.findall("./Controller/Tags/Tag")
print(controllers_tags)
print(len(controllers_tags))

rows = []

for tag in controllers_tags:
    name = tag.get("Name")
    data_type = tag.get("DataType")
    description = tag.findtext("Description")

    print("Name: ", name)
    print("DataType: ", data_type)
    print(description)
    print("\n")

    rows.append(
        {
            "name": name,
            "data_type": data_type,
            "description": description,
        }
    )

df = pd.DataFrame(rows)
df.to_csv("tags.csv", index=False)