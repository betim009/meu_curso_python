# 📘 Funções Lambda no Python

---

## 1️⃣ O que é uma função?

Antes de entender o que é `lambda`, precisamos lembrar o que é uma função.

Uma função é um bloco de código reutilizável que executa uma tarefa específica.

Exemplo:

```python
def soma(a, b):
    return a + b
```

Aqui:
- `def` cria a função
- `soma` é o nome da função
- `a` e `b` são parâmetros
- `return` devolve o resultado

---

## 2️⃣ O que é Lambda?

`lambda` é uma forma simplificada de criar funções no Python.

Ela é conhecida como:

> Função anônima (porque não precisa ter um nome definido com `def`)

Ela é usada quando queremos criar uma função pequena e simples.

---

## 3️⃣ Estrutura do Lambda

A estrutura é:

```python
lambda parametros: expressao
```

Ela sempre possui:

1. A palavra `lambda`
2. Os parâmetros
3. Dois pontos `:`
4. Uma expressão

⚠ Importante:
- O lambda retorna automaticamente o resultado da expressão.
- Não usamos a palavra `return`.

---

## 4️⃣ Comparando com função normal

### 🔹 Função normal

```python
def dobro(numero):
    return numero * 2
```

### 🔹 Usando lambda

```python
dobro = lambda numero: numero * 2
```

Funcionam da mesma forma:

```python
print(dobro(5))
```

Saída:

```
10
```

---

## 5️⃣ Quando usar lambda?

Use lambda quando:

- A função for simples
- Tiver apenas uma operação
- For usada rapidamente
- Não precisar de várias linhas

Não use lambda quando:

- A lógica for grande
- Precisar de vários passos
- Quiser deixar o código mais legível para iniciantes

---

## 6️⃣ Exemplos Práticos

### 📌 Exemplo 1 – Soma

```python
soma = lambda a, b: a + b
print(soma(3, 4))
```

Saída:

```
7
```

---

### 📌 Exemplo 2 – Ordenando com sorted()

```python
lista = [(1, 3), (2, 1), (4, 2)]

ordenado = sorted(lista, key=lambda x: x[1])

print(ordenado)
```

O que acontece:
- `x` representa cada tupla
- `x[1]` pega o segundo valor
- A ordenação acontece com base nesse valor

---

### 📌 Exemplo 3 – Usando com map()

```python
numeros = [1, 2, 3, 4]

dobro = list(map(lambda x: x * 2, numeros))

print(dobro)
```

Saída:

```
[2, 4, 6, 8]
```

---

### 📌 Exemplo 4 – Usando com filter()

```python
numeros = [1, 2, 3, 4, 5, 6]

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)
```

Saída:

```
[2, 4, 6]
```

---

## 7️⃣ Regras Importantes

✅ Só pode ter uma expressão  
❌ Não pode ter múltiplas linhas  
❌ Não pode ter vários comandos  
❌ Não pode usar `return`  
❌ Não é ideal para lógica complexa  

---

## 8️⃣ Erros Comuns

🚫 Tentar escrever várias linhas:

```python
lambda x:
    y = x + 1
    return y
```

Isso gera erro.

Lambda deve ser sempre assim:

```python
lambda x: x + 1
```

---

## 🔟 Lambda com Pandas (Muito Importante)

O `lambda` é muito usado com a biblioteca **pandas**, principalmente com o método `.apply()`.

Quando usamos `.apply()`, estamos dizendo:

> "Aplique uma função em cada valor da coluna."

Veja um exemplo:

```python
import pandas as pd

dados = {
    "nome": [" Ana ", " Carlos ", " Maria "]
}

df = pd.DataFrame(dados)

df["nome"] = df["nome"].apply(lambda x: x.strip())

print(df)
```

O que está acontecendo aqui?

- `x` representa cada valor da coluna `nome`
- `.strip()` remove espaços antes e depois do texto
- O `lambda` executa isso para cada linha da coluna

