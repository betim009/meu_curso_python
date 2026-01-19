import pandas as pd

pessoas = [
    {"nome": "Alberto"},
    {"nome": "Marcos"},
    {"nome": "Daniel"},
]

dataFrame = pd.DataFrame(pessoas)
dataFrame.to_csv("raw.csv")
dataFrame.to_xml("raw.xml")


a = pd.read_xml("a.xml")
print(a)
