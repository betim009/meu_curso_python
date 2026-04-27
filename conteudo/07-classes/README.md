# 07 - Classes em Python

Neste módulo você vai aprender a usar **classes** para organizar dados e comportamentos dentro de um programa.

Até aqui, você já aprendeu variáveis, tipos de dados, condições, repetições, funções, tratamento de erros e arquivos. Com isso, já consegue resolver muitos problemas. Mas quando um sistema começa a crescer, aparece uma dificuldade comum: os dados ficam espalhados.

Classes ajudam a transformar informações soltas em estruturas mais próximas do mundo real.

Ao final deste módulo, você será capaz de:

- Entender o que é uma classe.
- Criar objetos a partir de uma classe.
- Usar `__init__` para iniciar atributos.
- Criar métodos para representar comportamentos.
- Modelar entidades reais como `Cliente`, `Produto`, `Funcionario` e `Pedido`.
- Evitar erros comuns de iniciantes em orientação a objetos.
- Construir um sistema simples de cadastro orientado a objetos.

## Estrutura do módulo

```text
07-classes/
  README.md
  exemplos/
    01_cliente_basico.py
    02_produto_com_metodos.py
    03_funcionario.py
    04_pedido.py
    05_sistema_cadastro.py
  exercicios/
    README.md
    exercicio_01.md
    exercicio_02.md
    exercicio_03.md
    exercicio_04.md
    exercicio_05.md
    exercicio_06.md
    exercicio_07.md
    exercicio_08.md
    exercicio_09.md
    exercicio_10.md
    exercicio_11.md
    exercicio_12.md
    exercicio_13.md
    gabaritos/
      exercicio_01.py
      exercicio_02.py
      exercicio_03.py
      exercicio_04.py
      exercicio_05.py
      exercicio_06.py
      exercicio_07.py
      exercicio_08.py
      exercicio_09.py
      exercicio_10.py
      exercicio_11.py
      exercicio_12.py
      exercicio_13.py
  projeto/
    README.md
    sistema_cadastro.py
```

## 1. Introdução: o problema dos dados soltos

Imagine que você está criando um sistema para uma empresa cadastrar clientes.

No começo, você pode fazer assim:

```python
cliente_1_nome = "Ana Souza"
cliente_1_idade = 29
cliente_1_email = "ana@email.com"

cliente_2_nome = "Bruno Lima"
cliente_2_idade = 35
cliente_2_email = "bruno@email.com"
```

Isso funciona com dois clientes. Mas pense em um sistema real com 100, 1.000 ou 10.000 clientes.

O código começa a ficar difícil de manter:

- o nome fica separado da idade;
- a idade fica separada do e-mail;
- cada novo cliente exige novas variáveis;
- fica fácil trocar dados por engano;
- fica difícil criar ações como validar e-mail ou exibir dados.

Uma alternativa seria usar dicionários:

```python
cliente = {
    "nome": "Ana Souza",
    "idade": 29,
    "email": "ana@email.com"
}
```

Isso já melhora, porque os dados ficam agrupados. Mas ainda falta algo importante: **comportamento**.

Um cliente não tem apenas dados. Em um sistema, também podemos querer:

- exibir os dados do cliente;
- validar se o e-mail está correto;
- verificar se o cliente é maior de idade;
- atualizar o e-mail;
- ativar ou desativar o cadastro.

Classes existem para juntar essas duas coisas:

```text
dados + comportamentos = objeto organizado
```

## 2. O que é uma classe?

Uma classe é um **modelo** usado para criar objetos.

Pense em uma classe como um molde.

Uma fábrica pode ter um molde de camiseta. A partir desse molde, ela cria várias camisetas. Cada camiseta segue o mesmo formato, mas pode ter cor, tamanho e estampa diferentes.

Em Python, acontece algo parecido:

- `Cliente` é a classe, ou seja, o modelo.
- `ana` é um objeto criado a partir desse modelo.
- `bruno` é outro objeto criado a partir do mesmo modelo.

Exemplo mental:

```text
Classe Cliente
  - nome
  - idade
  - email
  - exibir dados
  - validar email
```

A classe define o que todo cliente deve ter e o que todo cliente sabe fazer.

## 3. Criando uma classe

Em Python, usamos a palavra `class` para criar uma classe.

```python
class Cliente:
    pass
```