Saída esperada:

```
     nome
0     Ana
1  Carlos
2   Maria
```

Outro exemplo:

```python
df["dobro"] = df["idade"].apply(lambda x: x * 2)
```

Aqui o lambda:

- Pega cada valor da coluna `idade`
- Multiplica por 2
- Cria uma nova coluna chamada `dobro`

📌 Por que usar lambda com pandas?

- Para transformar dados
- Para limpar dados
- Para criar novas colunas
- Para aplicar regras personalizadas

⚠ Cuidado:

Se a função ficar grande ou complexa, é melhor criar uma função normal com `def` e depois passar o nome dela para o `.apply()`.

---

## 🧠 Mais Exemplos de Lambda com Pandas

Agora vamos ver usos mais comuns e importantes do `lambda` dentro do pandas.

---

### 📌 1️⃣ Criando coluna com condição (if/else)

```python
import pandas as pd

dados = {
    "nota": [5, 8, 3, 10]
}

df = pd.DataFrame(dados)

df["situacao"] = df["nota"].apply(lambda x: "Aprovado" if x >= 7 else "Reprovado")

print(df)
```

O que acontece aqui?

- Para cada nota
- Se for maior ou igual a 7 → "Aprovado"
- Senão → "Reprovado"

Saída:

```
   nota   situacao
0     5  Reprovado
1     8   Aprovado
2     3  Reprovado
3    10   Aprovado
```

---

### 📌 2️⃣ Trabalhando com duas colunas ao mesmo tempo

Quando usamos `axis=1`, aplicamos a função linha por linha:

```python
dados = {
    "valor": [100, 200, 300],
    "desconto": [10, 20, 30]
}

df = pd.DataFrame(dados)

df["valor_final"] = df.apply(lambda linha: linha["valor"] - linha["desconto"], axis=1)

print(df)
```

Aqui:

- `linha` representa cada linha inteira
- A função calcula valor - desconto

---

### 📌 3️⃣ Alterando texto (transformação)

```python
dados = {
    "nome": ["ana", "carlos", "maria"]
}

df = pd.DataFrame(dados)

df["nome"] = df["nome"].apply(lambda x: x.upper())

print(df)
```

Aqui o lambda:

- Pega cada nome
- Transforma em maiúsculo

---

### 📌 4️⃣ Trabalhando com datas

```python
dados = {
    "ano_nascimento": [1990, 2000, 1985]
}

df = pd.DataFrame(dados)

df["idade"] = df["ano_nascimento"].apply(lambda x: 2025 - x)

print(df)
```

Aqui:

- Para cada ano
- Calcula a idade

---

### 📌 5️⃣ Usando map() ao invés de apply()

`map()` também aceita lambda, mas funciona apenas em Series (colunas):

```python
df["idade_dobrada"] = df["idade"].map(lambda x: x * 2)
```

📌 Diferença simples:

- `.apply()` é mais geral
- `.map()` é mais simples e específico para colunas

---

### 📌 Quando usar lambda no pandas?

Use lambda quando:

- Precisar transformar valores rapidamente
- Criar colunas novas
- Aplicar regras condicionais simples
- Fazer pequenas limpezas

Não use lambda quando:

- A regra for muito grande
- Tiver muitas condições
- Precisar de muita clareza para iniciantes

Nesses casos, crie uma função com `def` e depois use:

```python
def classificar(nota):
    if nota >= 7:
        return "Aprovado"
    return "Reprovado"

df["situacao"] = df["nota"].apply(classificar)
```

---

## 1️⃣1️⃣ Resumo Final

Lambda é:

- Uma função pequena
- Escrita em uma única linha
- Usada para operações simples
- Muito comum com `map()`, `filter()`, `sorted()` e `apply()`

Frase simples para memorizar:

> Lambda é uma forma rápida de criar funções pequenas em uma única linha.