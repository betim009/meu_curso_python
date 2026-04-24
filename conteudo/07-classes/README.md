# Classes em Python

Neste módulo, você vai aprender a criar **classes** e **objetos** em Python.

Classes são uma forma de organizar código quando queremos representar coisas do mundo real dentro de um programa, como produtos, alunos, contas bancárias, livros ou clientes.

---

## O que você vai aprender

- O que é uma classe.
- O que é um objeto.
- O que são atributos.
- O que são métodos.
- Para que serve o método `__init__`.
- Quando vale a pena usar classes.
- Erros comuns de quem está começando.

---

## Explicação simples

Imagine que você precisa guardar dados de vários produtos:

```python
produto_1_nome = "Arroz"
produto_1_preco = 25.90
produto_1_quantidade = 10

produto_2_nome = "Feijao"
produto_2_preco = 8.50
produto_2_quantidade = 20
```

Isso funciona, mas começa a ficar confuso quando aparecem muitos produtos.

Uma classe resolve esse problema criando um **modelo**.

```python
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
```

A classe `Produto` funciona como uma forma padronizada de criar produtos.

Agora podemos criar objetos:

```python
arroz = Produto("Arroz", 25.90, 10)
feijao = Produto("Feijao", 8.50, 20)
```

Cada objeto tem seus próprios dados.

---

## Exemplo comentado linha por linha

```python
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_dados(self):
        return f"{self.nome} - R$ {self.preco:.2f} - {self.quantidade} unidades"


produto = Produto("Arroz", 25.90, 10)
print(produto.mostrar_dados())
```

Explicando:

- `class Produto:` cria uma classe chamada `Produto`.
- `def __init__(...)` é executado quando um novo produto é criado.
- `self.nome = nome` guarda o nome dentro do objeto.
- `self.preco = preco` guarda o preço dentro do objeto.
- `self.quantidade = quantidade` guarda a quantidade dentro do objeto.
- `def mostrar_dados(self):` cria uma ação que o produto sabe executar.
- `Produto("Arroz", 25.90, 10)` cria um objeto a partir da classe.
- `produto.mostrar_dados()` chama o método do objeto.

Saída esperada:

```text
Arroz - R$ 25.90 - 10 unidades
```

---

## Classe, objeto, atributo e método

| Nome | Significado simples | Exemplo |
|---|---|---|
| Classe | Modelo para criar objetos | `Produto` |
| Objeto | Item criado a partir da classe | `arroz` |
| Atributo | Informação guardada no objeto | `nome`, `preco`, `quantidade` |
| Método | Função dentro da classe | `mostrar_dados()` |

---

## Quando usar classes?

Use classes quando:

- Você tem vários dados que pertencem à mesma coisa.
- Você quer juntar informações e comportamentos.
- Seu código está ficando cheio de listas ou dicionários difíceis de controlar.
- Você quer criar um sistema mais organizado.

Exemplos bons para classes:

- Produto
- Aluno
- Cliente
- ContaBancaria
- Livro
- Pedido
- Funcionario

---

## Por que usar classes?

Classes ajudam a:

- Organizar melhor o código.
- Evitar repetição.
- Representar melhor entidades reais.
- Criar projetos maiores com menos bagunça.

Sem classes, é comum o aluno criar muitas variáveis soltas. Com classes, os dados ficam agrupados.

---

## Erros comuns

### 1. Esquecer o `self`

Errado:

```python
class Produto:
    def mostrar_nome():
        print(self.nome)
```

Correto:

```python
class Produto:
    def mostrar_nome(self):
        print(self.nome)
```

O `self` representa o próprio objeto.

### 2. Confundir classe com objeto

```python
class Produto:
    pass

arroz = Produto()
```

`Produto` é a classe.  
`arroz` é o objeto.

### 3. Criar classe sem necessidade

Nem tudo precisa ser classe.

Se o problema é muito pequeno, uma função pode resolver. Classes fazem mais sentido quando há dados e ações relacionados.

### 4. Esquecer de chamar o método com parênteses

Errado:

```python
print(produto.mostrar_dados)
```

Correto:

```python
print(produto.mostrar_dados())
```

Sem os parênteses, o método não é executado.

---

## Exercícios

Os exercícios estão na pasta [`exercicios`](exercicios).

Faça nesta ordem:

1. [`exercicio_01.md`](exercicios/exercicio_01.md)
2. [`exercicio_02.md`](exercicios/exercicio_02.md)
3. [`exercicio_03.md`](exercicios/exercicio_03.md)
4. [`exercicio_04.md`](exercicios/exercicio_04.md)

Os gabaritos ficam em [`exercicios/gabaritos`](exercicios/gabaritos).

---

## Mini projeto

Depois dos exercícios, faça o projeto:

- [`Sistema simples de estoque`](projeto/README.md)

Nesse projeto, você vai criar classes para produtos e estoque, cadastrar itens e calcular valores.

---

## Resumo final

- Classe é um modelo.
- Objeto é algo criado a partir da classe.
- Atributos são dados do objeto.
- Métodos são ações do objeto.
- `__init__` prepara o objeto no momento da criação.
- Use classes quando quiser organizar dados e comportamentos relacionados.
