import matplotlib.pyplot as plt

# Dados
labels = ["A", "B", "C", "D"]
sizes = [15, 30, 45, 10]  # Percentual ou quantidade de cada setor

# Cria o gráfico de pizza
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)  # `autopct` adiciona percentual
plt.title("Gráfico de Pizza Simples")

plt.show()