Esse código cria uma classe vazia chamada `Cliente`.

Por convenção, nomes de classes usam a primeira letra maiúscula:

```python
class Produto:
    pass


class Funcionario:
    pass


class Pedido:
    pass
```

### Criando atributos com `__init__`

Na maioria das vezes, uma classe precisa receber dados iniciais.

Para isso, usamos o método especial `__init__`.

```python
class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
```

Vamos entender com calma:

- `class Cliente:` cria o modelo.
- `def __init__(...)` define o que acontece quando um cliente é criado.
- `self` representa o próprio objeto.
- `nome`, `idade` e `email` são dados recebidos.
- `self.nome`, `self.idade` e `self.email` são atributos guardados dentro do objeto.

Um atributo é uma informação que pertence ao objeto.

```python
self.nome = nome
```

Leia essa linha assim:

```text
Guarde dentro deste cliente o nome recebido.
```

## 4. Métodos

Métodos são funções que ficam dentro de uma classe.

Uma função comum trabalha sozinha:

```python
def exibir_mensagem():
    print("Sistema iniciado")
```

Um método trabalha com os dados do objeto:

```python
class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"E-mail: {self.email}")
```

O método `exibir_dados` usa os atributos do próprio cliente.

Isso é importante porque o comportamento fica perto dos dados que ele usa.

## 5. Instância: criando objetos

Uma instância é um objeto criado a partir de uma classe.

```python
ana = Cliente("Ana Souza", 29, "ana@email.com")
bruno = Cliente("Bruno Lima", 35, "bruno@email.com")
```

Aqui:

- `Cliente` é a classe;
- `ana` é uma instância de `Cliente`;
- `bruno` também é uma instância de `Cliente`;
- cada objeto tem seus próprios dados.

Podemos acessar os atributos:

```python
print(ana.nome)
print(bruno.email)
```

E podemos chamar métodos:

```python
ana.exibir_dados()
bruno.exibir_dados()
```

### Classe x objeto

| Conceito | Significado simples | Exemplo |
| --- | --- | --- |
| Classe | Modelo usado para criar objetos | `Cliente` |
| Objeto | Item criado a partir da classe | `ana` |
| Atributo | Dado guardado no objeto | `nome` |
| Método | Ação que o objeto sabe executar | `exibir_dados()` |

## 6. Uso real: organizando dados de sistema

Classes aparecem em sistemas reais porque programas normalmente lidam com entidades.

Uma entidade é algo importante para o sistema.

Em uma loja, entidades comuns seriam:

- cliente;
- produto;
- pedido;
- pagamento;
- funcionário.

Em uma escola:

- aluno;
- professor;
- turma;
- matrícula;
- nota.

Em uma clínica:

- paciente;
- médico;
- consulta;
- prontuário.

### Exemplo completo com cliente

```python
class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def exibir_dados(self):
        return f"{self.nome} | {self.idade} anos | {self.email}"

    def email_valido(self):
        return "@" in self.email and "." in self.email

    def maior_de_idade(self):
        return self.idade >= 18


cliente = Cliente("Ana Souza", 29, "ana@email.com")

print(cliente.exibir_dados())
print(cliente.email_valido())
print(cliente.maior_de_idade())
```

Saída esperada:

```text
Ana Souza | 29 anos | ana@email.com
True
True
```

Perceba o ganho:

- os dados do cliente ficam juntos;
- as validações do cliente ficam na própria classe;
- o código principal fica mais limpo;
- fica mais fácil criar outros clientes.

### Exemplo completo com produto

```python
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total_em_estoque(self):
        return self.preco * self.quantidade

    def exibir_resumo(self):
        total = self.valor_total_em_estoque()
        return f"{self.nome} - {self.quantidade} unidades - R$ {total:.2f}"


produto = Produto("Teclado", 150.00, 8)

print(produto.exibir_resumo())
```

Saída esperada:

```text
Teclado - 8 unidades - R$ 1200.00
```

Aqui, o produto não guarda apenas informações. Ele também sabe calcular o próprio valor total em estoque.

## 7. Boas práticas

### Use nomes claros

Prefira:

```python
class Cliente:
    pass
```

Evite:

```python
class Coisa:
    pass
```

O nome da classe deve explicar o que ela representa.

### Uma classe deve ter uma responsabilidade principal

Uma classe `Cliente` deve cuidar dos dados e regras do cliente.

