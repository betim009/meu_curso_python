
# 📈 Criando Gráficos com Pandas usando `plot()`

O método `plot()` do Pandas permite criar **gráficos direto de um DataFrame**.  
É uma maneira simples e rápida de **visualizar dados** sem precisar usar bibliotecas externas de forma complexa.

---

## 🧠 Por que usar gráficos?

Às vezes olhar apenas os números da tabela não é suficiente.  
Com gráficos, conseguimos **comparar, visualizar tendências e entender padrões**.

---

## 🧰 Pré-requisitos

Antes de usar gráficos com Pandas, é necessário instalar o `matplotlib`, pois o Pandas usa ele por trás dos panos.

### ✅ Como instalar:

Se você estiver usando um ambiente como VSCode ou PyCharm, abra o terminal e digite:

```bash
pip install matplotlib
```

Depois disso, no seu código Python, você deve importar o `matplotlib.pyplot`:

```python
import matplotlib.pyplot as plt
```

---

## 🧪 O que é o `plot()`?

📘 O `plot()` é um **método do DataFrame** usado para gerar gráficos.  
Você pode especificar o tipo de gráfico com o argumento `kind="..."`.

---

## ✅ Exemplo Prático com Produtos

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("produtos_estoque.csv")

df.plot(kind="bar", x="Produto", y="Estoque")

plt.title("Estoque por Produto")
plt.xlabel("Produto")
plt.ylabel("Quantidade")
plt.show()
```

📤 **Resultado esperado:**

Um gráfico de barras parecido com isso:

```
Produto    ██████████████████
           █████████████
           ███████████████
           ██████████
           ████████████████
           ↑               ↑
       Arroz           Açúcar
```

---

## 🗂 Outros tipos de gráfico

### 🔹 Gráfico de linha (padrão)

```python
df.plot(x="Produto", y="Preco")
plt.title("Preço por Produto")
plt.show()
```

📤 Apresenta os preços como uma linha contínua com pontos.

---

### 🔹 Gráfico de pizza

```python
df.set_index("Produto")["Estoque"].plot(kind="pie", autopct="%.1f%%")
plt.title("Distribuição de Estoque")
plt.ylabel("")  # Remove rótulo lateral
plt.show()
```

📤 Exibe uma pizza mostrando o percentual de estoque de cada produto.

---

### 🔹 Gráfico de dispersão

```python
df.plot(kind="scatter", x="Estoque", y="Preco")
plt.title("Relação entre Estoque e Preço")
plt.show()
```

📤 Pontos no gráfico mostrando se existe alguma relação entre o estoque e o preço.

---

## 📊 Resumo dos Tipos (`kind=`)

| Tipo        | Descrição                          |
|-------------|------------------------------------|
| `"line"`    | Gráfico de linha (padrão)          |
| `"bar"`     | Barras verticais                   |
| `"barh"`    | Barras horizontais                 |
| `"hist"`    | Histograma                         |
| `"box"`     | Boxplot (gráfico de caixa)         |
| `"pie"`     | Gráfico de pizza (só 1 coluna)     |
| `"scatter"` | Gráfico de dispersão (x e y)       |

---

## ⚠️ Cuidados

- Sempre use `plt.show()` após o `.plot()` para exibir o gráfico.
- Em gráficos de pizza, use **somente uma série (coluna)**.
- Pode ser necessário usar `set_index()` para rótulos claros.
- Se `matplotlib` não estiver instalado, o Pandas **não conseguirá mostrar o gráfico**.

---

## 🧠 Conclusão

Com `df.plot()`, você consegue **visualizar rapidamente qualquer coluna numérica** com 1 ou 2 linhas de código.

É ideal para quem está aprendendo a **explorar e apresentar dados de forma visual**.

