import plotly.graph_objs as go

# Dados para o gráfico
x = ["A", "B", "C", "D"]
y = [10, 20, 30, 40]

# Criando o gráfico de barras
fig = go.Figure(data=[go.Bar(x=x, y=y)])
fig.update_layout(
    title="Gráfico de Barras com Plotly",
    xaxis_title="Categorias",
    yaxis_title="Valores",
    template="plotly",
)

# Mostrando o gráfico em um navegador ou notebook
fig.show()
