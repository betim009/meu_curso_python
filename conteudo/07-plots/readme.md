
# 📊 Criando Gráficos em Python com Matplotlib e Plotly

Neste material, vamos aprender a **criar gráficos em Python** com duas bibliotecas muito usadas:

- **Matplotlib**: ideal para gráficos simples e rápidos.
- **Plotly**: ótimo para gráficos modernos e interativos.

O objetivo aqui é que você **entenda o que cada linha faz**, e **quando, como e por que usar** cada tipo de gráfico.

---

## 🔹 Parte 1 – Gráfico de Barras com Plotly

```python
import plotly.graph_objs as go

# Dados
x = ["A", "B", "C", "D"]
y = [10, 20, 30, 40]

# Cria a figura com gráfico de barras
fig = go.Figure(data=[go.Bar(x=x, y=y)])

# Personaliza título e eixos
fig.update_layout(
    title="Gráfico de Barras com Plotly",
    xaxis_title="Categorias",
    yaxis_title="Valores",
    template="plotly"
)

# Exibe o gráfico
fig.show()
```

### 🧠 Quando usar?
Quando você quiser criar **gráficos interativos**, como em dashboards e visualizações modernas.

### ✅ Por que usar?
- Os gráficos são **bonitos, dinâmicos e fáceis de explorar** com o mouse.
- Funcionam bem em Jupyter, Streamlit, navegadores, etc.

### ⚠️ Cuidado:
- Você precisa instalar a biblioteca antes:  
  `pip install plotly`

---

## 🔹 Parte 2 – Gráfico de Barras com Matplotlib

```python
import matplotlib.pyplot as plt

x = ["A", "B", "C", "D"]
y = [3, 8, 1, 10]

plt.bar(x, y)  # cria as barras
plt.title("Gráfico Simples")  # título do gráfico
plt.xlabel("Eixo X")  # nome do eixo X
plt.ylabel("Eixo Y")  # nome do eixo Y
plt.show()  # exibe o gráfico
```

### 🧠 Quando usar?
Quando quiser **um gráfico rápido e direto**, sem interatividade.

### ✅ Por que usar?
- É a biblioteca mais usada para **gráficos simples em Python**.
- Funciona bem para relatórios e scripts.

### ⚠️ Cuidado:
- Não se esqueça de `plt.show()`, senão o gráfico não aparece.
- Os dados do eixo X devem ser **categorias (strings)** e o Y **valores numéricos**.

📤 Resultado esperado:
```
A   ███
B   ████████
C   █
D   ██████████
```

---

## 🔹 Parte 3 – Gráfico de Linha com Matplotlib

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')
plt.title("Gráfico de Linha Simples")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.show()
```

### 🧠 Quando usar?
Para mostrar **evolução ou tendência de valores**, como crescimento ao longo do tempo.

### ✅ Por que usar?
É ideal para **valores ordenados**, como tempo, sequência de eventos ou índices.

### ⚠️ Cuidado:
- Use `marker='o'` se quiser ver os pontos visivelmente conectados.
- Os valores em `x` devem estar ordenados.

📤 Saída esperada:
Um gráfico ligando os pontos (1,2), (2,3), ..., (5,11) com bolinhas.

---

## 🔹 Parte 4 – Gráfico de Pizza com Matplotlib

```python
import matplotlib.pyplot as plt

labels = ["A", "B", "C", "D"]
sizes = [15, 30, 45, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Gráfico de Pizza Simples")
plt.show()
```

### 🧠 Quando usar?
Quando você quiser mostrar **partes de um todo** (ex: porcentagem de votos, fatias de vendas, etc).

### ✅ Por que usar?
Ajuda a ver **qual parte é maior ou menor** em uma divisão total.

### ⚠️ Cuidado:
- Os valores devem ser proporcionais entre si.
- O gráfico de pizza é ideal **quando não há muitas categorias** (2 a 6 no máximo).

📤 Saída esperada:
Um gráfico redondo com 4 fatias rotuladas A, B, C, D mostrando a porcentagem de cada uma.

---

## ✅ Conclusão

| Tipo de gráfico | Quando usar                         | Biblioteca recomendada |
|------------------|--------------------------------------|--------------------------|
| Barras           | Comparar valores                    | Matplotlib ou Plotly    |
| Linha            | Mostrar evolução ou tendência       | Matplotlib              |
| Pizza            | Mostrar partes de um todo           | Matplotlib              |
| Interativo       | Apresentações ou dashboards         | Plotly                  |