Ela não deveria gerar relatório financeiro, enviar e-mail, ler arquivo e cadastrar produto tudo ao mesmo tempo.

Comece simples:

```text
Cliente cuida de cliente.
Produto cuida de produto.
Pedido cuida de pedido.
```

### Métodos devem representar ações reais

Bons nomes de métodos:

- `exibir_dados`
- `calcular_total`
- `validar_email`
- `aplicar_desconto`
- `atualizar_estoque`

Nomes ruins:

- `fazer`
- `processar`
- `coisa`
- `executar_tudo`

### Evite criar classes sem necessidade

Nem tudo precisa virar classe.

Se você só precisa somar dois números, uma função resolve bem.

Classes fazem mais sentido quando existe:

- um conjunto de dados relacionados;
- comportamentos ligados a esses dados;
- necessidade de criar vários objetos parecidos.

## 8. Erros comuns

### Confundir classe com variável

Errado pensar que a classe já é o cliente final.

```python
class Cliente:
    pass
```

Isso é apenas o modelo. Para criar um cliente real no programa, precisamos instanciar:

```python
cliente = Cliente()
```

### Esquecer o `self`

Errado:

```python
class Cliente:
    def exibir_nome():
        print(self.nome)
```

Correto:

```python
class Cliente:
    def exibir_nome(self):
        print(self.nome)
```

O `self` permite que o método acesse os dados do próprio objeto.

### Criar atributos fora do `__init__` sem necessidade

Evite espalhar atributos pelo código:

```python
cliente = Cliente()
cliente.nome = "Ana"
cliente.email = "ana@email.com"
```

Para iniciantes, é mais claro iniciar os atributos no `__init__`:

```python
cliente = Cliente("Ana", "ana@email.com")
```

### Não usar métodos

Se você cria uma classe, mas deixa todas as regras fora dela, perde boa parte do benefício.

Menos organizado:

```python
cliente = Cliente("Ana", 29, "ana@email.com")

if "@" in cliente.email:
    print("E-mail válido")
```

Mais organizado:

```python
cliente = Cliente("Ana", 29, "ana@email.com")

if cliente.email_valido():
    print("E-mail válido")
```

### Misturar responsabilidades

Evite uma classe que faz tudo.

```python
class Sistema:
    # cadastra cliente
    # calcula folha de pagamento
    # controla estoque
    # gera relatório
    # envia e-mail
    pass
```

No começo, isso parece prático. Depois, vira um código difícil de alterar.

Prefira separar por entidades e responsabilidades:

```python
class Cliente:
    pass


class Produto:
    pass


class Pedido:
    pass
```

## 9. Mini desafios

Antes dos exercícios completos, tente resolver estes desafios rápidos:

1. Crie uma classe `Cliente` com `nome`, `idade` e `email`.
2. Adicione um método `exibir_dados` na classe `Cliente`.
3. Crie dois objetos da classe `Cliente` e exiba os dados dos dois.
4. Crie uma classe `Produto` com `nome`, `preco` e `quantidade`.
5. Adicione um método `calcular_total` que retorna `preco * quantidade`.
6. Crie uma classe `Funcionario` com `nome`, `cargo` e `salario`.
7. Adicione um método `aplicar_aumento(percentual)` na classe `Funcionario`.
8. Crie uma classe `Pedido` que recebe um cliente e uma lista de produtos.
9. Adicione um método que calcula o total do pedido.
10. Pense em uma entidade de um sistema que você gostaria de construir e liste seus atributos e métodos.

## 10. Resumo

- Classe é um modelo para criar objetos.
- Objeto é uma instância criada a partir de uma classe.
- Atributos são dados guardados dentro do objeto.
- Métodos são ações que o objeto sabe executar.
- `__init__` prepara o objeto no momento da criação.
- `self` representa o próprio objeto dentro da classe.
- Classes ajudam a representar entidades reais de sistemas.
- Uma boa classe junta dados e comportamentos relacionados.
- Classes devem ter nomes claros e responsabilidades bem definidas.

## Próximos passos

1. Estude os arquivos da pasta [`exemplos`](exemplos).
2. Resolva os exercícios em [`exercicios`](exercicios).
3. Compare com os gabaritos em [`exercicios/gabaritos`](exercicios/gabaritos).
4. Faça o projeto em [`projeto`](projeto).
