import matplotlib.pyplot as plt

# Dados
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Cria o gráfico de linha
plt.plot(x, y, marker='o')  # `marker='o'` coloca um ponto em cada dado
plt.title("Gráfico de Linha Simples")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.show()
